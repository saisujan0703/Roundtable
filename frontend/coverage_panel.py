"""
Covered-Claims Set panel
========================
Which of the risk pattern's claims the new coverage would pay — already paid today, newly covered (the gap the
product closes, and its incremental cost), still excluded by the wording, or not payable for other reasons.
A Claims reviewer can decide a loss description's coverage question, replacing the keyword screen.
Logic lives in backend/coverage.py; Actuarial uses the same set for the loss cost.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, Optional

import pandas as pd
import streamlit as st

from money import inr


def _md(text: Optional[str]) -> str:
    return (str(text) if text is not None else "").replace("$", "\\$")


def _money(v: Optional[float]) -> str:
    return inr(v, na="—")


def render_covered_claims(brief: Dict[str, Any], data: Optional[Dict[str, Any]],
                          decide: Callable[[Dict[str, Any]], bool]) -> None:
    """*decide({description, group, by, note})* records (group set) or clears (group None) a reviewer decision."""
    st.markdown("#### Covered-claims set")
    st.caption("Which of today's claims the new coverage would pay. The **newly covered** claims are the gap the "
               "product closes and drive its incremental loss cost; Actuarial prices from this same set.")
    if data is None:
        st.error("Could not load the covered-claims set from the backend.")
        return
    if not data.get("has_data"):
        st.info(data.get("reason") or "No claims history to build the covered-claims set from.")
        return

    t, n = data["totals"], data["newly_covered"]
    cols = st.columns(4)
    for col, key in zip(cols, ("already_paid", "newly_covered", "still_excluded", "not_payable")):
        col.metric(t[key]["label"].split(" (")[0], f"{t[key]['claims']:,}",
                   help=t[key]["label"] + (f" · est. {_money(t[key]['estimated_cost'])}"
                                           if t[key]["estimated_cost"] is not None else ""))
    if n["claims"]:
        st.success(f"**Newly covered:** {n['claims']} claims ({n['claims_per_year']} a year, "
                   f"{n['frequency_per_1000']} per 1,000 {n['exposure_unit']}), estimated severity "
                   f"{_money(n['estimated_severity'])}, about {_money(n['estimated_cost_per_year'])} a year — the "
                   "incremental loss cost Actuarial starts from.")
    elif t["still_excluded"]["claims"]:
        st.warning(f"**The wording closes none of the gap:** all {t['still_excluded']['claims']} coverage-denied "
                   "claims are still excluded by its exclusions. If the product is meant to pay them, revise the "
                   "wording, or record a reviewer decision below where the keyword screen is wrong.")
    with st.expander("Assumptions"):
        st.markdown("\n".join(f"- {_md(a)}" for a in data["assumptions"]))

    rows = data["rows"]
    st.dataframe(pd.DataFrame([{
        "Group": r["group_label"], "Loss description": r["description"], "Claims": r["claims"],
        "Why": r["detail"], "Est. cost": _money(r["estimated_cost"]), "Cost basis": r["source"],
    } for r in rows]), hide_index=True, width="stretch")
    if n.get("by_year"):
        st.caption("Newly covered by accident year: " + "; ".join(
            f"{y['year']}{' (partial)' if y['partial_year'] else ''}: {y['claims']} claims, "
            f"{y['frequency_per_1000']} per 1,000" for y in n["by_year"]))

    reviewable = [r for r in rows if r["reviewable"]]
    if not reviewable:
        return
    with st.expander("✍️ Reviewer decision on a loss description (replaces the keyword screen)"):
        descs = list(dict.fromkeys(r["description"] for r in reviewable))
        key = f"cov_{brief['id']}"
        with st.form(key=f"{key}_form", border=False):
            desc = st.selectbox("Loss description (its coverage-denied claims)", descs, key=f"{key}_desc")
            a, b = st.columns(2)
            choice = a.radio("Under the new coverage these claims are", ["Covered", "Excluded", "Clear my decision"],
                             key=f"{key}_choice", horizontal=True)
            by = b.text_input("Decided by", key=f"{key}_by", placeholder="e.g. Claims coverage specialist")
            note = st.text_area("Why", key=f"{key}_note", height=80,
                                placeholder="e.g. 'Cell failure is a sudden failure under C05, not gradual capacity loss'")
            if st.form_submit_button("Save decision", type="primary"):
                group = {"Covered": "newly_covered", "Excluded": "still_excluded"}.get(choice)
                if decide({"description": desc, "group": group, "by": by, "note": note}):
                    st.rerun()
        for d, o in data.get("overrides", {}).items():
            st.caption(f"“{_md(d)}” → **{'covered' if o['group'] == 'newly_covered' else 'excluded'}** "
                       f"by {_md(o['by'])} ({o['at'][:10]}): {_md(o['note'])}")
