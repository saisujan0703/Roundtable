"""
Roundtable post-generation verification
=======================================
Deterministic checks run on every piece of LLM-written text before it is saved, against the exact facts
the model was given. No model is involved in checking.

Checks
- numbers    every %, $, ratio and count in the text must match a computed value (within display rounding)
- citations  cited URLs must be sources that were actually retrieved; [n] references must exist
- trend      wording ("significant", "rising", "falling") must agree with the fitted frequency trend
- names      carriers and regulators named in the text must appear in the sources given to the model
- letters    no day counts, phone numbers or e-mail addresses (state rules come only via merge fields), and
             policy clause ids must exist in the uploaded form

Each check returns issues; `report()` turns them into the verification record stored with the artifact and
shown in the UI ("Verified" / "N warnings" / "N issues"). Callers decide the remedy (retry, replace with
the deterministic text, or drop the statement) and record it in the report's `actions`.
"""
from __future__ import annotations

import bisect
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence

ERROR, WARNING = "error", "warning"

# Numbers that are units of measure or conventions, not facts ("per 1,000", "95% range", "12 months")
_CONVENTIONS = {100.0, 1000.0, 95.0, 12.0, 24.0, 90.0}
_SMALL_PLAIN = 10  # plain integers up to this (counts like "three causes", list sizes) aren't checked

_NUM_RE = re.compile(
    r"(?<![\w.\-/])(?P<sign>[-+−])?(?P<cur>[$£€])?\s?"
    r"(?P<int>\d{1,3}(?:,\d{3})+|\d+)(?P<dec>\.\d+)?"
    r"(?:\s?(?P<unit>%|x\b|×|bn\b|million\b|billion\b|thousand\b|[kKmMB]\b))?"
)
_MULT = {"k": 1e3, "K": 1e3, "thousand": 1e3, "m": 1e6, "M": 1e6, "million": 1e6, "B": 1e9, "bn": 1e9, "billion": 1e9}


# ---------------------------------------------------------------------------
# Facts: every number reachable in the inputs the model saw
# ---------------------------------------------------------------------------
class FactNumbers:
    def __init__(self, *sources: Any):
        vals: List[float] = []
        for src in sources:
            self._walk(src, vals)
        base = {abs(v) for v in vals}
        # A fraction in the data may be written as a percent (0.363 -> 36.3%) and vice versa
        expanded = base | {v * 100 for v in base if v <= 10} | {v / 100 for v in base}
        self.values = sorted(expanded)

    @staticmethod
    def _walk(node: Any, out: List[float]) -> None:
        if isinstance(node, bool) or node is None:
            return
        if isinstance(node, (int, float)):
            out.append(float(node))
        elif isinstance(node, str):
            for m in _NUM_RE.finditer(node):
                v = _value(m)
                if v is not None:
                    out.append(v)
        elif isinstance(node, dict):
            for v in node.values():
                FactNumbers._walk(v, out)
        elif isinstance(node, (list, tuple, set)):
            for v in node:
                FactNumbers._walk(v, out)

    def contains(self, value: float, tolerance: float) -> bool:
        i = bisect.bisect_left(self.values, value - tolerance)
        return i < len(self.values) and self.values[i] <= value + tolerance


def _value(m: re.Match) -> Optional[float]:
    try:
        v = float(m.group("int").replace(",", "") + (m.group("dec") or ""))
    except ValueError:
        return None
    return abs(v * _MULT.get(m.group("unit") or "", 1.0))


def _snippet(text: str, start: int, end: int, pad: int = 50) -> str:
    a, b = max(0, start - pad), min(len(text), end + pad)
    return ("…" if a else "") + text[a:b].replace("\n", " ").strip() + ("…" if b < len(text) else "")


