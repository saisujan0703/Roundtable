"""
Roundtable rate indication
==========================
A directional pure-premium indication for the new coverage, built from the claims experience stored on a
brief (backend.analytics via brief.claims_analytics). Every number is computed here; the LLM never sees or
writes them. It is a pre-filing indication for the actuary to select from, not a rate filing.

Steps
1. Experience   the last N full accident years. With the covered-claims set (backend.coverage), only the claims
                the new coverage would newly pay are priced (the incremental cost); the pattern's other claims are
                already paid today and inside today's premium. Without it, or when the actuary prices a standalone
                product (price_whole_pattern), every claim of the pattern is priced.
2. CAT / large  catastrophe losses are taken out and non-CAT losses capped per claim at the large-loss threshold,
                so one event or one large claim does not drive the rate (backend.analytics.get_loss_composition)
3. Development  whole-pattern pricing: incurred to ultimate by accident year from the reconstructed development
                triangle (backend.reserving; chain-ladder or Bornhuetter-Ferguson). Newly covered claims are costed
                from paid claims, so only their COUNTS develop (claims not reported yet), with the reported-count
                triangle. Without a triangle the old heuristic is used and labelled
4. Trend        frequency trend (fitted ex-CAT, or the actuary's choice) and severity trend, from each accident
                year's midpoint to the average accident date of the proposed policies (effective date + 12 months
                for annual policies written evenly over a year)
5. Loads        long-run excess (large-loss) factor and catastrophe provision put back what step 2 took out
6. Behaviour    unreported demand: customers do not file claims they know are excluded, so today's denied claims
                understate how often the new coverage will be used (incremental pricing only); adverse selection:
                buyers of an optional cover are worse risks than the book. Both are actuarial judgement, shown
                as such, with defaults the actuary is expected to replace
7. Credibility  Z = sqrt(claims / 1,082); the complement is the trended mean of the external benchmarks the
                actuary has entered (bureau loss costs, competitors' filed rates, reinsurer quotes)
8. Expenses     ALAE from the data, ULAE, then expense and profit & contingencies:
                indicated premium = credibility-weighted loss cost x (1 + ALAE) x (1 + ULAE) / (1 - expense - profit)

Also reported: a range from the frequency trend's 95% interval, the indicated premium as a share of today's
average premium in the same scope, and how much each assumption moves the result.
"""
from __future__ import annotations

import calendar
from datetime import date
from typing import Any, Dict, List, Optional

FULL_CREDIBILITY_CLAIMS = 1082  # classical standard: 90% probability of being within 5% of the expected count
DEV_METHODS = ("chain_ladder", "bornhuetter_ferguson", "heuristic")
CAT_DRIVEN_SHARE_PCT = 50.0     # above this CAT share the pattern is priced with its CAT losses in (see notes)

DEFAULTS = {
    "experience_years": 3,
    "months_to_effective": 6,
    "frequency_trend_pct": None,   # None = the fitted trend when significant, else 0
    "severity_trend_pct": 5.0,
    "ulae_pct": 5.0,
    "expense_ratio_pct": 25.0,
    "profit_pct": 5.0,
    "apply_development": True,
    "dev_method": "chain_ladder",
    "tail_factor": 1.0,
    "large_loss_cap": 100_000.0,
    "cat_load_pct": None,          # None = the pattern's long-run CAT-to-non-CAT ratio
    "unreported_load_pct": 25.0,   # judgement: claims never filed because the cover was known to be excluded
    "adverse_selection_pct": 10.0,  # judgement: optional-cover buyers vs the whole book
    "apply_complement": True,
    "price_whole_pattern": False,  # standalone product: price every claim of the pattern, not only the gap
}
LIMITS = {
    "experience_years": (1, 10), "months_to_effective": (0, 36), "frequency_trend_pct": (-30.0, 50.0),
    "severity_trend_pct": (-10.0, 25.0), "ulae_pct": (0.0, 20.0), "expense_ratio_pct": (0.0, 60.0),
    "profit_pct": (-10.0, 20.0), "tail_factor": (1.0, 1.5), "large_loss_cap": (10_000.0, 5_000_000.0),
    "cat_load_pct": (0.0, 200.0), "unreported_load_pct": (0.0, 200.0), "adverse_selection_pct": (-20.0, 100.0),
}
BOOLS = ("apply_development", "apply_complement", "price_whole_pattern")
BENCHMARK_TYPES = {"loss_cost": "Loss cost (pure, per exposure)", "premium": "Premium / filed rate (per exposure)"}


