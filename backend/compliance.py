"""
Claims Compliance Matrix
========================
One row per state where the product's scope earns exposure: the claim-settlement deadlines (acknowledge,
decide, pay), the extension rule and the rejection / grievance notice, taken from
sources/state_claims_rules.json. Compliance decides which states the product launches in and confirms each
row (correcting the rule where needed); a row is never confirmed by Roundtable.

In India claim settlement is regulated nationally, so every state gets the same rule for the product's line:
the IRDAI Master Circular on Protection of Policyholders' Interests, 2024, or the Employee's Compensation
Act, 1923 for employee's compensation. A 'states' entry in the rules file overrides it for one state.
Deadlines the rule leaves open are blank and must be entered before a row is confirmed.
"""
from __future__ import annotations

import json
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional

RULES_PATH = Path(__file__).resolve().parent.parent / "sources" / "state_claims_rules.json"
STATUSES = ("Not confirmed", "Confirmed")
EDITABLE_RULE_FIELDS = ("acknowledge_days", "decision_days", "payment_days", "acknowledge_trigger", "decision_trigger",
                        "extension_rule", "denial_notice")
DAY_FIELDS = ("acknowledge_days", "decision_days", "payment_days")
DAY_TYPES = ("calendar", "business")


@lru_cache(maxsize=1)
def load_rules() -> Dict[str, Any]:
    return json.loads(RULES_PATH.read_text(encoding="utf-8"))


def rule_for(state: str, products: List[str]) -> Dict[str, Any]:
    """The rule for a state and these products: a state override if one applies, else the line's own national
    rule when every product is on that line, else the national default."""
    rules = load_rules()
    r = (rules.get("states") or {}).get(state)
    if r and (not r.get("lines") or not products or set(r["lines"]) & set(products)):
        return {**r, "placeholder": False}
    for line_rule in (rules.get("lines") or {}).values():
        if products and set(products) <= set(line_rule["lines"]):
            return {**line_rule, "placeholder": False}
    return {**rules["default"], "placeholder": bool(rules["default"].get("placeholder"))}


def build_matrix(plan: Dict[str, Any], products: List[str]) -> Dict[str, Any]:
    """Create the matrix from the operations plan's state footprint. Every state starts as a launch state."""
    rows = []
    for s in plan.get("states") or []:
        r = rule_for(s["state"], products)
        rows.append({
            "state": s["state"], "exposure_share_pct": s["exposure_share_pct"], "claims": s["claims"],
            "launch": True,
            "source": r["source"], "citation": r["citation"], "placeholder": r["placeholder"],
            "verified": r.get("verified"), "verified_url": r.get("verified_url"),
            "verification_note": r.get("verification_note"),
            **{k: r.get(k) for k in ("acknowledge_days", "acknowledge_day_type", "acknowledge_trigger", "decision_days",
                                     "decision_day_type", "decision_trigger", "payment_days", "payment_day_type",
                                     "extension_rule", "denial_notice")},
            "status": "Not confirmed", "confirmed_by": "", "note": "", "edited": False, "updated_at": None,
        })
    return {"generated_at": datetime.utcnow().isoformat(), "products": products, "states": rows}