def _strip_structure(text: str) -> str:
    """Blank out numbering that isn't a claim: markdown headings, list markers, [n] references, merge fields."""
    text = re.sub(r"(?m)^(\s*#+\s*)\d+\.", lambda m: m.group(1) + "  ", text)
    text = re.sub(r"(?m)^(\s*)\d+\.\s", lambda m: m.group(1) + "   ", text)
    text = re.sub(r"\[\d+(?:\s*[,–-]\s*\d+)*\]", lambda m: " " * len(m.group(0)), text)
    # Bucket labels: "0-30 days", "181-365 days", "365+ days"
    text = re.sub(r"\b\d+\s?(?:[-\u2013]\s?\d+|\+)\s*(?=days|months|years)", lambda m: " " * len(m.group(0)), text)
    text = re.sub(r"\{\{[^}]*\}\}", lambda m: " " * len(m.group(0)), text)
    text = re.sub(r"\b(?:C\d{2,3}|AY|FY|Q[1-4])\s?\d*", lambda m: " " * len(m.group(0)), text)
    return text


def issue(check: str, severity: str, location: str, text: str, detail: str) -> Dict[str, str]:
    return {"check": check, "severity": severity, "location": location, "text": text, "detail": detail}


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------
def check_numbers(text: str, facts: FactNumbers, location: str, severity_plain: str = WARNING) -> List[Dict[str, str]]:
    out = []
    clean = _strip_structure(text or "")
    for m in _NUM_RE.finditer(clean):
        v = _value(m)
        if v is None:
            continue
        unit, has_dec, cur = m.group("unit"), bool(m.group("dec")), m.group("cur")
        plain = not unit and not cur
        if plain and not has_dec and (v <= _SMALL_PLAIN or 1900 <= v <= 2100):
            continue  # small counts and years
        if v in _CONVENTIONS:
            continue
        decimals = len(m.group("dec") or ".")-1
        tol = 0.5 * 10 ** (-decimals) * _MULT.get(unit or "", 1.0) + 1e-9
        if facts.contains(v, tol):
            continue
        out.append(issue("numbers", WARNING if plain else ERROR, location, _snippet(text, m.start(), m.end()),
                         f"{m.group(0).strip()} doesn't match any value Roundtable computed or was given."))
    return out


def check_citation_urls(urls: Iterable[str], allowed: Iterable[str], location: str) -> List[Dict[str, str]]:
    allowed_norm = {_norm_url(u) for u in allowed if u}
    out = []
    for u in urls:
        if not u or u.startswith("sqlite://"):
            continue  # internal analytics reference
        if _norm_url(u) not in allowed_norm:
            out.append(issue("citations", ERROR, location, u, "Cited link was not among the sources retrieved for "
                                                              "this brief (it may be invented)."))
    return out


def _norm_url(u: str) -> str:
    return re.sub(r"^https?://(www\.)?", "", u.strip().lower()).rstrip("/")


def check_bracket_citations(text: str, n_sources: int, location: str) -> List[Dict[str, str]]:
    out = []
    for m in _REF_RE.finditer(text or ""):
        for n in re.findall(r"\d+", m.group(0)):
            if not 1 <= int(n) <= n_sources:
                out.append(issue("citations", ERROR, location, m.group(0), f"Reference [{n}] points to a source "
                                                                           f"that doesn't exist (only {n_sources} were given)."))
    return out


_REF_RE = re.compile(r"\[\d+(?:\s*[,–-]\s*\d+)*\]")


_SENT_RE = re.compile(r"(?<=[.!?])\s+|\n+")
_TREND_CONTEXT = re.compile(r"\b(trend|frequency|growth|grow(s|ing)?|increas\w*|ris(e|es|ing)|surg\w*|upward|"
                            r"declin\w*|decreas\w*|fall(s|ing)?|downward)\b", re.I)
_SIGNIFICANT = re.compile(r"\b(?<!not )(?<!not statistically )(statistically )?significant(ly)?\b", re.I)
_NOT_SIGNIFICANT = re.compile(r"\b((not|no|without|lacks?|lacking|never|nor)\s+(a\s+|any\s+)?(yet\s+)?"
                              r"(statistically\s+)?significant|insignificant|non-?significant|"
                              r"significance (is|was) not)\b", re.I)
_RISING = re.compile(r"\b(rising|increasing|growing|upward|surging|accelerating)\b", re.I)
_FALLING = re.compile(r"\b(falling|declining|decreasing|downward|shrinking)\b", re.I)


