"""
Rate indication panel (Actuarial workspace)
===========================================
Premium indication for the new coverage: the newly covered claims' loss cost, developed, trended, adjusted for
catastrophes, large losses and policyholder behaviour, credibility-weighted with external benchmarks, and loaded
for ALAE, ULAE, expenses and profit. The actuary tries assumptions (what-if), saves the selected ones, records
benchmarks and approves the indication with a selected rate; every figure comes from backend/pricing.py.
"""
from __future__ import annotations

import html
from datetime import date
from typing import Any, Callable, Dict, Optional

import pandas as pd
import streamlit as st

DEV_METHODS = {"chain_ladder": "Chain-ladder", "bornhuetter_ferguson": "Bornhuetter-Ferguson",
               "heuristic": "Heuristic (FNOL reserve ratio)"}


def _money(x: Optional[float], cents: bool = False) -> str:
    if x is None:
        return "—"
    return f"${x:,.2f}" if cents else f"${x:,.0f}"


def _md(text: str) -> str:
    return (text or "").replace("$", "\\$")


def render_pricing(brief: Dict[str, Any], call: Callable[..., Optional[Dict[str, Any]]]) -> None:
    """*call(method, path, **requests_kwargs)* calls /briefs/{id}/{path} on the backend."""
    bid = brief["id"]
    state_key = f"pricing_overrides_{bid}"
    overrides: Dict[str, Any] = st.session_state.get(state_key, {})

    st.markdown("### Rate indication")
    st.caption("The premium for the new coverage, built step by step from the claims it would newly pay. Computed in "
               "Python from the brief's claims data — the AI never sets a number. The actuary selects and approves it.")
    params = {k: (str(v).lower() if isinstance(v, bool) else v) for k, v in overrides.items()}
    data = call("GET", "pricing", timeout=120, params=params)
    if data is None:
        st.error("Could not load the rate indication from the backend.")
        return
    if not data.get("available"):
        st.info(data.get("reason", "No rate indication is available for this brief."))
        return

    a, unit = data["assumptions"], data["exposure_unit"]
    unit1 = unit[:-1] if unit.endswith("s") else unit
    rng, cred = data["range"], data["credibility"]
    incremental = data["priced_claims"] == "newly_covered"
    if data.get("what_if"):
        st.warning("**What-if:** these numbers use assumptions you are trying out, not the saved selection. Save them "
                   "to make them the selection, or reset.")

    # Headline: indicated premium, range, share of today's premium, credibility
    share = data.get("share_of_current_premium_pct")
    z_pct = round(100 * cred["z"])
    range_text = (f"{_money(rng['low'])} – {_money(rng['high'])}" if rng.get("low") is not None else "no statistical range")
    comp_txt = (f"blended with benchmark {_money(cred['complement'], cents=True)}" if cred.get("applied")
                else "no complement — experience at full weight")
    st.markdown(
        '<div class="rt-price-hero">'
        f'<div class="main"><div class="k">Indicated premium</div>'
        f'<div class="v">{_money(data["indicated_premium"], cents=True)}<small> per {html.escape(unit1)}</small></div>'
        f'<div class="sub">Range {range_text} · {html.escape(rng["basis"])}</div></div>'
        f'<div class="tile"><div class="k">vs today\'s average premium</div><div class="v">{f"{share:.1f}%" if share is not None else "—"}</div>'
        f'<div class="sub">of {_money(data.get("average_current_premium"))} in the same scope</div></div>'
        f'<div class="tile"><div class="k">Credibility (Z)</div><div class="v">{cred["z"]:.2f}</div>'
        f'<div class="rt-bar"><i style="width:{z_pct}%"></i></div>'
        f'<div class="sub">{cred["claims"]:,} claims · full at {cred["full_credibility_claims"]:,} · {html.escape(comp_txt)}</div></div>'
        '</div>',
        unsafe_allow_html=True,
    )
    priced = "claims the new coverage would newly pay" if incremental else "every claim of the pattern"
    st.caption(f"Prices the {priced}. For context, the whole pattern costs "
               f"{_money(data.get('pattern_loss_cost'), cents=True)} per {unit1} today, mostly already inside today's "
               f"premium. Effective {data['effective_date']}, average accident date {data['average_accident_date']}.")

    _render_assumptions(bid, data, a, overrides, state_key, incremental, call)

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
        "Non-CAT capped share": r.get("basic_share"),
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

    _render_benchmarks(bid, data, unit1, call)
    _render_approval(bid, data, call)

    for note in data["notes"]:
        st.markdown(f'<div class="insufficient-evidence">ℹ️ {html.escape(note)}</div>', unsafe_allow_html=True)


