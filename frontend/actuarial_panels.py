"""
Actuarial sections beyond the rate indication
=============================================
Loss development (backend/reserving.py), Rating plan (backend/rating_plan.py), Business plan
(backend/business_plan.py) and the Actuarial memorandum (backend/actuarial_memo.py). Every figure is computed by
the backend; these panels only lay it out. *call(method, path, **requests_kwargs)* calls /briefs/{id}/{path}.
"""
from __future__ import annotations

import html
from typing import Any, Callable, Dict, Optional

import pandas as pd
import streamlit as st

Call = Callable[..., Optional[Dict[str, Any]]]


def _money(x: Optional[float], cents: bool = False) -> str:
    if x is None:
        return "—"
    return f"${x:,.2f}" if cents else f"${x:,.0f}"


def _notes(notes) -> None:
    for n in notes or []:
        st.markdown(f'<div class="insufficient-evidence">ℹ️ {html.escape(n)}</div>', unsafe_allow_html=True)


def _triangle_df(section: Dict[str, Any], money: bool) -> pd.DataFrame:
    ages = section["ages"]
    rows = []
    for r in section["triangle"]:
        row = {"Accident year": r["year"]}
        for a in ages:
            v = r.get(str(a))
            row[f"{a} m"] = None if v is None else (round(v) if money else int(v))
        rows.append(row)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Loss development
# ---------------------------------------------------------------------------
def render_loss_development(brief: Dict[str, Any], call: Call) -> None:
    st.markdown("### Loss development")
    st.caption("Accident-year triangles of reported claims and incurred losses, age-to-age factors, and chain-ladder "
               "and Bornhuetter-Ferguson ultimates. The rate indication develops with these factors.")
    d = call("GET", "loss-development", timeout=120)
    if d is None:
        st.error("Could not load loss development from the backend.")
        return
    if not d.get("has_data"):
        st.info(d.get("reason", "No loss development for this brief."))
        return
    inc, cnt = d["incurred"], d["counts"]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Factors from", "pattern" if d["factor_basis"] == "pattern" else "whole scope",
              f"{d['factor_basis_claims']:,} claims", delta_color="off")
    c2.metric("IBNR claims (count)", f"{d['ibnr_claims']:,.1f}")
    c3.metric("IBNR + IBNER, chain-ladder", _money(d["ibnr_incurred_cl"]))
    c4.metric("IBNR + IBNER, BF", _money(d["ibnr_incurred_bf"]))

    tab_inc, tab_cnt = st.tabs(["Incurred losses", "Reported claim counts"])
    for tab, section, money in ((tab_inc, inc, True), (tab_cnt, cnt, False)):
        with tab:
            st.markdown("**Triangle** (cumulative, at each year end)")
            df = _triangle_df(section, money)
            st.dataframe(df, hide_index=True, use_container_width=True,
                         column_config={c: st.column_config.NumberColumn(format="$%d" if money else "%d")
                                        for c in df.columns if c != "Accident year"})
            st.markdown("**Age-to-age factors** (volume-weighted)")
            st.dataframe(pd.DataFrame([{"Ages": f"{f['from_age']}–{f['to_age']} m", "Selected": f["factor"],
                                        "Years used": f["years_used"],
                                        "Individual years": ", ".join(f"{x:.3f}" for x in f["individual"])}
                                       for f in section["factors"]]), hide_index=True, use_container_width=True)
            st.markdown("**Ultimates**")
            st.dataframe(pd.DataFrame([{
                "Accident year": r["year"], "Age (m)": r["age_months"], "Reported": r["latest"],
                "CDF to ultimate": r["cdf"], "Chain-ladder ultimate": r["chain_ladder_ultimate"],
                "BF ultimate": r["bf_ultimate"], "Note": "extrapolated (< 12 m)" if r["extrapolated"] else ""}
                for r in section["rows"]]), hide_index=True, use_container_width=True,
                column_config={k: st.column_config.NumberColumn(format="$%.0f" if money else "%.1f")
                               for k in ("Reported", "Chain-ladder ultimate", "BF ultimate")})
    st.caption("Change the tail factor and the method in Rate indication → Assumptions.")
    _notes(d.get("notes"))


