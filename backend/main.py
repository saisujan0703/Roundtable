"""
Roundtable FastAPI Backend Service
==================================
Provides RESTful APIs for creating, reviewing, editing, and approving
Product Decision Briefs across insurance domains (Claims slice first).
"""
from __future__ import annotations

import json
import wave
from datetime import datetime
from typing import Any, Dict, List, Literal, Optional

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from backend.database import get_connection
from backend.llm import MAX_PROXY_TAGS, generate_brief, resolve_analysis_basis, resolve_risk_tag_with_confidence
from backend import readiness
from backend.idea_assistant import refine_idea
from backend import speech
from backend import guideline as handling_guideline
from backend import scenarios as test_scenarios

app = FastAPI(
    title="Roundtable Decision Support API",
    description="AI-assisted insurance product decision support system for Guidewire APD readiness.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Claims sections a reviewer can annotate (matches the 11 brief sections)
CLAIMS_SECTIONS = range(1, 12)


def init_db() -> None:
    """Ensure the briefs table exists in roundtable.db, with the review-tracking columns."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS briefs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                tag_value TEXT NOT NULL,
                claims_finding_text TEXT NOT NULL,
                claims_status TEXT NOT NULL DEFAULT 'Draft',
                created_at TEXT NOT NULL,
                brief_json TEXT
            );
        """)
        # Migration: generated text is kept so reviewer edits can be shown as a diff;
        # section notes hold reviewer commentary per claims section (JSON {"1": "..."}).
        existing = {r["name"] for r in conn.execute("PRAGMA table_info(briefs)").fetchall()}
        for col, ddl in (("original_claims_text", "TEXT"), ("claims_edited_at", "TEXT"), ("section_notes", "TEXT"),
                         ("readiness_json", "TEXT"), ("guideline_json", "TEXT"),
                         ("scenarios_json", "TEXT")):
            if col not in existing:
                conn.execute(f"ALTER TABLE briefs ADD COLUMN {col} {ddl}")
        # Briefs created before tracking existed: their current text becomes the baseline
        conn.execute("UPDATE briefs SET original_claims_text = claims_finding_text WHERE original_claims_text IS NULL")
        conn.commit()


# Ensure table is ready at import time
init_db()


@app.on_event("startup")
def warm_analytics_cache() -> None:
    """Load claims data and portfolio trend fits once, in the background, so the first brief is fast."""
    import threading
    from backend.analytics import detect_notable_trends, get_relative_growth_benchmark

    threading.Thread(target=lambda: (detect_notable_trends(), get_relative_growth_benchmark("battery_fault")),
                     daemon=True).start()


# ---------------------------------------------------------------------------
# Request & Response Models
# ---------------------------------------------------------------------------
class CreateBriefRequest(BaseModel):
    title: str = Field(..., max_length=150, example="EV High-Voltage Battery Coverage Gap")
    tag_value: Optional[str] = None
    proxy_tags: Optional[List[str]] = Field(
        None, max_length=MAX_PROXY_TAGS,
        description="Related risk patterns to use as proxy claims history when the title matches no pattern of its own.")
    idea_context: Optional[str] = Field(
        None, max_length=4000,
        description="The PM's own description of the idea (from the idea assistant); background for the brief, not evidence.")


class IdeaMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(..., min_length=1, max_length=4000)


class RefineIdeaRequest(BaseModel):
    messages: List[IdeaMessage] = Field(..., min_length=1, max_length=20,
                                        description="The chat so far, oldest first, starting with the PM's story.")


class ProxyTagsRequest(BaseModel):
    proxy_tags: List[str] = Field(..., min_length=1, max_length=MAX_PROXY_TAGS,
                                  description="Risk patterns whose pooled claims stand in for this product's history.")


class UpdateClaimsTextRequest(BaseModel):
    claims_finding_text: str = Field(..., description="Human-edited Claims finding text.")


class SectionNoteRequest(BaseModel):
    note: str = Field(..., max_length=4000, description="Reviewer note for this claims section; empty clears it.")


