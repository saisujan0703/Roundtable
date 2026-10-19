"""
Audit log
=========
Who changed what, and when. One row per write request (POST / PUT / PATCH / DELETE) that reaches the API, recorded
by the authentication middleware in backend.main after the request has run, so the outcome (status code) is known:
  at          UTC time the request finished
  email/name/role  the signed-in user (for a sign-in attempt: the email it was made with)
  action      what was done, from the endpoint's name ("save actuarial settings")
  method/path the request itself; brief_id when the path is under /api/briefs/{id}
  status      HTTP status: 2xx done, 4xx refused (400 invalid, 401 bad sign-in, 403 not allowed, 423 locked)
  detail      the JSON request body, with secrets removed and long text cut short; for a file upload, its size only
Rows are append-only: nothing in the API updates or deletes them.
"""
from __future__ import annotations

import json
import re
from datetime import datetime
from typing import Any, Dict, List, Optional

from backend.database import get_connection

WRITE_METHODS = ("POST", "PUT", "PATCH", "DELETE")
SECRET_KEYS = re.compile(r"pass(word)?|token|secret|api_?key|authori[sz]ation", re.I)
MAX_TEXT = 500              # characters kept of any one string value
MAX_DETAIL = 8_000          # characters kept of the whole detail
MAX_LIMIT = 1_000
_BRIEF_ID = re.compile(r"^/api/briefs/(\d+)(?:/|$)")


def init_table() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS audit_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                at TEXT NOT NULL,
                email TEXT,
                name TEXT,
                role TEXT,
                action TEXT NOT NULL,
                method TEXT NOT NULL,
                path TEXT NOT NULL,
                brief_id INTEGER,
                status INTEGER NOT NULL,
                detail TEXT
            )
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_audit_brief ON audit_log (brief_id, id)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_audit_email ON audit_log (email, id)")
        conn.commit()


def redact(value: Any) -> Any:
    """The value with secret fields masked and long strings cut, recursively."""
    if isinstance(value, dict):
        return {k: "***" if SECRET_KEYS.search(str(k)) else redact(v) for k, v in value.items()}
    if isinstance(value, list):
        return [redact(v) for v in value]
    if isinstance(value, str) and len(value) > MAX_TEXT:
        return value[:MAX_TEXT] + f"… [{len(value) - MAX_TEXT} more characters]"
    return value


def describe_body(body: bytes, content_type: str) -> Optional[str]:
    """What the request sent, safe to store: redacted JSON, or the size of anything else (uploads, audio)."""
    if not body:
        return None
    if "json" in (content_type or ""):
        try:
            text = json.dumps(redact(json.loads(body)), ensure_ascii=False, sort_keys=True)
        except ValueError:
            text = "[unreadable JSON body]"
    else:
        text = f"[{(content_type or 'unknown type').split(';')[0]} body, {len(body):,} bytes]"
    return text if len(text) <= MAX_DETAIL else text[:MAX_DETAIL] + "… [cut]"


def action_name(endpoint: Any, method: str, path: str) -> str:
    """Readable action from the endpoint function's name, else the method and path."""
    name = getattr(endpoint, "__name__", None)
    return name.replace("_", " ") if name else f"{method} {path}"


def brief_id_of(path: str) -> Optional[int]:
    m = _BRIEF_ID.match(path)
    return int(m.group(1)) if m else None


def record(*, method: str, path: str, status: int, user: Optional[Dict[str, Any]] = None,
           email: Optional[str] = None, action: Optional[str] = None, detail: Optional[str] = None) -> None:
    user = user or {}
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO audit_log (at, email, name, role, action, method, path, brief_id, status, detail) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (datetime.utcnow().isoformat(timespec="seconds") + "Z", user.get("email") or email, user.get("name"),
             user.get("role"), action or f"{method} {path}", method, path, brief_id_of(path), int(status), detail))
        conn.commit()


def query(brief_id: Optional[int] = None, email: Optional[str] = None, outcome: Optional[str] = None,
          limit: int = 200, before_id: Optional[int] = None) -> List[Dict[str, Any]]:
    """Newest first. *outcome* "ok" = 2xx only, "refused" = 4xx/5xx only. Page back with *before_id*."""
    where, args = [], []
    if brief_id is not None:
        where.append("brief_id = ?")
        args.append(brief_id)
    if email:
        where.append("email = ?")
        args.append(email.strip().lower())
    if outcome == "ok":
        where.append("status < 300")
    elif outcome == "refused":
        where.append("status >= 400")
    if before_id is not None:
        where.append("id < ?")
        args.append(before_id)
    sql = "SELECT * FROM audit_log" + (" WHERE " + " AND ".join(where) if where else "") + " ORDER BY id DESC LIMIT ?"
    args.append(max(1, min(int(limit), MAX_LIMIT)))
    with get_connection() as conn:
        return [dict(r) for r in conn.execute(sql, args).fetchall()]
