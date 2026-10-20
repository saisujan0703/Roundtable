"""
Competitor and regulatory sources added by users
================================================
The curated files sources/competitors.json and sources/regulatory.json are the built-in starting set. Users add
more here, typed in or picked from a web search: each needs a name, a title, a summary in the reviewer's words
and the URL it came from, because the brief may only cite sources with a verifiable URL (backend.llm rule 6).
backend.rag reads both, so an added source is retrievable evidence for every brief from then on.

Web search (Tavily, TAVILY_API_KEY) only proposes candidates; nothing found online is stored until a person has
read it and saved it, with the summary edited to what the page actually says.
"""
from __future__ import annotations

import os
import re
from datetime import date, datetime
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

from backend.database import get_connection

TYPES = ("competitor", "regulatory")
MIN_SUMMARY = 40


class SourceError(ValueError):
    pass


def init_table() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS evidence_sources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_type TEXT NOT NULL,
                name TEXT NOT NULL,
                title TEXT NOT NULL,
                summary TEXT NOT NULL,
                url TEXT NOT NULL,
                date_collected TEXT NOT NULL,
                origin TEXT NOT NULL DEFAULT 'manual',
                added_by TEXT,
                added_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)
        conn.commit()


def _clean(f: Dict[str, Any]) -> Dict[str, Any]:
    kind = f.get("source_type")
    if kind not in TYPES:
        raise SourceError(f"source_type must be one of {TYPES}.")
    name = re.sub(r"\s+", " ", str(f.get("name") or "")).strip()[:120]
    title = re.sub(r"\s+", " ", str(f.get("title") or "")).strip()[:200]
    summary = str(f.get("summary") or "").strip()[:3000]
    url = str(f.get("url") or "").strip()[:500]
    if len(name) < 2:
        raise SourceError("Name the " + ("insurer (e.g. 'ICICI Lombard')." if kind == "competitor"
                                          else "regulator (e.g. 'IRDAI')."))
    if len(title) < 3:
        raise SourceError("Give the " + ("product or page title." if kind == "competitor" else "regulation or bulletin title."))
    if len(summary) < MIN_SUMMARY:
        raise SourceError(f"Summarise what the source says in at least {MIN_SUMMARY} characters: the brief quotes "
                          "and cites this text.")
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise SourceError("Enter the source's web address (http:// or https://); every cited source needs one.")
    try:
        collected = date.fromisoformat(str(f.get("date_collected") or date.today().isoformat())[:10]).isoformat()
    except ValueError:
        raise SourceError("date_collected must be YYYY-MM-DD.")
    origin = f.get("origin") if f.get("origin") in ("manual", "web") else "manual"
    return {"source_type": kind, "name": name, "title": title, "summary": summary, "url": url,
            "date_collected": collected, "origin": origin}


def list_sources(source_type: Optional[str] = None) -> List[Dict[str, Any]]:
    try:
        with get_connection() as conn:
            sql, args = "SELECT * FROM evidence_sources", []
            if source_type:
                sql, args = sql + " WHERE source_type = ?", [source_type]
            return [dict(r) for r in conn.execute(sql + " ORDER BY id DESC", args).fetchall()]
    except Exception:          # table not created yet (rag used on its own)
        return []


def add(fields: Dict[str, Any], by: str) -> Dict[str, Any]:
    s = _clean(fields)
    now = datetime.utcnow().isoformat(timespec="seconds")
    with get_connection() as conn:
        if conn.execute("SELECT 1 FROM evidence_sources WHERE url = ? AND title = ?", (s["url"], s["title"])).fetchone():
            raise SourceError("This source (same address and title) is already saved.")
        cur = conn.execute(
            "INSERT INTO evidence_sources (source_type, name, title, summary, url, date_collected, origin, added_by, "
            "added_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (s["source_type"], s["name"], s["title"], s["summary"], s["url"], s["date_collected"], s["origin"],
             by[:120], now, now))
        conn.commit()
        return dict(conn.execute("SELECT * FROM evidence_sources WHERE id = ?", (cur.lastrowid,)).fetchone())


def update(source_id: int, fields: Dict[str, Any]) -> Dict[str, Any]:
    s = _clean(fields)
    with get_connection() as conn:
        cur = conn.execute(
            "UPDATE evidence_sources SET source_type = ?, name = ?, title = ?, summary = ?, url = ?, date_collected = ?, "
            "updated_at = ? WHERE id = ?",
            (s["source_type"], s["name"], s["title"], s["summary"], s["url"], s["date_collected"],
             datetime.utcnow().isoformat(timespec="seconds"), source_id))
        conn.commit()
        if cur.rowcount == 0:
            raise KeyError(source_id)
        return dict(conn.execute("SELECT * FROM evidence_sources WHERE id = ?", (source_id,)).fetchone())


def delete(source_id: int) -> None:
    with get_connection() as conn:
        cur = conn.execute("DELETE FROM evidence_sources WHERE id = ?", (source_id,))
        conn.commit()
    if cur.rowcount == 0:
        raise KeyError(source_id)


def as_file_items() -> List[Dict[str, Any]]:
    """The added sources in the same shape as the curated JSON files, for backend.rag and backend.verification."""
    out = []
    for s in list_sources():
        common = {"source_url": s["url"], "date_collected": s["date_collected"], "source_type": s["source_type"],
                  "_id": f"src_{s['id']}"}
        if s["source_type"] == "competitor":
            out.append({"competitor_name": s["name"], "product_name": s["title"], "coverage_summary": s["summary"],
                        **common})
        else:
            out.append({"regulatory_body": s["name"], "regulation_title": s["title"], "summary": s["summary"], **common})
    return out


# ---------------------------------------------------------------------------
# Web search for candidates
# ---------------------------------------------------------------------------
def _tavily_key() -> Optional[str]:
    key = (os.environ.get("TAVILY_API_KEY") or "").strip()
    return key if key and key != "your_tavily_api_key_here" else None


def search_web(query: str, source_type: str, known_urls: List[str], max_results: int = 8) -> Dict[str, Any]:
    """Candidate pages for the reviewer to read and save. {"configured", "results": [...], "message"}."""
    if source_type not in TYPES:
        raise SourceError(f"source_type must be one of {TYPES}.")
    query = re.sub(r"\s+", " ", query or "").strip()[:200]
    if len(query) < 3:
        raise SourceError("Type what to search for (e.g. 'EV battery coverage endorsement').")
    key = _tavily_key()
    if not key:
        return {"configured": False, "results": [],
                "message": "Web search is off: set TAVILY_API_KEY in .env. You can still add sources by hand."}
    try:
        from tavily import TavilyClient
    except ImportError:
        return {"configured": False, "results": [], "message": "The 'tavily-python' package is not installed."}
    suffix = (" insurance India add-on cover policy wording" if source_type == "competitor"
              else " India IRDAI regulation circular notification")
    try:
        res = TavilyClient(api_key=key).search(query=query + suffix, search_depth="advanced", max_results=max_results)
    except Exception as e:
        return {"configured": True, "results": [], "message": f"Web search failed: {e}"}
    known = {u.rstrip("/") for u in known_urls}
    results = []
    for r in res.get("results") or []:
        url = (r.get("url") or "").strip()
        if not url or url.rstrip("/") in known:
            continue
        host = urlparse(url).netloc.removeprefix("www.")
        results.append({"title": (r.get("title") or "").strip()[:200], "url": url, "site": host,
                        "snippet": (r.get("content") or "").strip()[:1500],
                        "published": (r.get("published_date") or "")[:10] or None})
    return {"configured": True, "results": results,
            "message": None if results else "No new pages found; try other words."}