class GuidelineSectionRequest(BaseModel):
    body: str = Field(..., min_length=1, max_length=handling_guideline.MAX_SECTION_CHARS)


class ScenarioUpdateRequest(BaseModel):
    status: Optional[str] = None
    tester: Optional[str] = Field(None, max_length=100)
    note: Optional[str] = Field(None, max_length=2000)


class ReadinessUpdateRequest(BaseModel):
    status: Optional[str] = Field(None, description="Not started | In progress | Done | N/A")
    owner: Optional[str] = Field(None, max_length=120)
    note: Optional[str] = Field(None, max_length=4000)


class BriefRecord(BaseModel):
    id: int
    title: str
    tag_value: Optional[str] = None
    match_confidence: Optional[float] = None
    claims_finding_text: str
    claims_status: str
    created_at: str
    brief_data: Optional[Dict[str, Any]] = None
    original_claims_text: Optional[str] = None
    claims_edited: bool = False
    claims_edited_at: Optional[str] = None
    section_notes: Dict[str, str] = Field(default_factory=dict)


BRIEF_COLUMNS = ("id, title, tag_value, claims_finding_text, claims_status, created_at, brief_json, "
                 "original_claims_text, claims_edited_at, section_notes")


def _to_record(row) -> BriefRecord:
    brief_dict = json.loads(row["brief_json"]) if row["brief_json"] else None
    original = row["original_claims_text"]
    return BriefRecord(
        id=row["id"],
        title=row["title"],
        tag_value=row["tag_value"],
        match_confidence=brief_dict.get("match_confidence") if brief_dict else None,
        claims_finding_text=row["claims_finding_text"],
        claims_status=row["claims_status"],
        created_at=row["created_at"],
        brief_data=brief_dict,
        original_claims_text=original,
        claims_edited=original is not None and original != row["claims_finding_text"],
        claims_edited_at=row["claims_edited_at"],
        section_notes=json.loads(row["section_notes"]) if row["section_notes"] else {},
    )


def _require_brief(cursor, brief_id: int) -> None:
    cursor.execute("SELECT id FROM briefs WHERE id = ?", (brief_id,))
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")


# ---------------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------------
@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "roundtable-backend"}


@app.get("/api/tags")
def list_known_tags() -> List[str]:
    """Return distinct risk category tags present in the claims database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT risk_category_tag FROM claims ORDER BY risk_category_tag")
        rows = cursor.fetchall()
        return [r["risk_category_tag"] for r in rows if r["risk_category_tag"]]


@app.get("/api/proxy-suggestions")
def proxy_suggestions(title: str):
    """What the claims analysis would stand on for this title: direct match, proxy patterns or line baseline."""
    tag, confidence = resolve_risk_tag_with_confidence(title)
    return {"title": title, "match_confidence": confidence, **resolve_analysis_basis(title, tag)}


@app.post("/api/ideas/refine")
def refine_product_idea(req: RefineIdeaRequest):
    """Turn a PM's free-text product story into title options, a risk tag and proxy patterns for the brief form."""
    if req.messages[0].role != "user" or req.messages[-1].role != "user":
        raise HTTPException(status_code=400, detail="The conversation must start and end with a user message.")
    return refine_idea([m.model_dump() for m in req.messages])


MAX_AUDIO_BYTES = 12 * 1024 * 1024  # ~6 minutes of 16 kHz mono WAV


@app.post("/api/ideas/transcribe")
def transcribe_idea(audio: UploadFile = File(...)):
    """Transcribe a spoken product idea locally (faster-whisper); the recording is never stored or sent anywhere."""
    data = audio.file.read(MAX_AUDIO_BYTES + 1)
    if not data:
        raise HTTPException(status_code=400, detail="The recording is empty.")
    if len(data) > MAX_AUDIO_BYTES:
        raise HTTPException(status_code=413, detail="The recording is too long; keep it under about 6 minutes.")
    try:
        text = speech.transcribe(data)
    except speech.SpeechUnavailable as e:
        raise HTTPException(status_code=503, detail=str(e))
    except (wave.Error, EOFError, ValueError):
        raise HTTPException(status_code=400, detail="Could not read the recording; it must be a WAV file.")
    return {"text": text}