def check_trend_wording(text: str, annual_trend_pct: Optional[float], significant: Optional[bool],
                        location: str, other_patterns: Iterable[str] = ()) -> List[Dict[str, str]]:
    """*other_patterns*: names of other risk patterns; a sentence about them isn't about this trend."""
    if annual_trend_pct is None:
        return []
    others = [o.lower() for o in other_patterns if o]
    out = []
    for sent in _SENT_RE.split(text or ""):
        if not _TREND_CONTEXT.search(sent) or any(o in sent.lower() for o in others):
            continue
        if significant is False and _SIGNIFICANT.search(sent) and not _NOT_SIGNIFICANT.search(sent):
            out.append(issue("trend", ERROR, location, sent.strip()[:240],
                             f"Calls the trend significant, but the fitted trend ({annual_trend_pct:+.1f}%/yr) "
                             "is not statistically significant."))
        if "frequency" in sent.lower() or "trend" in sent.lower():
            if annual_trend_pct < 0 and _RISING.search(sent):
                out.append(issue("trend", ERROR, location, sent.strip()[:240],
                                 f"Describes frequency as rising, but the fitted trend is {annual_trend_pct:+.1f}%/yr."))
            if annual_trend_pct > 0 and _FALLING.search(sent):
                out.append(issue("trend", ERROR, location, sent.strip()[:240],
                                 f"Describes frequency as falling, but the fitted trend is {annual_trend_pct:+.1f}%/yr."))
    return out


