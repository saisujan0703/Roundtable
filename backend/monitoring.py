"""
Actual vs expected monitoring
=============================
The post-launch check that the coverage performs as priced, and the monitoring plan behind it.

Expected   from the rate indication (backend.pricing): frequency and pure loss cost per exposure at the average
           accident date, INCLUDING the behavioural loads (unreported demand, adverse selection) — those are exactly
           the assumptions monitoring has to confirm. Expected values are de-trended to the monitoring period's
           midpoint with the selected frequency and severity trends.
Actual     the priced claims (newly covered, or the whole pattern for standalone pricing) with a loss date in the
           period, developed to ultimate with the same factors as pricing, over the period's earned exposure.
Modes      live      once the effective date is at least MIN_LIVE_MONTHS behind the valuation date: the period is
                     effective date -> valuation date
           backtest  before launch: the current, partial accident year, which the indication did NOT use (pricing
                     uses complete years only), so it is a genuine hold-out test of the indication
Credibility A/E is credibility-weighted towards 1.00 (Z = sqrt(actual claims / 1,082)) before it is compared with the
           thresholds, so a few early claims cannot trigger a rate review on their own.

Live mode reads the same claims data as pricing; once the product writes its own coverage code in PolicyCenter /
ClaimCenter, filter to it (the policies that bought the cover), which is what makes adverse selection measurable.
"""
from __future__ import annotations

import math
from datetime import date
from typing import Any, Dict, List, Optional

import pandas as pd

from backend import analytics

FULL_CREDIBILITY_CLAIMS = 1082
MIN_LIVE_MONTHS = 3
AMBER = (0.90, 1.10)
RED = (0.80, 1.25)


def _yf(d: date) -> float:
    return d.year + (d.timetuple().tm_yday - 0.5) / (366 if d.year % 4 == 0 else 365)


def _status(ae: Optional[float]) -> str:
    if ae is None:
        return "no data"
    if ae < RED[0] or ae > RED[1]:
        return "red"
    if ae < AMBER[0] or ae > AMBER[1]:
        return "amber"
    return "green"


def _expected(indication: Dict[str, Any]) -> Dict[str, float]:
    """Expected frequency per 1,000 and pure loss cost per exposure at the average accident date."""
    a = indication["assumptions"]
    rows = indication["experience"]
    expo = sum(r["earned_exposure"] for r in rows) or 1.0
    f = a["frequency_trend_pct"] / 100
    freq = sum((r["frequency_per_1000"] or 0) * r["earned_exposure"] * r["development_factor"] * (1 + f) ** r["trend_years"]
               for r in rows) / expo
    loads = (1 + (a["unreported_load_pct"] / 100 if indication["priced_claims"] == "newly_covered" else 0)) * \
        (1 + a["adverse_selection_pct"] / 100)
    freq *= loads
    cred = indication["credibility"]
    if cred.get("applied") and cred.get("experience_loss_cost"):
        freq *= indication["pure_loss_cost"] / cred["experience_loss_cost"]  # the complement moves frequency too
    return {"frequency_per_1000": freq, "loss_cost": indication["pure_loss_cost"],
            "severity": 1000 * indication["pure_loss_cost"] / freq if freq else None}


