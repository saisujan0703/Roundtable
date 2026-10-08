"""
Launch Operations panel
=======================
The operational, regulatory and financial setup Claims owns before launch: the state claims compliance matrix
(launch states, deadlines, required notices, Compliance confirmation), adjuster staffing, large-loss and
reinsurance thresholds, statutory reporting lines, Medicare Section 111 and litigation hot spots.
Figures come from backend/operations.py; state rules from sources/state_claims_rules.json via backend/compliance.py.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional

import pandas as pd
import streamlit as st

EDIT_COLUMNS = ("launch", "acknowledge_days", "decision_days", "payment_days", "status", "confirmed_by", "note")


def _md(text: Optional[str]) -> str:
    return (str(text) if text is not None else "").replace("$", "\\$")


def _money(v: Optional[float]) -> str:
    return "n/a" if v is None else f"${v:,.0f}"


def _render_compliance(bid: int, data: Optional[Dict[str, Any]],
                       save_state: Callable[[str, Dict[str, Any]], bool]) -> None:
    st.markdown("#### State claim-handling compliance")
    st.caption("One row per state where this product's scope earns exposure. Untick the states it won't launch in, "
               "then Compliance checks each launch state's deadlines and required denial notice and confirms it. "
               "ClaimCenter diaries, the state-deadline test scenarios and the letters' state merge fields use "
               "these rows.")
    if not data:
        st.error("Could not load the compliance matrix from the backend.")
        return
    m, s = data["matrix"], data["summary"]
    if not m["states"]:
        st.info("No state footprint: this brief has no claims or exposure data to place it in states.")
        return
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Launch states", f"{s['launch_states']} / {s['states']}")
    c2.metric("Confirmed", f"{s['confirmed']} / {s['launch_states']}")
    c3.metric("No state rule loaded", s["placeholders"])
    c4.metric("Exposure covered", f"{s['launch_exposure_pct']}%")
    st.caption(f"⚠️ {data['rules_note']}")
    if s["ready"]:
        st.success("Every launch state's claim-handling rules are confirmed by Compliance.")

    rows = m["states"]
    df = pd.DataFrame([{
        "state": r["state"], "exposure_pct": r["exposure_share_pct"], "claims": r["claims"],
        "launch": r["launch"], "rule": "NAIC placeholder" if r["placeholder"] else ("Edited" if r["edited"] else "Loaded"),
        "acknowledge_days": r["acknowledge_days"], "decision_days": r["decision_days"],
        "payment_days": r["payment_days"], "status": r["status"], "confirmed_by": r["confirmed_by"], "note": r["note"],
    } for r in rows])
    edited = st.data_editor(
        df, key=f"cm_editor_{bid}", hide_index=True, width="stretch", height=min(420, 38 + 35 * len(df)),
        disabled=["state", "exposure_pct", "claims", "rule"],
        column_config={
            "state": st.column_config.TextColumn("State", width="small"),
            "exposure_pct": st.column_config.NumberColumn("Exposure %", format="%.1f"),
            "claims": st.column_config.NumberColumn("Claims"),
            "launch": st.column_config.CheckboxColumn("Launch"),
            "rule": st.column_config.TextColumn("Rule"),
            "acknowledge_days": st.column_config.NumberColumn("Ack. days", min_value=1, max_value=365, step=1),
            "decision_days": st.column_config.NumberColumn("Decision days", min_value=1, max_value=365, step=1),
            "payment_days": st.column_config.NumberColumn("Pay days", min_value=1, max_value=365, step=1),
            "status": st.column_config.SelectboxColumn("Status", options=data["statuses"]),
            "confirmed_by": st.column_config.TextColumn("Confirmed by"),
            "note": st.column_config.TextColumn("Note"),
        })
    if st.button("Save matrix changes", type="primary", key=f"cm_save_{bid}"):
        by_state = {r["state"]: r for r in rows}
        changed, ok = 0, True
        for rec in edited.to_dict("records"):
            old = by_state[rec["state"]]
            fields: Dict[str, Any] = {}
            for col in EDIT_COLUMNS:
                new = rec[col]
                if isinstance(new, float) and pd.isna(new):
                    new = None
                # Plain Python types: the editor hands back numpy values, which JSON can't encode
                if col.endswith("_days") and new is not None:
                    new = int(new)
                elif col == "launch":
                    new = bool(new)
                elif new is not None:
                    new = str(new)
                if new != old.get(col) and not (new in (None, "") and old.get(col) in (None, "")):
                    fields[col] = new
            if fields:
                changed += 1
                ok &= save_state(rec["state"], fields)
        if changed and ok:
            st.rerun()
        elif not changed:
            st.info("No changes to save.")

    with st.expander("📜 Rule detail per launch state (day types, extension rule, required denial notice)"):
        launch = [r for r in rows if r["launch"]]
        pick = st.selectbox("State", [r["state"] for r in launch], key=f"cm_pick_{bid}") if launch else None
        r = next((x for x in launch if x["state"] == pick), None)
        if r:
            st.caption(f"Source: {r['source']} — {r['citation']}"
                       + (" · **NAIC placeholder: enter this state's real rule**" if r["placeholder"] else ""))
            if r.get("verified_url"):
                st.caption(f"Checked against [{r['verified_url']}]({r['verified_url']}) on {r.get('verified')}"
                           + (f" — ⚠️ {r['verification_note']}" if r.get("verification_note") else ""))
            with st.form(key=f"cm_detail_{bid}_{r['state']}", border=False):
                a, b, c = st.columns(3)
                types = data["day_types"]
                ack_t = a.selectbox("Acknowledge: day type", types,
                                    index=types.index(r["acknowledge_day_type"] or "calendar"))
                dec_t = b.selectbox("Decision: day type", types, index=types.index(r["decision_day_type"] or "calendar"))
                pay_t = c.selectbox("Payment: day type", types, index=types.index(r["payment_day_type"] or "calendar"))
                st.caption(f"Decision clock starts {r.get('decision_trigger') or '[TBD]'}.")
                ext = st.text_area("Extension rule", value=r["extension_rule"] or "", height=80)
                notice = st.text_area("Required denial / complaint notice ({{state_required_notice}})",
                                      value=r["denial_notice"] or "", height=110)
                if st.form_submit_button("Save rule", type="primary"):
                    if save_state(r["state"], {"acknowledge_day_type": ack_t, "decision_day_type": dec_t,
                                               "payment_day_type": pay_t, "extension_rule": ext, "denial_notice": notice}):
                        st.rerun()


def _render_staffing(bid: int, plan: Dict[str, Any]) -> None:
    sf = plan.get("staffing") or {}
    st.markdown("#### Adjuster staffing")
    if not sf.get("has_data"):
        st.info("Not enough claims history to estimate staffing.")
        return
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Claims / month", f"{sf['projected_monthly_claims']:.0f}",
              help=f"{sf['claims_last_12_months']} reported in the last 12 months × uptake {sf['volume_factor']}")
    c2.metric("Avg. days open", sf["mean_cycle_days"], help=f"Median {sf['median_cycle_days']} days")
    c3.metric("Open claims at any time", f"{sf['projected_open_inventory']:.0f}")
    c4.metric("Adjusters needed", sf["adjusters_needed"], help=f"{sf['adjusters_needed_fte']} FTE")
    load_source = (f"today’s median across the {sf['observed_adjusters_in_scope']} adjusters handling this scope"
                   if sf["caseload_is_observed"] else "your target")
    groups = ", ".join(f"{g['group']} ({g['share_pct']}%)" for g in sf["handling_groups"])
    st.caption(f"Open inventory = claims per year × average days open ÷ 365. Caseload used: {sf['caseload_used']} open "
               f"claims per adjuster ({load_source}). Handled today by: {groups}.")


def _render_large_losses(plan: Dict[str, Any]) -> None:
    ll = plan.get("large_losses") or {}
    st.markdown("#### Large losses & reinsurance notification")
    if not ll.get("has_data"):
        st.info("No claims history to size large losses.")
        return
    st.caption(f"Claims at or above each candidate notice threshold, over {ll['years_of_data']} years of data. "
               f"Largest claim {_money(ll['largest'])}; 99th percentile {_money(ll['p99'])}. The actual threshold "
               "comes from the treaty terms [TBD — Reinsurance].")
    st.dataframe(pd.DataFrame([{"Threshold": _money(t["threshold"]), "Claims": t["claims"], "Per year": t["per_year"],
                                "Share of incurred %": t["share_of_incurred_pct"]} for t in ll["thresholds"]]),
                 hide_index=True, width="stretch")
    if ll["cat_claims"]:
        st.caption(f"Catastrophe exposure: {ll['cat_claims']} CAT-coded claims, {ll['cat_share_of_incurred_pct']}% of "
                   "incurred — " + ", ".join(f"{e['cat_code']} ({e['claims']})" for e in ll["cat_events"]) + ".")
    else:
        st.caption("No CAT-coded claims in this history.")


def _render_reporting(plan: Dict[str, Any]) -> None:
    sr, med, lit = plan.get("statutory_reporting") or {}, plan.get("medicare") or {}, plan.get("litigation") or {}
    st.markdown("#### Statutory reporting (suggested — Finance confirms)")
    if sr.get("has_data"):
        st.dataframe(pd.DataFrame([{"Product": r["product"], "Exposure": r["exposure_type"], "Coverage": r["coverage_type"],
                                    "Share %": r["share_pct"], "Annual Statement line": r["statement_line"],
                                    "Note": r["note"] or ""} for r in sr["rows"]]),
                     hide_index=True, width="stretch")
    else:
        st.info("No exposure history to map.")

    a, b = st.columns(2)
    with a:
        st.markdown("#### Medicare Section 111")
        if med.get("applies"):
            st.warning(f"Applies: {med['bi_claims']} claims ({med['bi_share_pct']}%) carry "
                       f"{', '.join(med['exposure_types'])} exposures. Add the coverage to the Section 111 reporting feed "
                       "and query Medicare status at FNOL.")
        else:
            st.success("No bodily-injury or medical exposures in this history; likely N/A.")
    with b:
        st.markdown("#### Litigation")
        if lit:
            base = f" vs {lit['baseline_rate_pct']}% baseline" if lit.get("baseline_rate_pct") is not None else ""
            st.caption(f"Litigation rate {lit['rate_pct']}%{base} ({lit['litigated_claims']} claims). States with the "
                       f"highest rate (≥10 claims) — where panel counsel is needed first:")
            if lit["states"]:
                st.dataframe(pd.DataFrame([{"State": s["state"], "Claims": s["claims"], "Litigated": s["litigated"],
                                            "Rate %": s["rate_pct"]} for s in lit["states"]]),
                             hide_index=True, width="stretch")


def render_operations(brief: Dict[str, Any], get_plan: Callable[[float, Optional[float]], Optional[Dict[str, Any]]],
                      compliance: Optional[Dict[str, Any]],
                      save_state: Callable[[str, Dict[str, Any]], bool]) -> None:
    """Render the tab. *get_plan(volume_factor, caseload)* and *save_state(state, fields)* call the backend."""
    bid = brief["id"]
    st.markdown("### Launch Operations")
    st.caption("State compliance, staffing, reinsurance, statutory reporting, Medicare and litigation setup for this "
               "coverage, computed from the same claims data as the brief.")

    _render_compliance(bid, compliance, save_state)
    st.markdown("---")

    a, b = st.columns(2)
    factor = a.slider("Expected claim volume vs today's pattern", 0.25, 3.0, 1.0, 0.25, key=f"op_factor_{bid}",
                      help="1.0 = the new coverage produces as many claims as this risk pattern does today.")
    use_target = b.toggle("Use a target caseload instead of today's", key=f"op_ct_{bid}")
    caseload = b.number_input("Target open claims per adjuster", 1, 1000, 100, key=f"op_cl_{bid}") if use_target else None
    plan = get_plan(factor, caseload)
    if not plan:
        st.error("Could not load the launch operations plan from the backend.")
        return
    if not plan.get("has_data"):
        st.info("This brief has no claims history (direct, proxy or line baseline) to compute the operations plan from.")
        return
    basis = plan["basis"]
    if basis["basis"] == "proxy":
        st.info(f"**Proxy data** from {' + '.join(basis['proxy_tags'])}: this product has no claims of its own.")
    elif basis["basis"] == "line_baseline":
        st.info(f"Whole-line baseline ({', '.join(basis['product_lines'])}): no comparable risk pattern exists.")
    st.caption(f"{plan['claims_analyzed']:,} claims analysed · valuation date {plan['valuation_date']}")

    _render_staffing(bid, plan)
    st.markdown("---")
    _render_large_losses(plan)
    st.markdown("---")
    _render_reporting(plan)
