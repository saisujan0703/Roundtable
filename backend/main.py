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


def init_db() -> None:
    """Ensure the briefs table exists in roundtable.db."""
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
        conn.commit()


# Ensure table is ready at import time
init_db()


# ---------------------------------------------------------------------------
# Request & Response Models
# ---------------------------------------------------------------------------
class CreateBriefRequest(BaseModel):
    title: str = Field(..., max_length=150, example="EV High-Voltage Battery Coverage Gap")
    tag_value: Optional[str] = None


class UpdateClaimsTextRequest(BaseModel):
    claims_finding_text: str = Field(..., description="Human-edited Claims finding text.")


class BriefRecord(BaseModel):
    id: int
    title: str
    tag_value: Optional[str] = None
    match_confidence: Optional[float] = None
    claims_finding_text: str
    claims_status: str
    created_at: str
    brief_data: Optional[Dict[str, Any]] = None


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
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, tag_value, claims_finding_text, claims_status, created_at, brief_json "
            "FROM briefs ORDER BY id DESC"
        )
        rows = cursor.fetchall()
        results = []
        for r in rows:
            brief_dict = json.loads(r["brief_json"]) if r["brief_json"] else None
            conf = brief_dict.get("match_confidence") if brief_dict else None
            results.append(
                BriefRecord(
                    id=r["id"],
                    title=r["title"],
                    tag_value=r["tag_value"],
                    match_confidence=conf,
                    claims_finding_text=r["claims_finding_text"],
                    claims_status=r["claims_status"],
                    created_at=r["created_at"],
                    brief_data=brief_dict,
                )
            )
        return results


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
    internal_statements = [
        ev.statement for ev in product_brief.internal_evidence
    ]
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
            INSERT INTO briefs (title, tag_value, claims_finding_text, claims_status, created_at, brief_json)
            VALUES (?, ?, ?, 'Draft', ?, ?)
            """,
            (req.title, tag_to_store, claims_finding_text, created_at, brief_json_str),
        )
        conn.commit()
        brief_id = cursor.lastrowid

    return BriefRecord(
        id=brief_id,
        title=req.title,
        tag_value=product_brief.tag_value,
        match_confidence=product_brief.match_confidence,
        claims_finding_text=claims_finding_text,
        claims_status="Draft",
        created_at=created_at,
        brief_data=json.loads(brief_json_str),
    )


@app.get("/api/briefs/{brief_id}", response_model=BriefRecord)
def get_brief(brief_id: int):
    """Fetch a single brief by ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, tag_value, claims_finding_text, claims_status, created_at, brief_json "
            "FROM briefs WHERE id = ?",
            (brief_id,),
        )
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")

        brief_dict = json.loads(row["brief_json"]) if row["brief_json"] else None
        conf = brief_dict.get("match_confidence") if brief_dict else None
        return BriefRecord(
            id=row["id"],
            title=row["title"],
            tag_value=row["tag_value"],
            match_confidence=conf,
            claims_finding_text=row["claims_finding_text"],
            claims_status=row["claims_status"],
            created_at=row["created_at"],
            brief_data=brief_dict,
        )


@app.put("/api/briefs/{brief_id}/claims", response_model=BriefRecord)
def update_claims_finding(brief_id: int, req: UpdateClaimsTextRequest):
    """Allow human Claims adjusters or reviewers to edit/correct the Claims finding text."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM briefs WHERE id = ?", (brief_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")

        cursor.execute(
            "UPDATE briefs SET claims_finding_text = ? WHERE id = ?",
            (req.claims_finding_text, brief_id),
        )
        conn.commit()

    return get_brief(brief_id)


@app.put("/api/briefs/{brief_id}/claims/approve", response_model=BriefRecord)
def approve_claims_finding(brief_id: int):
    """Human Claims reviewer approves the Claims section finding."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM briefs WHERE id = ?", (brief_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")

        cursor.execute(
            "UPDATE briefs SET claims_status = 'Approved' WHERE id = ?",
            (brief_id,),
        )
        conn.commit()

    return get_brief(brief_id)


@app.put("/api/briefs/{brief_id}/claims/reject", response_model=BriefRecord)
def reject_claims_finding(brief_id: int):
    """Human Claims reviewer rejects the Claims section finding."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM briefs WHERE id = ?", (brief_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail=f"Brief #{brief_id} not found")

        cursor.execute(
            "UPDATE briefs SET claims_status = 'Rejected' WHERE id = ?",
            (brief_id,),
        )
        conn.commit()

    return get_brief(brief_id)
