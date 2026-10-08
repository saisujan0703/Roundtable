"""
Policy Form (wording) for a brief
=================================
The product's draft or filed policy form, uploaded as PDF, DOCX or text, so Claims works from the real wording
instead of [TBD] placeholders:

- parse      the form into clauses, each tagged as insuring agreement, definition, exclusion, condition or limit
- quote      the guideline and letters quote these clauses (always flagged for Legal to confirm the right one)
- screen     each exclusion against the claims the brief stands on: which of today's claims would it catch?

The screen matches concepts (wear and tear, mechanical breakdown, flood...) between clause wording and claim loss
descriptions / denial reasons. It is a keyword screen to focus the wording review, not a coverage decision.
"""
from __future__ import annotations

import io
import re
import zipfile
from datetime import datetime
from typing import Any, Dict, List, Optional
from xml.etree import ElementTree

MAX_UPLOAD_BYTES = 5 * 1024 * 1024
MAX_TEXT_CHARS = 200_000
MAX_CLAUSE_CHARS = 2_500
KINDS = {"insuring_agreement": "Insuring agreement", "definition": "Definition", "exclusion": "Exclusion",
         "condition": "Condition", "limit": "Limit / deductible", "other": "Other"}

# Section headings -> clause kind (checked in this order)
_KIND_HEADINGS = [
    ("exclusion", ("exclusion", "we do not cover", "we will not pay", "not covered", "losses not insured")),
    ("definition", ("definition",)),
    ("condition", ("condition", "duties after loss", "duties in the event", "notice of loss", "proof of loss",
                   "your duties", "loss settlement", "appraisal", "suit against us", "subrogation", "other insurance")),
    ("limit", ("limit of", "limits of", "deductible", "sublimit", "special limit")),
    ("insuring_agreement", ("insuring agreement", "coverage", "what we cover", "we will pay", "perils insured",
                            "covered property", "covered peril")),
]

# Concepts shared by exclusion wording and claim loss descriptions; each maps to the denial reasons it explains.
# Terms match whole words / phrases; a trailing * matches a word stem (deteriorat* -> deterioration).
CONCEPTS: Dict[str, Dict[str, Any]] = {
    "wear and tear": {"terms": ("wear and tear", "wear-and-tear", "worn", "deteriorat*", "degrad*", "gradual*",
                                "capacity loss", "loss of capacity", "aging", "ageing", "rust", "corrosion", "rot",
                                "decay"), "denials": ("wear_tear_deterioration",)},
    "mechanical / electrical breakdown": {"terms": ("mechanical", "breakdown", "malfunction*", "cell failure",
                                                    "electrical failure", "defect*", "no external cause",
                                                    "manufacturing", "latent"),
                                          "denials": ("mechanical_breakdown_excluded",)},
    "flood / surface water": {"terms": ("flood*", "surface water", "submerged", "submersion", "tidal water",
                                        "overflow of a body", "storm surge"), "denials": ("flood_excluded",)},
    "leakage / seepage": {"terms": ("leak*", "continuous or repeated seepage"), "denials": ()},
    "water backup / sewer": {"terms": ("backup", "back up", "backs up", "sewer*", "drains", "sump"), "denials": ()},
    "theft": {"terms": ("theft", "stolen", "burglary", "larceny"), "denials": ()},
    "collision": {"terms": ("collision", "crash", "rollover", "upset", "rear-end", "rearend"), "denials": ()},
    "fire / thermal event": {"terms": ("fire", "thermal", "smoke", "explosion"), "denials": ()},
    "earth movement": {"terms": ("earthquake", "earth movement", "landslide", "sinkhole", "subsidence"),
                       "denials": ()},
    "neglect / maintenance": {"terms": ("neglect", "maintenance", "failure to maintain", "faulty workmanship",
                                        "improper installation", "poor installation"), "denials": ()},
    "intentional / fraud": {"terms": ("intentional*", "dishonest*", "fraud*", "misrepresent*", "concealment"),
                            "denials": ("fraud_misrepresentation",)},
    "late notice": {"terms": ("prompt notice", "notice of loss", "as soon as practicable", "late notice"),
                    "denials": ("late_notice",)},
    "freezing": {"terms": ("freez*",), "denials": ()},
    "mold": {"terms": ("mold", "mould", "fungus", "fungi"), "denials": ()},
}
_CONCEPT_RES = {name: re.compile("|".join(
    rf"\b{re.escape(t[:-1])}\w*" if t.endswith("*") else rf"\b{re.escape(t)}\b" for t in c["terms"]), re.I)
    for name, c in CONCEPTS.items()}