def update_state(matrix: Dict[str, Any], state: str, fields: Dict[str, Any]) -> Dict[str, Any]:
    """Change one state's launch flag, rule fields, status, confirmer or note.

    Changing a rule field reopens a confirmed row unless the same update confirms it again.
    Confirming requires a confirmer name, and a placeholder rule must be replaced first.
    """
    row = next((r for r in matrix["states"] if r["state"] == state), None)
    if row is None:
        raise KeyError(state)
    rule_changed = False
    for k in EDITABLE_RULE_FIELDS:
        if k in fields and fields[k] is not None and fields[k] != row.get(k):
            v = fields[k]
            if k in DAY_FIELDS:
                v = int(v) if v != "" else None
                if v is not None and not 0 < v <= 365:
                    raise ValueError(f"{k} must be between 1 and 365")
            else:
                v = str(v).strip()[:2000]
            row[k], rule_changed = v, True
    for k in ("acknowledge_day_type", "decision_day_type", "payment_day_type"):
        if fields.get(k) is not None:
            if fields[k] not in DAY_TYPES:
                raise ValueError(f"{k} must be one of {DAY_TYPES}")
            rule_changed |= fields[k] != row.get(k)
            row[k] = fields[k]
    if rule_changed:
        row["edited"], row["placeholder"] = True, False
        row["status"] = "Not confirmed"
    if fields.get("launch") is not None:
        row["launch"] = bool(fields["launch"])
    if fields.get("confirmed_by") is not None:
        row["confirmed_by"] = str(fields["confirmed_by"]).strip()[:120]
    if fields.get("note") is not None:
        row["note"] = str(fields["note"]).strip()[:2000]
    if fields.get("status") is not None:
        if fields["status"] not in STATUSES:
            raise ValueError(f"status must be one of {STATUSES}")
        if fields["status"] == "Confirmed":
            if not row["confirmed_by"]:
                raise ValueError(f"{state}: enter who confirmed the rule before confirming it.")
            if row["placeholder"]:
                raise ValueError(f"{state}: no rule is loaded; enter this state's deadlines and notice first.")
            missing = [k.replace("_days", "") for k in DAY_FIELDS if not row.get(k)]
            if missing:
                raise ValueError(f"{state}: enter the {', '.join(missing)} days first.")
            if any("[TBD" in (row.get(k) or "") for k in EDITABLE_RULE_FIELDS if k not in DAY_FIELDS):
                raise ValueError(f"{state}: replace the [TBD] items in the triggers, extension rule and notice first.")
        row["status"] = fields["status"]
    row["updated_at"] = datetime.utcnow().isoformat()
    return matrix


def summarize(matrix: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    rows = (matrix or {}).get("states") or []
    launch = [r for r in rows if r["launch"]]
    confirmed = [r for r in launch if r["status"] == "Confirmed"]
    return {
        "states": len(rows), "launch_states": len(launch), "confirmed": len(confirmed),
        "placeholders": sum(r["placeholder"] for r in launch),
        "launch_exposure_pct": round(sum(r["exposure_share_pct"] or 0 for r in launch), 1),
        "ready": bool(launch) and len(confirmed) == len(launch),
    }


def state_notices(matrix: Optional[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Per launch state: what {{state_required_notice}} and the deadline merge fields resolve to."""
    def days(n, t):
        return f"{n} {t} day{'s' if n != 1 else ''}" if n else "[TBD]"
    return [{"state": r["state"], "status": r["status"], "citation": r["citation"], "placeholder": r["placeholder"],
             "denial_notice": r["denial_notice"],
             "acknowledge": f"{days(r['acknowledge_days'], r['acknowledge_day_type'])}: "
                            f"{r.get('acknowledge_trigger') or ''}".rstrip(": "),
             "decision": f"{days(r['decision_days'], r['decision_day_type'])} {r.get('decision_trigger') or ''}".strip(),
             "payment": days(r["payment_days"], r["payment_day_type"])}
            for r in (matrix or {}).get("states") or [] if r["launch"]]


def needs_upgrade(matrix: Dict[str, Any]) -> bool:
    """A stored matrix built from rules that have since changed (e.g. the US state rules before India)."""
    products = matrix.get("products") or []
    return any(r.get("source") != rule_for(r["state"], products)["source"] for r in matrix.get("states") or [])


def carry_over(new: Dict[str, Any], old: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Rebuilt matrix (e.g. after the brief's scope changed): keep Compliance's work on states present in both.

    When the governing rule itself changed (a different source), only the launch flag and note carry over:
    the old deadlines and confirmation were for another rule."""
    prev = {r["state"]: r for r in (old or {}).get("states") or []}
    for r in new["states"]:
        o = prev.get(r["state"])
        if o and o.get("source") == r["source"]:
            r.update({k: o[k] for k in o if k not in ("exposure_share_pct", "claims")})
        elif o:
            r.update({k: o[k] for k in ("launch", "note") if k in o})
    return new