@app.get("/api/briefs", response_model=List[BriefRecord])
def list_briefs():
    """List all created briefs, most recent first."""
    with get_connection() as conn:
        rows = conn.execute(f"SELECT {BRIEF_COLUMNS} FROM briefs ORDER BY id DESC").fetchall()
        return [_to_record(r) for r in rows]


@app.post("/api/briefs", response_model=BriefRecord, status_code=201)
def create_brief(req: CreateBriefRequest):
    """Generate a new Product Decision Brief and store the initial Draft in SQLite.

    External RAG qualitative research runs directly off the title.
    Internal analytics matches the tag automatically if none is explicitly provided.
    """
    if len(req.title) > 150:
        raise HTTPException(status_code=400, detail="Product Idea Title exceeds maximum limit of 150 characters.")

    # Sanitize tag_value: treat empty string or whitespace as None to trigger auto-detection
    clean_tag = req.tag_value.strip() if req.tag_value and req.tag_value.strip() else None

    # Generate the structured decision brief via LLM / deterministic fallback
    product_brief = generate_brief(title=req.title, tag_value=clean_tag, proxy_tags=req.proxy_tags,
                                   idea_context=req.idea_context)
    claims_finding_text = _finding_text(product_brief, req.title)

    created_at = datetime.utcnow().isoformat()
    brief_json_str = product_brief.model_dump_json()
    tag_to_store = product_brief.tag_value or "unmatched"

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO briefs (title, tag_value, claims_finding_text, claims_status, created_at, brief_json,
                                original_claims_text, section_notes)
            VALUES (?, ?, ?, 'Draft', ?, ?, ?, '{}')
            """,
            (req.title, tag_to_store, claims_finding_text, created_at, brief_json_str, claims_finding_text),
        )
        conn.commit()
        brief_id = cursor.lastrowid

    return get_brief(brief_id)


def _finding_text(product_brief, title: str) -> str:
    """The initial Claims domain finding text, synthesized from the internal evidence."""
    internal_statements = [ev.statement for ev in product_brief.internal_evidence]
    return "\n\n".join(internal_statements) if internal_statements else f"Analysis for '{title}' completed."


@app.put("/api/briefs/{brief_id}/proxies", response_model=BriefRecord)
def rerun_with_proxies(brief_id: int, req: ProxyTagsRequest):
    """Re-run an unmatched brief's claims analysis on reviewer-chosen proxy risk patterns.

    The brief is regenerated in place and returns to Draft. Reviewer section notes are kept, and readiness
    items keep their status, owner and note while their guidance is rebuilt from the new numbers.
    """
    with get_connection() as conn:
        row = conn.execute("SELECT title, tag_value, claims_status, readiness_json, brief_json FROM briefs WHERE id = ?",
                           (brief_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
    if row["claims_status"] == "Approved":
        raise HTTPException(status_code=409, detail="Claims finding is approved; reject it before changing its proxies.")
    if row["tag_value"] and row["tag_value"] != "unmatched":
        raise HTTPException(status_code=409, detail="This brief has its own risk pattern; proxies apply only to unmatched briefs.")

    idea_context = json.loads(row["brief_json"] or "{}").get("idea_context")
    product_brief = generate_brief(title=row["title"], proxy_tags=req.proxy_tags, idea_context=idea_context)
    if product_brief.analysis_basis != "proxy":
        detail = ("None of the selected proxy risk patterns exist in the claims data." if product_brief.analysis_basis != "direct"
                  else f"The title now matches risk pattern '{product_brief.tag_value}' directly; create a new brief instead.")
        raise HTTPException(status_code=400, detail=detail)
    text = _finding_text(product_brief, row["title"])
    brief_json = product_brief.model_dump_json()

    readiness_json = None
    if row["readiness_json"]:
        old = {i["id"]: i for i in json.loads(row["readiness_json"])}
        items = readiness.build_checklist(json.loads(brief_json))
        for i in items:
            if i["id"] in old:
                i.update({k: old[i["id"]][k] for k in ("status", "owner", "note", "updated_at")})
        readiness_json = json.dumps(items)

    with get_connection() as conn:
        conn.execute(
            """UPDATE briefs SET brief_json = ?, claims_finding_text = ?, original_claims_text = ?, claims_edited_at = NULL,
                                 claims_status = 'Draft', readiness_json = ? WHERE id = ?""",
            (brief_json, text, text, readiness_json, brief_id),
        )
        # A drafted handling guideline quoted the old numbers: flag it for regeneration
        conn.execute("""UPDATE briefs SET guideline_json = json_set(guideline_json, '$.stale', json('true'))
                        WHERE id = ? AND guideline_json IS NOT NULL""", (brief_id,))
        conn.commit()
    return get_brief(brief_id)


@app.get("/api/briefs/{brief_id}", response_model=BriefRecord)
def get_brief(brief_id: int):
    """Fetch a single brief by ID."""
    with get_connection() as conn:
        row = conn.execute(f"SELECT {BRIEF_COLUMNS} FROM briefs WHERE id = ?", (brief_id,)).fetchone()
        if not row:
            raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
        return _to_record(row)


@app.put("/api/briefs/{brief_id}/claims", response_model=BriefRecord)
def update_claims_finding(brief_id: int, req: UpdateClaimsTextRequest):
    """Allow human Claims adjusters or reviewers to edit/correct the Claims finding text.

    The generated text is kept in original_claims_text, so the edit is visible as a diff.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        _require_brief(cursor, brief_id)
        cursor.execute(
            "UPDATE briefs SET claims_finding_text = ?, claims_edited_at = ? WHERE id = ?",
            (req.claims_finding_text, datetime.utcnow().isoformat(), brief_id),
        )
        conn.commit()

    return get_brief(brief_id)


