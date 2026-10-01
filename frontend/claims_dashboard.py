"""
Claims Findings Dashboard
=========================
Renders the 11 claims sections of a brief as charts, tables and tiles from the
structured analytics stored with the brief (brief_data["claims_analytics"]).
All numbers come from backend.analytics; this module only formats them.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional

import altair as alt
import pandas as pd
import streamlit as st

# Validated reference palette (dataviz references/palette.md, light mode)
SERIES = "#3D3FE0"      # slot 1: this risk pattern (Roundtable indigo)
COMPARE = "#eb6834"     # slot 2: second series where two measures share a chart
BASELINE = "#9a9892"    # neutral: baseline / comparison group
MUTED = "#c9c7c1"       # low-credibility marks
TEXT = "#5B5F6E"

DENIAL_NAMES = {
    "mechanical_breakdown_excluded": "Mechanical breakdown exclusion",
    "wear_tear_deterioration": "Wear & tear / gradual deterioration",
    "flood_excluded": "Flood / surface water exclusion",
    "excluded_peril": "Excluded peril",
    "coverage_not_purchased": "Coverage not purchased",
    "late_notice": "Late notice",
    "fraud_misrepresentation": "Fraud / misrepresentation",
    "wc_2B_preexisting_condition": "WC 2B pre-existing condition",
    "wc_1A_coming_and_going": "WC 1A coming and going",
    "wc_2D_no_medical_evidence": "WC 2D no medical evidence",
}
CAUSE_NAMES = {
    "vehcollision": "Collision with vehicle", "rearend": "Rear-end collision", "fixedobjcoll": "Fixed object",
    "otherobjcoll": "Road debris / other object", "animalcollision": "Animal collision", "rollover": "Rollover",
    "theftentire": "Vehicle theft", "theftparts": "Parts theft", "glassbreakage": "Glass breakage", "hail": "Hail",
    "vandalism": "Vandalism", "firedamage": "Vehicle fire", "waterdamage": "Water damage", "product": "Product failure",
    "loadingdamage": "Loading damage", "fire": "Fire", "wind": "Wind", "burglary": "Burglary", "mold": "Mold",
    "fall": "Fall / slip / trip", "strain": "Strain", "struck": "Struck by", "cut": "Cut / puncture",
    "caught_in": "Caught in / between", "burn_scald": "Burn / scald", "motorvehicle": "Motor vehicle",
}


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------
def _money(v: Optional[float]) -> str:
    """Compact money for Streamlit text; the $ is escaped so markdown does not start LaTeX math."""
    if v is None:
        return "n/a"
    if abs(v) >= 1_000_000:
        return f"\\${v / 1_000_000:,.2f}M"
    if abs(v) >= 10_000:
        return f"\\${v / 1_000:,.0f}K"
    return f"\\${v:,.0f}"


def _md(text: Optional[str]) -> str:
    """Escape $ in backend-built sentences before handing them to Streamlit markdown."""
    return (text or "").replace("$", "\\$")


def _pct(v: Optional[float]) -> str:
    return "n/a" if v is None else f"{v:.1f}%"


def _delta_pts(v: Optional[float], base: Optional[float], unit: str = " pts") -> Optional[str]:
    if v is None or base is None:
        return None
    return f"{v - base:+.1f}{unit} vs baseline"


def _chart(c: alt.Chart, height: Any = 260) -> None:
    st.altair_chart(
        (c.properties(height=height) if height is not None else c)
        .configure(background="transparent", font="Plus Jakarta Sans")   # must precede configure_* calls
        .configure_view(strokeWidth=0)
        .configure_axis(labelColor=TEXT, titleColor=TEXT, gridColor="#ECEDF3", domainColor="#d6d4ce",
                        labelFontSize=12, titleFontSize=12, titleFontWeight="normal")
        .configure_legend(labelColor=TEXT, titleColor=TEXT, orient="top", labelFontSize=12)
        .configure_title(color="#121318", fontSize=14, anchor="start", fontWeight=600),
        width="stretch",
    )


def _section(num: int, title: str, subtitle: str = "") -> None:
    st.markdown(f"##### {num}. {title}")
    if subtitle:
        st.caption(subtitle)


def _hbar(df: pd.DataFrame, cat: str, val: str, title: str, fmt: str, tooltip: List, color_field: Optional[str] = None,
          sort_desc: bool = True, rule_at: Optional[float] = None, height: Optional[int] = None) -> None:
    enc_color = (alt.Color(f"{color_field}:N", scale=alt.Scale(domain=["Credible", "Low credibility"], range=[SERIES, MUTED]),
                           legend=alt.Legend(title=None))
                 if color_field else alt.value(SERIES))
    base = alt.Chart(df).encode(
        y=alt.Y(f"{cat}:N", sort="-x" if sort_desc else None, title=None, axis=alt.Axis(labelLimit=220)),
        x=alt.X(f"{val}:Q", title=None, axis=alt.Axis(format=fmt, tickCount=5)),
    )
    bars = base.mark_bar(cornerRadiusEnd=4, height={"band": 0.7}).encode(color=enc_color, tooltip=tooltip)
    layer = bars
    if rule_at is not None:
        layer = bars + alt.Chart(pd.DataFrame({"x": [rule_at]})).mark_rule(color=BASELINE, strokeDash=[4, 3], strokeWidth=1.5).encode(x="x:Q")
    _chart(layer.properties(title=title), height or alt.Step(30))


# ---------------------------------------------------------------------------
# Sections
# ---------------------------------------------------------------------------
def _frequency(a: Dict[str, Any]) -> None:
    s, trend, fit = a["summary"], a["trend"], a["frequency_trend_fit"]
    _section(1, "Claim Frequency", f"Claims per 1,000 {s['exposure_unit']} · scope: {s['scope']} · valued {a['valuation_date']}")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Claims", f"{s['tag_count']:,}", help="Reported claims tagged with this risk pattern")
    c2.metric("Frequency / 1,000", f"{s['frequency_per_1000']:.1f}")
    c3.metric("Share of scope claims", _pct(s["share_of_scope_claims_pct"]))
    sig = "significant" if fit.get("significant") else "not significant"
    c4.metric("Fitted trend / yr", f"{fit['annual_trend_pct']:+.1f}%" if fit.get("has_data") else "n/a",
              help=_md(fit.get("narrative")), delta=sig if fit.get("has_data") else None, delta_color="off")

    df = pd.DataFrame(trend)
    df["AY"] = df["year"].astype(str) + df["partial_year"].map({True: "*", False: ""})
    df["Credibility"] = df["credible"].map({True: "Credible", False: "Low credibility"})
    left, right = st.columns(2)
    with left:
        long = df.melt(id_vars=["AY", "claims", "partial_year"], value_vars=["frequency_per_1000", "frequency_ex_cat_per_1000"],
                       var_name="measure", value_name="freq")
        long["measure"] = long["measure"].map({"frequency_per_1000": "All claims", "frequency_ex_cat_per_1000": "Ex-CAT, constant mix"})
        enc = dict(x=alt.X("AY:O", title="Accident year", axis=alt.Axis(labelAngle=0)),
                   y=alt.Y("freq:Q", title="per 1,000", scale=alt.Scale(zero=True)),
                   color=alt.Color("measure:N", scale=alt.Scale(domain=["All claims", "Ex-CAT, constant mix"], range=[SERIES, COMPARE]),
                                   legend=alt.Legend(title=None)),
                   tooltip=[alt.Tooltip("AY:O", title="AY"), alt.Tooltip("measure:N", title="Measure"),
                            alt.Tooltip("freq:Q", title="Per 1,000", format=".1f"), alt.Tooltip("claims:Q", title="Claims")])
        chart = alt.Chart(long).mark_line(strokeWidth=2).encode(**enc) + \
            alt.Chart(long).mark_point(size=70, filled=True, stroke="white", strokeWidth=2).encode(**enc)
        _chart(chart.properties(title="Frequency per 1,000 by accident year"))
    with right:
        bars = alt.Chart(df).mark_bar(cornerRadiusEnd=4, width={"band": 0.6}).encode(
            x=alt.X("AY:O", title="Accident year", axis=alt.Axis(labelAngle=0)),
            y=alt.Y("claims:Q", title="Claims"),
            color=alt.Color("Credibility:N", scale=alt.Scale(domain=["Credible", "Low credibility"], range=[SERIES, MUTED]),
                            legend=alt.Legend(title=None)),
            tooltip=[alt.Tooltip("AY:O"), alt.Tooltip("claims:Q", title="Claims"), alt.Tooltip("cat_claims:Q", title="CAT claims"),
                     alt.Tooltip("earned_exposure:Q", title="Earned exposure", format=",.0f")])
        _chart(bars.properties(title="Claim count by accident year"))
    st.caption("\\* Partial, immature accident year (IBNR and open reserves). " + _md(fit.get("narrative")))


def _severity(a: Dict[str, Any]) -> None:
    sev, lr, trend = a["severity"], a["loss_ratio"], a["trend"]
    _section(2, "Claim Severity & Loss Ratio", f"Gross incurred (paid + case reserve) vs {sev['baseline_label']}")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Mean severity", _money(sev["mean"]), delta=f"{sev['severity_index_vs_baseline']:.2f}x baseline"
              if sev.get("severity_index_vs_baseline") else None, delta_color="inverse")
    c2.metric("Median severity", _money(sev["median"]), help=f"90th percentile {_money(sev['p90'])}; largest {_money(sev['max'])}")
    c3.metric("Total-loss rate", _pct(sev["total_loss_rate_pct"]))
    c4.metric("Loss ratio points", f"{lr.get('loss_ratio_points', 0):.1f}" if lr.get("has_data") else "n/a",
              help=_md(lr.get("status")))

    left, right = st.columns(2)
    with left:
        cmp = pd.DataFrame([
            {"Statistic": "Mean", "Group": "This pattern", "Amount": sev["mean"]},
            {"Statistic": "Mean", "Group": "Baseline", "Amount": sev["baseline_mean"]},
            {"Statistic": "Median", "Group": "This pattern", "Amount": sev["median"]},
            {"Statistic": "Median", "Group": "Baseline", "Amount": sev["baseline_median"]},
        ])
        chart = alt.Chart(cmp).mark_bar(cornerRadiusEnd=4).encode(
            x=alt.X("Group:N", title=None, axis=None, sort=["This pattern", "Baseline"]),
            y=alt.Y("Amount:Q", title=None, axis=alt.Axis(format="$.2~s")),
            color=alt.Color("Group:N", scale=alt.Scale(domain=["This pattern", "Baseline"], range=[SERIES, BASELINE]),
                            legend=alt.Legend(title=None)),
            column=alt.Column("Statistic:N", title=None, header=alt.Header(labelColor=TEXT, labelOrient="bottom")),
            tooltip=["Statistic", "Group", alt.Tooltip("Amount:Q", format="$,.0f")],
        ).properties(width=130, height=220, title="Severity vs baseline")
        st.altair_chart(chart.configure(background="transparent", font="Plus Jakarta Sans").configure_view(strokeWidth=0).configure_legend(orient="top")
                        .configure_title(color="#121318", fontSize=14, anchor="start"), width="content")
    with right:
        if lr.get("has_data"):
            lrd = pd.DataFrame(lr["by_year"])
            partial = {r["year"]: r["partial_year"] for r in trend}
            lrd["AY"] = lrd["year"].astype(str) + lrd["year"].map(lambda y: "*" if partial.get(y) else "")
            chart = alt.Chart(lrd).mark_bar(cornerRadiusEnd=4, width={"band": 0.6}, color=SERIES).encode(
                x=alt.X("AY:O", title="Accident year", axis=alt.Axis(labelAngle=0)),
                y=alt.Y("loss_ratio_points:Q", title="Loss ratio points"),
                tooltip=[alt.Tooltip("AY:O"), alt.Tooltip("loss_ratio_points:Q", title="LR points", format=".1f")])
            labels = alt.Chart(lrd).mark_text(dy=-8, color=TEXT, fontSize=11).encode(
                x="AY:O", y="loss_ratio_points:Q", text=alt.Text("loss_ratio_points:Q", format=".1f"))
            _chart((chart + labels).properties(title="Loss + ALAE as points of earned premium"))
    st.caption(f"Large losses ≥ \\$100K: {sev['large_losses']} ({_pct(sev['large_loss_share_of_incurred_pct'])} of incurred) · "
               f"ALAE {_pct(sev['alae_ratio_pct'])} of loss · {_md(lr.get('status', ''))}")


def _history(a: Dict[str, Any]) -> None:
    _section(3, "Historical Claim Trends", _md(a["benchmark"].get("narrative", "")))
    df = pd.DataFrame(a["trend"])
    lr = {r["year"]: r["loss_ratio_points"] for r in a["loss_ratio"].get("by_year", [])}
    table = pd.DataFrame({
        "AY": df["year"].astype(str) + df["partial_year"].map({True: " (partial)", False: ""}),
        "Claims": df["claims"], "CAT": df["cat_claims"], "Exposure": df["earned_exposure"],
        "Freq /1,000": df["frequency_per_1000"], "Ex-CAT freq": df["frequency_ex_cat_per_1000"],
        "Avg severity": df["avg_severity"], "Loss cost / exp.": df["loss_cost_per_exposure"],
        "LR pts": df["year"].map(lr), "Open %": df["open_pct"],
        "Credible": df["credible"].map({True: "✓", False: "low"}),
    })
    st.dataframe(table, hide_index=True, width="stretch", column_config={
        "Exposure": st.column_config.NumberColumn(format="%,.0f"),
        "Freq /1,000": st.column_config.NumberColumn(format="%.1f"),
        "Ex-CAT freq": st.column_config.NumberColumn(format="%.1f"),
        "Avg severity": st.column_config.NumberColumn(format="$%,.0f"),
        "Loss cost / exp.": st.column_config.NumberColumn(format="$%,.0f"),
        "LR pts": st.column_config.NumberColumn(format="%.1f"),
        "Open %": st.column_config.NumberColumn(format="%.0f%%"),
    })
    samples = a.get("sample_claims") or []
    if samples:
        st.markdown("**Representative claims**")
        cols = st.columns(len(samples))
        for col, c in zip(cols, samples):
            with col:
                with st.container(border=True, key=f"rtcard_sample_{c['claim_id']}"):
                    st.markdown(f"**{c['label']}**  \n`{c['claim_id']}` · {c['claim_date']} · {c['location']}")
                    if c.get("vehicle"):
                        st.caption(c["vehicle"])
                    st.markdown(_md(c["description"]))
                    st.markdown(f"Incurred **{_money(c['incurred_amount'])}** · FNOL reserve {_money(c['initial_reserve'])}  \n"
                                f"Status: {c['claim_state']}" +
                                (f" · Denied: {DENIAL_NAMES.get(c['denial_reason'], c['denial_reason'])}" if c.get("denial_reason") else ""))


def _causes(a: Dict[str, Any]) -> None:
    _section(4, "Causes of Loss", "ClaimCenter LossCause recorded at FNOL")
    df = pd.DataFrame(a["loss_causes"])
    if df.empty:
        st.info("Insufficient evidence for causes of loss.")
        return
    df["Cause"] = df["loss_cause"].map(lambda c: CAUSE_NAMES.get(c, c))
    df["Share"] = df["pct"] * 100
    left, right = st.columns(2)
    with left:
        _hbar(df, "Cause", "cnt", "Claims by cause", ",.0f",
              [alt.Tooltip("Cause:N"), alt.Tooltip("cnt:Q", title="Claims"), alt.Tooltip("Share:Q", format=".1f", title="Share %"),
               alt.Tooltip("avg_incurred:Q", title="Avg incurred", format="$,.0f")])
    with right:
        _hbar(df, "Cause", "avg_incurred", "Average incurred by cause", "$.2~s",
              [alt.Tooltip("Cause:N"), alt.Tooltip("avg_incurred:Q", title="Avg incurred", format="$,.0f"),
               alt.Tooltip("incurred:Q", title="Total incurred", format="$,.0f")])
    desc = pd.DataFrame(a.get("loss_descriptions") or [])
    if not desc.empty:
        st.dataframe(desc.rename(columns={"description": "Most frequent loss descriptions", "cnt": "Claims", "avg_incurred": "Avg incurred"}),
                     hide_index=True, width="stretch",
                     column_config={"Avg incurred": st.column_config.NumberColumn(format="$%,.0f")})


def _loss_types(a: Dict[str, Any]) -> None:
    lt, s = a["loss_types"], a["summary"]
    _section(5, "Types of Losses", "By ClaimCenter exposure and coverage: paid vs case reserve")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Paid loss", _money(s["paid_loss"]))
    c2.metric("Case reserves", _money(s["outstanding_reserve"]))
    c3.metric("ALAE", _money(s["paid_expense"]))
    c4.metric("Recoveries", _money(s["recoveries"]), help="Subrogation + salvage")
    df = pd.DataFrame(lt["by_exposure"][:10])
    if df.empty:
        return
    df["Exposure / coverage"] = df["exposure_type"] + " · " + df["coverage_type"]
    long = df.melt(id_vars=["Exposure / coverage", "exposures", "incurred", "total_losses", "denied"],
                   value_vars=["paid", "outstanding"], var_name="Part", value_name="Amount")
    long["Part"] = long["Part"].map({"paid": "Paid", "outstanding": "Case reserve"})
    order = df.sort_values("incurred", ascending=False)["Exposure / coverage"].tolist()
    chart = alt.Chart(long).mark_bar(cornerRadiusEnd=4, height={"band": 0.7}, stroke="white", strokeWidth=2).encode(
        y=alt.Y("Exposure / coverage:N", sort=order, title=None, axis=alt.Axis(labelLimit=260)),
        x=alt.X("sum(Amount):Q", title=None, axis=alt.Axis(format="$.2~s")),
        color=alt.Color("Part:N", scale=alt.Scale(domain=["Paid", "Case reserve"], range=[SERIES, COMPARE]), legend=alt.Legend(title=None)),
        order=alt.Order("Part:N", sort="descending"),
        tooltip=[alt.Tooltip("Exposure / coverage:N"), alt.Tooltip("Part:N"), alt.Tooltip("Amount:Q", format="$,.0f"),
                 alt.Tooltip("exposures:Q", title="Exposures"), alt.Tooltip("total_losses:Q", title="Total losses"),
                 alt.Tooltip("denied:Q", title="Denied")])
    _chart(chart.properties(title="Incurred by exposure / coverage"), alt.Step(30))


def _segments(a: Dict[str, Any]) -> None:
    sg = a["segments"]
    _section(6, "Customer Segments Affected", f"Frequency index vs pattern average ({sg.get('avg_frequency_per_1000', 0):.1f} per 1,000 = 1.00x)")
    blocks = []
    if sg.get("by_product"):
        blocks.append(("Product line", pd.DataFrame(sg["by_product"]).rename(columns={"product_code": "Segment"})))
    if sg.get("by_powertrain"):
        blocks.append(("Powertrain", pd.DataFrame(sg["by_powertrain"]).rename(columns={"vehicle_powertrain": "Segment"})))
    if sg.get("by_vehicle_age"):
        blocks.append(("Vehicle age (years)", pd.DataFrame(sg["by_vehicle_age"]).rename(columns={"vehicle_age_band": "Segment"})))
    if sg.get("by_vehicle_model"):
        blocks.append(("Vehicle model", pd.DataFrame(sg["by_vehicle_model"]).rename(columns={"vehicle_model": "Segment"})))
    cols = st.columns(min(len(blocks), 2) or 1)
    for i, (title, df) in enumerate(blocks):
        if "credible" not in df:
            df["credible"] = True
        df["Credibility"] = df["credible"].map({True: "Credible", False: "Low credibility"})
        with cols[i % len(cols)]:
            _hbar(df, "Segment", "index_vs_avg", title, ".2f",
                  [alt.Tooltip("Segment:N"), alt.Tooltip("frequency_per_1000:Q", title="Per 1,000", format=".1f"),
                   alt.Tooltip("claims:Q", title="Claims"), alt.Tooltip("index_vs_avg:Q", title="Index", format=".2f")],
                  color_field="Credibility", sort_desc=title != "Vehicle age (years)", rule_at=1.0)


def _geography(a: Dict[str, Any]) -> None:
    geo = a["geography"]
    _section(7, "Geographic Patterns", "States with ≥10 claims; credible at ≥30 claims · dashed line = pattern average")
    df = pd.DataFrame(geo.get("states") or [])
    left, right = st.columns([3, 2])
    with left:
        if df.empty:
            st.info("Insufficient evidence for geographic patterns.")
        else:
            df["Credibility"] = df["credible"].map({True: "Credible", False: "Low credibility"})
            _hbar(df, "state", "index_vs_avg", "Frequency index by state", ".2f",
                  [alt.Tooltip("state:N", title="State"), alt.Tooltip("frequency_per_1000:Q", title="Per 1,000", format=".1f"),
                   alt.Tooltip("claims:Q", title="Claims"), alt.Tooltip("index_vs_avg:Q", title="Index", format=".2f")],
                  color_field="Credibility", rule_at=1.0)
    with right:
        st.metric("CAT share of incurred", _pct(geo.get("cat_share_of_incurred_pct")))
        cats = pd.DataFrame(geo.get("cat_events") or [])
        if not cats.empty:
            st.dataframe(cats.rename(columns={"cat_code": "Catastrophe", "claims": "Claims", "incurred": "Incurred"}),
                         hide_index=True, width="stretch",
                         column_config={"Incurred": st.column_config.NumberColumn(format="$%,.0f")})
        else:
            st.caption("No catastrophe-coded claims for this pattern.")
        st.caption(f"{geo.get('low_credibility_states', 0)} states below the credibility threshold.")


def _gaps(a: Dict[str, Any]) -> None:
    g = a["coverage_gaps"]
    _section(8, "Existing Coverage Gaps", "Claims the current policy form denies — direct evidence of unmet coverage demand")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(f"Denied ({g['denied_claims']} claims)", _pct(g["denial_rate_pct"]),
              delta=_delta_pts(g["denial_rate_pct"], g["baseline_denial_rate_pct"]), delta_color="inverse")
    c2.metric("Gap-exclusion denials", _pct(g["gap_denial_rate_pct"]), help="Denials under exclusions a new coverage could buy back")
    c3.metric("Denied loss", _money(g["gap_denial_estimated_loss"]), help="Customer loss estimated at FNOL on gap-exclusion denials")
    c4.metric("Closed without payment", _pct(g["closed_without_payment_pct"]),
              delta=_delta_pts(g["closed_without_payment_pct"], g["baseline_closed_without_payment_pct"]), delta_color="inverse")
    df = pd.DataFrame(g.get("denial_reasons") or [])
    if not df.empty:
        df["Reason"] = df["reason"].map(lambda r: DENIAL_NAMES.get(r, r))
        _hbar(df, "Reason", "claims", "Denials by reason", ",.0f",
              [alt.Tooltip("Reason:N"), alt.Tooltip("claims:Q", title="Claims"),
               alt.Tooltip("estimated_loss_at_fnol:Q", title="Est. loss at FNOL", format="$,.0f")])
    if (g.get("gap_denial_rate_pct") or 0) >= 5:
        st.warning(f"**Coverage gap signal:** {g['gap_denials']} claims ({_pct(g['gap_denial_rate_pct'])}), about "
                   f"{_money(g['gap_denial_estimated_loss'])} of customer loss, were denied under exclusions a new coverage could address.")
    else:
        st.info("No meaningful claims evidence of a coverage gap: exclusion-based denials are negligible for this pattern.")
    st.caption(f"Limit exhausted on {g['limit_exhausted_exposures']} exposures · {g['total_losses']} total losses")


def _recurring(a: Dict[str, Any]) -> None:
    h = a["handling"]
    _section(9, "Recurring Patterns", "Repeat claims, reopens, litigation, SIU and recoveries — deltas vs baseline")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Repeat-claim policies", f"{h['repeat_claim_policies']}")
    c2.metric("Reopen rate", _pct(h["reopen_rate_pct"]), delta=_delta_pts(h["reopen_rate_pct"], h["baseline_reopen_rate_pct"]),
              delta_color="inverse")
    c3.metric("Litigation rate", _pct(h["litigation_rate_pct"]),
              delta=_delta_pts(h["litigation_rate_pct"], h["baseline_litigation_rate_pct"]), delta_color="inverse")
    c4.metric("SIU referral rate", _pct(h["siu_referral_rate_pct"]),
              delta=_delta_pts(h["siu_referral_rate_pct"], h["baseline_siu_referral_rate_pct"]), delta_color="inverse")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Subrogation recovered", _money(h["subrogation_recovered"]))
    c2.metric("Subro recovery rate", _pct(h["subrogation_recovery_rate_pct"]), help="Of paid on other-party-at-fault claims")
    c3.metric("Salvage recovered", _money(h["salvage_recovered"]))
    c4.metric("Closed as fraud", f"{h['fraud_closures']}")
    notable = a.get("notable_portfolio_trends") or []
    if notable:
        st.caption("Portfolio patterns with a statistically significant frequency trend: " +
                   ", ".join(f"**{t['tag_value']}** {t['annual_trend_pct']:+.1f}%/yr" for t in notable))


def _emerging(a: Dict[str, Any]) -> None:
    rd, h, em = a["reserve_development"], a["handling"], a["emerging"]
    _section(10, "Emerging Risks", "Reserve development, cycle time and open inventory")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Reserve development", f"{rd.get('incurred_to_initial_ratio') or 0:.2f}x",
              delta=f"baseline {rd.get('baseline_incurred_to_initial_ratio') or 0:.2f}x", delta_color="off",
              help="Above 1.0 = initial reserves were too low (adverse development)")
    c2.metric("Median cycle time", f"{h['cycle_time_median_days']:.0f} days",
              delta=f"{h['cycle_time_median_days'] - h['baseline_cycle_time_median_days']:+.0f} days vs baseline", delta_color="inverse")
    c3.metric("Claims, last 12 months", f"{em.get('last_12m_claims', 0)}",
              delta=f"{em['last_12m_vs_prior_pct']:+.0f}% vs prior 12m" if em.get("last_12m_vs_prior_pct") is not None else None,
              delta_color="inverse")
    c4.metric("Median report lag", f"{h['report_lag_median_days']:.0f} days",
              delta=f"{_pct(h['late_reported_pct'])} after 30 days", delta_color="off")
    left, right = st.columns(2)
    with left:
        df = pd.DataFrame([r for r in rd.get("by_year", []) if r.get("incurred_to_initial_ratio")])
        if not df.empty:
            df["AY"] = df["year"].astype(str)
            base = rd.get("baseline_incurred_to_initial_ratio") or 1.0
            enc = dict(x=alt.X("AY:O", title="Accident year", axis=alt.Axis(labelAngle=0)),
                       y=alt.Y("incurred_to_initial_ratio:Q", title="Incurred ÷ FNOL reserve", scale=alt.Scale(zero=False)),
                       tooltip=[alt.Tooltip("AY:O"), alt.Tooltip("incurred_to_initial_ratio:Q", title="Ratio", format=".2f")])
            chart = (alt.Chart(df).mark_line(color=SERIES, strokeWidth=2).encode(**enc)
                     + alt.Chart(df).mark_point(color=SERIES, size=70, filled=True, stroke="white", strokeWidth=2).encode(**enc)
                     + alt.Chart(pd.DataFrame({"y": [base], "label": [f"Baseline {base:.2f}x"]})).mark_rule(
                         color=BASELINE, strokeDash=[4, 3], strokeWidth=1.5).encode(y="y:Q", tooltip=["label:N"]))
            _chart(chart.properties(title="Incurred ÷ FNOL reserve by AY"))
            st.caption("Dashed line = baseline. Above 1.0 means initial reserves were set too low.")
    with right:
        aging = pd.DataFrame([{"Age (days)": k, "Open claims": v} for k, v in h["open_aging"].items()])
        if not aging.empty:
            chart = alt.Chart(aging).mark_bar(cornerRadiusEnd=4, width={"band": 0.6}, color=SERIES).encode(
                x=alt.X("Age (days):O", sort=list(h["open_aging"].keys()), axis=alt.Axis(labelAngle=0)),
                y=alt.Y("Open claims:Q"),
                tooltip=["Age (days)", "Open claims"])
            _chart(chart.properties(title="Open inventory aging"))
            st.caption(f"{h['open_claims']} open claims · {_money(h['open_outstanding_reserve'])} reserved")


def _recommendation(a: Dict[str, Any]) -> None:
    rec = a.get("recommendation") or {}
    _section(11, "Recommendation — Is New Coverage Necessary?", "Directional finding for human review; the AI never approves")
    if not rec:
        return
    verdict = rec.get("verdict", "")
    box = st.success if verdict.startswith("BUILD") else st.warning if verdict.startswith(("ENDORSE", "PRICE")) else st.info
    box(f"**{verdict}** — {_md(rec.get('finding', ''))}")
    left, right = st.columns(2)
    with left:
        st.markdown("**Evidence signals**")
        st.markdown("\n".join(f"- {_md(s)}" for s in rec.get("signals", [])) or "- None above threshold")
    with right:
        st.markdown("**Suggested next steps**")
        st.markdown("\n".join(f"- {_md(x)}" for x in rec.get("actions", [])) or "- Continue quarterly monitoring")


def _proxy_banner(a: Dict[str, Any]) -> None:
    basis = a.get("basis") or {}
    if basis.get("basis") != "proxy":
        return
    how = "auto-suggested from the title" if basis.get("auto_suggested") else "selected by the reviewer"
    st.warning(f"**Proxy data — not this product's own claims.** No ClaimCenter claims are tagged for this product, so every "
               f"section below pools the claims of the related risk pattern(s) **{' + '.join(basis.get('proxy_tags', []))}** "
               f"({how}). Frequency and severity show how a comparable peril behaves; claim counts and dollar totals belong "
               f"to the proxy patterns, not to the new product.")


def _line_baseline(a: Dict[str, Any], key_prefix: str) -> bool:
    """Whole-line claims experience for a product with no own or proxy history."""
    lb = a.get("line_baseline") or {}
    if not lb.get("has_data"):
        return False
    st.info("**No direct or proxy claims history.** These are whole-line figures for "
            f"**{', '.join(lb['products'])}**, not this product's risk: a starting point for wording, reserving and KPI "
            "thresholds. Choose proxy risk patterns to run the full 11-section claims analysis on comparable claims.")
    with st.container(border=True, key=f"rtcard_{key_prefix}_line"):
        st.markdown("##### Line-of-Business Baseline")
        st.caption(f"{', '.join(lb['products'])} · valued {lb['valuation_date']} · frequency per 1,000 exposure-years")
        c = st.columns(6)
        c[0].metric("Claims", f"{lb['claims']:,}")
        c[1].metric("Frequency / 1,000", f"{lb['frequency_per_1000']:.1f}")
        c[2].metric("Avg severity", _money(lb["avg_severity"]), help=f"Median {_money(lb['median_severity'])}")
        c[3].metric("P90 severity", _money(lb["p90_severity"]))
        c[4].metric("Loss + ALAE ratio", _pct(lb["loss_ratio_pct"]))
        c[5].metric("Denial rate", _pct(lb["denial_rate_pct"]))
        df = pd.DataFrame(lb["top_patterns"])
        if not df.empty:
            df["Pattern"] = df["tag_value"].map(lambda t: CAUSE_NAMES.get(t, t))
            _hbar(df, "Pattern", "share_pct", "Most frequent risk patterns in the line (share of claims)", ".0f",
                  [alt.Tooltip("Pattern:N"), alt.Tooltip("claims:Q", title="Claims"),
                   alt.Tooltip("share_pct:Q", title="Share %", format=".1f"),
                   alt.Tooltip("avg_incurred:Q", title="Avg incurred", format="$,.0f")])
    return True


def _section_note(section: int, note: str, key_prefix: str, save_note: Optional[Callable[[int, str], bool]],
                  locked: bool) -> None:
    """Reviewer note beside a section's charts. Notes add judgement; they never change the numbers."""
    if note:
        st.info(f"**📝 Reviewer note:** {_md(note)}")
    if save_note is None or locked:
        return
    with st.expander("✏️ Edit reviewer note" if note else "📝 Add reviewer note"):
        text = st.text_area("Reviewer note", value=note, key=f"{key_prefix}_note_{section}", label_visibility="collapsed",
                            placeholder="e.g. 2024 spike driven by one hail event; treat as non-recurring.")
        c1, c2, _ = st.columns([1, 1, 3])
        if c1.button("Save note", key=f"{key_prefix}_save_{section}", type="primary", width="stretch"):
            if save_note(section, text):
                st.rerun()
        if note and c2.button("Remove", key=f"{key_prefix}_del_{section}", width="stretch"):
            if save_note(section, ""):
                st.rerun()


def render_claims_dashboard(analytics: Dict[str, Any], notes: Optional[Dict[str, str]] = None,
                            save_note: Optional[Callable[[int, str], bool]] = None,
                            key_prefix: str = "dash", locked: bool = False) -> bool:
    """Render the 11 claims sections, each with its reviewer note.

    Returns False when the brief has no structured analytics. *save_note(section, text)* persists a note;
    *locked* hides note editing (e.g. after sign-off). A brief with no own or proxy history shows the
    line-of-business baseline instead of the 11 sections.
    """
    if not analytics:
        return False
    if not analytics.get("summary", {}).get("has_data"):
        return _line_baseline(analytics, key_prefix)
    _proxy_banner(analytics)
    notes = notes or {}
    for section, fn in enumerate((_frequency, _severity, _history, _causes, _loss_types, _segments, _geography, _gaps,
                                  _recurring, _emerging, _recommendation), start=1):
        with st.container(border=True, key=f"rtcard_{key_prefix}_s{section}"):
            try:
                fn(analytics)
            except Exception as exc:   # one bad section should not blank the whole report
                st.warning(f"Could not render this section: {exc}")
            _section_note(section, notes.get(str(section), ""), key_prefix, save_note, locked)
    return True