# ---------------------------------------------------------------------------
# Rating plan
# ---------------------------------------------------------------------------
def render_rating_plan(brief: Dict[str, Any], call: Call) -> None:
    st.markdown("### Rating plan")
    st.caption("The base rate and the relativities that spread the selected rate across risks: a Poisson GLM for "
               "frequency, one-way severity, both credibility-weighted towards 1.00, plus deductible and limit factors.")
    p = call("GET", "rating-plan", timeout=120)
    if p is None:
        st.error("Could not load the rating plan from the backend.")
        return
    if not p.get("available"):
        st.info(p.get("reason", "No rating plan for this brief."))
        return
    unit = p["exposure_unit"]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Base rate", _money(p["base_rate"], True), f"at base levels", delta_color="off")
    c2.metric("Average (selected) rate", _money(p["indicated_premium"], True))
    c3.metric("Off-balance factor", f"{p['off_balance']:.4f}")
    c4.metric("Rate spread p10 – p90", f"{_money(p['spread']['p10'])} – {_money(p['spread']['p90'])}")
    st.caption("Base levels: " + ", ".join(f"{k.replace('_', ' ')} = {v}" for k, v in p["base_levels"].items())
               + f". GLM: {p['glm']['parameters']} parameters on {p['glm']['cells']} cells, "
               + ("converged" if p["glm"]["converged"] else "NOT converged") + f", deviance {p['glm']['deviance']}.")

    for v in p["variables"]:
        st.markdown(f"#### {v['label']}")
        st.dataframe(pd.DataFrame([{
            "Level": L["level"] + (" (base)" if L["base"] else ""), f"Exposure ({unit})": L["exposure"],
            "Claims": L["claims"], "GLM frequency": L["frequency_glm"],
            "Significant": "yes" if L["frequency_significant"] else "", "Z freq": L["frequency_z"],
            "Severity (one-way)": L["severity_oneway"], "Z sev": L["severity_z"], "Selected": L["selected"],
        } for L in v["levels"]]), hide_index=True, use_container_width=True,
            column_config={f"Exposure ({unit})": st.column_config.NumberColumn(format="%.0f")})

    left, right = st.columns(2)
    with left:
        st.markdown("#### Deductible factors")
        d = p["deductibles"]
        if d.get("available"):
            st.dataframe(pd.DataFrame([{"Deductible": _money(r["deductible"]) + (" (base)" if r["base"] else ""),
                                        "Book share": f"{r['exposure_share_pct']}%",
                                        "Loss eliminated": f"{r['loss_elimination_pct']}%", "Factor": r["factor"]}
                                       for r in d["rows"]]), hide_index=True, use_container_width=True)
            st.caption(f"Loss elimination on {d['losses']:,} ground-up paid losses.")
        else:
            st.info("No deductible spread in the data.")
    with right:
        st.markdown("#### Increased-limit factors")
        il = p["ilfs"]
        if il.get("available"):
            st.dataframe(pd.DataFrame([{"Limit": _money(r["limit"]) + (" (basic)" if r["basic"] else ""),
                                        "ILF": r["ilf"],
                                        "Losses above": f"{r['losses_above']}" + (" ⚠️ thin" if r["thin"] else "")}
                                       for r in il["rows"]]), hide_index=True, use_container_width=True)
        else:
            st.info(il.get("reason", "No limit factors."))

    st.markdown("#### Rates by territory at base levels")
    st.dataframe(pd.DataFrame([{"Territory": s["territory"], "Relativity": s["relativity"],
                                "Rate": s["rate_at_base_levels"]} for s in p["state_rates"]]),
                 hide_index=True, use_container_width=True,
                 column_config={"Rate": st.column_config.NumberColumn(format="$%.2f")})
    _notes(p.get("notes"))


# ---------------------------------------------------------------------------
# Business plan
# ---------------------------------------------------------------------------
PLAN_FIELDS = [  # key, label, min, max, step
    ("take_up_pct", "Take-up % of eligible book", 0.1, 100.0, 1.0),
    ("growth_pct", "Growth %/yr", -50.0, 200.0, 1.0),
    ("years", "Plan years", 1, 5, 1),
    ("launch_cost", "One-off launch cost ($)", 0.0, 1e8, 10_000.0),
    ("fixed_expense_per_year", "Fixed expenses per year ($)", 0.0, 1e8, 5_000.0),
    ("quota_share_pct", "Quota share ceded %", 0.0, 90.0, 5.0),
    ("ceding_commission_pct", "Ceding commission %", 0.0, 60.0, 1.0),
    ("premium_to_surplus", "Premium-to-capital ratio", 0.5, 6.0, 0.1),
    ("investment_yield_pct", "Investment yield %", 0.0, 15.0, 0.25),
    ("loss_payout_years", "Average loss payout (years)", 0.1, 10.0, 0.1),
    ("tax_rate_pct", "Tax rate %", 0.0, 50.0, 1.0),
    ("annual_rate_change_pct", "Annual rate change % (default = loss trend)", -30.0, 50.0, 0.5),
]


