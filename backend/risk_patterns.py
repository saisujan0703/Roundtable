"""
Custom risk patterns
====================
Risk patterns beyond the risk_category_tag values ClaimCenter already sets. A custom pattern is a saved definition
over the claims data: claims whose loss description, loss cause or denial reason mention any of its keywords
(case-insensitive, at a word start, so 'flood' finds 'flooding' but 'ebike' does not find 'webike'), optionally
limited to some products. It gets a key 'custom_<slug>' and is used everywhere a built-in tag is: briefs, proxy
pooling ('custom_ebike_fire+vehiclefire'), pricing, the idea assistant.

A keyword pattern is a screen over free text, not a coded field: the preview shows sample matches so the reviewer
can check what it catches before saving. Patterns in use by a brief cannot be deleted.
"""
from __future__ import annotations

import json
import re
from datetime import datetime
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

from backend.database import get_connection

PREFIX = "custom_"
PRODUCTS = ("PersonalAuto", "BusinessAuto", "HOPHomeowners", "CommercialProperty", "WorkersComp")
TEXT_COLUMNS = ("loss_description", "loss_cause", "denial_reason")
MAX_KEYWORDS = 20
MIN_KEYWORD = 3


class PatternError(ValueError):
    pass


def init_table() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS risk_patterns (
                key TEXT PRIMARY KEY,
                label TEXT NOT NULL,
                keywords_json TEXT NOT NULL,
                products_json TEXT NOT NULL,
                description TEXT,
                created_by TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)
        conn.commit()


def version() -> Tuple[int, str]:
    """Changes whenever a pattern is added, edited or removed (cache key for analytics)."""
    try:
        with get_connection() as conn:
            row = conn.execute("SELECT COUNT(*), COALESCE(MAX(updated_at), '') FROM risk_patterns").fetchone()
        return int(row[0]), str(row[1])
    except Exception:
        return 0, ""


@lru_cache(maxsize=4)
def _load(ver: Tuple[int, str]) -> Dict[str, Dict[str, Any]]:
    try:
        with get_connection() as conn:
            rows = conn.execute("SELECT * FROM risk_patterns ORDER BY label").fetchall()
    except Exception:
        return {}
    return {r["key"]: {"key": r["key"], "label": r["label"], "keywords": json.loads(r["keywords_json"]),
                       "products": json.loads(r["products_json"]), "description": r["description"] or "",
                       "created_by": r["created_by"], "created_at": r["created_at"], "updated_at": r["updated_at"]}
            for r in rows}


def all_patterns() -> Dict[str, Dict[str, Any]]:
    return _load(version())


def get(key: str) -> Optional[Dict[str, Any]]:
    return all_patterns().get(key)


def is_custom(key: str) -> bool:
    return str(key).startswith(PREFIX)


def regex(keywords: List[str]) -> re.Pattern:
    """Any keyword at a word start; spaces, hyphens and underscores in a phrase match each other."""
    parts = [r"[\s_\-]+".join(re.escape(w) for w in re.split(r"[\s_\-]+", k.strip()) if w) for k in keywords]
    return re.compile(r"\b(?:" + "|".join(p for p in parts if p) + ")", re.I)


def clean(label: str, keywords: List[str], products: Optional[List[str]], description: str = "") -> Dict[str, Any]:
    label = (label or "").strip()[:80]
    if len(label) < 3:
        raise PatternError("Give the pattern a name of at least 3 characters (e.g. 'E-bike battery fire').")
    kws, seen = [], set()
    for k in keywords or []:
        k = re.sub(r"\s+", " ", str(k)).strip().lower()[:60]
        if k and k not in seen:
            if len(k) < MIN_KEYWORD:
                raise PatternError(f"Keyword '{k}' is too short: use at least {MIN_KEYWORD} letters so it doesn't "
                                   "match unrelated words.")
            seen.add(k)
            kws.append(k)
    if not kws:
        raise PatternError("Add at least one keyword to find the claims (e.g. 'e-bike', 'scooter', 'lithium').")
    if len(kws) > MAX_KEYWORDS:
        raise PatternError(f"At most {MAX_KEYWORDS} keywords.")
    prods = list(dict.fromkeys(products or []))
    bad = [p for p in prods if p not in PRODUCTS]
    if bad:
        raise PatternError(f"Unknown product(s) {', '.join(bad)}; choose from {', '.join(PRODUCTS)}.")
    return {"label": label, "keywords": kws, "products": prods, "description": (description or "").strip()[:1000]}


def slug(label: str) -> str:
    return PREFIX + (re.sub(r"[^a-z0-9]+", "_", label.lower()).strip("_")[:40] or "pattern")


def save(fields: Dict[str, Any], by: str, key: Optional[str] = None) -> Dict[str, Any]:
    """Create (key None) or update a pattern. Returns it."""
    p = clean(fields.get("label", ""), fields.get("keywords") or [], fields.get("products"), fields.get("description", ""))
    now = datetime.utcnow().isoformat(timespec="microseconds")
    with get_connection() as conn:
        if key is None:
            key, n = slug(p["label"]), 2
            base = key
            while conn.execute("SELECT 1 FROM risk_patterns WHERE key = ?", (key,)).fetchone():
                key, n = f"{base}_{n}", n + 1
            conn.execute("INSERT INTO risk_patterns (key, label, keywords_json, products_json, description, created_by, "
                         "created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                         (key, p["label"], json.dumps(p["keywords"]), json.dumps(p["products"]), p["description"],
                          by[:120], now, now))
        else:
            cur = conn.execute("UPDATE risk_patterns SET label = ?, keywords_json = ?, products_json = ?, description = ?, "
                               "updated_at = ? WHERE key = ?",
                               (p["label"], json.dumps(p["keywords"]), json.dumps(p["products"]), p["description"],
                                now, key))
            if cur.rowcount == 0:
                raise KeyError(key)
        conn.commit()
    return get(key)


def briefs_using(key: str) -> List[int]:
    with get_connection() as conn:
        rows = conn.execute("SELECT id, tag_value, brief_json FROM briefs").fetchall()
    # The key appears as the brief's tag, a proxy tag or part of a pooled analysis key ('a+custom_x')
    word = re.compile(rf"(?<![a-z0-9_]){re.escape(key)}(?![a-z0-9_])")
    return [r["id"] for r in rows
            if key in (r["tag_value"] or "").split("+") or word.search(r["brief_json"] or "")]


def delete(key: str) -> None:
    used = briefs_using(key)
    if used:
        raise PatternError(f"Brief(s) {', '.join('#' + str(i) for i in used)} use this pattern; it can't be deleted.")
    with get_connection() as conn:
        cur = conn.execute("DELETE FROM risk_patterns WHERE key = ?", (key,))
        conn.commit()
    if cur.rowcount == 0:
        raise KeyError(key)
