"""
Rate indication panel (Actuarial workspace)
===========================================
Directional premium indication for the new coverage: the newly covered claims' loss cost, developed, trended
and loaded for ALAE, ULAE, expenses and profit. The actuary edits the assumptions; every figure comes from
backend/pricing.py and nothing is stored.
"""
from __future__ import annotations

import html
from typing import Any, Callable, Dict, Optional

import pandas as pd
import streamlit as st


def _money(x: Optional[float], cents: bool = False) -> str:
    if x is None:
        return "—"
    return f"${x:,.2f}" if cents else f"${x:,.0f}"


def _md(text: str) -> str:
    return (text or "").replace("$", "\\$")


def render_pricing(brief: Dict[str, Any], fetch: Callable[[Dict[str, Any]], Optional[Dict[str, Any]]]) -> None:
    """*fetch(overrides)* calls GET /briefs/{id}/pricing with the assumption overrides as query parameters."""
    bid = brief["id"]
    state_key = f"pricing_overrides_{bid}"
    overrides: Dict[str, Any] = st.session_state.get(state_key, {})

    st.markdown("### Rate indication")
    st.caption("A directional premium for the new coverage, built step by step from the claims it would newly pay. "
               "Computed in Python from the brief's claims data — the AI never sets a number. Not a rate filing.")
    data = fetch(overrides)
    if data is None:
        st.error("Could not load the rate indication from the backend.")
        return
    if not data.get("available"):
        st.info(data.get("reason", "No rate indication is available for this brief."))
        return

    a, unit = data["assumptions"], data["exposure_unit"]
    rng, cred = data["range"], data["credibility"]

    # Headline: indicated premium, range, share of today's premium, credibility
    share = data.get("share_of_current_premium_pct")
    z_pct = round(100 * cred["z"])
    range_text = (f"{_money(rng['low'])} – {_money(rng['high'])}" if rng.get("low") is not None else "no statistical range")
    st.markdown(
        '<div class="rt-price-hero">'
        f'<div class="main"><div class="k">Indicated premium</div>'
        f'<div class="v">{_money(data["indicated_premium"], cents=True)}<small> per {html.escape(unit[:-1] if unit.endswith("s") else unit)}</small></div>'
        f'<div class="sub">Range {range_text} · {html.escape(rng["basis"])}</div></div>'
        f'<div class="tile"><div class="k">vs today\'s average premium</div><div class="v">{f"{share:.1f}%" if share is not None else "—"}</div>'
        f'<div class="sub">of {_money(data.get("average_current_premium"))} in the same scope</div></div>'
        f'<div class="tile"><div class="k">Credibility (Z)</div><div class="v">{cred["z"]:.2f}</div>'
        f'<div class="rt-bar"><i style="width:{z_pct}%"></i></div>'
        f'<div class="sub">{cred["claims"]:,} claims · full credibility at {cred["full_credibility_claims"]:,}</div></div>'
        '</div>',
        unsafe_allow_html=True,
    )
    priced = ("claims the new coverage would newly pay" if data["priced_claims"] == "newly_covered"
              else "every claim of the pattern")
    st.caption(f"Prices the {priced}. For context, the whole pattern costs "
               f"{_money(data.get('pattern_loss_cost'), cents=True)} per {unit[:-1] if unit.endswith('s') else unit} "
               f"today, mostly already inside today's premium. Effective {data['effective_date']}, average accident date "
               f"{data['average_accident_date']}.")

    # Assumptions
    with st.expander("⚙️ Assumptions", expanded=bool(overrides)):
        fitted = a.get("fitted_frequency_trend_pct")
        fitted_txt = (f"fitted {fitted:+.1f}%/yr, {'significant' if a.get('fitted_trend_significant') else 'not significant'}"
                      if fitted is not None else "no fitted trend")
        with st.form(key=f"pricing_form_{bid}", border=False):
            c1, c2, c3 = st.columns(3)
            vals = {
                "experience_years": c1.number_input("Experience years", 1, 10, int(a["experience_years"]), 1),
                "months_to_effective": c2.number_input("Months to effective date", 0, 36, int(a["months_to_effective"]), 1),
                "frequency_trend_pct": c3.number_input(f"Frequency trend %/yr ({fitted_txt})", -30.0, 50.0,
                                                       float(a["frequency_trend_pct"]), 0.5),
                "severity_trend_pct": c1.number_input("Severity trend %/yr", -10.0, 25.0, float(a["severity_trend_pct"]), 0.5),
                "ulae_pct": c2.number_input("ULAE %", 0.0, 20.0, float(a["ulae_pct"]), 0.5),
                "expense_ratio_pct": c3.number_input("Expense ratio %", 0.0, 60.0, float(a["expense_ratio_pct"]), 0.5),
                "profit_pct": c1.number_input("Profit & contingencies %", -10.0, 20.0, float(a["profit_pct"]), 0.5),
            }
            if data["priced_claims"] == "whole_pattern":
                vals["apply_development"] = c2.checkbox("Develop open claims", value=bool(a["apply_development"]))
            b1, b2 = st.columns([1, 1])
            if b1.form_submit_button("Recalculate", type="primary", use_container_width=True):
                st.session_state[state_key] = vals
                st.rerun()
            if b2.form_submit_button("Reset to defaults", use_container_width=True):
                st.session_state.pop(state_key, None)
                st.rerun()

    left, right = st.columns([1.15, 1])
    with left:
        st.markdown("#### How the premium is built")
        steps = "".join(
            f'<div class="rt-step"><span class="n">{i}</span><span class="t">{html.escape(s["step"])}</span>'
            f'<span class="v">{_money(s["value"], cents=True)}</span></div>'
            for i, s in enumerate(data["steps"], 1))
        st.markdown(f'<div class="rt-steps">{steps}</div>', unsafe_allow_html=True)
    with right:
        st.markdown("#### What moves it most")
        base = data["indicated_premium"] or 0
        sens = data["sensitivity"]
        span = max([abs(s["high"] - base) for s in sens] + [abs(base - s["low"]) for s in sens] + [1e-9])
        bars = ""
        for s in sens:
            lo_w, hi_w = 50 * (base - s["low"]) / span, 50 * (s["high"] - base) / span
            bars += (f'<div class="rt-tornado-row"><div class="l">{html.escape(s["assumption"])}</div>'
                     f'<div class="track"><i class="lo" style="width:{max(lo_w, 0):.1f}%"></i>'
                     f'<i class="hi" style="width:{max(hi_w, 0):.1f}%"></i></div>'
                     f'<div class="r">{_money(s["low"])} – {_money(s["high"])}</div></div>')
        st.markdown(f'<div class="rt-tornado">{bars}</div>', unsafe_allow_html=True)

    st.markdown("#### Experience by accident year")
    rows = data["experience"]
    df = pd.DataFrame([{
        "Accident year": r["year"],
        f"Exposure ({unit})": r["earned_exposure"],
        "Claims": r["claims"],
        "Frequency / 1,000": r["frequency_per_1000"],
        "Avg severity": r["avg_severity"],
        "Loss cost": r["loss_cost_per_exposure"],
        "Development": r["development_factor"],
        "Trend factor": r["trend_factor"],
        "Trended loss cost": r["trended_loss_cost"],
        "Credible": "yes" if r["credible"] else "low",
    } for r in rows])
    st.dataframe(df, hide_index=True, use_container_width=True, column_config={
        "Avg severity": st.column_config.NumberColumn(format="$%.0f"),
        "Loss cost": st.column_config.NumberColumn(format="$%.2f"),
        "Trended loss cost": st.column_config.NumberColumn(format="$%.2f"),
        f"Exposure ({unit})": st.column_config.NumberColumn(format="%.0f"),
    })

    for note in data["notes"]:
        st.markdown(f'<div class="insufficient-evidence">ℹ️ {html.escape(note)}</div>', unsafe_allow_html=True)