_HEADING_RE = re.compile(r"^(section\s+[ivx\d]+\b.*|part\s+[a-z\d]+\b.*|[A-Z][A-Z0-9 ,&/'\-–—:()]{3,80})$")
# Page furniture repeated on every page of a printed form
_FOOTER_RE = re.compile(r"^page \d+ of \d+|\bcopyright\b|^[A-Z]{2} \d\d \d\d( \d\d){1,2}$", re.I)
_ITEM_RE = re.compile(r"^\s*(\(?[a-z0-9]{1,3}[.)]|[•\-–])\s+")


# ---------------------------------------------------------------------------
# Text extraction
# ---------------------------------------------------------------------------
class FormError(ValueError):
    pass


def extract_text(data: bytes, filename: str) -> str:
    name = (filename or "").lower()
    if name.endswith(".pdf"):
        try:
            from pypdf import PdfReader
        except ImportError:
            raise FormError("PDF support needs the 'pypdf' package (pip install pypdf); upload DOCX or text instead.")
        try:
            text = "\n".join(p.extract_text() or "" for p in PdfReader(io.BytesIO(data)).pages)
        except Exception as e:
            raise FormError(f"Could not read the PDF: {e}")
        if len(text.strip()) < 200:
            raise FormError("The PDF has almost no text layer (scanned image?). Upload a text PDF, DOCX or .txt.")
    elif name.endswith(".docx"):
        try:
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                root = ElementTree.fromstring(z.read("word/document.xml"))
        except Exception as e:
            raise FormError(f"Could not read the Word document: {e}")
        ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
        text = "\n".join("".join(t.text or "" for t in p.iter(f"{ns}t")) for p in root.iter(f"{ns}p"))
    elif name.endswith((".txt", ".md")):
        text = data.decode("utf-8", errors="replace")
    else:
        raise FormError("Upload the policy form as PDF, DOCX, TXT or MD.")
    return text[:MAX_TEXT_CHARS]


# ---------------------------------------------------------------------------
# Clause parsing
# ---------------------------------------------------------------------------
def _kind_for(heading: str) -> Optional[str]:
    h = heading.lower()
    for kind, keys in _KIND_HEADINGS:
        if any(k in h for k in keys):
            return kind
    return None


def _is_heading(line: str) -> bool:
    s = line.strip()
    if not s or len(s) > 90 or s.endswith((".", ";", ",")):
        return False
    letters = [c for c in s if c.isalpha()]
    upper = letters and sum(c.isupper() for c in letters) / len(letters) > 0.8
    return bool(upper and _HEADING_RE.match(s)) or bool(re.match(r"^(section|part)\s+[ivx\d]+\b", s, re.I))


