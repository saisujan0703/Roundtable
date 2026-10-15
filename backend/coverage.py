"""
Covered-Claims Set
==================
Which of the brief's historical claims the NEW coverage would pay. Claims (the wording review) and Actuarial
(the loss cost) both use this one definition, so the two workspaces agree.

Every claim of the brief's risk pattern falls in one group:

  already_paid     paid today under existing cover: the new coverage overlaps, no new cost
  newly_covered    denied today for a coverage reason (exclusion / mechanical breakdown / wear and tear / flood /
                   excluded peril) and NOT caught by the new wording's exclusions: the gap the product closes, and
                   its incremental loss cost
  still_excluded   caught by one of the new wording's exclusions (named by clause)
  not_payable      not a coverage question: late notice, fraud, below deductible, coverage not purchased,
                   or still open without payment

Denied claims carry no incurred amount, so what they would have cost is ESTIMATED from paid claims with the same
loss description (or, failing that, the pattern's paid claims). Estimates are labelled as such.
Without an uploaded policy form, every coverage denial counts as newly covered, and that assumption is stated.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

import pandas as pd

from backend import analytics, operations, policy_form

GROUPS = {
    "already_paid": "Already paid today (overlap with existing cover)",
    "newly_covered": "Newly covered (incremental)",
    "still_excluded": "Still excluded by the new wording",
    "not_payable": "Not payable for other reasons",
}
OTHER_REASONS = {"late_notice": "late notice", "fraud_misrepresentation": "fraud / misrepresentation",
                 "coverage_not_purchased": "coverage not purchased", "below_deductible": "below deductible"}


def _r(x, n=1):
    return None if x is None or pd.isna(x) else round(float(x), n)


def _classify(row, form: Optional[Dict[str, Any]]) -> tuple:
    """(group, detail) for one claim."""
    reason = row.denial_reason if isinstance(row.denial_reason, str) else None
    paid = (row.claim_amount or 0) > 0 and not row.coverage_denied_flag
    if paid:
        return "already_paid", "paid under existing cover"
    if reason in analytics.GAP_DENIAL_REASONS:
        clause = policy_form.excluding_clause(form, row.loss_description or "", reason) if form else None
        if clause:
            return "still_excluded", f"{clause['id']}: {policy_form.short_name(clause, 60)}"
        return "newly_covered", f"denied today: {reason.replace('_', ' ')}"
    if reason or isinstance(row.no_payment_reason, str):
        code = reason or row.no_payment_reason
        return "not_payable", OTHER_REASONS.get(code, code.replace("_", " "))
    return "not_payable", "open, nothing paid yet"


REVIEWABLE = ("newly_covered", "still_excluded")  # the coverage question a reviewer can decide


def build(brief: Dict[str, Any], form: Optional[Dict[str, Any]] = None,
          overrides: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """The covered-claims set. *overrides* maps a loss description to a reviewer's decision
    ({"group": "newly_covered" | "still_excluded", "by", "note", "at"}), which replaces the keyword screen for
    that description's coverage-denied claims."""
    basis = operations.resolve_basis(brief)
    if basis["basis"] not in ("direct", "proxy"):
        return {"has_data": False, "basis": basis,
                "reason": "The covered-claims set needs a risk pattern (direct or proxy) to stand on."}
    _, tc, _, be = analytics._scope_frames(basis["key"])
    if tc.empty:
        return {"has_data": False, "basis": basis, "reason": "No claims for this risk pattern."}

    c = tc.copy()
    c["loss_description"] = c["loss_description"].fillna("(no description)")
    groups = [_classify(r, form) for r in c.itertuples()]
    c["group"], c["detail"] = [g for g, _ in groups], [d for _, d in groups]
    c["screen_group"] = c["group"]
    for desc, o in (overrides or {}).items():
        hit = (c["loss_description"] == desc) & c["group"].isin(REVIEWABLE)
        c.loc[hit, "group"] = o["group"]
        c.loc[hit, "detail"] = f"reviewer decision ({o['by']}): {o['note'][:60]}"

    # What a denied claim would have cost: paid claims with the same description, else the pattern's paid claims
    paid = c[c["group"] == "already_paid"]
    by_desc = paid.groupby("loss_description")["claim_amount"].mean()
    pattern_avg = float(paid["claim_amount"].mean()) if len(paid) else None
    # Only the coverage question needs an estimate; "not payable" claims cost nothing either way
    c["est_cost"] = [r.claim_amount if r.group == "already_paid" else
                     by_desc.get(r.loss_description, pattern_avg) if r.group in REVIEWABLE else None
                     for r in c.itertuples()]
    c["est_source"] = ["actual" if r.group == "already_paid" else
                       "—" if r.group not in REVIEWABLE else
                       ("paid claims, same description" if r.loss_description in by_desc.index else
                        "paid claims, whole pattern" if pattern_avg else "no paid claims to estimate from")
                       for r in c.itertuples()]

    valuation = analytics._data()["valuation"]
    expo_by_year = be.groupby("calendar_year")["earned_exposure"].sum()
    total_expo = float(be["earned_exposure"].sum())
    new = c[c["group"] == "newly_covered"]
    by_year = []
    for ay, g in new.groupby("ay"):
        expo = float(expo_by_year.get(ay, 0))
        by_year.append({"year": int(ay), "claims": int(len(g)), "estimated_cost": _r(g["est_cost"].sum(), 0),
                        "earned_exposure": _r(expo, 0),
                        "frequency_per_1000": _r(1000 * len(g) / expo, 3) if expo else None,
                        "partial_year": bool(ay == valuation.year)})
    span_years = max((valuation - c["loss_date"].min()).days / 365.25, 1.0)

    table = (c.groupby(["group", "detail", "loss_description"])
             .agg(claims=("claim_id", "size"), estimated_cost=("est_cost", "sum"), source=("est_source", "first"),
                  screen_group=("screen_group", "first"))
             .reset_index().sort_values(["group", "claims"], ascending=[True, False]))
    return {
        "has_data": True,
        "basis": basis,
        "valuation_date": analytics.valuation_date(),
        "policy_form": form["filename"] if form else None,
        "claims_in_pattern": int(len(c)),
        "assumptions": _assumptions(form, basis),
        "totals": {g: {"label": GROUPS[g], "claims": int((c["group"] == g).sum()),
                       "estimated_cost": _r(c.loc[c["group"] == g, "est_cost"].sum(), 0) if g != "not_payable" else None}
                   for g in GROUPS},
        "newly_covered": {
            "claims": int(len(new)),
            "claims_per_year": _r(len(new) / span_years),
            "frequency_per_1000": _r(1000 * len(new) / total_expo, 3) if total_expo else None,
            "estimated_severity": _r(new["est_cost"].mean(), 0) if len(new) else None,
            "estimated_cost_per_year": _r(new["est_cost"].sum() / span_years, 0) if len(new) else None,
            "estimate_sources": new["est_source"].value_counts().to_dict(),
            "exposure_unit": analytics.get_tag_scope(basis["key"])["exposure_unit"],
            "by_year": by_year,
            # One [accident year, estimated cost, catastrophe?, loss date] per claim, for the CAT / large-loss split
            # in pricing and actual-vs-expected monitoring
            "items": [[int(r.ay), _r(r.est_cost, 2) or 0.0, bool(isinstance(r.cat_code, str) and r.cat_code),
                       r.loss_date.strftime("%Y-%m-%d")] for r in new.itertuples()],
        },
        "rows": [{"group": r.group, "group_label": GROUPS[r.group], "detail": r.detail, "description": r.loss_description,
                  "claims": int(r.claims), "estimated_cost": _r(r.estimated_cost, 0) if r.group != "not_payable" else None,
                  "source": r.source, "reviewable": r.screen_group in REVIEWABLE,
                  "overridden": r.loss_description in (overrides or {}) and r.screen_group in REVIEWABLE}
                 for r in table.itertuples()],
        "overrides": overrides or {},
    }


