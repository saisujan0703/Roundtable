"""
PolicyCenter rating tests
=========================
Test cases that check the PolicyCenter rating engine (rate book / rate routines) reproduces the approved rating
plan (backend.rating_plan), with the expected premium worked step by step like a rating worksheet.

Cases
  base             every variable at its base level, base deductible, basic limit
  one-at-a-time    each non-base level of each variable, the rest at base (isolates one rate table row)
  deductible       each deductible factor; limit: each increased-limit factor with enough data behind it
  combined         the highest- and lowest-rated combinations, so the multiplication order and rounding are tested

Expected premium = round(base rate x product of factors, 2): factors at 4 decimals, as the plan shows them, and the
premium rounded once to cents. A tester runs each case in PolicyCenter (quote with those characteristics) and records
the premium PolicyCenter produced; a case passes when it is within TOLERANCE of the expected premium.

The cases are tied to the plan they were generated from (fingerprint): if the plan changes (new selected rate,
relativities, data), the stored results are stale and the cases must be regenerated and rerun.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import math
from datetime import datetime
from typing import Any, Dict, List, Optional

TOLERANCE = 0.01
STATUSES = ("Not run", "Pass", "Fail", "Blocked")


def plan_fingerprint(plan: Dict[str, Any]) -> str:
    parts = [plan.get("base_rate"),
             [(v["name"], [(L["level"], L["selected"]) for L in v["levels"]]) for v in plan.get("variables") or []],
             [(r["deductible"], r["factor"]) for r in (plan.get("deductibles") or {}).get("rows") or []],
             [(r["limit"], r["ilf"]) for r in (plan.get("ilfs") or {}).get("rows") or []]]
    return hashlib.sha256(json.dumps(parts, default=str).encode()).hexdigest()[:16]


def _case(cid: str, kind: str, title: str, plan: Dict[str, Any], levels: Dict[str, str],
          deductible: Optional[Dict[str, Any]], limit: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    steps = [{"step": "Base rate", "factor": None, "running": plan["base_rate"]}]
    running = plan["base_rate"]
    for v in plan["variables"]:
        L = next(x for x in v["levels"] if x["level"] == levels[v["name"]])
        running *= L["selected"]
        steps.append({"step": f"{v['label']} = {L['level']}", "factor": L["selected"], "running": round(running, 4)})
    if deductible:
        running *= deductible["factor"]
        steps.append({"step": f"Deductible ${deductible['deductible']:,.0f}", "factor": deductible["factor"],
                      "running": round(running, 4)})
    if limit:
        running *= limit["ilf"]
        steps.append({"step": f"Limit ${limit['limit']:,.0f}", "factor": limit["ilf"], "running": round(running, 4)})
    return {"id": cid, "kind": kind, "title": title, "inputs": {
                **{v["label"]: levels[v["name"]] for v in plan["variables"]},
                "Deductible": deductible["deductible"] if deductible else (plan.get("deductibles") or {}).get("base_deductible"),
                "Limit": limit["limit"] if limit else (plan.get("ilfs") or {}).get("basic_limit")},
            "worksheet": steps, "expected_premium": round(running + 1e-9, 2),
            "status": "Not run", "actual_premium": None, "tester": "", "note": "", "run_at": None}


def generate(plan: Dict[str, Any]) -> Dict[str, Any]:
    if not plan.get("available"):
        raise ValueError(plan.get("reason") or "No rating plan to test.")
    base = dict(plan["base_levels"])
    ded = plan.get("deductibles") or {}
    base_ded = next((r for r in ded.get("rows") or [] if r["base"]), None)
    cases = [_case("RT-001", "base", "Base case: every variable at base", plan, base, base_ded, None)]
    n = 1
    for v in plan["variables"]:
        for L in v["levels"]:
            if L["base"]:
                continue
            n += 1
            cases.append(_case(f"RT-{n:03d}", "one-at-a-time", f"{v['label']} = {L['level']}", plan,
                               {**base, v["name"]: L["level"]}, base_ded, None))
    for r in ded.get("rows") or []:
        if r["base"]:
            continue
        n += 1
        cases.append(_case(f"RT-{n:03d}", "deductible", f"Deductible ${r['deductible']:,.0f}", plan, base, r, None))
    for r in (plan.get("ilfs") or {}).get("rows") or []:
        if r["basic"] or r["thin"]:
            continue
        n += 1
        cases.append(_case(f"RT-{n:03d}", "limit", f"Limit ${r['limit']:,.0f}", plan, base, base_ded, r))
    hi = {v["name"]: max(v["levels"], key=lambda L: L["selected"])["level"] for v in plan["variables"]}
    lo = {v["name"]: min(v["levels"], key=lambda L: L["selected"])["level"] for v in plan["variables"]}
    rows = ded.get("rows") or []
    for label, levels, d in (("Highest-rated combination", hi, min(rows, key=lambda r: r["deductible"]) if rows else None),
                             ("Lowest-rated combination", lo, max(rows, key=lambda r: r["deductible"]) if rows else None)):
        n += 1
        cases.append(_case(f"RT-{n:03d}", "combined", label, plan, levels, d, None))
    return {"generated_at": datetime.utcnow().isoformat(), "plan_fingerprint": plan_fingerprint(plan),
            "base_rate": plan["base_rate"], "tolerance": TOLERANCE, "cases": cases}


def record(tests: Dict[str, Any], case_id: str, actual: Optional[float], status: Optional[str], tester: str,
           note: str) -> Dict[str, Any]:
    case = next((c for c in tests["cases"] if c["id"] == case_id), None)
    if case is None:
        raise KeyError(case_id)
    tester = tester.strip()[:120]
    if not tester:
        raise ValueError("Enter who ran the case in PolicyCenter.")
    if actual is not None:
        if actual < 0 or math.isnan(actual):
            raise ValueError("The PolicyCenter premium must be a non-negative amount.")
        case["actual_premium"] = round(float(actual), 2)
        case["status"] = "Pass" if abs(case["actual_premium"] - case["expected_premium"]) <= tests["tolerance"] else "Fail"
    elif status in ("Blocked", "Not run"):
        case["status"] = status
        case["actual_premium"] = None
    else:
        raise ValueError("Enter the premium PolicyCenter produced, or mark the case Blocked.")
    if case["status"] in ("Fail", "Blocked") and not note.strip():
        raise ValueError("Describe the failure or what blocks the case.")
    case.update({"tester": tester, "note": note.strip()[:1000], "run_at": datetime.utcnow().isoformat()})
    return tests


def summarize(tests: Optional[Dict[str, Any]], plan: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not tests:
        return {"generated": False, "stale": False, "total": 0, "pass": 0, "fail": 0, "blocked": 0, "not_run": 0,
                "all_passed": False}
    stale = bool(plan and plan.get("available") and plan_fingerprint(plan) != tests["plan_fingerprint"])
    count = lambda s: sum(c["status"] == s for c in tests["cases"])
    total = len(tests["cases"])
    return {"generated": True, "stale": stale, "total": total, "pass": count("Pass"), "fail": count("Fail"),
            "blocked": count("Blocked"), "not_run": count("Not run"),
            "all_passed": not stale and total > 0 and count("Pass") == total}


def to_csv(tests: Dict[str, Any]) -> str:
    """One row per case for a PolicyCenter test harness or a QA spreadsheet."""
    keys = sorted({k for c in tests["cases"] for k in c["inputs"]})
    out = io.StringIO()
    w = csv.writer(out)
    w.writerow(["case_id", "kind", "title", *keys, "expected_premium", "actual_premium", "status", "tester", "note"])
    for c in tests["cases"]:
        w.writerow([c["id"], c["kind"], c["title"], *(c["inputs"].get(k) for k in keys), f"{c['expected_premium']:.2f}",
                    "" if c["actual_premium"] is None else f"{c['actual_premium']:.2f}", c["status"], c["tester"],
                    c["note"]])
    return out.getvalue()