def _render_assumptions(bid: int, data: Dict[str, Any], a: Dict[str, Any], overrides: Dict[str, Any], state_key: str,
                        incremental: bool, call: Callable[..., Optional[Dict[str, Any]]]) -> None:
    saved = data.get("saved_assumptions") or {}
    with st.expander("⚙️ Assumptions" + (" · saved selection in use" if saved and not overrides else ""),
                     expanded=bool(overrides)):
        prov = data.get("provenance") or {}
        if prov:
            st.caption("Defaults from company assumptions: " + "; ".join(
                f"{k.replace('_pct', '').replace('_', ' ')} — {_md(v)}" for k, v in prov.items()))
        else:
            st.caption("⚠️ Expense, ULAE and profit defaults are placeholders: set them in Company assumptions.")
        fitted = a.get("fitted_frequency_trend_pct")
        fitted_txt = (f"fitted {fitted:+.1f}%/yr, {'significant' if a.get('fitted_trend_significant') else 'not significant'}"
                      if fitted is not None else "no fitted trend")
        with st.form(key=f"pricing_form_{bid}", border=False):
            st.markdown("**Experience and trend**")
            c1, c2, c3 = st.columns(3)
            vals = {
                "experience_years": c1.number_input("Experience years", 1, 10, int(a["experience_years"]), 1),
                "months_to_effective": c2.number_input("Months to effective date", 0, 36, int(a["months_to_effective"]), 1),
                "frequency_trend_pct": c3.number_input(f"Frequency trend %/yr ({fitted_txt})", -30.0, 50.0,
                                                       float(a["frequency_trend_pct"]), 0.5),
                "severity_trend_pct": c1.number_input("Severity trend %/yr", -10.0, 25.0, float(a["severity_trend_pct"]), 0.5),
            }
            st.markdown("**Development**")
            d1, d2, d3 = st.columns(3)
            methods = list(DEV_METHODS)
            vals["dev_method"] = d1.selectbox(
                "Method", methods, index=methods.index(a["dev_method"]), format_func=DEV_METHODS.get,
                help="Newly covered claims develop on reported counts (chain-ladder) whatever the method; the method "
                     "applies when the whole pattern is priced.")
            vals["tail_factor"] = d2.number_input("Tail factor beyond the last age", 1.0, 1.5, float(a["tail_factor"]), 0.005,
                                                  format="%.3f")
            vals["apply_development"] = d3.checkbox("Apply development", value=bool(a["apply_development"]))
            st.markdown("**Catastrophes and large losses**")
            l1, l2 = st.columns(2)
            vals["large_loss_cap"] = l1.number_input("Large-loss cap per claim ($)", 10_000.0, 5_000_000.0,
                                                     float(a["large_loss_cap"]), 10_000.0, format="%.0f")
            vals["cat_load_pct"] = l2.number_input(f"CAT provision % (data: {a['data_cat_load_pct']:.1f}%)", 0.0, 200.0,
                                                   float(a["cat_load_pct"]), 0.5,
                                                   help="Replace with a catastrophe-model load where one exists.")
            st.markdown("**Policyholder behaviour (judgement)**")
            b1, b2 = st.columns(2)
            if incremental:
                vals["unreported_load_pct"] = b1.number_input(
                    "Unreported demand %", 0.0, 200.0, float(a["unreported_load_pct"]), 5.0,
                    help="Losses never reported because the policyholder knew they were excluded.")
            vals["adverse_selection_pct"] = b2.number_input(
                "Adverse selection %", -20.0, 100.0, float(a["adverse_selection_pct"]), 1.0,
                help="Buyers of an optional cover are worse risks than the whole book.")
            st.markdown("**Expenses and profit**")
            e1, e2, e3 = st.columns(3)
            vals["ulae_pct"] = e1.number_input("ULAE %", 0.0, 20.0, float(a["ulae_pct"]), 0.5)
            vals["expense_ratio_pct"] = e2.number_input("Expense ratio %", 0.0, 60.0, float(a["expense_ratio_pct"]), 0.5)
            vals["profit_pct"] = e3.number_input("Profit & contingencies %", -10.0, 20.0, float(a["profit_pct"]), 0.5)
            vals["apply_complement"] = st.checkbox("Blend with the benchmark complement (credibility)",
                                                   value=bool(a["apply_complement"]))
            vals["price_whole_pattern"] = st.checkbox(
                "Standalone product: price every claim of the pattern", value=bool(a["price_whole_pattern"]),
                help="For a cover sold on its own (parametric, a separate policy) rather than a top-up that only "
                     "pays what today's form denies.")
            b1, b2, b3 = st.columns(3)
            try_it = b1.form_submit_button("Try (what-if)", use_container_width=True)
            save = b2.form_submit_button("Save as selected", type="primary", use_container_width=True)
            reset = b3.form_submit_button("Reset what-if", use_container_width=True)
        if try_it:
            st.session_state[state_key] = vals
            st.rerun()
        if save:
            # Keep only what differs from the defaults, so company settings changes still reach this product
            defaults = data.get("defaults") or {}
            changed = {k: v for k, v in vals.items()
                       if not (k in defaults and (v == defaults[k] or (isinstance(v, float) and isinstance(defaults[k], (int, float))
                                                                        and abs(v - defaults[k]) < 1e-9)))}
            if call("PUT", "actuarial/assumptions", json={"assumptions": changed}) is not None:
                st.session_state.pop(state_key, None)
                st.rerun()
        if reset:
            st.session_state.pop(state_key, None)
            st.rerun()
        if saved and st.button("Clear the saved selection (back to defaults)", key=f"pricing_clear_{bid}"):
            if call("PUT", "actuarial/assumptions", json={"assumptions": {}}) is not None:
                st.session_state.pop(state_key, None)
                st.rerun()