def _clamp(name: str, value: float) -> float:
    lo, hi = LIMITS[name]
    return max(lo, min(hi, value))


def _year_fraction(d: date) -> float:
    return d.year + (d.timetuple().tm_yday - 0.5) / (366 if d.year % 4 == 0 else 365)


def _add_months(d: date, months: int) -> date:
    y, m = divmod(d.month - 1 + months, 12)
    return date(d.year + y, m + 1, min(d.day, calendar.monthrange(d.year + y, m + 1)[1]))


def assumptions(analytics: Dict[str, Any], overrides: Optional[Dict[str, Any]] = None,
                composition: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Defaults filled in from the data, with the actuary's overrides applied and clamped to sane limits."""
    fit = analytics.get("frequency_trend_fit") or {}
    fitted = fit.get("annual_trend_pct") if fit.get("has_data") else None
    cat = (composition or {}).get("cat") or {}
    data_cat = 100 * (cat.get("ratio_to_noncat") or 0.0)
    a = dict(DEFAULTS)
    a["frequency_trend_pct"] = fitted if (fitted is not None and fit.get("significant")) else 0.0
    a["cat_load_pct"] = round(data_cat, 2)
    for k, v in (overrides or {}).items():
        if k not in a or v is None:
            continue
        if k in BOOLS:
            a[k] = v if isinstance(v, bool) else str(v).lower() in ("1", "true", "yes")
        elif k == "dev_method":
            a[k] = v if v in DEV_METHODS else DEFAULTS["dev_method"]
        else:
            a[k] = float(v)
    for k in LIMITS:
        a[k] = _clamp(k, float(a[k]))
    a["experience_years"] = int(a["experience_years"])
    a["months_to_effective"] = int(a["months_to_effective"])
    a["fitted_frequency_trend_pct"] = fitted
    a["fitted_trend_significant"] = bool(fit.get("significant"))
    a["data_cat_load_pct"] = round(data_cat, 2)
    return a


def _benchmark_loss_cost(b: Dict[str, Any], a: Dict[str, Any], alae_pct: float, target: float) -> Optional[float]:
    """One external benchmark as a pure loss cost per exposure, trended from its as-of date to *target*."""
    try:
        value = float(b["value"])
        as_of = date.fromisoformat(str(b["as_of"])[:10])
    except (KeyError, TypeError, ValueError):
        return None
    if value <= 0:
        return None
    if b.get("kind") == "premium":
        plr = float(b.get("permissible_loss_ratio_pct") or 65.0) / 100
        value = value * plr / ((1 + alae_pct / 100) * (1 + a["ulae_pct"] / 100))
    years = target - _year_fraction(as_of)
    return value * ((1 + a["frequency_trend_pct"] / 100) * (1 + a["severity_trend_pct"] / 100)) ** years


def _indicate(rows: List[Dict[str, Any]], a: Dict[str, Any], ctx: Dict[str, Any],
              freq_trend_pct: Optional[float] = None) -> Dict[str, Any]:
    """The indication for one set of assumptions; *freq_trend_pct* overrides a's frequency trend (for ranges)."""
    f = (a["frequency_trend_pct"] if freq_trend_pct is None else freq_trend_pct) / 100
    s = a["severity_trend_pct"] / 100
    incremental, split = ctx["incremental"], ctx["split"]
    dev_by_year = ctx["count_dev"] if incremental else ctx["incurred_dev"].get(a["dev_method"], {})
    out_rows, weighted, exposure = [], 0.0, 0.0
    for r in rows:
        share = split(r["year"], a) if ctx["remove_cat_large"] else 1.0
        if not a["apply_development"]:
            dev = 1.0
        elif a["dev_method"] == "heuristic" or r["year"] not in dev_by_year:
            dev = 1.0 if incremental else 1 + (r["open_pct"] or 0) / 100 * max(
                ctx["heuristic_ratio"].get(r["year"], ctx["heuristic_all"]) - 1, 0)
        else:
            dev = dev_by_year[r["year"]] or 1.0
        years = target_years = ctx["target"] - (r["year"] + 0.5)
        trend = ((1 + f) * (1 + s)) ** target_years
        basic = r["loss_cost_per_exposure"] * share
        trended = basic * dev * trend
        out_rows.append({**r, "basic_share": round(share, 4), "basic_loss_cost": round(basic, 2),
                         "development_factor": round(dev, 4), "trend_years": round(years, 2),
                         "trend_factor": round(trend, 4), "trended_loss_cost": round(trended, 2)})
        weighted += trended * r["earned_exposure"]
        exposure += r["earned_exposure"]
    basic_lc = weighted / exposure if exposure else 0.0
    excess = ctx["excess_factor"] if ctx["remove_cat_large"] else 1.0
    cat_load = a["cat_load_pct"] / 100 if ctx["remove_cat_large"] else 0.0
    with_large = basic_lc * excess
    with_cat = with_large * (1 + cat_load)
    unreported = a["unreported_load_pct"] / 100 if incremental else 0.0
    with_behaviour = with_cat * (1 + unreported) * (1 + a["adverse_selection_pct"] / 100)

    z = ctx["z"]
    complements = [c for c in (_benchmark_loss_cost(b, a, ctx["alae"], ctx["target"]) for b in ctx["benchmarks"])
                   if c is not None]
    complement = sum(complements) / len(complements) if complements else None
    blended = (z * with_behaviour + (1 - z) * complement
               if complement is not None and a["apply_complement"] else with_behaviour)

    with_alae = blended * (1 + ctx["alae"] / 100)
    with_ulae = with_alae * (1 + a["ulae_pct"] / 100)
    permissible = 1 - (a["expense_ratio_pct"] + a["profit_pct"]) / 100
    premium = with_ulae / permissible if permissible > 0 else float("nan")
    return {"rows": out_rows, "basic_loss_cost": basic_lc, "with_large": with_large, "with_cat": with_cat,
            "with_behaviour": with_behaviour, "complement": complement, "complements": complements,
            "blended": blended, "with_alae": with_alae, "with_ulae": with_ulae,
            "permissible_loss_ratio": permissible, "premium": premium,
            "loss_cost": blended}


def _incremental_rows(pattern_rows: List[Dict[str, Any]], covered: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Experience rows for the claims the new coverage would newly pay (backend.coverage), per accident year.
    Their cost is estimated from paid claims, so they carry no open reserves to develop."""
    new = {r["year"]: r for r in (covered.get("newly_covered") or {}).get("by_year") or []}
    rows = []
    for r in pattern_rows:
        n = new.get(r["year"]) or {}
        claims, cost, expo = n.get("claims") or 0, n.get("estimated_cost") or 0.0, r["earned_exposure"]
        rows.append({"year": r["year"], "earned_exposure": expo, "claims": claims,
                     "frequency_per_1000": round(1000 * claims / expo, 3) if expo else None,
                     "avg_severity": round(cost / claims, 2) if claims else None,
                     "loss_cost_per_exposure": round(cost / expo, 2) if expo else 0.0,
                     "open_pct": 0.0, "credible": r["credible"]})
    return rows


def _splitter(incremental: bool, composition: Dict[str, Any], covered: Optional[Dict[str, Any]]):
    """split(year, a) -> share of the year's loss that is non-CAT and below the large-loss cap."""
    if incremental:
        items = ((covered or {}).get("newly_covered") or {}).get("items") or []

        def split(year: int, a: Dict[str, Any]) -> float:
            ys = [(cost, cat) for y, cost, cat, *_ in items if y == year]
            total = sum(c for c, _ in ys)
            return sum(min(c, a["large_loss_cap"]) for c, cat in ys if not cat) / total if total else 1.0
        return split
    by_year = {r["year"]: r for r in composition.get("by_year") or []}

    def split(year: int, a: Dict[str, Any]) -> float:
        r = by_year.get(year)
        return (r["noncat_capped"] / r["incurred"]) if r and r["incurred"] else 1.0
    return split


def rate_indication(analytics: Dict[str, Any], overrides: Optional[Dict[str, Any]] = None,
                    covered: Optional[Dict[str, Any]] = None, context: Optional[Dict[str, Any]] = None,
                    ) -> Dict[str, Any]:
    """The full indication for a brief's stored claims analytics. With *covered* (backend.coverage.build) it prices
    only the claims the new coverage would newly pay; without it, every claim of the pattern.
    *context* carries what is computed live from the claims data: {"development": backend.reserving.development,
    "composition": backend.analytics.get_loss_composition (at the selected cap), "benchmarks": [...]}.
    {"available": False, "reason"} when there is no claims experience to price from."""
    from backend.reserving import factors_by_year

    context = context or {}
    summary = analytics.get("summary") or {}
    basis = (analytics.get("basis") or {}).get("basis", "direct")
    if not summary.get("has_data") or basis == "line_baseline":
        return {"available": False,
                "reason": "This brief has no claims experience of its own or from proxy patterns, so there is nothing to "
                          "price from. Select proxy risk patterns for the brief to get an indication."}
    composition = context.get("composition") or {}
    a = assumptions(analytics, overrides, composition)
    full = [r for r in analytics.get("trend") or [] if not r.get("partial_year") and r.get("earned_exposure")]
    pattern_rows = full[-a["experience_years"]:]
    if not pattern_rows:
        return {"available": False, "reason": "No complete accident year with earned exposure to price from."}
    pattern_rows = [{k: r.get(k) for k in ("year", "earned_exposure", "claims", "frequency_per_1000", "avg_severity",
                                           "loss_cost_per_exposure", "open_pct", "credible")} for r in pattern_rows]
    incremental = bool(covered and covered.get("has_data")) and not a["price_whole_pattern"]
    rows = _incremental_rows(pattern_rows, covered) if incremental else pattern_rows
    pattern_exposure = sum(r["earned_exposure"] for r in pattern_rows)
    pattern_loss_cost = (sum(r["loss_cost_per_exposure"] * r["earned_exposure"] for r in pattern_rows) / pattern_exposure
                         if pattern_exposure else None)

    valuation = date.fromisoformat(str(analytics.get("valuation_date") or summary.get("valuation_date"))[:10])
    effective = _add_months(valuation, a["months_to_effective"])
    target_date = _add_months(effective, 12)
    rd = analytics.get("reserve_development") or {}
    sev = analytics.get("severity") or {}
    alae = sev.get("alae_ratio_pct") or 0.0
    dev = context.get("development") or {}
    cat_share = ((composition.get("cat") or {}).get("cat_share_pct") or 0.0)
    cat_driven = cat_share > CAT_DRIVEN_SHARE_PCT
    n_claims = sum(r["claims"] or 0 for r in rows)
    benchmarks = [b for b in context.get("benchmarks") or [] if b.get("include", True)]
    ctx = {
        "incremental": incremental,
        "target": _year_fraction(target_date),
        "alae": alae,
        "split": _splitter(incremental, composition, covered),
        "remove_cat_large": bool(composition.get("has_data")) and not cat_driven,
        "excess_factor": ((composition.get("excess") or {}).get("factor") or 1.0),
        "incurred_dev": {m: factors_by_year(dev, m)["incurred"] for m in ("chain_ladder", "bornhuetter_ferguson")},
        "count_dev": factors_by_year(dev)["count"],
        "heuristic_all": rd.get("incurred_to_initial_ratio") or 1.0,
        "heuristic_ratio": {r["year"]: r.get("incurred_to_initial_ratio") for r in rd.get("by_year") or [] if r.get("year")},
        "z": min(1.0, (n_claims / FULL_CREDIBILITY_CLAIMS) ** 0.5),
        "benchmarks": benchmarks,
    }
    if not dev.get("has_data") and a["dev_method"] != "heuristic":
        a["dev_method"] = "heuristic"

    central = _indicate(rows, a, ctx)
    fit = analytics.get("frequency_trend_fit") or {}
    lo_t, hi_t = fit.get("ci95_low_pct"), fit.get("ci95_high_pct")
    if fit.get("has_data") and lo_t is not None and hi_t is not None:
        low = _indicate(rows, a, ctx, freq_trend_pct=_clamp("frequency_trend_pct", lo_t))
        high = _indicate(rows, a, ctx, freq_trend_pct=_clamp("frequency_trend_pct", hi_t))
        range_basis = f"frequency trend at its 95% interval ({lo_t:+.1f}% to {hi_t:+.1f}% a year)"
    else:
        low = high = None
        range_basis = "no fitted frequency trend, so no statistical range"

    # Today's average premium in the same scope (earned premium / earned exposure, all years)
    lr = analytics.get("loss_ratio") or {}
    all_exposure = sum(r.get("earned_exposure") or 0 for r in analytics.get("trend") or [])
    avg_premium = (lr.get("earned_premium") or 0) / all_exposure if all_exposure else None

    def premium_with(**changes) -> float:
        return _indicate(rows, {**a, **changes}, ctx)["premium"]

    base = central["premium"]
    swings = [
        ("Frequency trend ±5 pts", {"frequency_trend_pct": a["frequency_trend_pct"] - 5},
         {"frequency_trend_pct": a["frequency_trend_pct"] + 5}),
        ("Severity trend ±3 pts", {"severity_trend_pct": a["severity_trend_pct"] - 3},
         {"severity_trend_pct": a["severity_trend_pct"] + 3}),
        ("Expense ratio ±5 pts", {"expense_ratio_pct": a["expense_ratio_pct"] - 5},
         {"expense_ratio_pct": a["expense_ratio_pct"] + 5}),
        ("Profit & contingencies ±3 pts", {"profit_pct": a["profit_pct"] - 3}, {"profit_pct": a["profit_pct"] + 3}),
        ("Adverse selection 0% / 2x", {"adverse_selection_pct": 0.0},
         {"adverse_selection_pct": _clamp("adverse_selection_pct", 2 * a["adverse_selection_pct"])}),
    ]
    if incremental:
        swings.append(("Unreported demand 0% / 2x", {"unreported_load_pct": 0.0},
                       {"unreported_load_pct": _clamp("unreported_load_pct", 2 * a["unreported_load_pct"])}))
    else:
        swings.append(("Development on / off", {"apply_development": False}, {"apply_development": True}))
    if ctx["remove_cat_large"]:
        swings.append(("CAT load 0% / 2x", {"cat_load_pct": 0.0},
                       {"cat_load_pct": _clamp("cat_load_pct", 2 * a["cat_load_pct"])}))
    if central["complement"] is not None and a["apply_complement"]:
        swings.append(("Credibility complement off / on", {"apply_complement": False}, {"apply_complement": True}))
    sens = []
    for label, lo_kw, hi_kw in swings:
        p_lo, p_hi = premium_with(**lo_kw), premium_with(**hi_kw)
        sens.append({"assumption": label, "low": round(min(p_lo, p_hi), 2), "high": round(max(p_lo, p_hi), 2),
                     "swing": round(abs(p_hi - p_lo), 2)})
    sens.sort(key=lambda x: -x["swing"])

    unit = summary.get("exposure_unit") or "exposure-years"
    dev_label = ("reported counts, chain-ladder" if incremental and a["dev_method"] != "heuristic" else
                 {"chain_ladder": "chain-ladder", "bornhuetter_ferguson": "Bornhuetter-Ferguson",
                  "heuristic": "heuristic"}[a["dev_method"]])
    notes = ["Directional indication on synthetic demo data — the actuary selects the final rate. Not a rate filing."]
    if incremental:
        notes.append("Prices only the claims the new coverage would newly pay (denied today for a coverage reason and not "
                     "excluded by the new wording). Their cost is estimated from paid claims with the same loss "
                     "description, so only claim COUNTS are developed (late-reported claims, from the reported-count "
                     "triangle). " + " ".join((covered or {}).get("assumptions") or []))
        if not any(r["claims"] for r in rows):
            notes.append("No claims in the experience period would be newly covered, so the data shows no incremental "
                         "cost: the product overlaps what the current form already pays.")
        notes.append(f"Unreported demand {a['unreported_load_pct']:.0f}%: policyholders rarely report a loss they know "
                     "is excluded, so today's denied claims understate how often the cover will be used. Judgement — "
                     "replace with evidence (competitor experience, a customer survey, early post-launch emergence).")
    else:
        notes.append(("Standalone pricing (the actuary's selection): every claim of the pattern is priced, as for a "
                      "product sold on its own (e.g. parametric or a separate policy), not as a top-up to today's cover. "
                      if a["price_whole_pattern"] else
                      "Prices every claim of the pattern, including those already paid today (no covered-claims set "
                      "was available). ") + f"Development: {dev_label}"
                     + (" from the reconstructed triangle (Loss development section)." if a["dev_method"] != "heuristic"
                        else " (open claims develop like this pattern's claims did from their initial reserve)."))
    notes.append(f"Adverse selection {a['adverse_selection_pct']:.0f}%: buyers of an optional cover tend to be worse "
                 "risks than the whole book. Judgement — revisit once take-up data exists.")
    if ctx["remove_cat_large"]:
        exc = composition.get("excess") or {}
        notes.append(f"Non-CAT losses capped at ${a['large_loss_cap']:,.0f} per claim; excess factor "
                     f"{ctx['excess_factor']:.3f} from the {exc.get('source', 'pattern')}'s long-run losses above the cap. "
                     f"CAT losses removed and replaced by a {a['cat_load_pct']:.1f}% provision "
                     + ("(the pattern's long-run CAT-to-non-CAT ratio over "
                        f"{(composition.get('cat') or {}).get('years', 'all years')}; a short history — replace with a "
                        "catastrophe-model load where one exists)." if a["cat_load_pct"] == a["data_cat_load_pct"]
                        else "(the actuary's selection)."))
    elif cat_driven:
        notes.append(f"Catastrophes are {cat_share:.0f}% of this pattern's losses: the experience is priced with its "
                     "CAT losses in, which a few years cannot represent. Price this cover with a catastrophe model.")
    if central["complement"] is None:
        notes.append(f"Credibility Z = {ctx['z']:.2f} but no external benchmark is entered, so the experience is used at "
                     "full weight. Add a bureau loss cost, competitor filed rate or reinsurer quote as the complement.")
    elif not a["apply_complement"]:
        notes.append("The credibility complement is switched off: the experience is used at full weight.")
    if basis == "proxy":
        notes.insert(0, "PROXY — the experience is the pooled claims of related patterns "
                        f"({' + '.join((analytics.get('basis') or {}).get('proxy_tags') or [])}), not this product's own. "
                        "Confirm the perils are comparable before relying on it.")
    if avg_premium and base > 0.5 * avg_premium:
        notes.insert(0, f"SANITY CHECK — the indication is {100 * base / avg_premium:.0f}% of today's whole average "
                        "premium in this scope. A single cover rarely costs that much: check that the risk pattern"
                        + (" (proxy)" if basis == "proxy" else "") + " is not broader than what the product pays.")
    if not all(r["credible"] for r in rows):
        notes.append("Some experience years are flagged low credibility (too few claims).")
    if a["frequency_trend_pct"] == 0 and a["fitted_frequency_trend_pct"] and not a["fitted_trend_significant"]:
        notes.append(f"The fitted frequency trend ({a['fitted_frequency_trend_pct']:+.1f}%/yr) is not statistically "
                     "significant, so 0% is used by default.")

    steps = [{"step": "Experience loss cost (exposure-weighted"
                      + (", ex-CAT, capped" if ctx["remove_cat_large"] else "") + f", developed ({dev_label}) and trended)",
              "value": round(central["basic_loss_cost"], 2)}]
    if ctx["remove_cat_large"]:
        steps += [{"step": f"× excess (large-loss) factor {ctx['excess_factor']:.3f}", "value": round(central["with_large"], 2)},
                  {"step": f"+ CAT provision {a['cat_load_pct']:.1f}%", "value": round(central["with_cat"], 2)}]
    behaviour = (f"+ unreported demand {a['unreported_load_pct']:.0f}%, " if incremental else "+ ") + \
        f"adverse selection {a['adverse_selection_pct']:.0f}%"
    steps.append({"step": behaviour, "value": round(central["with_behaviour"], 2)})
    if central["complement"] is not None and a["apply_complement"]:
        steps.append({"step": f"Credibility-weighted: Z {ctx['z']:.2f} × experience + {1 - ctx['z']:.2f} × benchmark "
                              f"{central['complement']:,.2f}", "value": round(central["blended"], 2)})
    steps += [
        {"step": f"+ ALAE {alae:.1f}%", "value": round(central["with_alae"], 2)},
        {"step": f"+ ULAE {a['ulae_pct']:.1f}%", "value": round(central["with_ulae"], 2)},
        {"step": f"÷ permissible loss ratio {central['permissible_loss_ratio']:.1%} "
                 f"(expense {a['expense_ratio_pct']:.0f}%, profit {a['profit_pct']:.0f}%)", "value": round(base, 2)},
    ]
    return {
        "available": True,
        "basis": basis,
        "priced_claims": "newly_covered" if incremental else "whole_pattern",
        # Context: what the whole pattern costs per exposure today (mostly already inside today's premium)
        "pattern_loss_cost": round(pattern_loss_cost, 2) if pattern_loss_cost is not None else None,
        "exposure_unit": unit,
        "assumptions": a,
        "valuation_date": valuation.isoformat(),
        "effective_date": effective.isoformat(),
        "average_accident_date": target_date.isoformat(),
        "alae_pct": alae,
        "experience": central["rows"],
        "steps": steps,
        "loss_and_lae_per_exposure": round(central["with_ulae"], 2),
        "pure_loss_cost": round(central["blended"], 2),
        "indicated_premium": round(base, 2),
        "range": {"low": round(low["premium"], 2) if low else None, "high": round(high["premium"], 2) if high else None,
                  "basis": range_basis},
        "average_current_premium": round(avg_premium, 2) if avg_premium else None,
        "share_of_current_premium_pct": round(100 * base / avg_premium, 1) if avg_premium else None,
        "credibility": {"claims": n_claims, "z": round(ctx["z"], 3), "full_credibility_claims": FULL_CREDIBILITY_CLAIMS,
                        "experience_loss_cost": round(central["with_behaviour"], 2),
                        "complement": round(central["complement"], 2) if central["complement"] is not None else None,
                        "benchmarks_used": len(central["complements"]),
                        "applied": central["complement"] is not None and a["apply_complement"]},
        "cat_large": {"applied": ctx["remove_cat_large"], "cat_driven": cat_driven, "cat_share_pct": cat_share,
                      "excess_factor": ctx["excess_factor"], "excess_source": (composition.get("excess") or {}).get("source"),
                      "cap": a["large_loss_cap"], "cat_load_pct": a["cat_load_pct"]},
        "development": {"method": a["dev_method"], "label": dev_label, "applied": a["apply_development"],
                        "factor_basis": dev.get("factor_basis"), "measure": "count" if incremental else "incurred"},
        "sensitivity": sens,
        "notes": notes,
    }
