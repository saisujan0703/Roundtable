"""
Actuarial implementation and governance sections
================================================
PolicyCenter rating tests (backend/rating_tests.py), actual-vs-expected monitoring (backend/monitoring.py),
parametric pricing (backend/parametric.py) and the company actuarial settings (backend/actuarial_settings.py).
Every figure comes from the backend. *call(method, path, **kw)* calls /briefs/{id}/{path}; the settings panel takes
*api(method, path, **kw)* for /api/{path}.
"""
from __future__ import annotations

import html
from typing import Any, Callable, Dict, Optional

import pandas as pd
import streamlit as st

from money import TABLE_FORMAT, TABLE_FORMAT_PAISE, inr

Call = Callable[..., Optional[Dict[str, Any]]]
STATUS_ICON = {"green": "🟢", "amber": "🟠", "red": "🔴", "no data": "⚪"}
CASE_ICON = {"Pass": "✅", "Fail": "❌", "Blocked": "⛔", "Not run": "⚪"}


def _money(x: Optional[float], cents: bool = False) -> str:
    return inr(x, paise=cents, na="—")


def _md(text: Optional[str]) -> str:
    return (text or "").replace("$", "\\$")


def _notes(notes) -> None:
    for n in notes or []:
        st.markdown(f'<div class="insufficient-evidence">ℹ️ {html.escape(n)}</div>', unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# PolicyCenter rating tests
# ---------------------------------------------------------------------------
def render_rating_tests(brief: Dict[str, Any], call: Call) -> None:
    bid = brief["id"]
    st.markdown("### PolicyCenter rating tests")
    st.caption("Cases that check PolicyCenter's rate book reproduces the rating plan: the base case, every relativity "
               "one at a time, deductibles, limits and the extreme combinations, each with its expected worksheet. "
               "Quote each case in PolicyCenter and record the premium it produced. The launch gate needs all to pass.")
    data = call("GET", "rating-tests", timeout=120)
    if data is None:
        st.error("Could not load the rating tests.")
        return
    tests, s = data.get("tests"), data["summary"]
    c1, c2 = st.columns([1, 3])
    label = "Regenerate cases" if tests else "Generate cases"
    if c1.button(label, type="primary" if not tests or s["stale"] else "secondary", key=f"rt_gen_{bid}",
                 use_container_width=True):
        if call("POST", "actuarial/rating-tests", timeout=120) is not None:
            st.rerun()
    if not tests:
        c2.info("No cases yet. Generate them once the rate is approved (they use the rating plan at that moment).")
        return
    if s["stale"]:
        st.warning("The rating plan changed since these cases were generated (new selected rate, relativities or "
                   "data): regenerate and rerun them.")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Pass", f"{s['pass']} / {s['total']}")
    m2.metric("Fail", s["fail"])
    m3.metric("Blocked", s["blocked"])
    m4.metric("Not run", s["not_run"])
    st.download_button("Download cases (.csv)", data["csv"], file_name=f"rating_tests_brief_{bid}.csv", mime="text/csv")

    cases = tests["cases"]
    st.dataframe(pd.DataFrame([{
        "": CASE_ICON.get(c["status"], ""), "Case": c["id"], "Kind": c["kind"], "Title": c["title"],
        **{k: v for k, v in c["inputs"].items()}, "Expected": c["expected_premium"], "PolicyCenter": c["actual_premium"],
        "Tester": c["tester"], "Note": c["note"]} for c in cases]), hide_index=True, use_container_width=True,
        column_config={"Expected": st.column_config.NumberColumn(format=TABLE_FORMAT_PAISE),
                       "PolicyCenter": st.column_config.NumberColumn(format=TABLE_FORMAT_PAISE)})

    st.markdown("#### Record a result")
    ids = [c["id"] for c in cases]
    pick = st.selectbox("Case", ids, format_func=lambda i: f"{i} — {next(c['title'] for c in cases if c['id'] == i)}",
                        key=f"rt_pick_{bid}")
    case = next(c for c in cases if c["id"] == pick)
    with st.expander(f"Worksheet for {pick}: expected {_money(case['expected_premium'], True)}", expanded=False):
        st.dataframe(pd.DataFrame([{"Step": w["step"], "Factor": w["factor"], "Running premium": w["running"]}
                                   for w in case["worksheet"]]), hide_index=True, use_container_width=True)
    with st.form(key=f"rt_form_{bid}_{pick}", clear_on_submit=False):
        c1, c2, c3 = st.columns(3)
        actual = c1.number_input("Premium PolicyCenter produced (₹)", 0.0, 1e8,
                                 float(case["actual_premium"] or 0.0), 0.01, format="%.2f")
        tester = c2.text_input("Tester", value=case["tester"] or st.session_state.get("user_name", ""))
        blocked = c3.checkbox("Blocked (could not run)", value=case["status"] == "Blocked")
        note = st.text_input("Note (required for a fail or a block)", value=case["note"])
        if st.form_submit_button("Save result", type="primary"):
            body = {"tester": tester, "note": note}
            body.update({"status": "Blocked"} if blocked else {"actual_premium": actual})
            if call("PUT", f"actuarial/rating-tests/{pick}", json=body, timeout=120) is not None:
                st.rerun()


# ---------------------------------------------------------------------------
# Actual vs expected monitoring
# ---------------------------------------------------------------------------
def render_monitoring(brief: Dict[str, Any], call: Call) -> None:
    st.markdown("### Actual vs expected")
    st.caption("Does the coverage perform as priced? Before launch this is a hold-out backtest on the current accident "
               "year (which the indication did not use); after launch it compares the live experience with plan.")
    m = call("GET", "monitoring", timeout=120)
    if m is None:
        st.error("Could not load monitoring.")
        return
    if not m.get("available"):
        st.info(m.get("reason", "Nothing to monitor yet."))
        return
    overall = m["overall"]
    text = (f"{STATUS_ICON[overall]} **{overall.upper()}** — {m['mode']} {m['period']['start']} to {m['period']['end']}: "
            f"{m['claims_reported']} claims ({m['claims_ultimate']:.1f} at ultimate) on {m['exposure']:,.0f} "
            f"{m['exposure_unit']}; credibility Z = {m['credibility_z']:.2f}.")
    {"green": st.success, "amber": st.warning, "red": st.error}.get(overall, st.info)(_md(text))
    st.dataframe(pd.DataFrame([{
        "": STATUS_ICON.get(k["status"], ""), "KPI": k["kpi"], "Unit": k["unit"], "Actual": k["actual"],
        "Expected": k["expected"], "A/E": k["a_to_e"], "Credibility-weighted A/E": k["credibility_weighted_a_to_e"],
        "90% interval of A/E": f"{k['ci90'][0]:.2f} – {k['ci90'][1]:.2f}" if k.get("ci90") else "—",
        "Significant": "yes" if k.get("significant") else ""} for k in m["kpis"]]),
        hide_index=True, use_container_width=True)
    st.caption(f"Bands on the credibility-weighted A/E: amber outside {m['thresholds']['amber'][0]:.2f}–"
               f"{m['thresholds']['amber'][1]:.2f}, red outside {m['thresholds']['red'][0]:.2f}–"
               f"{m['thresholds']['red'][1]:.2f}; a 90% interval that excludes 1.00 is at least amber.")
    st.markdown("#### Actions")
    for t in m["triggers"]:
        st.markdown(f"- {_md(t)}")
    st.markdown("#### Monitoring plan")
    st.dataframe(pd.DataFrame([{"KPI": p["kpi"], "Cadence": p["cadence"], "Threshold": p["threshold"],
                                "Owner": p["owner"]} for p in m["plan"]]), hide_index=True, use_container_width=True)
    _notes(m.get("notes"))


# ---------------------------------------------------------------------------
# Parametric pricing
# ---------------------------------------------------------------------------
def render_parametric(brief: Dict[str, Any], call: Call) -> None:
    bid = brief["id"]
    key = f"param_whatif_{bid}"
    what_if = st.session_state.get(key, {})
    st.markdown("### Parametric option")
    st.caption("A fixed payout when an event index crosses a trigger, instead of indemnity. Priced from the company's "
               "catastrophe events of this peril, credibility-weighted with hazard probabilities you enter per state, "
               "with a risk load for lumpy payouts. Basis risk shows who would have had a loss and no payout.")
    p = call("GET", "parametric", timeout=120, params=what_if)
    if p is None:
        st.error("Could not load the parametric pricing.")
        return
    if not p.get("available"):
        st.info(p.get("reason", "No parametric pricing for this brief."))
        return
    if p.get("what_if"):
        st.warning("**What-if:** trigger or payout you are trying out, not the saved design.")
    cfg, br = p["config"], p["basis_risk"]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Average rate", _money(p["average_rate"], True), f"per {p['exposure_unit'].rstrip('s')}", delta_color="off")
    c2.metric("Expected payout", _money(p["expected_payout_per_policy"], True))
    c3.metric("Risk load", f"{p['risk_load_pct']:.1f}%")
    c4.metric("Miss rate (basis risk)", f"{br['miss_rate_pct']:.0f}%" if br["miss_rate_pct"] is not None else "—",
              f"{br['hits']} hit · {br['misses']} miss · {br['false_alarms']} false alarm", delta_color="off")

    with st.expander("⚙️ Trigger, payout and hazard data", expanded=not p["saved_config"]):
        with st.form(key=f"param_form_{bid}", border=False):
            f1, f2, f3 = st.columns(3)
            trig = f1.number_input("Trigger: event loss per exposure in the state (₹)", 0.001, 1e6,
                                   float(cfg["trigger_index"]), 1.0, format="%.2f")
            payout = f2.number_input("Payout per policy (₹)", 1.0, 1e7, float(cfg["payout"]), 100.0)
            material = f3.number_input("Material-loss index ($ per exposure)", 0.0, 1e6,
                                       float(cfg["material_loss_index"]), 1.0, format="%.2f",
                                       help="Index at which policyholders have a loss that matters — for basis risk.")
            st.markdown("**Hazard probabilities** (annual probability the trigger is reached, per state, with source)")
            hz = pd.DataFrame(cfg.get("hazard") or [], columns=["state", "annual_probability", "source"])
            edited = st.data_editor(hz, num_rows="dynamic", use_container_width=True, key=f"param_hz_{bid}",
                                    column_config={"state": st.column_config.TextColumn("State", max_chars=2),
                                                   "annual_probability": st.column_config.NumberColumn(
                                                       "Annual probability", min_value=0.0, max_value=1.0, format="%.4f"),
                                                   "source": st.column_config.TextColumn("Source (e.g. NOAA SPC, cat model)")})
            b1, b2, b3 = st.columns(3)
            try_it = b1.form_submit_button("Try (what-if)", use_container_width=True)
            save = b2.form_submit_button("Save design", type="primary", use_container_width=True)
            reset = b3.form_submit_button("Reset what-if", use_container_width=True)
        if try_it:
            st.session_state[key] = {"trigger_index": trig, "payout": payout, "material_loss_index": material}
            st.rerun()
        if save:
            hazard = [{"state": str(r["state"]).strip(), "annual_probability": float(r["annual_probability"]),
                       "source": str(r["source"] or "")} for _, r in edited.iterrows()
                      if str(r.get("state") or "").strip() and pd.notna(r.get("annual_probability"))]
            body = {"config": {"trigger_index": trig, "payout": payout, "material_loss_index": material, "hazard": hazard}}
            if call("PUT", "actuarial/parametric", json=body) is not None:
                st.session_state.pop(key, None)
                st.rerun()
        if reset:
            st.session_state.pop(key, None)
            st.rerun()

    st.markdown("#### Rate by state")
    st.dataframe(pd.DataFrame([{
        "State": s["state"], "Book share %": s["exposure_share_pct"], "Burn probability": s["burn_probability"],
        "Hazard probability": s["hazard_probability"], "Hazard source": s["hazard_source"],
        "Selected probability": s["selected_probability"], "Expected payout": s["expected_payout"], "Rate": s["rate"]}
        for s in sorted(p["states"], key=lambda s: -s["selected_probability"])]), hide_index=True,
        use_container_width=True, column_config={"Expected payout": st.column_config.NumberColumn(format=TABLE_FORMAT_PAISE),
                                                 "Rate": st.column_config.NumberColumn(format=TABLE_FORMAT_PAISE)})
    st.markdown("#### Catastrophe events in the data")
    if p["events"]:
        st.dataframe(pd.DataFrame([{"Event": e["event"], "State": e["state"], "Date": e["date"], "Claims": e["claims"],
                                    "Incurred": e["incurred"], "Index ($/exposure)": e["index_per_exposure"],
                                    "Triggers": "yes" if e["triggers"] else "", "Basis": e["basis"]}
                                   for e in p["events"]]), hide_index=True, use_container_width=True,
                     column_config={"Incurred": st.column_config.NumberColumn(format=TABLE_FORMAT)})
    else:
        st.info("No catastrophe events of this peril in the data.")
    st.caption(f"{p['events_observed']} event(s) in {p['years_observed']:.1f} years; burn credibility Z = "
               f"{p['credibility_z']:.2f}.")
    _notes(p.get("notes"))


# ---------------------------------------------------------------------------
# Company actuarial settings
# ---------------------------------------------------------------------------
def render_company_settings(api: Call) -> None:
    st.markdown("### Company assumptions")
    st.caption("Company-level assumptions with their sources — expense study, ULAE study, capital plan. They replace "
               "the placeholder defaults for every product (each product can still override). The expense ratio is "
               "the sum of its components; profit & contingencies is derived from the target return on equity.")
    data = api("GET", "actuarial/settings")
    if data is None:
        st.error("Could not load the company settings.")
        return
    fields, values, sources = data["fields"], data["values"], data["sources"]
    d = data["derived"]
    c1, c2, c3 = st.columns(3)
    c1.metric("Expense ratio", f"{d['expense_ratio_pct']:.1f}%")
    c2.metric("Profit & contingencies (from ROE)", f"{d['profit_pct']:.2f}%")
    c3.metric("Last updated", (data.get("updated_at") or "never")[:10], data.get("updated_by") or "placeholders in use",
              delta_color="off")
    limit = d.get("eom_limit_pct")
    if limit is not None and d["expense_ratio_pct"] > limit:
        st.warning(f"The expense ratio is above the {limit:.0f}% of gross written premium that IRDAI's Expenses of "
                   "Management Regulations, 2024 allow across the whole book.")
    st.caption("GST is charged on top of the premium and is not an expense here. With Indian investment yields the "
               "profit provision can be negative: investment income on capital and reserves earns the return.")
    with st.form(key="company_settings_form"):
        new_v, new_s = {}, {}
        for k, f in fields.items():
            a, b, c = st.columns([1.3, 0.8, 2.2])
            use = a.checkbox(f["label"], value=k in values, key=f"cs_use_{k}",
                             help=f"Placeholder {f['default']} until set.")
            v = b.number_input("Value", float(f["min"]), float(f["max"]), float(values.get(k, f["default"])),
                               key=f"cs_v_{k}", label_visibility="collapsed")
            src = c.text_input("Source", value=sources.get(k, ""), key=f"cs_s_{k}", label_visibility="collapsed",
                               placeholder="Source, e.g. '2025 expense study, Exhibit 3'")
            if use:
                new_v[k], new_s[k] = v, src
        if st.form_submit_button("Save company assumptions", type="primary"):
            if api("PUT", "actuarial/settings", json={"values": new_v, "sources": new_s}) is not None:
                st.rerun()
    st.caption("Ticked rows are company settings (a source is required); unticked rows stay on the placeholder.")
