"""
Launch Gate (go / no-go)
========================
One launch decision for the new coverage, tied to the work products Claims prepared:

criteria   computed from the brief's stored artifacts (finding, guideline, readiness, test scenarios,
           letters, actuarial approval of the rate indication, state compliance matrix); none can be ticked by hand
sign-offs  one per function (Claims, Claims Legal, Compliance, Product, Actuarial, Finance / Reinsurance)

GO needs every criterion met and every function's approval. An approval is given against the current
artifact versions; if any of them changes afterwards, the approval is stale and must be given again.
Any rejection makes the gate NO-GO until that function signs again.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime
from typing import Any, Dict, List, Optional

from backend import compliance, readiness, workflow
from backend import scenarios as test_scenarios
from backend import letters as customer_letters

FUNCTIONS = {
    "claims": "Claims",
    "legal": "Claims Legal",
    "compliance": "Compliance",
    "product": "Product",
    "actuarial": "Actuarial",
    "finance": "Finance / Reinsurance",
}
DECISIONS = ("Approve", "Approve with conditions", "Reject")


def _crit(key: str, label: str, passed: bool, detail: str) -> Dict[str, Any]:
    return {"key": key, "label": label, "passed": bool(passed), "detail": detail}


def criteria(row: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Gate criteria from a briefs row (dict of the JSON columns already parsed)."""
    g, sc, lt = row.get("guideline"), row.get("scenarios"), row.get("letters")
    items, matrix = row.get("readiness"), row.get("compliance")
    gv = test_scenarios.guideline_version(g)
    out = []
    if row.get("enforce_workflow"):
        wf_status = workflow.status(row.get("workflow"))
        out.append(_crit("pm_decision", "PM decided to proceed with the idea", wf_status == workflow.PROCEED,
                         f"Idea status: {wf_status}."))
    out.append(_crit("finding", "Claims finding approved", row.get("claims_status") == "Approved",
                     f"Claims finding is {row.get('claims_status') or 'Draft'}."))

    if not g:
        out.append(_crit("guideline", "Handling guideline approved", False, "Not drafted yet."))
    else:
        ok = g.get("status") == "Approved" and not g.get("stale")
        out.append(_crit("guideline", "Handling guideline approved", ok,
                         "Approved." if ok else ("The brief changed since it was drafted; redraft it." if g.get("stale")
                                                 else f"Guideline is {g.get('status', 'Draft')}.")))

    if items:
        s = readiness.summarize(items)
        out.append(_crit("readiness", "Required readiness items complete", s["ready"],
                         f"{s['required_complete']} of {s['required_total']} required items Done or N/A."))
    else:
        out.append(_crit("readiness", "Required readiness items complete", False, "Checklist not opened yet."))

    if not sc:
        out.append(_crit("scenarios", "ClaimCenter test scenarios all pass", False, "Not generated yet."))
    else:
        s, stale = test_scenarios.summarize(sc), sc.get("guideline_version") != gv
        out.append(_crit("scenarios", "ClaimCenter test scenarios all pass", s["all_passed"] and not stale,
                         ("Built from an older guideline; regenerate and rerun. " if stale else "")
                         + f"{s['pass']} of {s['total']} pass, {s['fail']} fail, {s['blocked']} blocked, "
                           f"{s['not_run']} not run."))

    if not lt:
        out.append(_crit("letters", "Customer letters approved, no [TBD]", False, "Not drafted yet."))
    else:
        ls, stale = lt["letters"], lt.get("guideline_version") != gv
        approved = sum(l["status"] == "Approved" for l in ls)
        tbds = sum(customer_letters.unresolved_tbds(l) for l in ls)
        out.append(_crit("letters", "Customer letters approved, no [TBD]",
                         approved == len(ls) and tbds == 0 and not stale,
                         ("Drafted from an older guideline; redraft. " if stale else "")
                         + f"{approved} of {len(ls)} approved; {tbds} open [TBD] item(s)."))

    act = row.get("actuarial")
    if act is not None:  # computed by the caller from the current indication (backend.actuarial.status)
        out.append(_crit("actuarial", "Rate indication approved by Actuarial on current data", act["approved"],
                         act["detail"]))
    rt = row.get("rating_tests")
    if rt is not None:
        out.append(_crit("rating_tests", "PolicyCenter rating tests all pass", rt["all_passed"],
                         "Not generated yet (Rating tests section)." if not rt["generated"] else
                         ("The rating plan changed since the cases were generated; regenerate and rerun. "
                          if rt["stale"] else "")
                         + f"{rt['pass']} of {rt['total']} pass, {rt['fail']} fail, {rt['blocked']} blocked, "
                           f"{rt['not_run']} not run."))

    if not matrix:
        out.append(_crit("compliance", "State compliance confirmed for every launch state", False,
                         "Compliance matrix not opened yet (Launch operations tab)."))
    else:
        s = compliance.summarize(matrix)
        out.append(_crit("compliance", "State compliance confirmed for every launch state", s["ready"],
                         f"{s['confirmed']} of {s['launch_states']} launch states confirmed"
                         + (f"; {s['placeholders']} still on the NAIC placeholder" if s["placeholders"] else "") + "."))
    return out