def _assumptions(form: Optional[Dict[str, Any]], basis: Dict[str, Any]) -> List[str]:
    out = ["The product covers the brief's risk pattern; claims outside it are not in scope.",
           "Claims already paid under existing cover overlap with the new coverage and add no new cost.",
           "Denied claims have no incurred amount: their cost is estimated from paid claims with the same loss "
           "description (or the pattern's paid claims)."]
    if form:
        out.append(f"Exclusions come from the uploaded wording ({form['filename']}), matched by keyword concepts — "
                   "a screen, not a coverage decision.")
    else:
        out.append("No policy wording uploaded: every coverage denial counts as newly covered. Upload the wording "
                   "(Policy wording tab) to apply its exclusions.")
    if basis["basis"] == "proxy":
        out.append(f"Proxy data from {' + '.join(basis['proxy_tags'])}: this product has no claims of its own.")
    out.append("Keyword-screen results can be overridden per loss description by a Claims reviewer's decision.")
    out.append("Synthetic demo data: the method is real, the figures are illustrative.")
    return out


def set_override(overrides: Optional[Dict[str, Any]], description: str, group: Optional[str], by: str,
                 note: str) -> Dict[str, Any]:
    """Record (group given) or clear (group None) a reviewer's coverage decision for one loss description."""
    from datetime import datetime
    overrides = dict(overrides or {})
    if group is None:
        overrides.pop(description, None)
        return overrides
    if group not in REVIEWABLE:
        raise ValueError(f"group must be one of {REVIEWABLE}")
    by, note = by.strip()[:120], note.strip()[:1000]
    if not by or not note:
        raise ValueError("Enter who decided and why; this replaces the keyword screen.")
    overrides[description[:300]] = {"group": group, "by": by, "note": note, "at": datetime.utcnow().isoformat()}
    return overrides
