"""
Roundtable rate indication
==========================
A directional pure-premium indication for the new coverage, built from the claims experience stored on a
brief (backend.analytics via brief.claims_analytics). Every number is computed here; the LLM never sees or
writes them. It is a pre-filing sanity check for the actuary, not a rate filing.

Steps
1. Experience   the last N full accident years. With the covered-claims set (backend.coverage), only the claims
                the new coverage would newly pay are priced (the incremental cost); the pattern's other claims are
                already paid today and inside today's premium. Without it, every claim of the pattern is priced.
2. Development  (whole-pattern pricing only; newly covered claims are estimated from paid claims)
                open claims are assumed to develop like this pattern's claims did from their initial reserve:
                factor = 1 + open share x (incurred-to-initial ratio - 1). A heuristic; there is no paid/incurred
                triangle by development age in the data
3. Trend        frequency trend (fitted ex-CAT, or the actuary's choice) and severity trend, from each accident
                year's midpoint to the average accident date of the proposed policies (effective date + 12 months
                for annual policies written evenly over a year)
4. Loads        ALAE from the data, ULAE, then expense and profit & contingencies:
                indicated premium = trended ultimate loss cost x (1 + ALAE) x (1 + ULAE) / (1 - expense - profit)

Also reported: credibility (square-root rule, 1,082 claims for full credibility), a range from the frequency
trend's 95% interval, the indicated premium as a share of today's average premium in the same scope, and how
much each assumption moves the result.
"""
from __future__ import annotations

import calendar
from datetime import date
from typing import Any, Dict, List, Optional

FULL_CREDIBILITY_CLAIMS = 1082  # classical standard: 90% probability of being within 5% of the expected count

DEFAULTS = {
    "experience_years": 3,
    "months_to_effective": 6,
    "frequency_trend_pct": None,   # None = the fitted trend when significant, else 0
    "severity_trend_pct": 5.0,
    "ulae_pct": 5.0,
    "expense_ratio_pct": 25.0,
    "profit_pct": 5.0,
    "apply_development": True,
}
LIMITS = {
    "experience_years": (1, 10), "months_to_effective": (0, 36), "frequency_trend_pct": (-30.0, 50.0),
    "severity_trend_pct": (-10.0, 25.0), "ulae_pct": (0.0, 20.0), "expense_ratio_pct": (0.0, 60.0),
    "profit_pct": (-10.0, 20.0),
}


def _clamp(name: str, value: float) -> float:
    lo, hi = LIMITS[name]
    return max(lo, min(hi, value))


def _year_fraction(d: date) -> float:
    return d.year + (d.timetuple().tm_yday - 0.5) / (366 if d.year % 4 == 0 else 365)


def _add_months(d: date, months: int) -> date:
    y, m = divmod(d.month - 1 + months, 12)
    return date(d.year + y, m + 1, min(d.day, calendar.monthrange(d.year + y, m + 1)[1]))