def _known_names() -> List[str]:
    """Carriers and regulators Roundtable knows by name: curated sources plus major US carriers."""
    names = {"Progressive", "GEICO", "State Farm", "Allstate", "Liberty Mutual", "Travelers", "Nationwide", "Farmers",
             "USAA", "Chubb", "The Hartford", "Erie Insurance", "American Family", "AIG", "Zurich", "Lemonade",
             "Root Insurance", "Hiscox", "Plymouth Rock", "Tesla", "Swiss Re", "Munich Re", "Allianz", "AXA",
             "NAIC", "NHTSA", "FEMA", "NFPA", "IIHS", "NICB", "OSHA", "CPSC", "IRDAI"}
    src = Path(__file__).resolve().parent.parent / "sources"
    items: List[Dict[str, Any]] = []
    for f in ("competitors.json", "regulatory.json"):
        try:
            items += json.loads((src / f).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            pass
    try:
        from backend.evidence_sources import as_file_items
        items += as_file_items()
    except Exception:
        pass
    for d in items:
        n = d.get("competitor_name") or d.get("regulatory_body") or ""
        n = re.split(r"\s[\(/]", n)[0].strip()
        if 2 < len(n) < 40:
            names.add(n)
    return sorted(names, key=len, reverse=True)


def check_names(text: str, source_text: str, location: str) -> List[Dict[str, str]]:
    """Flag carriers/regulators named in *text* that appear nowhere in the sources the model was given."""
    out, src = [], (source_text or "").lower()
    for name in _known_names():
        if re.search(rf"\b{re.escape(name)}\b", text or "") and name.lower() not in src:
            out.append(issue("names", ERROR, location, name, f"Names {name}, which isn't in any source given for "
                                                             "this text."))
    return out


_DAYS_RE = re.compile(r"\b\d+\s*(?:calendar\s+|business\s+|working\s+)?days?\b", re.I)
_PHONE_RE = re.compile(r"(?<!\d)(?:\+?1[\s.-]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}(?!\d)")
_EMAIL_RE = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b")
_CLAUSE_RE = re.compile(r"\b(?:clause\s+)?(C\d{2,3})\b")


def check_letter_rules(body: str, location: str, clause_ids: Optional[Sequence[str]] = None) -> List[Dict[str, str]]:
    out = []
    plain = re.sub(r"\{\{[^}]*\}\}|\[TBD[^\]]*\]", " ", body or "")
    for m in _DAYS_RE.finditer(plain):
        out.append(issue("letters", ERROR, location, _snippet(plain, m.start(), m.end()),
                         "Writes a number of days; state deadlines must come from {{decision_due_date}} / "
                         "{{payment_due_date}} merge fields."))
    for rx, what in ((_PHONE_RE, "phone number"), (_EMAIL_RE, "e-mail address")):
        for m in rx.finditer(plain):
            out.append(issue("letters", ERROR, location, m.group(0),
                             f"Contains {'an' if what[0] in 'aeiou' else 'a'} {what}; contact details come from merge fields, never the model."))
    return out + check_clause_ids(body, clause_ids, location)


def check_clause_ids(text: str, clause_ids: Optional[Sequence[str]], location: str) -> List[Dict[str, str]]:
    known = set(clause_ids or [])
    return [issue("clauses", ERROR, location, m.group(0),
                  f"Cites clause {m.group(1)}, which isn't in the uploaded policy form.")
            for m in _CLAUSE_RE.finditer(text or "") if m.group(1) not in known]


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
def report(issues: List[Dict[str, str]], checked: Dict[str, int], actions: Optional[List[str]] = None,
           method: Optional[str] = None) -> Dict[str, Any]:
    errors = sum(1 for i in issues if i["severity"] == ERROR)
    warnings = len(issues) - errors
    status = "issues" if errors else "warnings" if warnings else "verified"
    return {"status": status, "errors": errors, "warnings": warnings, "issues": issues[:60],
            "checked": checked, "actions": actions or [], "generation_method": method,
            "checked_at": datetime.utcnow().isoformat()}


def feedback(issues: List[Dict[str, str]], limit: int = 12) -> str:
    """Issue list phrased for a retry prompt."""
    lines = [f"- [{i['location']}] {i['detail']} Text: \"{i['text']}\"" for i in issues if i["severity"] == ERROR]
    return ("Your previous answer failed automatic verification. Fix exactly these problems, using only numbers "
            "and sources from the input, and keep everything else:\n" + "\n".join(lines[:limit]))


# ---------------------------------------------------------------------------
# Brief
# ---------------------------------------------------------------------------
def _trend(analytics: Optional[Dict[str, Any]]) -> tuple:
    fit = (analytics or {}).get("frequency_trend_fit") or {}
    return (fit.get("annual_trend_pct"), fit.get("significant")) if fit.get("has_data") else (None, None)


def brief_texts(brief: Dict[str, Any]) -> List[tuple]:
    """(location, text, citation urls) for every model-written field of a brief."""
    items = [("Problem statement", brief.get("problem_statement") or "", [])]
    for sec, label in (("internal_evidence", "Claims evidence"), ("competitor_comparison", "Competitors"),
                       ("regulatory_notes", "Regulatory")):
        for n, ev in enumerate(brief.get(sec) or [], 1):
            items.append((f"{label} #{n}", ev.get("statement") or "",
                          [c.get("source_url") for c in ev.get("citations") or []]))
    items.append(("Recommendation", brief.get("recommendation") or "", []))
    return items


def _analytics_constants() -> List[float]:
    from backend import analytics as an
    return [an.LARGE_LOSS_THRESHOLD, an.MIN_CREDIBLE_CLAIMS]


def verify_brief(brief: Dict[str, Any], analytics: Optional[Dict[str, Any]], retrieved: List[Dict[str, Any]],
                 extra_urls: Iterable[str] = (), computed_text: Iterable[str] = ()) -> List[Dict[str, str]]:
    """All issues in a brief's model-written text. *analytics* and *retrieved* are what the model was given;
    *computed_text* is Python-written text for the same data (the deterministic brief), whose figures count as facts."""
    facts = FactNumbers(analytics or {}, [d.get("text") for d in retrieved], brief.get("title"),
                        list(computed_text), _analytics_constants())
    allowed = [d.get("metadata", {}).get("source_url") for d in retrieved] + list(extra_urls)
    source_text = " ".join([d.get("text", "") + " " + json.dumps(d.get("metadata", {})) for d in retrieved]
                           + [brief.get("title") or "", brief.get("idea_context") or ""])
    pct, sig = _trend(analytics)
    own = set(((analytics or {}).get("basis") or {}).get("proxy_tags") or []) | {brief.get("tag_value")}
    others = [t.get("tag_value") for t in (analytics or {}).get("notable_portfolio_trends") or []
              if t.get("tag_value") not in own] + ["portfolio patterns"]
    out: List[Dict[str, str]] = []
    for loc, text, urls in brief_texts(brief):
        out += check_numbers(text, facts, loc)
        out += check_citation_urls(urls, allowed, loc)
        out += check_trend_wording(text, pct, sig, loc, others)
        out += check_names(text, source_text, loc)
    return out


def checked_counts(texts: Iterable[str]) -> Dict[str, int]:
    numbers = sum(len(list(_NUM_RE.finditer(_strip_structure(t or "")))) for t in texts)
    return {"numbers": numbers}


def brief_checked_counts(brief: Dict[str, Any]) -> Dict[str, int]:
    items = brief_texts(brief)
    return {**checked_counts(t for _, t, _ in items), "statements": len(items),
            "citations": sum(len(u) for _, _, u in items)}


_EVIDENCE_SECTIONS = (("internal_evidence", "Claims evidence"), ("competitor_comparison", "Competitors"),
                      ("regulatory_notes", "Regulatory"))


def drop_uncited(submitted: Dict[str, Any], computed: Optional[Dict[str, Any]] = None) -> tuple:
    """Deal with model statements that have no citation (and don't say 'Insufficient evidence') so one bad statement
    doesn't fail the whole brief's schema check: a claims section is replaced with the computed section of the same
    number, anything else is removed. Returns (cleaned dict, actions)."""
    by_number = {_section_number(e.get("statement")): e for e in (computed or {}).get("internal_evidence") or []}
    actions = []
    for key, label in _EVIDENCE_SECTIONS:
        kept = []
        for ev in submitted.get(key) or []:
            stmt = str((ev or {}).get("statement") or "").strip()
            n = _section_number(stmt)
            if (ev or {}).get("citations") or stmt.lower().startswith("insufficient evidence"):
                kept.append(ev)
            elif key == "internal_evidence" and by_number.get(n):
                kept.append(by_number[n])
                actions.append(f"Replaced uncited claims section {n} with the computed section.")
            else:
                actions.append(f"Removed an uncited {label.lower()} statement: \"{stmt[:120]}\"")
        submitted[key] = kept
    return submitted, actions


def _section_number(statement: str) -> Optional[int]:
    m = re.match(r"\s*#+\s*(\d+)\.", statement or "")
    return int(m.group(1)) if m else None


def remediate_brief(brief: Dict[str, Any], computed: Dict[str, Any], issues: List[Dict[str, str]]) -> tuple:
    """Fix what still fails after the retry. Claims sections and the problem statement / recommendation are
    replaced with the Python-written version; competitor and regulatory statements are removed (their sources
    can't be stood in for). Only ERROR issues trigger a fix. Returns (brief dict, actions)."""
    failing = {i["location"] for i in issues if i["severity"] == ERROR}
    actions = []
    for field, label in (("problem_statement", "Problem statement"), ("recommendation", "Recommendation")):
        if label in failing and computed.get(field):
            brief[field] = computed[field]
            actions.append(f"Replaced the {label.lower()} with the computed version.")
    by_number = {_section_number(e.get("statement")): e for e in computed.get("internal_evidence") or []}
    for key, label in _EVIDENCE_SECTIONS:
        new = []
        for n, ev in enumerate(brief.get(key) or [], 1):
            if f"{label} #{n}" not in failing:
                new.append(ev)
            elif key == "internal_evidence" and by_number.get(_section_number(ev.get("statement"))):
                new.append(by_number[_section_number(ev.get("statement"))])
                actions.append(f"Replaced {label.lower()} #{n} with the computed section.")
            else:
                actions.append(f"Removed {label.lower()} #{n}: \"{str(ev.get('statement'))[:100]}\"")
        brief[key] = new
    return brief, actions