@app.put("/api/briefs/{brief_id}/notes/{section}", response_model=BriefRecord)
def update_section_note(brief_id: int, section: int, req: SectionNoteRequest):
    """Save (or clear, with an empty note) the reviewer note for one claims section (1-11).

    Notes sit beside the section's charts; they never change the computed numbers.
    """
    if section not in CLAIMS_SECTIONS:
        raise HTTPException(status_code=400, detail="Section must be between 1 and 11.")
    with get_connection() as conn:
        cursor = conn.cursor()
        _require_brief(cursor, brief_id)
        row = cursor.execute("SELECT section_notes FROM briefs WHERE id = ?", (brief_id,)).fetchone()
        notes = json.loads(row["section_notes"]) if row["section_notes"] else {}
        text = req.note.strip()
        if text:
            notes[str(section)] = text
        else:
            notes.pop(str(section), None)
        cursor.execute("UPDATE briefs SET section_notes = ? WHERE id = ?", (json.dumps(notes), brief_id))
        conn.commit()

    return get_brief(brief_id)


@app.put("/api/briefs/{brief_id}/claims/approve", response_model=BriefRecord)
def approve_claims_finding(brief_id: int):
    """Human Claims reviewer approves the Claims section finding."""
    with get_connection() as conn:
        cursor = conn.cursor()
        _require_brief(cursor, brief_id)
        cursor.execute("UPDATE briefs SET claims_status = 'Approved' WHERE id = ?", (brief_id,))
        conn.commit()

    return get_brief(brief_id)


@app.put("/api/briefs/{brief_id}/claims/reject", response_model=BriefRecord)
def reject_claims_finding(brief_id: int):
    """Human Claims reviewer rejects the Claims section finding."""
    with get_connection() as conn:
        cursor = conn.cursor()
        _require_brief(cursor, brief_id)
        cursor.execute("UPDATE briefs SET claims_status = 'Rejected' WHERE id = ?", (brief_id,))
        conn.commit()

    return get_brief(brief_id)