def assumptions(analytics: Dict[str, Any], overrides: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Defaults filled in from the data, with the actuary's overrides applied and clamped to sane limits."""
    fit = analytics.get("frequency_trend_fit") or {}
    fitted = fit.get("annual_trend_pct") if fit.get("has_data") else None
    a = dict(DEFAULTS)
    a["frequency_trend_pct"] = fitted if (fitted is not None and fit.get("significant")) else 0.0
    for k, v in (overrides or {}).items():
        if k in a and v is not None:
            a[k] = bool(v) if k == "apply_development" else float(v)
    for k in LIMITS:
        a[k] = _clamp(k, float(a[k]))
    a["experience_years"] = int(a["experience_years"])
    a["months_to_effective"] = int(a["months_to_effective"])
    a["fitted_frequency_trend_pct"] = fitted
    a["fitted_trend_significant"] = bool(fit.get("significant"))
    return a


def _indicate(rows: List[Dict[str, Any]], a: Dict[str, Any], alae_pct: float, target: float,
              dev_ratio_by_year: Dict[int, float], dev_ratio_all: float, freq_trend_pct: Optional[float] = None,
              ) -> Dict[str, Any]:
    """The indication for one set of assumptions; *freq_trend_pct* overrides a's frequency trend (for ranges)."""
    f = (a["frequency_trend_pct"] if freq_trend_pct is None else freq_trend_pct) / 100
    s = a["severity_trend_pct"] / 100
    out_rows, weighted, exposure = [], 0.0, 0.0
    for r in rows:
        dev_ratio = dev_ratio_by_year.get(r["year"], dev_ratio_all) or 1.0
        dev = 1 + (r["open_pct"] or 0) / 100 * max(dev_ratio - 1, 0) if a["apply_development"] else 1.0
        years = target - (r["year"] + 0.5)
        trend = ((1 + f) * (1 + s)) ** years
        trended = r["loss_cost_per_exposure"] * dev * trend
        out_rows.append({**r, "development_factor": round(dev, 4), "trend_years": round(years, 2),
                         "trend_factor": round(trend, 4), "trended_loss_cost": round(trended, 2)})
        weighted += trended * r["earned_exposure"]
        exposure += r["earned_exposure"]
    loss_cost = weighted / exposure if exposure else 0.0
    with_alae = loss_cost * (1 + alae_pct / 100)
    with_ulae = with_alae * (1 + a["ulae_pct"] / 100)
    permissible = 1 - (a["expense_ratio_pct"] + a["profit_pct"]) / 100
    premium = with_ulae / permissible if permissible > 0 else float("nan")
    return {"rows": out_rows, "loss_cost": loss_cost, "with_alae": with_alae, "with_ulae": with_ulae,
            "permissible_loss_ratio": permissible, "premium": premium}


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


def rate_indication(analytics: Dict[str, Any], overrides: Optional[Dict[str, Any]] = None,
                    covered: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """The full indication for a brief's stored claims analytics. With *covered* (backend.coverage.build) it prices
    only the claims the new coverage would newly pay; without it, every claim of the pattern.
    {"available": False, "reason"} when there is no claims experience to price from."""
    summary = analytics.get("summary") or {}
    basis = (analytics.get("basis") or {}).get("basis", "direct")
    if not summary.get("has_data") or basis == "line_baseline":
        return {"available": False,
                "reason": "This brief has no claims experience of its own or from proxy patterns, so there is nothing to "
                          "price from. Select proxy risk patterns for the brief to get an indication."}
    a = assumptions(analytics, overrides)
    full = [r for r in analytics.get("trend") or [] if not r.get("partial_year") and r.get("earned_exposure")]
    pattern_rows = full[-a["experience_years"]:]
    if not pattern_rows:
        return {"available": False, "reason": "No complete accident year with earned exposure to price from."}
    pattern_rows = [{k: r.get(k) for k in ("year", "earned_exposure", "claims", "frequency_per_1000", "avg_severity",
                                           "loss_cost_per_exposure", "open_pct", "credible")} for r in pattern_rows]
    incremental = bool(covered and covered.get("has_data"))
    rows = _incremental_rows(pattern_rows, covered) if incremental else pattern_rows
    pattern_exposure = sum(r["earned_exposure"] for r in pattern_rows)
    pattern_loss_cost = (sum(r["loss_cost_per_exposure"] * r["earned_exposure"] for r in pattern_rows) / pattern_exposure
                         if pattern_exposure else None)

    valuation = date.fromisoformat(str(analytics.get("valuation_date") or summary.get("valuation_date"))[:10])
    effective = _add_months(valuation, a["months_to_effective"])
    target_date = _add_months(effective, 12)
    target = _year_fraction(target_date)
    rd = analytics.get("reserve_development") or {}
    dev_all = rd.get("incurred_to_initial_ratio") or 1.0
    dev_by_year = {r["year"]: r.get("incurred_to_initial_ratio") for r in rd.get("by_year") or [] if r.get("year")}
    sev = analytics.get("severity") or {}
    alae = sev.get("alae_ratio_pct") or 0.0

    central = _indicate(rows, a, alae, target, dev_by_year, dev_all)
    fit = analytics.get("frequency_trend_fit") or {}
    lo_t, hi_t = fit.get("ci95_low_pct"), fit.get("ci95_high_pct")
    if fit.get("has_data") and lo_t is not None and hi_t is not None:
        low = _indicate(rows, a, alae, target, dev_by_year, dev_all, freq_trend_pct=_clamp("frequency_trend_pct", lo_t))
        high = _indicate(rows, a, alae, target, dev_by_year, dev_all, freq_trend_pct=_clamp("frequency_trend_pct", hi_t))
        range_basis = f"frequency trend at its 95% interval ({lo_t:+.1f}% to {hi_t:+.1f}% a year)"
    else:
        low = high = None
        range_basis = "no fitted frequency trend, so no statistical range"

    # Today's average premium in the same scope (earned premium / earned exposure, all years)
    lr = analytics.get("loss_ratio") or {}
    all_exposure = sum(r.get("earned_exposure") or 0 for r in analytics.get("trend") or [])
    avg_premium = (lr.get("earned_premium") or 0) / all_exposure if all_exposure else None

    n_claims = sum(r["claims"] or 0 for r in rows)
    z = min(1.0, (n_claims / FULL_CREDIBILITY_CLAIMS) ** 0.5)

    def premium_with(**changes) -> float:
        return _indicate(rows, {**a, **changes}, alae, target, dev_by_year, dev_all)["premium"]

    base = central["premium"]
    sens = []
    for label, lo_kw, hi_kw in (
        ("Frequency trend ±5 pts", {"frequency_trend_pct": a["frequency_trend_pct"] - 5},
         {"frequency_trend_pct": a["frequency_trend_pct"] + 5}),
        ("Severity trend ±3 pts", {"severity_trend_pct": a["severity_trend_pct"] - 3},
         {"severity_trend_pct": a["severity_trend_pct"] + 3}),
        ("Expense ratio ±5 pts", {"expense_ratio_pct": a["expense_ratio_pct"] - 5},
         {"expense_ratio_pct": a["expense_ratio_pct"] + 5}),
        ("Profit & contingencies ±3 pts", {"profit_pct": a["profit_pct"] - 3}, {"profit_pct": a["profit_pct"] + 3}),
        ("Development on / off", {"apply_development": False}, {"apply_development": True}),
    ):
        p_lo, p_hi = premium_with(**lo_kw), premium_with(**hi_kw)
        sens.append({"assumption": label, "low": round(min(p_lo, p_hi), 2), "high": round(max(p_lo, p_hi), 2),
                     "swing": round(abs(p_hi - p_lo), 2)})
    if incremental:  # estimated from paid claims: nothing to develop
        sens = [x for x in sens if not x["assumption"].startswith("Development")]
    sens.sort(key=lambda x: -x["swing"])

    unit = summary.get("exposure_unit") or "exposure-years"
    notes = ["Directional estimate — not actuarial. A pre-filing check, not a rate filing; synthetic demo data."]
    if incremental:
        notes.append("Prices only the claims the new coverage would newly pay (denied today for a coverage reason and not "
                     "excluded by the new wording). Their cost is estimated from paid claims with the same loss "
                     "description, so no development is applied. " + " ".join((covered or {}).get("assumptions") or []))
        if not any(r["claims"] for r in rows):
            notes.append("No claims in the experience period would be newly covered, so the data shows no incremental "
                         "cost: the product overlaps what the current form already pays.")
    else:
        notes.append("Prices every claim of the pattern, including those already paid today (no covered-claims set "
                     "was available). Development is a heuristic (open claims develop like this pattern's claims did "
                     "from their initial reserve); there is no development triangle and no IBNR load.")
    if basis == "proxy":
        notes.insert(0, "PROXY — the experience is the pooled claims of related patterns "
                        f"({' + '.join((analytics.get('basis') or {}).get('proxy_tags') or [])}), not this product's own. "
                        "Confirm the perils are comparable before relying on it.")
    if not all(r["credible"] for r in rows):
        notes.append("Some experience years are flagged low credibility (too few claims).")
    if a["frequency_trend_pct"] == 0 and a["fitted_frequency_trend_pct"] and not a["fitted_trend_significant"]:
        notes.append(f"The fitted frequency trend ({a['fitted_frequency_trend_pct']:+.1f}%/yr) is not statistically "
                     "significant, so 0% is used by default.")

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
        "steps": [
            {"step": "Experience loss cost (exposure-weighted, developed and trended)", "value": round(central["loss_cost"], 2)},
            {"step": f"+ ALAE {alae:.1f}%", "value": round(central["with_alae"], 2)},
            {"step": f"+ ULAE {a['ulae_pct']:.1f}%", "value": round(central["with_ulae"], 2)},
            {"step": f"÷ permissible loss ratio {central['permissible_loss_ratio']:.1%} "
                     f"(expense {a['expense_ratio_pct']:.0f}%, profit {a['profit_pct']:.0f}%)", "value": round(base, 2)},
        ],
        "indicated_premium": round(base, 2),
        "range": {"low": round(low["premium"], 2) if low else None, "high": round(high["premium"], 2) if high else None,
                  "basis": range_basis},
        "average_current_premium": round(avg_premium, 2) if avg_premium else None,
        "share_of_current_premium_pct": round(100 * base / avg_premium, 1) if avg_premium else None,
        "credibility": {"claims": n_claims, "z": round(z, 3), "full_credibility_claims": FULL_CREDIBILITY_CLAIMS},
        "sensitivity": sens,
        "notes": notes,
    }
