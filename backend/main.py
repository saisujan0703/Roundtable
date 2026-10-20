"""
Roundtable FastAPI Backend Service
==================================
Provides RESTful APIs for creating, reviewing, editing, and approving
Product Decision Briefs across insurance domains (Claims slice first).
"""
from __future__ import annotations

import json
import logging
import wave
from datetime import datetime
from typing import Any, Dict, List, Literal, Optional

from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from starlette.concurrency import run_in_threadpool

from backend.database import get_connection
from backend.llm import MAX_PROXY_TAGS, generate_brief, resolve_analysis_basis, resolve_risk_tag_with_confidence
from backend import audit
from backend import auth
from backend import evidence_sources
from backend import risk_patterns
from backend import market_radar
from backend import pricing
from backend import readiness
from backend.idea_assistant import refine_idea
from backend import speech
from backend import guideline as handling_guideline
from backend import scenarios as test_scenarios
from backend import letters as customer_letters
from backend import compliance as state_compliance
from backend import launch_gate
from backend import operations as launch_operations
from backend import policy_form
from backend import workflow as idea_workflow
from backend import coverage as covered_claims
from backend import actuarial
from backend import actuarial_memo
from backend import actuarial_settings
from backend import filing_research
from backend import monitoring
from backend import parametric
from backend import rating_tests
from backend import analytics as claims_analytics
from backend import business_plan
from backend import competitor_landscape
from backend import rating_plan
from backend import reserving

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

# Idea workflow (PM -> Claims + Actuarial recommendations -> decision): switched off for now. When True,
# launch-readiness writes are refused until the decision is Proceed, and the launch gate requires it.
# The workflow endpoints work either way.
ENFORCE_IDEA_WORKFLOW = False

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
                         ("scenarios_json", "TEXT"), ("letters_json", "TEXT"), ("compliance_json", "TEXT"),
                         ("launch_json", "TEXT"), ("policy_form_json", "TEXT"),
                         ("workflow_json", "TEXT"), ("coverage_overrides_json", "TEXT"),
                         ("actuarial_json", "TEXT"), ("landscape_json", "TEXT")):
            if col not in existing:
                conn.execute(f"ALTER TABLE briefs ADD COLUMN {col} {ddl}")
        # Briefs created before tracking existed: their current text becomes the baseline
        conn.execute("UPDATE briefs SET original_claims_text = claims_finding_text WHERE original_claims_text IS NULL")
        conn.commit()


# Ensure tables are ready at import time
init_db()
auth.init_auth_tables()
audit.init_table()
risk_patterns.init_table()
evidence_sources.init_table()
actuarial_settings.init_table()
market_radar.init_radar_tables()

# Paths reachable without a session: sign-in itself, health, and the API docs
PUBLIC_PATHS = {"/api/health", "/api/auth/login", "/docs", "/redoc", "/openapi.json", "/docs/oauth2-redirect"}


log = logging.getLogger("roundtable")


async def _audit(request: Request, status: int, body: bytes, **who) -> None:
    """Record one write in the audit log. A failure to record is logged, never turned into a failed request."""
    try:
        await run_in_threadpool(
            audit.record, method=request.method, path=request.url.path, status=status,
            action=audit.action_name(request.scope.get("endpoint"), request.method, request.url.path),
            detail=audit.describe_body(body, request.headers.get("content-type", "")), **who)
    except Exception:
        log.exception("Audit log write failed for %s %s", request.method, request.url.path)


def _login_email(body: bytes) -> Optional[str]:
    try:
        return str(json.loads(body).get("email") or "").strip().lower() or None
    except (ValueError, AttributeError):
        return None


@app.middleware("http")
async def enforce_authentication(request: Request, call_next):
    """Every API call needs a valid bearer token; writes are further limited by role (auth.required_role).
    Every write that reaches here, done or refused, is recorded in the audit log (backend.audit); sign-in
    attempts are recorded under the email they were made with."""
    audited = request.method in audit.WRITE_METHODS
    body = await request.body() if audited else b""
    if request.method == "OPTIONS" or request.url.path in PUBLIC_PATHS:
        response = await call_next(request)
        if audited and request.url.path == "/api/auth/login":
            await _audit(request, response.status_code, body, email=_login_email(body))
        return response
    header = request.headers.get("authorization", "")
    token = header[7:].strip() if header.lower().startswith("bearer ") else ""
    user = auth.user_for_token(token) if token else None
    if user is None:
        return JSONResponse({"detail": "Not signed in or session expired."}, status_code=401,
                            headers={"WWW-Authenticate": "Bearer"})
    needed = auth.required_role(request.method, request.url.path)
    if needed and user["role"] != needed:
        if audited:
            await _audit(request, 403, body, user=user)
        return JSONResponse({"detail": f"Only the {needed} can do this ({user['role']} is read-only here)."},
                            status_code=403)
    request.state.user = user
    request.state.token = token
    response = await call_next(request)
    if audited:
        await _audit(request, response.status_code, body, user=user)
    return response


@app.on_event("startup")
def warm_analytics_cache() -> None:
    """Load claims data and portfolio trend fits once, in the background, so the first brief is fast."""
    import threading
    from backend.analytics import detect_notable_trends, get_relative_growth_benchmark

    threading.Thread(target=lambda: (detect_notable_trends(), get_relative_growth_benchmark("battery_fault")),
                     daemon=True).start()
    market_radar.start_scheduler()


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


class LetterEditRequest(BaseModel):
    subject: str = Field(..., min_length=1, max_length=200)
    body: str = Field(..., min_length=1, max_length=customer_letters.MAX_LETTER_CHARS)


class ReadinessUpdateRequest(BaseModel):
    status: Optional[str] = Field(None, description="Not started | In progress | Done | N/A")
    owner: Optional[str] = Field(None, max_length=120)
    note: Optional[str] = Field(None, max_length=4000)


class ComplianceStateRequest(BaseModel):
    launch: Optional[bool] = None
    acknowledge_days: Optional[int] = Field(None, ge=1, le=365)
    acknowledge_day_type: Optional[str] = None
    decision_days: Optional[int] = Field(None, ge=1, le=365)
    decision_day_type: Optional[str] = None
    payment_days: Optional[int] = Field(None, ge=1, le=365)
    payment_day_type: Optional[str] = None
    extension_rule: Optional[str] = Field(None, max_length=2000)
    denial_notice: Optional[str] = Field(None, max_length=2000)
    status: Optional[str] = Field(None, description="Not confirmed | Confirmed")
    confirmed_by: Optional[str] = Field(None, max_length=120)
    note: Optional[str] = Field(None, max_length=2000)


class SignOffRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    decision: str = Field(..., description="Approve | Approve with conditions | Reject")
    note: str = Field("", max_length=2000, description="Conditions or reason for rejection.")


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
    workflow: Dict[str, Any] = Field(default_factory=dict,
                                     description="Idea lifecycle summary (status, round, recommendations).")


BRIEF_COLUMNS = ("id, title, tag_value, claims_finding_text, claims_status, created_at, brief_json, "
                 "original_claims_text, claims_edited_at, section_notes, workflow_json")


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
        workflow=idea_workflow.summary(json.loads(row["workflow_json"]) if row["workflow_json"] else None),
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


class LoginRequest(BaseModel):
    email: str
    password: str
    role: Literal["Claims Lead", "Lead Actuary"]


@app.post("/api/auth/login")
def auth_login(req: LoginRequest):
    try:
        return auth.login(req.email, req.password, req.role)
    except auth.AuthError as e:
        raise HTTPException(status_code=e.status, detail=e.detail)


@app.get("/api/auth/me")
def auth_me(request: Request):
    return request.state.user


@app.post("/api/auth/logout")
def auth_logout(request: Request):
    auth.logout(request.state.token)
    return {"status": "signed out"}


@app.get("/api/audit")
def get_audit_log(brief_id: Optional[int] = None, email: Optional[str] = None,
                  outcome: Optional[Literal["ok", "refused"]] = None, limit: int = 200,
                  before_id: Optional[int] = None):
    """The audit log (backend.audit), newest first; page back with before_id = the last row's id."""
    rows = audit.query(brief_id=brief_id, email=email, outcome=outcome, limit=limit, before_id=before_id)
    return {"entries": rows, "next_before_id": rows[-1]["id"] if len(rows) == max(1, min(limit, audit.MAX_LIMIT)) else None}