def build(indication: Dict[str, Any], key: str, covered: Optional[Dict[str, Any]], development: Dict[str, Any],
          selected_rate: float) -> Dict[str, Any]:
    if not indication.get("available"):
        return {"available": False, "reason": indication.get("reason", "No indication to monitor against.")}
    scope, tc, _, be = analytics._scope_frames(key)
    valuation = analytics._data()["valuation"]
    val_d = valuation.date()
    effective = date.fromisoformat(indication["effective_date"])
    months_live = (val_d.year - effective.year) * 12 + val_d.month - effective.month
    if months_live >= MIN_LIVE_MONTHS:
        mode, start = "live", effective
    else:
        mode, start = "backtest", date(val_d.year, 1, 1)
    end = val_d
    a = indication["assumptions"]
    exp = _expected(indication)
    mid = _yf(start) + (_yf(end) - _yf(start)) / 2
    years_back = _yf(date.fromisoformat(indication["average_accident_date"])) - mid
    f, s = a["frequency_trend_pct"] / 100, a["severity_trend_pct"] / 100
    exp_freq = exp["frequency_per_1000"] / (1 + f) ** years_back
    exp_lc = exp["loss_cost"] / ((1 + f) * (1 + s)) ** years_back

    # Actual: priced claims in the period, developed like pricing
    incremental = indication["priced_claims"] == "newly_covered"
    if incremental:
        items = ((covered or {}).get("newly_covered") or {}).get("items") or []
        claims = pd.DataFrame(items, columns=["ay", "cost", "cat", "loss_date"]) if items else \
            pd.DataFrame(columns=["ay", "cost", "cat", "loss_date"])
        claims["loss_date"] = pd.to_datetime(claims["loss_date"])
    else:
        claims = pd.DataFrame({"ay": tc["ay"], "cost": tc["claim_amount"].fillna(0).clip(lower=0),
                               "cat": tc["cat_code"].notna(), "loss_date": tc["loss_date"]})
    in_period = claims[(claims["loss_date"] >= pd.Timestamp(start)) & (claims["loss_date"] <= pd.Timestamp(end))]
    count_dev = {r["year"]: r["cdf"] for r in (development.get("counts") or {}).get("rows") or []}
    inc_dev = {r["year"]: r["cdf"] for r in (development.get("incurred") or {}).get("rows") or []}
    n_reported = int(len(in_period))
    n_ult = sum(count_dev.get(int(y), 1.0) for y in in_period["ay"])
    dev_for_cost = count_dev if incremental else inc_dev
    loss_ult = float(sum(c * dev_for_cost.get(int(y), 1.0) for y, c in zip(in_period["ay"], in_period["cost"])))

    # Earned exposure in the period: calendar-year earned exposure pro-rated to the days covered
    expo = 0.0
    for cy, ex in be.groupby("calendar_year")["earned_exposure"].sum().items():
        cy = int(cy)
        y_start, y_end = max(start, date(cy, 1, 1)), min(end, date(cy, 12, 31))
        if y_end < y_start:
            continue
        earned_end = val_d if cy == val_d.year else date(cy, 12, 31)
        span = (earned_end - date(cy, 1, 1)).days + 1
        expo += float(ex) * min(1.0, ((y_end - y_start).days + 1) / span)
    if expo <= 0:
        return {"available": False, "reason": "No earned exposure in the monitoring period."}

    act_freq = 1000 * n_ult / expo
    act_lc = loss_ult / expo
    act_sev = loss_ult / n_ult if n_ult else None
    z = min(1.0, math.sqrt(n_reported / FULL_CREDIBILITY_CLAIMS))

    def kpi(name, actual, expected, unit, ci=None):
        ae = actual / expected if expected and actual is not None else None
        cw = 1 + z * (ae - 1) if ae is not None else None
        status = _status(cw)
        # Few claims but a clear signal: if the 90% interval excludes 1.00 the deviation is real even when
        # credibility pulls the weighted A/E back into the green band
        significant = bool(ci and (ci[0] > 1 or ci[1] < 1))
        if significant and status == "green":
            status = "amber"
        return {"kpi": name, "unit": unit, "actual": round(actual, 2) if actual is not None else None,
                "expected": round(expected, 2) if expected is not None else None,
                "a_to_e": round(ae, 3) if ae is not None else None,
                "credibility_weighted_a_to_e": round(cw, 3) if cw is not None else None,
                "ci90": ci, "significant": significant, "status": status}

    ci = None
    if exp_freq and n_reported:
        lo, hi = max(n_reported - 1.645 * math.sqrt(n_reported), 0), n_reported + 1.645 * math.sqrt(n_reported)
        scale = n_ult / n_reported
        ci = [round(1000 * lo * scale / expo / exp_freq, 3), round(1000 * hi * scale / expo / exp_freq, 3)]
    kpis = [kpi("Claim frequency", act_freq, exp_freq, "per 1,000 exposures", ci),
            kpi("Severity", act_sev, exp_lc * 1000 / exp_freq if exp_freq else None, "₹ per claim"),
            kpi("Pure loss cost", act_lc, exp_lc, "₹ per exposure")]
    exp_lr = indication["loss_and_lae_per_exposure"] / selected_rate if selected_rate else None
    act_lr = (act_lc * indication["loss_and_lae_per_exposure"] / indication["pure_loss_cost"] / selected_rate
              if selected_rate and indication["pure_loss_cost"] else None)
    kpis.append(kpi("Loss & LAE ratio at the selected rate", 100 * act_lr if act_lr is not None else None,
                    100 * exp_lr if exp_lr else None, "%"))

    worst = "red" if any(k["status"] == "red" for k in kpis) else "amber" if any(k["status"] == "amber" for k in kpis) \
        else "green"
    triggers = []
    lc = kpis[2]
    if lc["status"] == "red":
        triggers.append("Loss cost outside the red band: open a rate review (re-run the indication with emerged data).")
    if kpis[0]["status"] in ("amber", "red") and (kpis[0]["credibility_weighted_a_to_e"] or 1) > 1:
        triggers.append("Frequency above plan"
                        + (" (statistically significant: the 90% interval excludes 1.00)" if kpis[0]["significant"] else "")
                        + ": revisit the frequency trend selection" +
                        (f" (fitted {a['fitted_frequency_trend_pct']:+.1f}%/yr, {a['frequency_trend_pct']:+.1f}% used)"
                         if a.get("fitted_frequency_trend_pct") is not None else "")
                        + ", then the unreported-demand and adverse-selection loads against the policies that bought "
                          "the cover.")
    if kpis[1]["status"] in ("amber", "red") and (kpis[1]["credibility_weighted_a_to_e"] or 1) > 1:
        triggers.append("Severity above plan: check large losses, repair costs and the severity trend.")
    if worst == "green":
        triggers.append("Within tolerance: continue the monitoring cadence.")

    plan = [
        {"kpi": "Claim frequency, severity, loss cost (A/E)", "cadence": "monthly in year 1, then quarterly",
         "threshold": f"amber outside {AMBER[0]:.2f}–{AMBER[1]:.2f}, red outside {RED[0]:.2f}–{RED[1]:.2f} "
                      "(credibility-weighted)", "owner": "Pricing actuary"},
        {"kpi": "Loss & LAE ratio at the selected rate", "cadence": "quarterly",
         "threshold": "red band triggers a rate review", "owner": "Pricing actuary"},
        {"kpi": "Take-up vs business plan", "cadence": "monthly", "threshold": "below half of plan: revisit the "
         "business case and fixed costs", "owner": "Product"},
        {"kpi": "Buyer profile vs book (adverse selection)", "cadence": "quarterly",
         "threshold": "buyer loss cost > book x (1 + adverse-selection load)", "owner": "Pricing actuary"},
        {"kpi": "Claims on the new coverage: denial rate, report lag, litigation", "cadence": "monthly",
         "threshold": "denials of the new cover > 10%; lag beyond the pricing pattern", "owner": "Claims"},
        {"kpi": "Reserve adequacy (IBNR on the new coverage)", "cadence": "quarterly",
         "threshold": "incurred development beyond the selected factors", "owner": "Reserving actuary"},
    ]
    notes = []
    if mode == "backtest":
        notes.append(f"BACKTEST — the product is not live (effective {indication['effective_date']}). The period "
                     f"{start} to {end} is the current partial accident year, which the indication did not use: this "
                     "checks the indication against data it has not seen.")
    else:
        notes.append(f"LIVE — {months_live} months since the effective date. Actual is the priced claims in the period; "
                     "filter to the policies with the new coverage once PolicyCenter writes it.")
    notes.append("The current accident year is immature: actual claims and losses are developed to ultimate with the "
                 "pricing factors (extrapolated below 12 months), which adds uncertainty to an early A/E.")
    if n_reported < 30:
        notes.append(f"Only {n_reported} claims in the period: A/E is weighted {z:.0%} towards the data and the rest "
                     "towards plan.")
    return {
        "available": True, "mode": mode, "period": {"start": start.isoformat(), "end": end.isoformat()},
        "exposure": round(expo, 1), "exposure_unit": scope["exposure_unit"],
        "claims_reported": n_reported, "claims_ultimate": round(n_ult, 1), "credibility_z": round(z, 3),
        "kpis": kpis, "overall": worst, "triggers": triggers, "plan": plan,
        "thresholds": {"amber": AMBER, "red": RED}, "notes": notes,
    }