def render_business_plan(brief: Dict[str, Any], call: Call) -> None:
    bid = brief["id"]
    key = f"bplan_overrides_{bid}"
    overrides = st.session_state.get(key, {})
    st.markdown("### Business plan")
    st.caption("Volume, underwriting result, reinsurance, capital and return for the new coverage at the selected "
               "rate, with stress scenarios. The inputs are planning assumptions — set them from the business case.")
    b = call("GET", "business-plan", timeout=120, params=overrides)
    if b is None:
        st.error("Could not load the business plan from the backend.")
        return
    if not b.get("available"):
        st.info(b.get("reason") or "No business plan for this brief.")
        return
    if overrides:
        st.warning("**What-if:** these numbers use inputs you are trying out, not the saved plan.")
    t, p = b["totals"], b["inputs"]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(f"{p['years']}-yr written premium", _money(t["written_premium"]))
    c2.metric("Combined ratio", f"{t['combined_ratio_pct']:.1f}%" if t["combined_ratio_pct"] is not None else "—")
    c3.metric("After-tax result", _money(t["after_tax_result"]))
    be = b.get("breakeven_take_up_pct")
    c4.metric("Break-even take-up", f"{be:.1f}%" if be is not None else "none", help="Over the plan years, after "
              "launch and fixed costs.")
    vs = b.get("rate_vs_indication_pct")
    st.caption(f"Rate {_money(b['rate'], True)} per exposure"
               + (f" ({vs:+.1f}% vs the indication)" if vs is not None else " (the indication is $0)") + " · "
               f"eligible book {b['eligible_exposure']:,.0f} {b['exposure_unit']} · loss & LAE "
               f"{_money(b['loss_and_lae_per_exposure'], True)} per exposure.")

    with st.expander("⚙️ Plan inputs", expanded=bool(overrides)):
        with st.form(key=f"bplan_form_{bid}", border=False):
            cols = st.columns(3)
            vals: Dict[str, Any] = {}
            for i, (k, label, lo, hi, step) in enumerate(PLAN_FIELDS):
                cur = p[k]
                if isinstance(step, int):
                    vals[k] = cols[i % 3].number_input(label, int(lo), int(hi), int(cur), int(step))
                else:
                    vals[k] = cols[i % 3].number_input(label, float(lo), float(hi), float(cur), float(step))
            rate = st.number_input("Rate per exposure ($) — 0 = the selected rate", 0.0, 1e7,
                                   float(p["rate"] or 0.0), 1.0)
            if rate > 0:
                vals["rate"] = rate
            c1, c2, c3 = st.columns(3)
            try_it = c1.form_submit_button("Try (what-if)", use_container_width=True)
            save = c2.form_submit_button("Save plan", type="primary", use_container_width=True)
            reset = c3.form_submit_button("Reset", use_container_width=True)
        if try_it:
            st.session_state[key] = vals
            st.rerun()
        if save:
            if call("PUT", "actuarial/business-plan", json={"inputs": vals}) is not None:
                st.session_state.pop(key, None)
                st.rerun()
        if reset:
            st.session_state.pop(key, None)
            st.rerun()

    st.markdown("#### Projection")
    st.dataframe(pd.DataFrame([{
        "Year": y["year"], "Exposures": y["exposures"], "Written premium": y["written_premium"],
        "Loss & LAE": y["loss_and_lae"], "Expenses": y["expenses"], "Ceded premium": y["ceded_premium"],
        "Underwriting result": y["underwriting_result"], "Investment income": y["investment_income"],
        "After tax": y["after_tax_result"], "Capital": y["capital"], "Combined ratio %": y["combined_ratio_pct"],
        "Return on capital %": y["return_on_capital_pct"]} for y in b["projection"]]),
        hide_index=True, use_container_width=True,
        column_config={k: st.column_config.NumberColumn(format="$%.0f") for k in
                       ("Written premium", "Loss & LAE", "Expenses", "Ceded premium", "Underwriting result",
                        "Investment income", "After tax", "Capital")})
    st.markdown("#### Stress scenarios")
    st.dataframe(pd.DataFrame([{"Scenario": s["scenario"], "Written premium": s["written_premium"],
                                "Combined ratio %": s["combined_ratio_pct"], "After-tax result": s["after_tax_result"],
                                "Return on capital %": s["return_on_peak_capital_pct"]} for s in b["scenarios"]]),
                 hide_index=True, use_container_width=True,
                 column_config={k: st.column_config.NumberColumn(format="$%.0f")
                                for k in ("Written premium", "After-tax result")})
    _notes(b.get("notes"))


# ---------------------------------------------------------------------------
# Actuarial memorandum
# ---------------------------------------------------------------------------
def render_actuarial_memo(brief: Dict[str, Any], call: Call) -> None:
    st.markdown("### Actuarial memorandum")
    st.caption("A draft memorandum and exhibits for the Appointed Actuary's technical note (IRDAI Use & File), "
               "assembled from the indication, development, rating plan and business plan. Nothing is generated: "
               "every number is copied from those sections.")
    m = call("GET", "actuarial-memo", timeout=180)
    if m is None:
        st.error("Could not build the memorandum.")
        return
    if not m.get("available"):
        st.info(m.get("reason", "No memorandum for this brief."))
        return
    if m["draft"]:
        st.warning("DRAFT — approve the indication (Rate indication section) before the PMC reviews the product.")
    if m["tbd"]:
        st.info(f"{len(m['tbd'])} item(s) only the insurer or Appointed Actuary can supply are marked [TBD]: "
                + "; ".join(m["tbd"]) + ".")
    st.download_button("Download memorandum (.md)", m["markdown"], file_name=m["filename"], mime="text/markdown",
                       type="primary")
    with st.container(border=True):
        st.markdown(m["markdown"].replace("$", "\\$"))
