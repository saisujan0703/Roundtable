"""
Actuarial workspace state
=========================
What the Lead Actuary records on a brief, stored in briefs.actuarial_json:

assumptions     the selected pricing assumptions (backend.pricing.DEFAULTS keys); the indication, rating plan,
                business plan and memorandum are all computed with them
benchmarks      external data for the credibility complement: industry loss costs (Insurance Information Bureau
                of India), competitors' published rates, reinsurer quotes (GIC Re and others). Entered by hand with
                their source, because the data behind them is licensed or outside this system
business_plan   the business-plan inputs (backend.business_plan.DEFAULTS keys)
approval        the actuary's approval of the indication: selected rate, name, note, and a fingerprint of the
                inputs it was given against. If the indication changes (new data, other assumptions, a changed
                covered-claims set or benchmark) the approval is stale and the launch gate criterion fails.
"""
from __future__ import annotations

import hashlib
import json
import uuid
from datetime import date, datetime
from typing import Any, Dict, Optional

from backend import pricing
from backend.money import inr

MAX_BENCHMARKS = 12
SELECTION_TOLERANCE_PCT = 5.0   # a selected rate further than this from the indication needs a written reason


def empty() -> Dict[str, Any]:
    return {"assumptions": {}, "benchmarks": [], "business_plan": {}, "approval": None}


def load(raw: Optional[str]) -> Dict[str, Any]:
    state = empty()
    if raw:
        state.update(json.loads(raw))
    return state


def save_assumptions(state: Dict[str, Any], values: Dict[str, Any]) -> Dict[str, Any]:
    """Keep the known pricing assumptions only; pricing.assumptions clamps them when they are used."""
    clean = {}
    for k, v in values.items():
        if k not in pricing.DEFAULTS or v is None:
            continue
        if k in pricing.BOOLS:
            clean[k] = bool(v)
        elif k == "dev_method":
            if v not in pricing.DEV_METHODS:
                raise ValueError(f"dev_method must be one of {pricing.DEV_METHODS}")
            clean[k] = v
        else:
            clean[k] = float(v)
    state["assumptions"] = clean
    return state


def add_benchmark(state: Dict[str, Any], fields: Dict[str, Any], by: str) -> Dict[str, Any]:
    kind = fields.get("kind")
    if kind not in pricing.BENCHMARK_TYPES:
        raise ValueError(f"kind must be one of {tuple(pricing.BENCHMARK_TYPES)}")
    source = (fields.get("source") or "").strip()[:200]
    if not source:
        raise ValueError("Name the source (e.g. 'IIB motor OD statistics, private car, MH, FY2024-25').")
    try:
        value = float(fields.get("value"))
    except (TypeError, ValueError):
        raise ValueError("Enter the benchmark value per exposure.")
    if value <= 0:
        raise ValueError("The benchmark value must be positive.")
    try:
        as_of = date.fromisoformat(str(fields.get("as_of"))[:10])
    except ValueError:
        raise ValueError("Enter the date the benchmark applies to (YYYY-MM-DD); it is trended from there.")
    plr = fields.get("permissible_loss_ratio_pct")
    if kind == "premium":
        plr = float(plr or 65.0)
        if not 20 <= plr <= 100:
            raise ValueError("The permissible loss ratio must be between 20% and 100%.")
    if len(state["benchmarks"]) >= MAX_BENCHMARKS:
        raise ValueError(f"At most {MAX_BENCHMARKS} benchmarks.")
    state["benchmarks"].append({
        "id": uuid.uuid4().hex[:10], "kind": kind, "source": source, "value": value, "as_of": as_of.isoformat(),
        "permissible_loss_ratio_pct": plr if kind == "premium" else None,
        "unit": (fields.get("unit") or "").strip()[:80], "url": (fields.get("url") or "").strip()[:500],
        "note": (fields.get("note") or "").strip()[:1000], "include": True,
        "added_by": by[:120], "added_at": datetime.utcnow().isoformat(),
    })
    return state