# ---------------------------------------------------------------------------
# Claims Readiness checklist
# ---------------------------------------------------------------------------
def _load_readiness(conn, brief_id: int) -> list:
    row = conn.execute("SELECT brief_json, readiness_json FROM briefs WHERE id = ?", (brief_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
    if row["readiness_json"]:
        return json.loads(row["readiness_json"])
    # First access: build the checklist from this brief's claims analytics and store it
    items = readiness.build_checklist(json.loads(row["brief_json"]) if row["brief_json"] else {})
    conn.execute("UPDATE briefs SET readiness_json = ? WHERE id = ?", (json.dumps(items), brief_id))
    conn.commit()
    return items


@app.get("/api/briefs/{brief_id}/readiness")
def get_readiness(brief_id: int):
    """Claims launch-readiness checklist for a brief, with completion summary."""
    with get_connection() as conn:
        items = _load_readiness(conn, brief_id)
    return {"brief_id": brief_id, "items": items, "summary": readiness.summarize(items),
            "statuses": list(readiness.STATUSES), "stages": readiness.STAGES}


@app.put("/api/briefs/{brief_id}/readiness/{item_id}")
def update_readiness_item(brief_id: int, item_id: str, req: ReadinessUpdateRequest):
    """Update status, owner or note of one readiness item."""
    with get_connection() as conn:
        items = _load_readiness(conn, brief_id)
        try:
            items = readiness.update_item(items, item_id, req.status, req.owner, req.note)
        except KeyError:
            raise HTTPException(status_code=404, detail=f"Readiness item '{item_id}' not found")
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc))
        conn.execute("UPDATE briefs SET readiness_json = ? WHERE id = ?", (json.dumps(items), brief_id))
        conn.commit()
    return {"brief_id": brief_id, "items": items, "summary": readiness.summarize(items),
            "statuses": list(readiness.STATUSES), "stages": readiness.STAGES}