def _render_benchmarks(bid: int, data: Dict[str, Any], unit1: str, call: Callable[..., Optional[Dict[str, Any]]]) -> None:
    benchmarks = data.get("benchmarks") or []
    cred = data["credibility"]
    with st.expander(f"📚 Credibility complement — external benchmarks ({len(benchmarks)})", expanded=False):
        st.caption(f"With Z = {cred['z']:.2f}, the experience gets {cred['z']:.0%} of the weight and the mean of the "
                   "benchmarks below (trended to the average accident date) the rest. Enter IIB industry loss costs, "
                   f"competitors' published rates or reinsurer quotes (e.g. GIC Re), per {unit1}, with their source.")
        for b in benchmarks:
            c1, c2, c3 = st.columns([5, 1.2, 1])
            kind = "loss cost" if b["kind"] == "loss_cost" else f"premium @ {b['permissible_loss_ratio_pct']:.0f}% PLR"
            c1.markdown(f"{'✅' if b.get('include', True) else '⏸️'} **{_md(b['source'])}** — {_money(b['value'], True)} "
                        f"{kind}, as of {b['as_of']}" + (f" · {_md(b['unit'])}" if b.get("unit") else "")
                        + (f" · [link]({b['url']})" if b.get("url") else ""))
            if c2.button("Exclude" if b.get("include", True) else "Include", key=f"bm_inc_{bid}_{b['id']}"):
                if call("PUT", f"actuarial/benchmarks/{b['id']}", json={"include": not b.get("include", True)}) is not None:
                    st.rerun()
            if c3.button("Delete", key=f"bm_del_{bid}_{b['id']}"):
                if call("DELETE", f"actuarial/benchmarks/{b['id']}") is not None:
                    st.rerun()
        with st.form(key=f"bm_form_{bid}", clear_on_submit=True):
            types = data.get("benchmark_types") or {"loss_cost": "Loss cost", "premium": "Premium"}
            c1, c2, c3 = st.columns(3)
            kind = c1.selectbox("Type", list(types), format_func=types.get)
            value = c2.number_input(f"Value per {unit1} ($)", 0.0, 1e7, 0.0, 1.0)
            as_of = c3.date_input("Applies as of", value=date.today())
            source = st.text_input("Source", placeholder="e.g. IIB motor OD statistics, private car, MH, FY2024-25")
            c4, c5, c6 = st.columns(3)
            plr = c4.number_input("Permissible loss ratio % (premium only)", 20.0, 100.0, 65.0, 1.0)
            unit = c5.text_input("Exposure unit", placeholder=f"per {unit1}")
            url = c6.text_input("Reference URL")
            if st.form_submit_button("Add benchmark", type="primary"):
                body = {"kind": kind, "value": value, "as_of": as_of.isoformat(), "source": source,
                        "permissible_loss_ratio_pct": plr, "unit": unit, "url": url}
                if call("POST", "actuarial/benchmarks", json=body) is not None:
                    st.rerun()

        st.markdown("**Import an industry / reinsurer file (CSV)**")
        st.caption("Columns: source, kind (loss_cost | premium), value, as_of — optional state, unit, url, "
                   "permissible_loss_ratio_pct, note. Rows for states outside the launch states are skipped.")
        up = st.file_uploader("Industry CSV", type=["csv"], key=f"bm_csv_{bid}", label_visibility="collapsed")
        if up is not None and st.button("Import file", key=f"bm_csv_go_{bid}"):
            res = call("POST", "actuarial/benchmarks/import", files={"file": (up.name, up.getvalue(), "text/csv")},
                       timeout=60)
            if res is not None:
                st.success(f"Imported {res['added']} benchmark(s); skipped {res['skipped_other_states']} for other states.")
                for e in res["errors"]:
                    st.warning(e)

        st.markdown("**Competitor products to read**")
        if st.button("Find competitor products (IRDAI UIN and web)", key=f"bm_leads_{bid}"):
            st.session_state[f"bm_leads_data_{bid}"] = call("GET", "filing-leads", timeout=60)
        leads = st.session_state.get(f"bm_leads_data_{bid}")
        if leads:
            st.markdown(" · ".join(f"[{r['label']}]({r['url']})" for r in leads.get("registers", [])))
            if leads.get("how_to"):
                st.caption(leads["how_to"])
            st.caption(leads["web_status"] + " Leads only: read the product, check its rating base and exposure unit, "
                                             "then enter the figure above.")
            for w in leads["web"]:
                st.markdown(f"- [{_md(w['title'])}]({w['url']}) — {_md(w['snippet'][:200])}")