@app.get("/api/briefs/{brief_id}/audit")
def get_brief_audit_log(brief_id: int, outcome: Optional[Literal["ok", "refused"]] = None, limit: int = 200,
                        before_id: Optional[int] = None):
    """Everything recorded against one brief."""
    with get_connection() as conn:
        _require_brief(conn.cursor(), brief_id)
    return get_audit_log(brief_id=brief_id, outcome=outcome, limit=limit, before_id=before_id)


@app.get("/api/tags")
def list_known_tags() -> List[str]:
    """Every risk pattern a brief can stand on: the claims' risk_category_tag values, then custom patterns."""
    return claims_analytics.list_tags()


# ---------------------------------------------------------------------------
# Custom risk patterns (backend.risk_patterns)
# ---------------------------------------------------------------------------
class RiskPatternRequest(BaseModel):
    label: str = Field(..., max_length=80)
    keywords: List[str] = Field(..., max_length=risk_patterns.MAX_KEYWORDS)
    products: List[str] = Field(default_factory=list)
    description: str = Field("", max_length=1000)


class PatternPreviewRequest(BaseModel):
    keywords: List[str] = Field(..., max_length=risk_patterns.MAX_KEYWORDS)
    products: List[str] = Field(default_factory=list)


@app.get("/api/risk-patterns")
def list_risk_patterns():
    claims = claims_analytics._data()["claims"]
    return {"patterns": [{**p, "claims": int(claims_analytics._match(claims, k).sum()),
                          "used_by_briefs": risk_patterns.briefs_using(k)}
                         for k, p in risk_patterns.all_patterns().items()],
            "products": list(risk_patterns.PRODUCTS), "builtin_tags": claims_analytics.builtin_tags()}


@app.post("/api/risk-patterns/preview")
def preview_risk_pattern(req: PatternPreviewRequest):
    """What these keywords would catch in the claims data, before saving them as a pattern."""
    try:
        clean = risk_patterns.clean("preview", req.keywords, req.products)
    except risk_patterns.PatternError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return claims_analytics.preview_pattern(clean["keywords"], clean["products"])


@app.post("/api/risk-patterns", status_code=201)
def create_risk_pattern(req: RiskPatternRequest, request: Request):
    try:
        return risk_patterns.save(req.model_dump(), request.state.user.get("name", ""))
    except risk_patterns.PatternError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put("/api/risk-patterns/{key}")
def update_risk_pattern(key: str, req: RiskPatternRequest, request: Request):
    try:
        return risk_patterns.save(req.model_dump(), request.state.user.get("name", ""), key=key)
    except risk_patterns.PatternError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Risk pattern {key} not found.")


@app.delete("/api/risk-patterns/{key}")
def delete_risk_pattern(key: str):
    try:
        risk_patterns.delete(key)
    except risk_patterns.PatternError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Risk pattern {key} not found.")
    return {"deleted": key}


# ---------------------------------------------------------------------------
# Competitor and regulatory sources (curated files + backend.evidence_sources)
# ---------------------------------------------------------------------------
class SourceRequest(BaseModel):
    source_type: Literal["competitor", "regulatory"]
    name: str = Field(..., max_length=120)
    title: str = Field(..., max_length=200)
    summary: str = Field(..., max_length=3000)
    url: str = Field(..., max_length=500)
    date_collected: Optional[str] = None
    origin: Literal["manual", "web"] = "manual"


class SourceSearchRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=200)
    source_type: Literal["competitor", "regulatory"]


def _builtin_sources() -> List[dict]:
    from backend.rag import SOURCES_DIR, _json_items
    out = []
    for i in _json_items(SOURCES_DIR / "competitors.json"):
        out.append({"source_type": "competitor", "name": i.get("competitor_name"), "title": i.get("product_name"),
                    "summary": i.get("coverage_summary"), "url": i.get("source_url"),
                    "date_collected": i.get("date_collected"), "origin": "built-in"})
    for i in _json_items(SOURCES_DIR / "regulatory.json"):
        out.append({"source_type": "regulatory", "name": i.get("regulatory_body"), "title": i.get("regulation_title"),
                    "summary": i.get("summary"), "url": i.get("source_url"),
                    "date_collected": i.get("date_collected"), "origin": "built-in"})
    return out


@app.get("/api/sources")
def list_evidence_sources(source_type: Optional[Literal["competitor", "regulatory"]] = None):
    """Every competitor and regulatory source briefs can cite: the ones users added, then the built-in set."""
    added = evidence_sources.list_sources(source_type)
    builtin = [b for b in _builtin_sources() if not source_type or b["source_type"] == source_type]
    return {"added": added, "builtin": builtin}


@app.post("/api/sources", status_code=201)
def add_evidence_source(req: SourceRequest, request: Request):
    try:
        return evidence_sources.add(req.model_dump(), request.state.user.get("name", ""))
    except evidence_sources.SourceError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put("/api/sources/{source_id}")
def update_evidence_source(source_id: int, req: SourceRequest):
    try:
        return evidence_sources.update(source_id, req.model_dump())
    except evidence_sources.SourceError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except KeyError:
        raise HTTPException(status_code=404, detail="Source not found.")