def parse_clauses(text: str) -> List[Dict[str, Any]]:
    """Split the form into clauses. A clause is a heading's text, or one lettered / numbered item under an
    exclusions or conditions heading (each exclusion is screened on its own)."""
    clauses: List[Dict[str, Any]] = []
    # excl_list: the items that follow belong to a lead-in such as "We do not insure, however, for loss:"
    state = {"section": "Preamble", "kind": "other", "heading": "Preamble", "item": False, "excl_list": False}
    buf: List[str] = []
    excludes = re.compile(r"\bwe (do not|will not) (cover|insure|pay)\b|\bis excluded\b|\bare excluded\b", re.I)

    def flush():
        body = re.sub(r"\s+", " ", " ".join(buf)).strip()
        if len(body) >= 25:
            kind = state["kind"]
            # A listed item under a coverage heading that takes cover away is an exclusion: it opens with
            # exclusion language, or follows an exclusion lead-in
            if kind in ("other", "insuring_agreement") and state["item"] and (
                    state["excl_list"] or excludes.search(body[:90])):
                kind = "exclusion"
            clauses.append({"id": f"C{len(clauses) + 1:02d}", "kind": kind, "section": state["section"],
                            "heading": state["heading"][:120], "text": body[:MAX_CLAUSE_CHARS]})
            if body.endswith(":"):
                # A lead-in (its last sentence) decides what its list is; a nested item lead-in ("c. Caused by:")
                # stays in its parent's list unless it grants cover
                lead = re.split(r"(?<=[.;])\s+", body)[-1]
                nested = (state["item"] and _ITEM_RE.match(body) and state["excl_list"]
                          and not re.search(r"\bwe (will )?(cover|insure)\b", body, re.I))
                state["excl_list"] = bool(excludes.search(lead) or nested)
        buf.clear()

    for raw in text.splitlines():
        line = raw.strip()
        if not line or _FOOTER_RE.search(line):
            continue
        if _is_heading(line):
            flush()
            pretty = line.title() if line.isupper() else line
            kind = _kind_for(line)
            if kind or re.match(r"^(section|part)\s+[ivx\d]+\b", line, re.I):
                # A new section (e.g. EXCLUSIONS, SECTION II)
                state.update(section=pretty, kind=kind or "other", heading=pretty, item=False, excl_list=False)
            else:
                # A sub-heading inside the current section (e.g. "WEAR AND TEAR" under EXCLUSIONS)
                state.update(heading=f"{state['section']} — {pretty}", item=True, excl_list=False)
            continue
        m = _ITEM_RE.match(line)
        if m and buf and state["kind"] != "other":
            flush()
            state.update(heading=f"{state['section']} — {m.group(1).strip('().')}", item=True)
        buf.append(line)
    flush()
    return clauses


def build_record(data: bytes, filename: str) -> Dict[str, Any]:
    text = extract_text(data, filename)
    clauses = parse_clauses(text)
    if not clauses:
        raise FormError("No clauses found in the document.")
    counts = {k: sum(c["kind"] == k for c in clauses) for k in KINDS}
    return {"filename": filename[:200], "uploaded_at": datetime.utcnow().isoformat(), "characters": len(text),
            "clauses": clauses, "counts": counts}


# ---------------------------------------------------------------------------
# Finding clauses for the guideline and letters
# ---------------------------------------------------------------------------
def concepts_in(text: str) -> List[str]:
    return [name for name, rx in _CONCEPT_RES.items() if rx.search(text or "")]


_GIVES_BACK = re.compile(r"\b(is|are) covered[.;]?$|\bwe (do )?(cover|insure|pay)\b|\bdoes not apply\b", re.I)


def _exclusion_concepts(clause: Dict[str, Any]) -> set:
    """Concepts an exclusion takes away. Sentences that give cover back ("unless it results in a fire",
    "direct loss by fire resulting from water damage is covered") are dropped before matching."""
    sentences = re.split(r"(?<=[.;])\s+", clause["text"])
    core = " ".join(s for s in sentences if not _GIVES_BACK.search(s))
    core = re.sub(r"\b(unless|except|however)\b[^.;]*", " ", core, flags=re.I)
    return set(concepts_in(clause["heading"] + " " + core))


def clauses_of(form: Optional[Dict[str, Any]], kind: str) -> List[Dict[str, Any]]:
    """Clauses of one kind, without lead-ins such as "We do not cover loss to the battery:" that only
    introduce a list."""
    return [c for c in (form or {}).get("clauses") or [] if c["kind"] == kind and not c["text"].rstrip().endswith(":")]


def short_name(clause: Dict[str, Any], limit: int = 70) -> str:
    """A clause as a short reason, e.g. 'wear and tear, gradual deterioration, or loss of capacity…'."""
    t = re.sub(r"^\(?[a-z0-9]{1,3}[.)]\s*", "", clause["text"]).strip()
    t = re.sub(r"^(caused by|resulting from|arising out of|any loss caused by)\s+", "", t, flags=re.I)
    t = t.rstrip(".;")
    return t if len(t) <= limit else t[:limit].rsplit(" ", 1)[0] + "…"