# ---------------------------------------------------------------------------
# Claims handling guideline
# ---------------------------------------------------------------------------
def _load_guideline(conn, brief_id: int):
    row = conn.execute("SELECT title, brief_json, claims_status, guideline_json FROM briefs WHERE id = ?",
                       (brief_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
    return row, (json.loads(row["guideline_json"]) if row["guideline_json"] else None)


def _guideline_response(brief_id: int, title: str, g: Optional[dict]) -> dict:
    return {"brief_id": brief_id, "guideline": g,
            "markdown": handling_guideline.to_markdown(title, g) if g else None}


def _save_guideline(conn, brief_id: int, g: dict) -> None:
    conn.execute("UPDATE briefs SET guideline_json = ? WHERE id = ?", (json.dumps(g), brief_id))
    conn.commit()


@app.get("/api/briefs/{brief_id}/guideline")
def get_guideline(brief_id: int):
    """The drafted claims handling guideline for a brief (null until drafted), plus a markdown export."""
    with get_connection() as conn:
        row, g = _load_guideline(conn, brief_id)
    return _guideline_response(brief_id, row["title"], g)


@app.post("/api/briefs/{brief_id}/guideline")
def draft_guideline(brief_id: int):
    """Draft (or redraft) the guideline from the brief's claims analytics. An approved guideline is never overwritten."""
    with get_connection() as conn:
        row, g = _load_guideline(conn, brief_id)
    if g and g.get("status") == "Approved":
        raise HTTPException(status_code=409, detail="The guideline is approved; reopen it by editing a section before redrafting.")
    brief = json.loads(row["brief_json"]) if row["brief_json"] else {"title": row["title"]}
    g = handling_guideline.generate_guideline(brief)
    with get_connection() as conn:
        _save_guideline(conn, brief_id, g)
    return _guideline_response(brief_id, row["title"], g)


@app.put("/api/briefs/{brief_id}/guideline/sections/{key}")
def edit_guideline_section(brief_id: int, key: str, req: GuidelineSectionRequest):
    """Reviewer edit of one section; the guideline returns to Draft."""
    with get_connection() as conn:
        row, g = _load_guideline(conn, brief_id)
        if not g:
            raise HTTPException(status_code=404, detail="No guideline drafted for this brief yet.")
        try:
            handling_guideline.edit_section(g, key, req.body)
        except KeyError:
            raise HTTPException(status_code=404, detail=f"Unknown guideline section '{key}'")
        _save_guideline(conn, brief_id, g)
    return _guideline_response(brief_id, row["title"], g)


@app.put("/api/briefs/{brief_id}/guideline/approve")
def approve_guideline(brief_id: int):
    """Human Claims sign-off. Requires the brief's Claims finding to be approved first, and a current guideline."""
    with get_connection() as conn:
        row, g = _load_guideline(conn, brief_id)
        if not g:
            raise HTTPException(status_code=404, detail="No guideline drafted for this brief yet.")
        if row["claims_status"] != "Approved":
            raise HTTPException(status_code=409, detail="Approve the Claims finding before approving the handling guideline.")
        if g.get("stale"):
            raise HTTPException(status_code=409, detail="The brief changed since this guideline was drafted; redraft it first.")
        g["status"], g["approved_at"] = "Approved", datetime.utcnow().isoformat()
        _save_guideline(conn, brief_id, g)
    return _guideline_response(brief_id, row["title"], g)


# ---------------------------------------------------------------------------
# ClaimCenter test scenarios (built from the handling guideline)
# ---------------------------------------------------------------------------
def _scenarios_response(brief_id: int, row, record: Optional[dict]) -> dict:
    g = json.loads(row["guideline_json"]) if row["guideline_json"] else None
    return {
        "brief_id": brief_id,
        "has_guideline": g is not None,
        "scenarios": record,
        "summary": test_scenarios.summarize(record) if record else None,
        # The guideline was edited or redrafted after these scenarios were built
        "stale": bool(record and record.get("guideline_version") != test_scenarios.guideline_version(g)),
        "statuses": list(test_scenarios.STATUSES),
        "categories": test_scenarios.CATEGORIES,
    }


def _load_scenarios_row(conn, brief_id: int):
    row = conn.execute("SELECT title, brief_json, guideline_json, scenarios_json FROM briefs WHERE id = ?",
                       (brief_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
    return row, (json.loads(row["scenarios_json"]) if row["scenarios_json"] else None)


@app.get("/api/briefs/{brief_id}/scenarios")
def get_scenarios(brief_id: int):
    """ClaimCenter test scenarios for a brief (null until generated), with pass/fail summary and staleness."""
    with get_connection() as conn:
        row, record = _load_scenarios_row(conn, brief_id)
    return _scenarios_response(brief_id, row, record)


@app.post("/api/briefs/{brief_id}/scenarios")
def generate_test_scenarios(brief_id: int):
    """(Re)generate the scenarios from the brief's current handling guideline. Recorded test results are replaced."""
    with get_connection() as conn:
        row, _ = _load_scenarios_row(conn, brief_id)
    if not row["guideline_json"]:
        raise HTTPException(status_code=409, detail="Draft the handling guideline first; the test scenarios are built from it.")
    g = json.loads(row["guideline_json"])
    brief = json.loads(row["brief_json"]) if row["brief_json"] else {"title": row["title"]}
    record = test_scenarios.generate_scenarios(brief, g, handling_guideline.to_markdown(row["title"], g))
    with get_connection() as conn:
        conn.execute("UPDATE briefs SET scenarios_json = ? WHERE id = ?", (json.dumps(record), brief_id))
        conn.commit()
        row, record = _load_scenarios_row(conn, brief_id)
    return _scenarios_response(brief_id, row, record)


@app.put("/api/briefs/{brief_id}/scenarios/{scenario_id}")
def update_test_scenario(brief_id: int, scenario_id: str, req: ScenarioUpdateRequest):
    """Record a tester's result for one scenario: status, tester and notes."""
    with get_connection() as conn:
        row, record = _load_scenarios_row(conn, brief_id)
        if not record:
            raise HTTPException(status_code=404, detail="No test scenarios generated for this brief yet.")
        try:
            test_scenarios.update_scenario(record, scenario_id, req.status, req.tester, req.note)
        except KeyError:
            raise HTTPException(status_code=404, detail=f"Unknown scenario '{scenario_id}'")
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        conn.execute("UPDATE briefs SET scenarios_json = ? WHERE id = ?", (json.dumps(record), brief_id))
        conn.commit()
    return _scenarios_response(brief_id, row, record)
