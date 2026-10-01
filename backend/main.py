"""
Roundtable FastAPI Backend Service
==================================
Provides RESTful APIs for creating, reviewing, editing, and approving
Product Decision Briefs across insurance domains (Claims slice first).
"""
from __future__ import annotations

import json
from datetime import datetime
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from backend.database import get_connection
from backend.llm import generate_brief
from backend import readiness

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
                         ("readiness_json", "TEXT")):
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


class UpdateClaimsTextRequest(BaseModel):
    claims_finding_text: str = Field(..., description="Human-edited Claims finding text.")


class SectionNoteRequest(BaseModel):
    note: str = Field(..., max_length=4000, description="Reviewer note for this claims section; empty clears it.")


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
    product_brief = generate_brief(title=req.title, tag_value=clean_tag)

    # Synthesize the initial Claims domain finding text from internal evidence
    internal_statements = [ev.statement for ev in product_brief.internal_evidence]
    claims_finding_text = (
        "\n\n".join(internal_statements)
        if internal_statements
        else f"Analysis for '{req.title}' completed."
    )

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