@app.delete("/api/sources/{source_id}")
def delete_evidence_source(source_id: int):
    try:
        evidence_sources.delete(source_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Source not found.")
    return {"deleted": source_id}


@app.post("/api/sources/search")
def search_evidence_sources(req: SourceSearchRequest):
    """Web pages to review and add (nothing is saved here). Pages already saved or built in are left out."""
    known = [s["url"] for s in evidence_sources.list_sources()] + [b["url"] for b in _builtin_sources()]
    try:
        return evidence_sources.search_web(req.query, req.source_type, known)
    except evidence_sources.SourceError as e:
        raise HTTPException(status_code=400, detail=str(e))


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
        row = conn.execute("SELECT title, tag_value, claims_status, readiness_json, compliance_json, brief_json "
                           "FROM briefs WHERE id = ?", (brief_id,)).fetchone()
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
        items = readiness.carry_over(readiness.build_checklist(json.loads(brief_json)), json.loads(row["readiness_json"]))
        readiness_json = json.dumps(items)
    compliance_json = None
    if row["compliance_json"]:
        # The proxies change the state footprint; Compliance's work on states still in it is kept
        compliance_json = json.dumps(state_compliance.carry_over(_build_matrix(json.loads(brief_json)),
                                                                 json.loads(row["compliance_json"])))

    with get_connection() as conn:
        conn.execute(
            """UPDATE briefs SET brief_json = ?, claims_finding_text = ?, original_claims_text = ?, claims_edited_at = NULL,
                                 claims_status = 'Draft', readiness_json = ?, compliance_json = ? WHERE id = ?""",
            (brief_json, text, text, readiness_json, compliance_json, brief_id),
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
    stored = json.loads(row["readiness_json"]) if row["readiness_json"] else None
    if stored and not readiness.needs_upgrade(stored):
        return stored
    # First access (or a checklist stored before the newer items existed): build it from this brief's
    # claims analytics and launch operations plan, keeping any recorded progress, and store it
    items = readiness.build_checklist(json.loads(row["brief_json"]) if row["brief_json"] else {})
    if stored:
        items = readiness.carry_over(items, stored)
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
    _require_proceed(brief_id)
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
def _form(row) -> Optional[dict]:
    """The brief's uploaded policy form, if any (row must select policy_form_json)."""
    return json.loads(row["policy_form_json"]) if row["policy_form_json"] else None


def _load_guideline(conn, brief_id: int):
    row = conn.execute("SELECT title, brief_json, claims_status, guideline_json, policy_form_json "
                       "FROM briefs WHERE id = ?",
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
    _require_proceed(brief_id)
    with get_connection() as conn:
        row, g = _load_guideline(conn, brief_id)
    if g and g.get("status") == "Approved":
        raise HTTPException(status_code=409, detail="The guideline is approved; reopen it by editing a section before redrafting.")
    brief = json.loads(row["brief_json"]) if row["brief_json"] else {"title": row["title"]}
    g = handling_guideline.generate_guideline(brief, _form(row))
    with get_connection() as conn:
        _save_guideline(conn, brief_id, g)
    return _guideline_response(brief_id, row["title"], g)


@app.put("/api/briefs/{brief_id}/guideline/sections/{key}")
def edit_guideline_section(brief_id: int, key: str, req: GuidelineSectionRequest):
    """Reviewer edit of one section; the guideline returns to Draft."""
    _require_proceed(brief_id)
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
    _require_proceed(brief_id)
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
    row = conn.execute("SELECT title, brief_json, guideline_json, scenarios_json, compliance_json FROM briefs WHERE id = ?",
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
    _require_proceed(brief_id)
    with get_connection() as conn:
        row, _ = _load_scenarios_row(conn, brief_id)
    if not row["guideline_json"]:
        raise HTTPException(status_code=409, detail="Draft the handling guideline first; the test scenarios are built from it.")
    g = json.loads(row["guideline_json"])
    brief = json.loads(row["brief_json"]) if row["brief_json"] else {"title": row["title"]}
    matrix = json.loads(row["compliance_json"]) if row["compliance_json"] else None
    record = test_scenarios.generate_scenarios(brief, g, handling_guideline.to_markdown(row["title"], g), matrix)
    with get_connection() as conn:
        conn.execute("UPDATE briefs SET scenarios_json = ? WHERE id = ?", (json.dumps(record), brief_id))
        conn.commit()
        row, record = _load_scenarios_row(conn, brief_id)
    return _scenarios_response(brief_id, row, record)


@app.put("/api/briefs/{brief_id}/scenarios/{scenario_id}")
def update_test_scenario(brief_id: int, scenario_id: str, req: ScenarioUpdateRequest):
    """Record a tester's result for one scenario: status, tester and notes."""
    _require_proceed(brief_id)
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


# ---------------------------------------------------------------------------
# Customer letter templates (built from the handling guideline)
# ---------------------------------------------------------------------------
def _load_letters_row(conn, brief_id: int):
    row = conn.execute("SELECT title, brief_json, guideline_json, letters_json, compliance_json, policy_form_json "
                       "FROM briefs WHERE id = ?",
                       (brief_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
    return row, (json.loads(row["letters_json"]) if row["letters_json"] else None)


def _letters_response(brief_id: int, row, record: Optional[dict]) -> dict:
    g = json.loads(row["guideline_json"]) if row["guideline_json"] else None
    if record:
        for l in record["letters"]:
            l["tbd_count"] = customer_letters.unresolved_tbds(l)
    return {
        "brief_id": brief_id,
        "has_guideline": g is not None,
        "guideline_approved": bool(g and g.get("status") == "Approved"),
        "letters": record,
        "stale": bool(record and record.get("guideline_version") != test_scenarios.guideline_version(g)),
        "merge_fields": customer_letters.MERGE_FIELDS,
        "scenario_letters": customer_letters.SCENARIO_LETTERS,
        # What the state merge fields resolve to in each launch state
        "state_notices": state_compliance.state_notices(
            json.loads(row["compliance_json"]) if row["compliance_json"] else None),
        "markdown": customer_letters.to_markdown(row["title"], record) if record else None,
    }


def _save_letters(conn, brief_id: int, record: dict) -> None:
    for l in record["letters"]:
        l.pop("tbd_count", None)
    conn.execute("UPDATE briefs SET letters_json = ? WHERE id = ?", (json.dumps(record), brief_id))
    conn.commit()


@app.get("/api/briefs/{brief_id}/letters")
def get_letters(brief_id: int):
    """Customer letter templates for a brief (null until drafted), with approval state and staleness."""
    with get_connection() as conn:
        row, record = _load_letters_row(conn, brief_id)
    return _letters_response(brief_id, row, record)


@app.post("/api/briefs/{brief_id}/letters")
def draft_letters(brief_id: int):
    """(Re)draft every letter from the current guideline. Refused once any letter is approved."""
    _require_proceed(brief_id)
    with get_connection() as conn:
        row, record = _load_letters_row(conn, brief_id)
    if not row["guideline_json"]:
        raise HTTPException(status_code=409, detail="Draft the handling guideline first; the letters are built from it.")
    g = json.loads(row["guideline_json"])
    # Approvals given against an older guideline no longer count, so stale letters can always be redrafted
    stale = bool(record and record.get("guideline_version") != test_scenarios.guideline_version(g))
    if record and not stale and any(l["status"] == "Approved" for l in record["letters"]):
        raise HTTPException(status_code=409, detail="Some letters are approved; edit them individually instead of redrafting all.")
    brief = json.loads(row["brief_json"]) if row["brief_json"] else {"title": row["title"]}
    record = customer_letters.generate_letters(brief, g, handling_guideline.to_markdown(row["title"], g), _form(row))
    with get_connection() as conn:
        _save_letters(conn, brief_id, record)
        row, record = _load_letters_row(conn, brief_id)
    return _letters_response(brief_id, row, record)


@app.put("/api/briefs/{brief_id}/letters/{key}")
def edit_customer_letter(brief_id: int, key: str, req: LetterEditRequest):
    """Reviewer edit of one letter's subject and body; the letter returns to Draft."""
    _require_proceed(brief_id)
    with get_connection() as conn:
        row, record = _load_letters_row(conn, brief_id)
        if not record:
            raise HTTPException(status_code=404, detail="No letters drafted for this brief yet.")
        try:
            customer_letters.edit_letter(record, key, req.subject, req.body)
        except KeyError:
            raise HTTPException(status_code=404, detail=f"Unknown letter '{key}'")
        _save_letters(conn, brief_id, record)
    return _letters_response(brief_id, row, record)


@app.put("/api/briefs/{brief_id}/letters/{key}/approve")
def approve_customer_letter(brief_id: int, key: str):
    """Legal / Claims sign-off on one letter. Requires an approved guideline and current letters."""
    _require_proceed(brief_id)
    with get_connection() as conn:
        row, record = _load_letters_row(conn, brief_id)
        if not record:
            raise HTTPException(status_code=404, detail="No letters drafted for this brief yet.")
        g = json.loads(row["guideline_json"]) if row["guideline_json"] else None
        if not (g and g.get("status") == "Approved"):
            raise HTTPException(status_code=409, detail="Approve the handling guideline before approving letters.")
        if record.get("guideline_version") != test_scenarios.guideline_version(g):
            raise HTTPException(status_code=409, detail="The guideline changed since these letters were drafted; redraft them first.")
        try:
            customer_letters.approve_letter(record, key)
        except KeyError:
            raise HTTPException(status_code=404, detail=f"Unknown letter '{key}'")
        _save_letters(conn, brief_id, record)
    return _letters_response(brief_id, row, record)


# ---------------------------------------------------------------------------
# Launch operations plan (staffing, reinsurance, statutory reporting, Medicare, litigation, state footprint)
# ---------------------------------------------------------------------------
def _brief_json(conn, brief_id: int) -> dict:
    row = conn.execute("SELECT title, brief_json FROM briefs WHERE id = ?", (brief_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
    return json.loads(row["brief_json"]) if row["brief_json"] else {"title": row["title"]}


@app.get("/api/briefs/{brief_id}/verification")
def get_brief_verification(brief_id: int):
    """The brief's verification report. Briefs made before verification existed are checked now, against
    today's analytics and sources (so a cited source that has since been replaced shows up as an issue)."""
    from backend import llm as brief_llm, verification

    with get_connection() as conn:
        brief = _brief_json(conn, brief_id)
    if brief.get("verification"):
        return {**brief["verification"], "checked_later": False}
    method = brief.get("generation_method") or ""
    if method.startswith("offline") or method.endswith("error_fallback"):
        rep = verification.report([], verification.brief_checked_counts(brief), [], method)
        return {**rep, "status": "computed", "checked_later": True}
    tag = brief.get("tag_value") if brief.get("analysis_basis") == "direct" else None
    basis = resolve_analysis_basis(brief["title"], tag, brief.get("proxy_tags") or None)
    payload = brief_llm._build_llm_payload(brief["title"], tag, basis)
    tag2, conf = resolve_risk_tag_with_confidence(brief["title"], tag)
    computed = brief_llm._deterministic_synthesis(brief["title"], tag2, conf, payload).model_dump()
    issues = verification.verify_brief(
        brief, brief.get("claims_analytics"), payload["retrieved_evidence"],
        [e.get("url") for e in brief.get("external_market_evidence") or []],
        [t for _, t, _ in verification.brief_texts(computed)])
    rep = verification.report(issues, verification.brief_checked_counts(brief),
                              ["Checked after the brief was made, against today's data and sources."], method)
    return {**rep, "checked_later": True}


@app.get("/api/briefs/{brief_id}/operations")
def get_operations(brief_id: int, volume_factor: float = 1.0, caseload: Optional[float] = None):
    """The computed launch operations plan. *volume_factor* scales today's claim volume to the expected uptake;
    *caseload* overrides today's observed open claims per adjuster."""
    if not 0.05 <= volume_factor <= 20:
        raise HTTPException(status_code=400, detail="volume_factor must be between 0.05 and 20.")
    if caseload is not None and not 1 <= caseload <= 1000:
        raise HTTPException(status_code=400, detail="caseload must be between 1 and 1000.")
    with get_connection() as conn:
        brief = _brief_json(conn, brief_id)
    return {"brief_id": brief_id, **launch_operations.build_plan(brief, volume_factor, caseload)}


# ---------------------------------------------------------------------------
# State claims compliance matrix
# ---------------------------------------------------------------------------
def _build_matrix(brief: dict) -> dict:
    plan = launch_operations.build_plan(brief)
    return state_compliance.build_matrix(plan, plan.get("products") or [])


def _compliance_response(brief_id: int, matrix: dict) -> dict:
    return {"brief_id": brief_id, "matrix": matrix, "summary": state_compliance.summarize(matrix),
            "statuses": list(state_compliance.STATUSES), "day_types": list(state_compliance.DAY_TYPES),
            "rules_note": state_compliance.load_rules()["_note"]}


def _load_compliance(conn, brief_id: int) -> dict:
    row = conn.execute("SELECT title, brief_json, compliance_json FROM briefs WHERE id = ?", (brief_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
    if row["compliance_json"]:
        return json.loads(row["compliance_json"])
    # First access: one row per state in the product's footprint, every state a launch state
    matrix = _build_matrix(json.loads(row["brief_json"]) if row["brief_json"] else {"title": row["title"]})
    conn.execute("UPDATE briefs SET compliance_json = ? WHERE id = ?", (json.dumps(matrix), brief_id))
    conn.commit()
    return matrix


@app.get("/api/briefs/{brief_id}/compliance")
def get_compliance(brief_id: int):
    """State claim-handling compliance matrix for the brief's footprint, with confirmation summary."""
    with get_connection() as conn:
        return _compliance_response(brief_id, _load_compliance(conn, brief_id))


@app.put("/api/briefs/{brief_id}/compliance/{state}")
def update_compliance_state(brief_id: int, state: str, req: ComplianceStateRequest):
    """Compliance edits one state: launch flag, deadlines, notice, confirmation."""
    _require_proceed(brief_id)
    with get_connection() as conn:
        matrix = _load_compliance(conn, brief_id)
        try:
            state_compliance.update_state(matrix, state.upper(), req.model_dump(exclude_unset=True))
        except KeyError:
            raise HTTPException(status_code=404, detail=f"State '{state}' is not in this product's footprint")
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        conn.execute("UPDATE briefs SET compliance_json = ? WHERE id = ?", (json.dumps(matrix), brief_id))
        conn.commit()
    return _compliance_response(brief_id, matrix)


# ---------------------------------------------------------------------------
# Launch gate: go / no-go with sign-offs
# ---------------------------------------------------------------------------
def _gate_row(conn, brief_id: int):
    row = conn.execute("SELECT claims_status, guideline_json, readiness_json, scenarios_json, letters_json, "
                       "compliance_json, launch_json, workflow_json FROM briefs WHERE id = ?", (brief_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
    load = lambda col: json.loads(row[col]) if row[col] else None
    return ({"claims_status": row["claims_status"], "guideline": load("guideline_json"),
             "readiness": load("readiness_json"), "scenarios": load("scenarios_json"),
             "letters": load("letters_json"), "compliance": load("compliance_json"),
             "workflow": load("workflow_json"), "enforce_workflow": ENFORCE_IDEA_WORKFLOW,
             **_actuarial_gate(conn, brief_id)}, load("launch_json"))


@app.get("/api/briefs/{brief_id}/launch-gate")
def get_launch_gate(brief_id: int):
    """Go / no-go status: criteria computed from the brief's artifacts, plus each function's sign-off."""
    with get_connection() as conn:
        data, gate = _gate_row(conn, brief_id)
    return {"brief_id": brief_id, **launch_gate.evaluate(data, gate)}


@app.put("/api/briefs/{brief_id}/launch-gate/{function}")
def sign_launch_gate(brief_id: int, function: str, req: SignOffRequest):
    """Record one function's sign-off. Approving requires every launch criterion to be met."""
    _require_proceed(brief_id)
    with get_connection() as conn:
        data, gate = _gate_row(conn, brief_id)
        try:
            gate = launch_gate.sign(data, gate, function, req.name, req.decision, req.note)
        except KeyError:
            raise HTTPException(status_code=404, detail=f"Unknown function '{function}'")
        except PermissionError as e:
            raise HTTPException(status_code=409, detail=str(e))
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        conn.execute("UPDATE briefs SET launch_json = ? WHERE id = ?", (json.dumps(gate), brief_id))
        conn.commit()
    return {"brief_id": brief_id, **launch_gate.evaluate(data, gate)}


@app.delete("/api/briefs/{brief_id}/launch-gate/{function}")
def withdraw_launch_signoff(brief_id: int, function: str):
    """Withdraw one function's sign-off."""
    with get_connection() as conn:
        data, gate = _gate_row(conn, brief_id)
        try:
            gate = launch_gate.withdraw(gate, function)
        except KeyError:
            raise HTTPException(status_code=404, detail=f"Unknown function '{function}'")
        conn.execute("UPDATE briefs SET launch_json = ? WHERE id = ?", (json.dumps(gate), brief_id))
        conn.commit()
    return {"brief_id": brief_id, **launch_gate.evaluate(data, gate)}


# ---------------------------------------------------------------------------
# Policy form (wording): upload, clauses, exclusion screen against the brief's claims
# ---------------------------------------------------------------------------
def _policy_form_response(brief_id: int, brief: dict, form: Optional[dict]) -> dict:
    screen = None
    if form:
        frames = launch_operations._frames(launch_operations.resolve_basis(brief))
        if frames is not None:
            screen = policy_form.screen_exclusions(form, frames[0])
    return {"brief_id": brief_id, "form": form, "screen": screen, "kinds": policy_form.KINDS}


@app.get("/api/briefs/{brief_id}/policy-form")
def get_policy_form(brief_id: int):
    """The uploaded policy form's clauses (null until uploaded) and the exclusion screen against today's claims."""
    with get_connection() as conn:
        row = conn.execute("SELECT title, brief_json, policy_form_json FROM briefs WHERE id = ?", (brief_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
    brief = json.loads(row["brief_json"]) if row["brief_json"] else {"title": row["title"]}
    return _policy_form_response(brief_id, brief, _form(row))


def _mark_guideline_stale(conn, brief_id: int) -> None:
    """The guideline quoted the old wording (or none): flag it for redrafting, like a change of proxies."""
    conn.execute("""UPDATE briefs SET guideline_json = json_set(guideline_json, '$.stale', json('true'))
                    WHERE id = ? AND guideline_json IS NOT NULL""", (brief_id,))


@app.post("/api/briefs/{brief_id}/policy-form")
def upload_policy_form(brief_id: int, file: UploadFile = File(...)):
    """Upload (or replace) the policy form as PDF, DOCX, TXT or MD. A drafted guideline is flagged for redrafting."""
    data = file.file.read(policy_form.MAX_UPLOAD_BYTES + 1)
    if not data:
        raise HTTPException(status_code=400, detail="The file is empty.")
    if len(data) > policy_form.MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail="The policy form must be under 5 MB.")
    try:
        form = policy_form.build_record(data, file.filename or "policy-form")
    except policy_form.FormError as e:
        raise HTTPException(status_code=400, detail=str(e))
    with get_connection() as conn:
        cursor = conn.cursor()
        _require_brief(cursor, brief_id)
        cursor.execute("UPDATE briefs SET policy_form_json = ? WHERE id = ?", (json.dumps(form), brief_id))
        _mark_guideline_stale(conn, brief_id)
        conn.commit()
    return get_policy_form(brief_id)


@app.delete("/api/briefs/{brief_id}/policy-form")
def delete_policy_form(brief_id: int):
    """Remove the uploaded policy form; a drafted guideline is flagged for redrafting."""
    with get_connection() as conn:
        cursor = conn.cursor()
        _require_brief(cursor, brief_id)
        cursor.execute("UPDATE briefs SET policy_form_json = NULL WHERE id = ?", (brief_id,))
        _mark_guideline_stale(conn, brief_id)
        conn.commit()
    return get_policy_form(brief_id)


# ---------------------------------------------------------------------------
# Idea workflow: PM -> Claims + Actuarial recommendations -> PM decision
# ---------------------------------------------------------------------------
class TeamReviewRequest(BaseModel):
    recommendation: str = Field(..., description="Support | Support with conditions | Do not support")
    reviewer: str = Field(..., min_length=1, max_length=120)
    rationale: str = Field(..., min_length=1, max_length=4000)


class PMDecisionRequest(BaseModel):
    decision: str = Field(..., description="Proceed | Revise | Stop")
    by: str = Field(..., min_length=1, max_length=120)
    note: str = Field("", max_length=4000, description="Required for Revise (what to change) and Stop (why).")


def _load_workflow(conn, brief_id: int):
    row = conn.execute("SELECT claims_status, workflow_json FROM briefs WHERE id = ?", (brief_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
    return row, (json.loads(row["workflow_json"]) if row["workflow_json"] else idea_workflow.new())


def _require_proceed(brief_id: int) -> None:
    """Launch-readiness work is locked until the PM decides to proceed with the idea (when the workflow is on)."""
    if not ENFORCE_IDEA_WORKFLOW:
        return
    with get_connection() as conn:
        _, wf = _load_workflow(conn, brief_id)
    if not idea_workflow.is_proceeding(wf):
        raise HTTPException(status_code=409, detail=f"Launch readiness opens once the PM decides to proceed "
                                                    f"(idea status: {idea_workflow.status(wf)}).")


def _workflow_response(brief_id: int, wf: dict) -> dict:
    return {"brief_id": brief_id, "workflow": wf, **idea_workflow.summary(wf), "teams": idea_workflow.TEAMS,
            "recommendations_allowed": list(idea_workflow.RECOMMENDATIONS),
            "decisions_allowed": list(idea_workflow.DECISIONS)}


@app.get("/api/briefs/{brief_id}/workflow")
def get_workflow(brief_id: int):
    """Where the idea is: team recommendations for the current round, PM decision and history."""
    with get_connection() as conn:
        _, wf = _load_workflow(conn, brief_id)
    return _workflow_response(brief_id, wf)


@app.put("/api/briefs/{brief_id}/workflow/review/{team}")
def submit_team_review(brief_id: int, team: str, req: TeamReviewRequest):
    """A team's recommendation to the PM (claims | actuarial). Can be changed until the PM decides."""
    with get_connection() as conn:
        row, wf = _load_workflow(conn, brief_id)
        try:
            wf = idea_workflow.review(wf, team, req.recommendation, req.reviewer, req.rationale, row["claims_status"])
        except KeyError:
            raise HTTPException(status_code=404, detail=f"Unknown team '{team}'")
        except PermissionError as e:
            raise HTTPException(status_code=409, detail=str(e))
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        conn.execute("UPDATE briefs SET workflow_json = ? WHERE id = ?", (json.dumps(wf), brief_id))
        conn.commit()
    return _workflow_response(brief_id, wf)


@app.put("/api/briefs/{brief_id}/workflow/decision")
def submit_pm_decision(brief_id: int, req: PMDecisionRequest):
    """The PM's decision once both teams have recommended: Proceed, Revise (new review round) or Stop."""
    with get_connection() as conn:
        _, wf = _load_workflow(conn, brief_id)
        try:
            wf = idea_workflow.decide(wf, req.decision, req.by, req.note)
        except PermissionError as e:
            raise HTTPException(status_code=409, detail=str(e))
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        conn.execute("UPDATE briefs SET workflow_json = ? WHERE id = ?", (json.dumps(wf), brief_id))
        conn.commit()
    return _workflow_response(brief_id, wf)


# ---------------------------------------------------------------------------
# Covered-claims set: which historical claims the new coverage would pay (shared by Claims and Actuarial)
# ---------------------------------------------------------------------------
class CoverageOverrideRequest(BaseModel):
    description: str = Field(..., min_length=1, max_length=300, description="Loss description the decision applies to.")
    group: Optional[str] = Field(None, description="newly_covered | still_excluded; null clears the decision.")
    by: str = Field("", max_length=120)
    note: str = Field("", max_length=1000)


def _covered_claims(conn, brief_id: int) -> dict:
    row = conn.execute("SELECT title, brief_json, policy_form_json, coverage_overrides_json FROM briefs WHERE id = ?",
                       (brief_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
    brief = json.loads(row["brief_json"]) if row["brief_json"] else {"title": row["title"]}
    overrides = json.loads(row["coverage_overrides_json"]) if row["coverage_overrides_json"] else {}
    return covered_claims.build(brief, _form(row), overrides)


@app.get("/api/briefs/{brief_id}/covered-claims")
def get_covered_claims(brief_id: int):
    """Which of the pattern's claims the new coverage would pay: already paid, newly covered (incremental cost),
    still excluded by the wording, or not payable for other reasons."""
    with get_connection() as conn:
        return {"brief_id": brief_id, **_covered_claims(conn, brief_id), "groups": covered_claims.GROUPS}


# ---------------------------------------------------------------------------
# Actuarial: rate indication, loss development, rating plan, business plan, memorandum, approval
# ---------------------------------------------------------------------------
def _actuarial_state(conn, brief_id: int) -> dict:
    row = conn.execute("SELECT actuarial_json FROM briefs WHERE id = ?", (brief_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
    return actuarial.load(row["actuarial_json"])


def _save_actuarial(conn, brief_id: int, state: dict) -> None:
    conn.execute("UPDATE briefs SET actuarial_json = ? WHERE id = ?", (json.dumps(state), brief_id))
    conn.commit()


def _indication(conn, brief_id: int, overrides: Optional[dict] = None) -> dict:
    """Everything the actuarial sections compute from: {brief, title, state, key, indication, development}. The
    saved assumptions apply first, then *overrides* (what-if values from the UI, not stored)."""
    row = conn.execute("SELECT title, brief_json FROM briefs WHERE id = ?", (brief_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
    brief = json.loads(row["brief_json"]) if row["brief_json"] else {"title": row["title"]}
    state = _actuarial_state(conn, brief_id)
    covered = _covered_claims(conn, brief_id)
    settings = actuarial_settings.load()
    company = actuarial_settings.pricing_defaults(settings)
    merged = {**company, **state["assumptions"], **(overrides or {})}
    basis = launch_operations.resolve_basis(brief)
    key = basis.get("key") if basis["basis"] in ("direct", "proxy") else None
    dev, comp = {}, {}
    if key:
        cap = pricing._clamp("large_loss_cap", float(merged.get("large_loss_cap") or pricing.DEFAULTS["large_loss_cap"]))
        dev = reserving.development(key, merged.get("tail_factor") or 1.0)
        comp = claims_analytics.get_loss_composition(key, cap)
    ind = pricing.rate_indication(brief.get("claims_analytics") or {}, merged, covered,
                                  {"development": dev, "composition": comp, "benchmarks": state["benchmarks"]})
    defaults = pricing.assumptions(brief.get("claims_analytics") or {}, company, comp)
    return {"brief": brief, "title": row["title"], "state": state, "key": key, "indication": ind, "development": dev,
            "covered": covered, "settings": settings, "defaults": defaults,
            "provenance": actuarial_settings.provenance(settings)}


def _actuarial_gate(conn, brief_id: int) -> dict:
    """The launch gate's actuarial inputs: approval status of the indication and the rating-test summary."""
    state = _actuarial_state(conn, brief_id)
    if not state.get("approval") and not state.get("rating_tests"):
        return {"actuarial": actuarial.status(state, None), "rating_tests": rating_tests.summarize(None, None)}
    ctx = _indication(conn, brief_id)
    plan = _rating_plan(ctx) if state.get("rating_tests") else None
    return {"actuarial": actuarial.status(state, ctx["indication"]),
            "rating_tests": rating_tests.summarize(state.get("rating_tests"), plan)}


def _eligible_exposure(key: Optional[str]) -> float:
    """The scope's latest full-year earned exposure: today's book that could buy the cover."""
    if not key:
        return 0.0
    _, _, _, be = claims_analytics._scope_frames(key)
    val_year = claims_analytics._data()["valuation"].year
    by_year = be[be["calendar_year"] < val_year].groupby("calendar_year")["earned_exposure"].sum()
    return float(by_year.iloc[-1]) if len(by_year) else 0.0


def _rating_plan(ctx: dict) -> dict:
    ind = ctx["indication"]
    if not ind.get("available") or not ctx["key"]:
        return {"available": False, "reason": ind.get("reason", "No risk pattern to rate on.")}
    a = ind["assumptions"]
    return rating_plan.build(ctx["key"], actuarial.selected_rate(ctx["state"], ind), a["experience_years"],
                             a["large_loss_cap"], ind["priced_claims"])


def _business_plan(ctx: dict, values: Optional[dict] = None) -> dict:
    ind = ctx["indication"]
    if not ind.get("available"):
        return {"available": False, "reason": ind.get("reason")}
    return business_plan.build(ind, _eligible_exposure(ctx["key"]), actuarial.selected_rate(ctx["state"], ind),
                               {**actuarial_settings.business_plan_defaults(ctx["settings"]),
                                **ctx["state"].get("business_plan", {}), **(values or {})})


@app.get("/api/briefs/{brief_id}/pricing")
def get_rate_indication(brief_id: int, experience_years: Optional[int] = None, months_to_effective: Optional[int] = None,
                        frequency_trend_pct: Optional[float] = None, severity_trend_pct: Optional[float] = None,
                        ulae_pct: Optional[float] = None, expense_ratio_pct: Optional[float] = None,
                        profit_pct: Optional[float] = None, apply_development: Optional[bool] = None,
                        dev_method: Optional[str] = None, tail_factor: Optional[float] = None,
                        large_loss_cap: Optional[float] = None, cat_load_pct: Optional[float] = None,
                        unreported_load_pct: Optional[float] = None, adverse_selection_pct: Optional[float] = None,
                        apply_complement: Optional[bool] = None, price_whole_pattern: Optional[bool] = None):
    """Rate indication for the new coverage (backend.pricing) with the actuary's saved assumptions. Query parameters
    are what-if overrides on top of them and are not stored. Includes the benchmarks and the approval status."""
    overrides = {k: v for k, v in dict(
        experience_years=experience_years, months_to_effective=months_to_effective,
        frequency_trend_pct=frequency_trend_pct, severity_trend_pct=severity_trend_pct, ulae_pct=ulae_pct,
        expense_ratio_pct=expense_ratio_pct, profit_pct=profit_pct, apply_development=apply_development,
        dev_method=dev_method, tail_factor=tail_factor, large_loss_cap=large_loss_cap, cat_load_pct=cat_load_pct,
        unreported_load_pct=unreported_load_pct, adverse_selection_pct=adverse_selection_pct,
        apply_complement=apply_complement, price_whole_pattern=price_whole_pattern).items() if v is not None}
    with get_connection() as conn:
        ctx = _indication(conn, brief_id, overrides)
        saved = _indication(conn, brief_id)["indication"] if overrides else ctx["indication"]
    state = ctx["state"]
    return {"brief_id": brief_id, **ctx["indication"], "saved_assumptions": state["assumptions"],
            "defaults": ctx["defaults"], "provenance": ctx["provenance"],
            "what_if": bool(overrides), "benchmarks": state["benchmarks"],
            "benchmark_types": pricing.BENCHMARK_TYPES, "approval_status": actuarial.status(state, saved)}


class AssumptionsRequest(BaseModel):
    assumptions: Dict[str, Any] = Field(..., description="backend.pricing.DEFAULTS keys; {} resets to the defaults.")


@app.put("/api/briefs/{brief_id}/actuarial/assumptions")
def save_actuarial_assumptions(brief_id: int, req: AssumptionsRequest):
    """The actuary's selected assumptions; every actuarial section is computed with them from now on."""
    with get_connection() as conn:
        state = _actuarial_state(conn, brief_id)
        try:
            actuarial.save_assumptions(state, req.assumptions)
        except (TypeError, ValueError) as e:
            raise HTTPException(status_code=400, detail=str(e))
        _save_actuarial(conn, brief_id, state)
    return {"brief_id": brief_id, "assumptions": state["assumptions"]}


class BenchmarkRequest(BaseModel):
    kind: str = Field(..., description="loss_cost | premium")
    source: str = Field(..., min_length=1, max_length=200)
    value: float = Field(..., gt=0)
    as_of: str = Field(..., description="YYYY-MM-DD the value applies to")
    permissible_loss_ratio_pct: Optional[float] = None
    unit: str = Field("", max_length=80)
    url: str = Field("", max_length=500)
    note: str = Field("", max_length=1000)


@app.post("/api/briefs/{brief_id}/actuarial/benchmarks")
def add_actuarial_benchmark(brief_id: int, req: BenchmarkRequest, request: Request):
    """Record one external benchmark (bureau loss cost, competitor filed rate, reinsurer quote) for the complement."""
    with get_connection() as conn:
        state = _actuarial_state(conn, brief_id)
        try:
            actuarial.add_benchmark(state, req.model_dump(), request.state.user.get("name", ""))
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        _save_actuarial(conn, brief_id, state)
    return {"brief_id": brief_id, "benchmarks": state["benchmarks"]}


class BenchmarkIncludeRequest(BaseModel):
    include: bool


@app.put("/api/briefs/{brief_id}/actuarial/benchmarks/{benchmark_id}")
def include_actuarial_benchmark(brief_id: int, benchmark_id: str, req: BenchmarkIncludeRequest):
    with get_connection() as conn:
        state = _actuarial_state(conn, brief_id)
        try:
            actuarial.set_benchmark_included(state, benchmark_id, req.include)
        except KeyError:
            raise HTTPException(status_code=404, detail="Benchmark not found.")
        _save_actuarial(conn, brief_id, state)
    return {"brief_id": brief_id, "benchmarks": state["benchmarks"]}


@app.delete("/api/briefs/{brief_id}/actuarial/benchmarks/{benchmark_id}")
def remove_actuarial_benchmark(brief_id: int, benchmark_id: str):
    with get_connection() as conn:
        state = _actuarial_state(conn, brief_id)
        try:
            actuarial.remove_benchmark(state, benchmark_id)
        except KeyError:
            raise HTTPException(status_code=404, detail="Benchmark not found.")
        _save_actuarial(conn, brief_id, state)
    return {"brief_id": brief_id, "benchmarks": state["benchmarks"]}


class IndicationApprovalRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    note: str = Field("", max_length=2000)
    selected_premium: Optional[float] = Field(None, gt=0, description="Selected rate; defaults to the indication.")


@app.put("/api/briefs/{brief_id}/actuarial/approval")
def approve_indication(brief_id: int, req: IndicationApprovalRequest):
    """The Lead Actuary approves the indication (with the saved assumptions) and selects the rate."""
    with get_connection() as conn:
        ctx = _indication(conn, brief_id)
        try:
            actuarial.approve(ctx["state"], ctx["indication"], req.name, req.note, req.selected_premium)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        _save_actuarial(conn, brief_id, ctx["state"])
    return {"brief_id": brief_id, **actuarial.status(ctx["state"], ctx["indication"])}


@app.delete("/api/briefs/{brief_id}/actuarial/approval")
def withdraw_indication_approval(brief_id: int):
    with get_connection() as conn:
        state = _actuarial_state(conn, brief_id)
        state["approval"] = None
        _save_actuarial(conn, brief_id, state)
    return {"brief_id": brief_id, **actuarial.status(state, None)}


@app.get("/api/briefs/{brief_id}/loss-development")
def get_loss_development(brief_id: int):
    """Reconstructed reported-count and incurred triangles, chain-ladder and BF ultimates (backend.reserving),
    with the saved tail factor."""
    with get_connection() as conn:
        ctx = _indication(conn, brief_id)
    if not ctx["key"]:
        return {"brief_id": brief_id, "has_data": False,
                "reason": "Loss development needs a risk pattern (direct or proxy) to stand on."}
    return {"brief_id": brief_id, **ctx["development"]}


@app.get("/api/briefs/{brief_id}/rating-plan")
def get_rating_plan(brief_id: int):
    """Base rate and relativities balanced to the selected rate (backend.rating_plan)."""
    with get_connection() as conn:
        ctx = _indication(conn, brief_id)
    return {"brief_id": brief_id, **_rating_plan(ctx)}


@app.get("/api/briefs/{brief_id}/business-plan")
def get_business_plan(brief_id: int, take_up_pct: Optional[float] = None, growth_pct: Optional[float] = None,
                      years: Optional[int] = None, launch_cost: Optional[float] = None,
                      fixed_expense_per_year: Optional[float] = None, quota_share_pct: Optional[float] = None,
                      ceding_commission_pct: Optional[float] = None, premium_to_surplus: Optional[float] = None,
                      investment_yield_pct: Optional[float] = None, loss_payout_years: Optional[float] = None,
                      tax_rate_pct: Optional[float] = None, rate: Optional[float] = None,
                      annual_rate_change_pct: Optional[float] = None):
    """Three-year projection at the selected rate (backend.business_plan); query parameters are what-ifs on top of
    the saved inputs."""
    values = {k: v for k, v in dict(
        take_up_pct=take_up_pct, growth_pct=growth_pct, years=years, launch_cost=launch_cost,
        fixed_expense_per_year=fixed_expense_per_year, quota_share_pct=quota_share_pct,
        ceding_commission_pct=ceding_commission_pct, premium_to_surplus=premium_to_surplus,
        investment_yield_pct=investment_yield_pct, loss_payout_years=loss_payout_years, tax_rate_pct=tax_rate_pct,
        rate=rate, annual_rate_change_pct=annual_rate_change_pct).items() if v is not None}
    with get_connection() as conn:
        ctx = _indication(conn, brief_id)
    return {"brief_id": brief_id, **_business_plan(ctx, values), "saved_inputs": ctx["state"].get("business_plan", {})}


class BusinessPlanRequest(BaseModel):
    inputs: Dict[str, Any] = Field(..., description="backend.business_plan.DEFAULTS keys; {} resets to the defaults.")


@app.put("/api/briefs/{brief_id}/actuarial/business-plan")
def save_business_plan(brief_id: int, req: BusinessPlanRequest):
    with get_connection() as conn:
        state = _actuarial_state(conn, brief_id)
        try:
            clean = business_plan.inputs(req.inputs)
        except (TypeError, ValueError) as e:
            raise HTTPException(status_code=400, detail=str(e))
        state["business_plan"] = {k: clean[k] for k, v in req.inputs.items() if k in clean and v is not None}
        _save_actuarial(conn, brief_id, state)
    return {"brief_id": brief_id, "inputs": state["business_plan"]}


@app.get("/api/briefs/{brief_id}/actuarial-memo")
def get_actuarial_memo(brief_id: int):
    """Draft actuarial memorandum and exhibits for the rate filing (backend.actuarial_memo)."""
    with get_connection() as conn:
        ctx = _indication(conn, brief_id)
        comp = conn.execute("SELECT compliance_json FROM briefs WHERE id = ?", (brief_id,)).fetchone()["compliance_json"]
    matrix = json.loads(comp) if comp else {}
    states = [r["state"] for r in matrix.get("states", []) if r.get("launch")] or None
    status = actuarial.status(ctx["state"], ctx["indication"])
    plan = _rating_plan(ctx)
    extras = {"provenance": ctx["provenance"],
              "rating_tests": rating_tests.summarize(ctx["state"].get("rating_tests"), plan),
              "monitoring": _monitoring(ctx), "parametric": _parametric(ctx) if ctx["state"].get("parametric") else None}
    memo = actuarial_memo.build(ctx["title"], ctx["indication"], ctx["development"], plan,
                                _business_plan(ctx), ctx["state"], status, states, extras)
    return {"brief_id": brief_id, **memo}


@app.put("/api/briefs/{brief_id}/covered-claims/override")
def set_coverage_override(brief_id: int, req: CoverageOverrideRequest):
    """A Claims reviewer decides whether one loss description's coverage-denied claims are covered or excluded,
    replacing the keyword screen (group null clears the decision)."""
    with get_connection() as conn:
        row = conn.execute("SELECT coverage_overrides_json FROM briefs WHERE id = ?", (brief_id,)).fetchone()
        if not row:
            raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
        current = json.loads(row["coverage_overrides_json"]) if row["coverage_overrides_json"] else {}
        try:
            updated = covered_claims.set_override(current, req.description, req.group, req.by, req.note)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        conn.execute("UPDATE briefs SET coverage_overrides_json = ? WHERE id = ?", (json.dumps(updated), brief_id))
        conn.commit()
        return {"brief_id": brief_id, **_covered_claims(conn, brief_id), "groups": covered_claims.GROUPS}


# ---------------------------------------------------------------------------
# Market Radar: news-driven product opportunities with proof (backend/market_radar.py)
# ---------------------------------------------------------------------------
class RadarScanRequest(BaseModel):
    topic: Optional[str] = Field(None, max_length=120, description="Scan one free-text news topic instead of the watchlist.")


@app.get("/api/radar")
def get_market_radar(include_dismissed: bool = False):
    return market_radar.list_signals(include_dismissed)


@app.post("/api/radar/scan")
def scan_market_radar(req: RadarScanRequest):
    topic = (req.topic or "").strip()
    if topic and len(topic) < 4:
        raise HTTPException(status_code=400, detail="Describe the news topic in a few words.")
    # A single topic is quick enough to answer inline; the full scan runs in the background
    result = (market_radar.run_scan("custom", [market_radar.custom_topic(topic)]) if topic
              else market_radar.start_scan_in_background())
    if result["status"] == "offline":
        raise HTTPException(status_code=503, detail=result["message"])
    if result["status"] == "busy":
        raise HTTPException(status_code=409, detail=result["message"])
    return result


def _require_signal(topic_id: str) -> dict:
    sig = market_radar.get_signal(topic_id)
    if sig is None:
        raise HTTPException(status_code=404, detail="Signal not found.")
    return sig


@app.put("/api/radar/signals/{topic_id}/dismiss")
def dismiss_market_signal(topic_id: str):
    _require_signal(topic_id)
    return market_radar.set_status(topic_id, "dismissed")


@app.put("/api/radar/signals/{topic_id}/restore")
def restore_market_signal(topic_id: str):
    _require_signal(topic_id)
    return market_radar.set_status(topic_id, "new")


@app.post("/api/radar/signals/{topic_id}/brief", response_model=BriefRecord, status_code=201)
def brief_from_market_signal(topic_id: str):
    """Open a full decision brief for the signal; the news it was built on goes in as background context."""
    sig = _require_signal(topic_id)
    sources = "\n".join(f"- [{a['source']}] {a['title']} ({a['url']})" for a in sig["articles"][:8])
    context = (f"Market Radar signal: {sig['label']} (score {sig['score']}/100, {sig['recommendation']}).\n"
               f"{sig['rationale']}\n\nNews that triggered it:\n{sources}")[:4000]
    record = create_brief(CreateBriefRequest(title=sig["product_idea"][:150], tag_value=sig["tag_value"],
                                             idea_context=context))
    market_radar.set_status(topic_id, "briefed", record.id)
    return record


# ---------------------------------------------------------------------------
# Company actuarial settings (replace the placeholder defaults, with cited sources)
# ---------------------------------------------------------------------------
class ActuarialSettingsRequest(BaseModel):
    values: Dict[str, Optional[float]]
    sources: Dict[str, str] = Field(default_factory=dict)


@app.get("/api/actuarial/settings")
def get_actuarial_settings():
    s = actuarial_settings.load()
    return {**s, "fields": {k: {"label": v[0], "default": v[1], "min": v[2], "max": v[3]}
                            for k, v in actuarial_settings.FIELDS.items()},
            "derived": {"expense_ratio_pct": round(actuarial_settings.expense_ratio_pct(s), 2),
                        "profit_pct": actuarial_settings.profit_pct(s)}}


@app.put("/api/actuarial/settings")
def save_actuarial_settings(req: ActuarialSettingsRequest, request: Request):
    """The Lead Actuary sets company-level assumptions; each needs its source cited."""
    try:
        actuarial_settings.save(req.values, req.sources, request.state.user.get("name", ""))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return get_actuarial_settings()


# ---------------------------------------------------------------------------
# PolicyCenter rating tests
# ---------------------------------------------------------------------------
def _rating_tests_response(brief_id: int, state: dict, plan: dict) -> dict:
    tests = state.get("rating_tests")
    return {"brief_id": brief_id, "tests": tests, "csv": rating_tests.to_csv(tests) if tests else None,
            "summary": rating_tests.summarize(tests, plan), "statuses": rating_tests.STATUSES}


@app.get("/api/briefs/{brief_id}/rating-tests")
def get_rating_tests(brief_id: int):
    with get_connection() as conn:
        ctx = _indication(conn, brief_id)
    return _rating_tests_response(brief_id, ctx["state"], _rating_plan(ctx))


@app.post("/api/briefs/{brief_id}/actuarial/rating-tests")
def generate_rating_tests(brief_id: int):
    """(Re)generate the PolicyCenter rating test cases from the current rating plan; earlier results are dropped."""
    with get_connection() as conn:
        ctx = _indication(conn, brief_id)
        plan = _rating_plan(ctx)
        try:
            ctx["state"]["rating_tests"] = rating_tests.generate(plan)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        _save_actuarial(conn, brief_id, ctx["state"])
    return _rating_tests_response(brief_id, ctx["state"], plan)


class RatingTestResultRequest(BaseModel):
    actual_premium: Optional[float] = None
    status: Optional[str] = Field(None, description="Blocked | Not run (when no premium is given)")
    tester: str = Field(..., min_length=1, max_length=120)
    note: str = Field("", max_length=1000)


@app.put("/api/briefs/{brief_id}/actuarial/rating-tests/{case_id}")
def record_rating_test(brief_id: int, case_id: str, req: RatingTestResultRequest):
    """Record the premium PolicyCenter produced for one case (pass / fail is computed) or mark it Blocked."""
    with get_connection() as conn:
        state = _actuarial_state(conn, brief_id)
        if not state.get("rating_tests"):
            raise HTTPException(status_code=404, detail="Generate the rating tests first.")
        try:
            rating_tests.record(state["rating_tests"], case_id, req.actual_premium, req.status, req.tester, req.note)
        except KeyError:
            raise HTTPException(status_code=404, detail=f"Case {case_id} not found")
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        _save_actuarial(conn, brief_id, state)
        ctx = _indication(conn, brief_id)
    return _rating_tests_response(brief_id, state, _rating_plan(ctx))


@app.get("/api/briefs/{brief_id}/rating-tests.csv")
def export_rating_tests(brief_id: int):
    from fastapi.responses import PlainTextResponse
    with get_connection() as conn:
        state = _actuarial_state(conn, brief_id)
    if not state.get("rating_tests"):
        raise HTTPException(status_code=404, detail="Generate the rating tests first.")
    return PlainTextResponse(rating_tests.to_csv(state["rating_tests"]), media_type="text/csv")


# ---------------------------------------------------------------------------
# Actual vs expected monitoring
# ---------------------------------------------------------------------------
def _monitoring(ctx: dict) -> dict:
    ind = ctx["indication"]
    if not ind.get("available") or not ctx["key"]:
        return {"available": False, "reason": ind.get("reason", "No risk pattern to monitor.")}
    return monitoring.build(ind, ctx["key"], ctx["covered"], ctx["development"],
                            actuarial.selected_rate(ctx["state"], ind))


@app.get("/api/briefs/{brief_id}/monitoring")
def get_monitoring(brief_id: int):
    """Actual vs expected against the indication (a hold-out backtest before launch), and the monitoring plan."""
    with get_connection() as conn:
        ctx = _indication(conn, brief_id)
    return {"brief_id": brief_id, **_monitoring(ctx)}


# ---------------------------------------------------------------------------
# Parametric pricing
# ---------------------------------------------------------------------------
def _parametric(ctx: dict, config: Optional[dict] = None) -> dict:
    a = ctx["indication"].get("assumptions") or ctx["defaults"]
    return parametric.build(ctx["key"], {**ctx["state"].get("parametric", {}), **(config or {})},
                            a["expense_ratio_pct"], a["profit_pct"])


@app.get("/api/briefs/{brief_id}/parametric")
def get_parametric(brief_id: int, trigger_index: Optional[float] = None, payout: Optional[float] = None,
                   material_loss_index: Optional[float] = None):
    """Parametric price for the brief's perils: burn on company CAT events blended with hazard probabilities."""
    what_if = {k: v for k, v in dict(trigger_index=trigger_index, payout=payout,
                                     material_loss_index=material_loss_index).items() if v is not None}
    with get_connection() as conn:
        ctx = _indication(conn, brief_id)
    return {"brief_id": brief_id, **_parametric(ctx, what_if), "what_if": bool(what_if),
            "saved_config": ctx["state"].get("parametric", {})}


class ParametricRequest(BaseModel):
    config: Dict[str, Any]


@app.put("/api/briefs/{brief_id}/actuarial/parametric")
def save_parametric(brief_id: int, req: ParametricRequest):
    with get_connection() as conn:
        state = _actuarial_state(conn, brief_id)
        try:
            state["parametric"] = parametric.validate_config(req.config)
        except (TypeError, ValueError) as e:
            raise HTTPException(status_code=400, detail=str(e))
        _save_actuarial(conn, brief_id, state)
    return {"brief_id": brief_id, "config": state["parametric"]}


# ---------------------------------------------------------------------------
# External rate data: bureau CSV import and competitor filing leads
# ---------------------------------------------------------------------------
def _launch_states(conn, brief_id: int) -> List[str]:
    comp = conn.execute("SELECT compliance_json FROM briefs WHERE id = ?", (brief_id,)).fetchone()["compliance_json"]
    matrix = json.loads(comp) if comp else {}
    return [r["state"] for r in matrix.get("states", []) if r.get("launch")]


@app.post("/api/briefs/{brief_id}/actuarial/benchmarks/import")
async def import_benchmarks(brief_id: int, request: Request, file: UploadFile = File(...)):
    """Import a bureau / vendor loss-cost CSV as benchmarks (rows outside the launch states are skipped)."""
    raw = await file.read()
    if len(raw) > 2_000_000:
        raise HTTPException(status_code=413, detail="File too large (2 MB max).")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
    with get_connection() as conn:
        state = _actuarial_state(conn, brief_id)
        try:
            result = filing_research.import_csv(state, text, request.state.user.get("name", ""),
                                                _launch_states(conn, brief_id))
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        _save_actuarial(conn, brief_id, state)
    return {"brief_id": brief_id, **result, "benchmarks": state["benchmarks"]}


# ---------------------------------------------------------------------------
# Competitor landscape (backend.competitor_landscape)
# ---------------------------------------------------------------------------
@app.get("/api/briefs/{brief_id}/competitor-landscape")
def get_competitor_landscape(brief_id: int):
    """The last competitor scan for this brief (carriers, coverage, prices, ratings), or none yet."""
    with get_connection() as conn:
        row = conn.execute("SELECT landscape_json FROM briefs WHERE id = ?", (brief_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
    return {"brief_id": brief_id, "landscape": json.loads(row["landscape_json"]) if row["landscape_json"] else None,
            "search_configured": competitor_landscape.tavily_key() is not None,
            "regions": {k: v["label"] for k, v in competitor_landscape.REGIONS.items()}}


class LandscapeRequest(BaseModel):
    region: Literal["US", "IN", "UK", "GLOBAL"] = "US"


@app.post("/api/briefs/{brief_id}/competitor-landscape")
def refresh_competitor_landscape(brief_id: int, req: Optional[LandscapeRequest] = None):
    """Search the web for carriers offering this kind of cover and store the verified result (about a minute)."""
    with get_connection() as conn:
        row = conn.execute("SELECT title, brief_json FROM briefs WHERE id = ?", (brief_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
    context = (json.loads(row["brief_json"] or "{}").get("idea_context") or "")[:1200]
    result = competitor_landscape.build(row["title"], context, region=(req.region if req else "US"))
    if not result.get("configured"):
        raise HTTPException(status_code=400, detail=result["message"])
    with get_connection() as conn:
        conn.execute("UPDATE briefs SET landscape_json = ? WHERE id = ?", (json.dumps(result), brief_id))
        conn.commit()
    return {"brief_id": brief_id, "landscape": result, "search_configured": True}


@app.get("/api/briefs/{brief_id}/filing-leads")
def get_filing_leads(brief_id: int):
    """SERFF Filing Access links for the launch states and web results for comparable rate filings."""
    with get_connection() as conn:
        row = conn.execute("SELECT title, brief_json FROM briefs WHERE id = ?", (brief_id,)).fetchone()
        if not row:
            raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")
        states = _launch_states(conn, brief_id)
    brief = json.loads(row["brief_json"]) if row["brief_json"] else {}
    scope = (brief.get("claims_analytics") or {}).get("scope") or {}
    if not states:  # no launch states chosen yet: the product's ten largest states by exposure
        frames = launch_operations._frames(launch_operations.resolve_basis(brief))
        states = [r["state"] for r in launch_operations.state_footprint(frames[0], frames[2])[:10]] if frames else []
    return {"brief_id": brief_id, **filing_research.filing_leads(row["title"], scope.get("description", ""), states)}