def fingerprint(row: Dict[str, Any]) -> str:
    """Identifies the artifact versions a sign-off was given against."""
    g, sc, lt, m = row.get("guideline") or {}, row.get("scenarios") or {}, row.get("letters") or {}, row.get("compliance") or {}
    parts = [row.get("claims_status"), test_scenarios.guideline_version(g), g.get("approved_at"),
             sc.get("generated_at"), lt.get("generated_at"),
             sorted(l.get("approved_at") or "" for l in lt.get("letters", [])),
             sorted([r["state"], r["status"], *(r.get(k) for k in compliance.EDITABLE_RULE_FIELDS)]
                    for r in m.get("states", []) if r["launch"]),
             ((row.get("actuarial") or {}).get("approval") or {}).get("fingerprint"),
             {k: (row.get("rating_tests") or {}).get(k) for k in ("total", "pass", "stale")}]
    return hashlib.sha256(json.dumps(parts, default=str).encode()).hexdigest()[:16]


def evaluate(row: Dict[str, Any], gate: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    crit = criteria(row)
    fp = fingerprint(row)
    signoffs = (gate or {}).get("signoffs") or {}
    views = []
    for key, label in FUNCTIONS.items():
        s = signoffs.get(key)
        stale = bool(s and s["decision"] != "Reject" and s.get("fingerprint") != fp)
        views.append({"function": key, "label": label, **(s or {}), "signed": s is not None, "stale": stale})
    all_met = all(c["passed"] for c in crit)
    rejected = [v for v in views if v.get("decision") == "Reject"]
    approved = [v for v in views if v.get("decision", "").startswith("Approve") and not v["stale"]]
    if rejected:
        status = "NO-GO"
    elif all_met and len(approved) == len(FUNCTIONS):
        status = "GO"
    else:
        status = "NOT READY"
    return {
        "status": status,
        "criteria": crit,
        "criteria_met": sum(c["passed"] for c in crit),
        "signoffs": views,
        "approvals": len(approved),
        "conditions": [{"function": v["label"], "note": v.get("note")} for v in approved
                       if v["decision"] == "Approve with conditions"],
        "functions": FUNCTIONS,
        "decisions": list(DECISIONS),
        "fingerprint": fp,
    }


def sign(row: Dict[str, Any], gate: Optional[Dict[str, Any]], function: str, name: str, decision: str,
         note: str) -> Dict[str, Any]:
    """Record one function's sign-off. Approvals need every criterion met; rejections and conditions need a reason."""
    if function not in FUNCTIONS:
        raise KeyError(function)
    if decision not in DECISIONS:
        raise ValueError(f"decision must be one of {DECISIONS}")
    name, note = name.strip()[:120], note.strip()[:2000]
    if not name:
        raise ValueError("Enter the name of the person signing off.")
    if decision != "Approve" and not note:
        raise ValueError("Give the reason (for a rejection) or the conditions (for a conditional approval).")
    if decision.startswith("Approve"):
        unmet = [c["label"] for c in criteria(row) if not c["passed"]]
        if unmet:
            raise PermissionError("Launch criteria not met: " + "; ".join(unmet) + ".")
    gate = gate or {"signoffs": {}}
    gate["signoffs"][function] = {"name": name, "decision": decision, "note": note,
                                  "signed_at": datetime.utcnow().isoformat(), "fingerprint": fingerprint(row)}
    return gate


def withdraw(gate: Optional[Dict[str, Any]], function: str) -> Dict[str, Any]:
    if function not in FUNCTIONS:
        raise KeyError(function)
    gate = gate or {"signoffs": {}}
    gate["signoffs"].pop(function, None)
    return gate