def _render_approval(bid: int, data: Dict[str, Any], call: Callable[..., Optional[Dict[str, Any]]]) -> None:
    status = data.get("approval_status") or {}
    ap = status.get("approval")
    st.markdown("#### Actuarial approval")
    if status.get("approved"):
        st.success(f"✅ {_md(status['detail'])}" + (f" Note: {_md(ap['note'])}" if ap and ap.get("note") else ""))
    elif status.get("stale"):
        st.warning(f"⚠️ {_md(status['detail'])}")
    else:
        st.info(_md(status.get("detail", "Not approved yet.")))
    st.caption("The launch gate requires this approval, and it goes stale if the data, the saved assumptions, the "
               "covered-claims set or the benchmarks change. The rating plan, business plan and memorandum use the "
               "selected rate once approved.")
    if data.get("what_if"):
        st.caption("Save or reset the what-if assumptions before approving: the approval is given on the saved selection.")
        return
    with st.form(key=f"approve_form_{bid}"):
        c1, c2 = st.columns(2)
        name = c1.text_input("Approving actuary", value=(ap or {}).get("name") or st.session_state.get("user_name", ""))
        selected = c2.number_input("Selected rate ($)", 0.0, 1e7, float(data["indicated_premium"] or 0.0), 1.0,
                                   help="Defaults to the indication; more than 5% away needs a reason.")
        note = st.text_area("Reason / note", placeholder="Required when the selected rate differs from the indication "
                                                         "by more than 5%.")
        c3, c4 = st.columns(2)
        approve = c3.form_submit_button("Approve indication", type="primary", use_container_width=True)
        withdraw = c4.form_submit_button("Withdraw approval", use_container_width=True, disabled=not ap)
    if approve:
        if call("PUT", "actuarial/approval", json={"name": name, "note": note, "selected_premium": selected}) is not None:
            st.rerun()
    if withdraw:
        if call("DELETE", "actuarial/approval") is not None:
            st.rerun()