def set_benchmark_included(state: Dict[str, Any], benchmark_id: str, include: bool) -> Dict[str, Any]:
    for b in state["benchmarks"]:
        if b["id"] == benchmark_id:
            b["include"] = bool(include)
            return state
    raise KeyError(benchmark_id)


def remove_benchmark(state: Dict[str, Any], benchmark_id: str) -> Dict[str, Any]:
    before = len(state["benchmarks"])
    state["benchmarks"] = [b for b in state["benchmarks"] if b["id"] != benchmark_id]
    if len(state["benchmarks"]) == before:
        raise KeyError(benchmark_id)
    return state


def fingerprint(indication: Dict[str, Any]) -> str:
    """Identifies the indication an approval was given against: its result and everything that produced it."""
    parts = [indication.get("valuation_date"), indication.get("priced_claims"), indication.get("indicated_premium"),
             {k: v for k, v in (indication.get("assumptions") or {}).items()},
             [(r["year"], r["claims"], r["loss_cost_per_exposure"]) for r in indication.get("experience") or []],
             (indication.get("credibility") or {}).get("complement")]
    return hashlib.sha256(json.dumps(parts, sort_keys=True, default=str).encode()).hexdigest()[:16]


def approve(state: Dict[str, Any], indication: Dict[str, Any], name: str, note: str,
            selected_premium: Optional[float]) -> Dict[str, Any]:
    if not indication.get("available"):
        raise ValueError("There is no indication to approve.")
    name, note = name.strip()[:120], note.strip()[:2000]
    if not name:
        raise ValueError("Enter the name of the approving actuary.")
    indicated = indication["indicated_premium"]
    selected = float(selected_premium) if selected_premium else indicated
    if selected <= 0:
        raise ValueError("Select a positive rate: the indication is $0 (no incremental cost in the data), so the "
                         "rate has to come from a benchmark or judgement.")
    deviation = 100 * (selected / indicated - 1) if indicated else None
    if deviation is None and not note:
        raise ValueError("The indication is $0, so the selected rate needs a written basis (benchmark, judgement).")
    if deviation is not None and abs(deviation) > SELECTION_TOLERANCE_PCT and not note:
        raise ValueError(f"The selected rate is {deviation:+.1f}% from the indication; give the reason "
                         "(e.g. market position, rate capping, judgement on thin data).")
    state["approval"] = {"name": name, "note": note, "approved_at": datetime.utcnow().isoformat(),
                         "indicated_premium": indicated, "selected_premium": round(selected, 2),
                         "deviation_pct": round(deviation, 2) if deviation is not None else None,
                         "fingerprint": fingerprint(indication)}
    return state


def status(state: Dict[str, Any], indication: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """{approved, stale, detail, approval} for the launch gate and the UI."""
    ap = state.get("approval")
    if not ap:
        return {"approved": False, "stale": False, "approval": None,
                "detail": "Indication not approved by the Lead Actuary yet (Rate indication section)."}
    if not indication or not indication.get("available"):
        return {"approved": False, "stale": True, "approval": ap,
                "detail": "The approved indication can no longer be computed for this brief."}
    stale = ap.get("fingerprint") != fingerprint(indication)
    return {"approved": not stale, "stale": stale, "approval": ap,
            "detail": (f"Inputs changed since {ap['name']} approved it (indication now "
                       f"{inr(indication['indicated_premium'], True)}, approved {inr(ap['indicated_premium'], True)}); re-approve."
                       if stale else
                       f"Approved by {ap['name']}: selected {inr(ap['selected_premium'], True)} "
                       f"(indicated {inr(ap['indicated_premium'], True)}).")}


def selected_rate(state: Dict[str, Any], indication: Dict[str, Any]) -> float:
    """The approved selected rate when the approval is current, else the indication."""
    st = status(state, indication)
    return st["approval"]["selected_premium"] if st["approved"] else indication["indicated_premium"]