def find_clause(form: Optional[Dict[str, Any]], kind: str, about: str) -> Optional[Dict[str, Any]]:
    """The clause of *kind* sharing the most concepts with *about* (e.g. a denial reason), if any share one."""
    wanted = set(concepts_in(about))
    best, score = None, 0
    for c in clauses_of(form, kind):
        has = _exclusion_concepts(c) if kind == "exclusion" else set(concepts_in(c["heading"] + " " + c["text"]))
        s = len(wanted & has)
        if s > score:
            best, score = c, s
    return best


def quote(clause: Dict[str, Any], form: Dict[str, Any], limit: int = 600) -> str:
    text = clause["text"] if len(clause["text"]) <= limit else clause["text"][:limit].rsplit(" ", 1)[0] + " …"
    return f"> {text}\n>\n> — *{clause['heading']}* ({form['filename']}, clause {clause['id']})"


def prompt_excerpt(form: Optional[Dict[str, Any]], max_chars: int = 14_000) -> Optional[str]:
    """Clauses for the model, insuring agreement / exclusions / conditions first."""
    if not form:
        return None
    order = {"insuring_agreement": 0, "exclusion": 1, "condition": 2, "definition": 3, "limit": 4, "other": 5}
    out, used = [], 0
    for c in sorted(form["clauses"], key=lambda c: order[c["kind"]]):
        piece = f"[{c['id']} | {KINDS[c['kind']]} | {c['heading']}]\n{c['text']}\n"
        if used + len(piece) > max_chars:
            break
        out.append(piece)
        used += len(piece)
    return "\n".join(out)


def excluding_clause(form: Optional[Dict[str, Any]], description: str,
                     denial_reason: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """The first exclusion in the form that catches a claim, by its loss description or today's denial reason."""
    desc = set(concepts_in(description))
    for c in clauses_of(form, "exclusion"):
        cc = _exclusion_concepts(c)
        if cc & desc or (denial_reason and any(denial_reason in CONCEPTS[n]["denials"] for n in cc)):
            return c
    return None


# ---------------------------------------------------------------------------
# Exclusion screen against the brief's claims
# ---------------------------------------------------------------------------
def screen_exclusions(form: Dict[str, Any], claims) -> Dict[str, Any]:
    """For each exclusion: today's claims whose description (or denial reason) shares a concept with it.

    *claims* is the pandas frame of claims the brief stands on (backend.operations frames).
    """
    total = len(claims)
    groups = (claims.assign(desc=claims["loss_description"].fillna("(no description)"))
              .groupby("desc").agg(claims=("claim_id", "size"), incurred=("claim_amount", "sum"),
                                   denied=("coverage_denied_flag", "sum")).reset_index())
    group_concepts = {r.desc: set(concepts_in(r.desc)) for r in groups.itertuples()}
    rows = []
    for c in clauses_of(form, "exclusion"):
        cc = _exclusion_concepts(c)
        matched = [r for r in groups.itertuples() if cc & group_concepts[r.desc]]
        denial_codes = [d for name in cc for d in CONCEPTS[name]["denials"]]
        denied_now = int(claims["denial_reason"].isin(denial_codes).sum()) if denial_codes else 0
        n = sum(r.claims for r in matched)
        rows.append({
            "clause_id": c["id"], "heading": c["heading"], "text": c["text"][:400],
            "concepts": sorted(cc),
            "matched_claims": int(n), "matched_share_pct": round(100 * n / total, 1) if total else 0.0,
            "matched_incurred": round(float(sum(r.incurred for r in matched)), 0),
            "denied_today_same_reason": denied_now,
            "descriptions": [{"description": r.desc, "claims": int(r.claims), "incurred": round(float(r.incurred), 0),
                              "concepts": sorted(cc & group_concepts[r.desc])}
                             for r in sorted(matched, key=lambda r: -r.claims)[:6]],
        })
    rows.sort(key=lambda r: -r["matched_claims"])
    uncaught = [{"description": r.desc, "claims": int(r.claims)} for r in groups.sort_values("claims", ascending=False)
                .itertuples() if not any(r.desc in [d["description"] for d in x["descriptions"]] for x in rows)][:6]
    return {"claims_screened": int(total), "exclusions": rows, "not_matched_by_any_exclusion": uncaught,
            "method": "concept keyword screen of clause wording against claim loss descriptions and denial reasons"}
