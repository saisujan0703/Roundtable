"""
Roundtable Guidewire Reference Tools
====================================
Exact-name lookups over the PolicyCenter / ClaimCenter data dictionaries and typelist catalogs, offered
to the LLM as tools (backend.llm_client.agent_call) instead of retrieving chunks up front.

- Each doc is split on its "### Entity: X" / "### Typelist: X" headings into a {name: section} index,
  built once on first use. A lookup returns the whole section, so fields and codes are never cut mid-table.
- search_names() lets the model find the exact name when it only has a business term ("loss cause").
- exists() is the server-side check that names the model cites are real.
"""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple

DOCS_DIR = Path(__file__).resolve().parent.parent

DOCS = {
    ("entity", "PC"): "01_PC_ENTITY_DATA_DICTIONARY.md",
    ("entity", "CC"): "02_CC_ENTITY_DATA_DICTIONARY.md",
    ("typelist", "PC"): "03_PC_TYPELIST_CATALOG.md",
    ("typelist", "CC"): "04_CC_TYPELIST_CATALOG.md",
}
_HEADING = {"entity": "Entity", "typelist": "Typelist"}

MAX_SECTION_CHARS = 6000  # some entities list hundreds of fields; keep a tool result well inside the context
MAX_SEARCH_RESULTS = 15


@lru_cache(maxsize=None)
def _index(kind: str, app: str) -> Dict[str, str]:
    """{lowercased name: section text} for one doc; empty if the doc is missing."""
    path = DOCS_DIR / DOCS[(kind, app)]
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    parts = re.split(rf"^### {_HEADING[kind]}: *(\S+) *$", text, flags=re.MULTILINE)
    # parts = [preamble, name1, body1, name2, body2, ...]
    sections: Dict[str, str] = {}
    for name, body in zip(parts[1::2], parts[2::2]):
        body = body.split("\n---", 1)[0].strip()
        sections[name.lower()] = f"### {_HEADING[kind]}: {name}\n\n{body}"
    return sections


def app_code(app: Any) -> str:
    return "CC" if str(app or "").strip().upper() == "CC" else "PC"


def exists(kind: str, app: str, name: str) -> bool:
    return kind in _HEADING and str(name or "").strip().lower() in _index(kind, app_code(app))


def canonical_name(kind: str, app: str, name: str) -> str:
    """The name as the doc spells it (from the section heading)."""
    section = _index(kind, app_code(app)).get(str(name or "").strip().lower(), "")
    return section.split("\n", 1)[0].split(": ", 1)[-1] if section else str(name)


def _shorten(section: str) -> str:
    if len(section) <= MAX_SECTION_CHARS:
        return section
    return section[:MAX_SECTION_CHARS].rsplit("\n", 1)[0] + "\n\n[... truncated: remaining rows omitted]"


def _lookup(kind: str, name: str, app: str) -> str:
    app = app_code(app)
    section = _index(kind, app).get(str(name or "").strip().lower())
    if section:
        return _shorten(section)
    close = _search(kind, app, name)[:5]
    hint = f" Closest names: {', '.join(close)}." if close else ""
    return f"No {app} {kind} named '{name}'.{hint} Use search_names to find the exact name."


def _search(kind: str, app: str, query: str) -> List[str]:
    """Names ranked by how many query words appear in the name (strongest) or the section text."""
    words = [w for w in re.findall(r"[a-z0-9]+", str(query or "").lower()) if len(w) >= 3]
    if not words:
        return []
    scored: List[Tuple[int, str]] = []
    for key, section in _index(kind, app).items():
        score = sum(3 for w in words if w in key) + sum(1 for w in words if w in section.lower())
        if score:
            scored.append((score, section.split("\n", 1)[0].split(": ", 1)[-1]))
    scored.sort(key=lambda s: (-s[0], s[1]))
    return [name for _, name in scored[:MAX_SEARCH_RESULTS]]


def lookup_entity(name: str, app: str = "PC") -> str:
    return _lookup("entity", name, app)


def lookup_typelist(name: str, app: str = "PC") -> str:
    return _lookup("typelist", name, app)


def search_names(query: str, kind: str = "entity", app: str = "PC") -> str:
    kind = "typelist" if str(kind).lower() == "typelist" else "entity"
    app = app_code(app)
    names = _search(kind, app, query)
    return (f"{app} {kind} names matching '{query}': {', '.join(names)}" if names
            else f"No {app} {kind} names match '{query}'.")


_APP_PROP = {"type": "string", "enum": ["PC", "CC"],
             "description": "PC = PolicyCenter (policies, coverages), CC = ClaimCenter (claims, exposures, losses)."}

TOOLS: List[Dict[str, Any]] = [
    {
        "name": "lookup_entity",
        "description": "Get one Guidewire entity's definition: database table, fields with types and typelists, "
                       "foreign keys and child arrays. Needs the exact entity name (e.g. PersonalAutoLine, Exposure).",
        "input_schema": {"type": "object", "properties": {"name": {"type": "string"}, "app": _APP_PROP},
                         "required": ["name", "app"]},
    },
    {
        "name": "lookup_typelist",
        "description": "Get one Guidewire typelist's valid codes with display names (e.g. LossCause, CoverageType). "
                       "Needs the exact typelist name.",
        "input_schema": {"type": "object", "properties": {"name": {"type": "string"}, "app": _APP_PROP},
                         "required": ["name", "app"]},
    },
    {
        "name": "search_names",
        "description": "Find exact entity or typelist names from a business term (e.g. 'loss cause', 'vehicle', "
                       "'rideshare'). Use it before lookup_* when unsure of the name.",
        "input_schema": {"type": "object", "properties": {
            "query": {"type": "string"},
            "kind": {"type": "string", "enum": ["entity", "typelist"]},
            "app": _APP_PROP,
        }, "required": ["query", "kind", "app"]},
    },
]

HANDLERS: Dict[str, Callable[..., str]] = {
    "lookup_entity": lookup_entity,
    "lookup_typelist": lookup_typelist,
    "search_names": search_names,
}
