"""
Business plan
=============
Three-year projection of the new coverage at the selected rate: volume, underwriting result, reinsurance,
capital and return, with stress scenarios and the break-even take-up. Every input is an assumption the actuary
sets (DEFAULTS are placeholders, not company figures); the loss cost comes from backend.pricing.

Per plan year t (0-based)
  policies     eligible exposure (the scope's latest full-year earned exposure) x take-up x (1 + growth)^t
  premium      exposures x rate x (1 + annual rate change)^t (written = earned; annual policies, no seasonality);
               the rate change defaults to the loss trend, i.e. rates are revised each year to keep pace
  loss & LAE   exposures x indicated loss & LAE per exposure x loss trend^t (frequency x severity trend)
  expenses     variable expense ratio x premium + fixed expenses; one-off launch cost in year 1
  reinsurance  quota share: cede the share of premium and losses, receive a ceding commission on ceded premium
  capital      net written premium / premium-to-capital ratio (a proxy: the IRDAI solvency margin is set by the
               Actuarial, Finance and Investment Functions of Insurers Regulations, 2024, control level 150%)
  investment   yield x (capital + loss reserves held, approx. net losses x payout years / 2)
  after tax    (underwriting result + investment income) x (1 - tax rate)
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

DEFAULTS = {
    "take_up_pct": 15.0,
    "growth_pct": 5.0,
    "years": 3,
    "launch_cost": 5_000_000.0,             # Rs 50 lakh
    "fixed_expense_per_year": 1_000_000.0,  # Rs 10 lakh
    "quota_share_pct": 0.0,
    "ceding_commission_pct": 30.0,
    "premium_to_surplus": 2.0,
    "investment_yield_pct": 7.0,      # Indian government bond yields
    "loss_payout_years": 1.0,
    "tax_rate_pct": 25.17,            # Income Tax Act s.115BAA: 22% + 10% surcharge + 4% cess
    "rate": None,               # None = the approved selected rate, else the indication
    "annual_rate_change_pct": None,  # None = the selected loss trend (rates keep pace with losses)
}
LIMITS = {
    "take_up_pct": (0.1, 100.0), "growth_pct": (-50.0, 200.0), "years": (1, 5), "launch_cost": (0.0, 1e8),
    "fixed_expense_per_year": (0.0, 1e8), "quota_share_pct": (0.0, 90.0), "ceding_commission_pct": (0.0, 60.0),
    "premium_to_surplus": (0.5, 6.0), "investment_yield_pct": (0.0, 15.0), "loss_payout_years": (0.1, 10.0),
    "tax_rate_pct": (0.0, 50.0), "rate": (0.01, 1e7), "annual_rate_change_pct": (-30.0, 50.0),
}
SCENARIOS = [
    ("Base plan", {}),
    ("Losses +25%", {"loss_factor": 1.25}),
    ("Take-up halved", {"take_up_factor": 0.5}),
    ("Rate 10% below plan (competitive pressure)", {"rate_factor": 0.9}),
    ("Shock year: losses +50% in year 1", {"year1_loss_factor": 1.5}),
]


def inputs(values: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    p = dict(DEFAULTS)
    for k, v in (values or {}).items():
        if k in p and v is not None:
            lo, hi = LIMITS[k]
            p[k] = max(lo, min(hi, float(v)))
    p["years"] = int(p["years"])
    return p


def _project(p: Dict[str, Any], eligible: float, rate: float, loss_per_exposure: float, loss_trend: float,
             expense_ratio: float, loss_factor: float = 1.0, take_up_factor: float = 1.0, rate_factor: float = 1.0,
             year1_loss_factor: float = 1.0) -> Dict[str, Any]:
    qs, cc = p["quota_share_pct"] / 100, p["ceding_commission_pct"] / 100
    years: List[Dict[str, Any]] = []
    for t in range(p["years"]):
        expo = eligible * p["take_up_pct"] / 100 * take_up_factor * (1 + p["growth_pct"] / 100) ** t
        prem = expo * rate * rate_factor * (1 + p["annual_rate_change_pct"] / 100) ** t
        loss = expo * loss_per_exposure * loss_trend ** t * loss_factor * (year1_loss_factor if t == 0 else 1.0)
        expense = prem * expense_ratio + p["fixed_expense_per_year"] + (p["launch_cost"] if t == 0 else 0.0)
        net_prem, net_loss = prem * (1 - qs), loss * (1 - qs)
        commission = prem * qs * cc
        uw = net_prem - net_loss - expense + commission
        capital = net_prem / p["premium_to_surplus"]
        invest = p["investment_yield_pct"] / 100 * (capital + net_loss * p["loss_payout_years"] / 2)
        after_tax = (uw + invest) * (1 - p["tax_rate_pct"] / 100)
        years.append({"year": t + 1, "exposures": round(expo, 1), "written_premium": round(prem, 0),
                      "loss_and_lae": round(loss, 0), "expenses": round(expense, 0),
                      "ceded_premium": round(prem * qs, 0), "ceded_losses": round(loss * qs, 0),
                      "ceding_commission": round(commission, 0), "underwriting_result": round(uw, 0),
                      "investment_income": round(invest, 0), "after_tax_result": round(after_tax, 0),
                      "capital": round(capital, 0),
                      "loss_ratio_pct": round(100 * loss / prem, 1) if prem else None,
                      "expense_ratio_pct": round(100 * expense / prem, 1) if prem else None,
                      "combined_ratio_pct": round(100 * (net_loss + expense - commission) / net_prem, 1) if net_prem else None,
                      "return_on_capital_pct": round(100 * after_tax / capital, 1) if capital else None})
    tot = {k: round(sum(y[k] for y in years), 0) for k in ("written_premium", "loss_and_lae", "expenses",
                                                           "underwriting_result", "investment_income", "after_tax_result")}
    net_prem = sum(y["written_premium"] - y["ceded_premium"] for y in years)
    net_cost = sum(y["loss_and_lae"] - y["ceded_losses"] + y["expenses"] - y["ceding_commission"] for y in years)
    peak_capital = max(y["capital"] for y in years)
    tot["combined_ratio_pct"] = round(100 * net_cost / net_prem, 1) if net_prem else None
    tot["peak_capital"] = peak_capital
    tot["return_on_peak_capital_pct"] = round(100 * tot["after_tax_result"] / (peak_capital * p["years"]), 1) if peak_capital else None
    return {"years": years, "totals": tot}


def build(indication: Dict[str, Any], eligible_exposure: float, rate: float, values: Optional[Dict[str, Any]] = None,
          ) -> Dict[str, Any]:
    if not indication.get("available"):
        return {"available": False, "reason": indication.get("reason", "No indication to plan from.")}
    p = inputs(values)
    a = indication["assumptions"]
    rate = p["rate"] or rate
    loss = indication["loss_and_lae_per_exposure"]
    trend = (1 + a["frequency_trend_pct"] / 100) * (1 + a["severity_trend_pct"] / 100)
    if p["annual_rate_change_pct"] is None:
        p["annual_rate_change_pct"] = round(100 * (trend - 1), 2)
    exp_ratio = a["expense_ratio_pct"] / 100
    args = (p, eligible_exposure, rate, loss, trend, exp_ratio)
    base = _project(*args)
    scenarios = []
    for label, kw in SCENARIOS:
        r = _project(*args, **kw)
        scenarios.append({"scenario": label, **{k: r["totals"][k] for k in
                                                ("written_premium", "combined_ratio_pct", "after_tax_result",
                                                 "return_on_peak_capital_pct")}})
    # Break-even take-up: the underwriting result is linear in take-up (fixed and launch costs aside)
    unit = _project({**p, "take_up_pct": 1.0, "launch_cost": 0.0, "fixed_expense_per_year": 0.0}, *args[1:])
    margin_per_pt = unit["totals"]["underwriting_result"]
    fixed = p["launch_cost"] + p["fixed_expense_per_year"] * p["years"]
    breakeven = round(fixed / margin_per_pt, 2) if margin_per_pt > 0 else None
    indicated = indication["indicated_premium"]
    notes = ["Every input here is a planning assumption, not company data; set them from the business case.",
             f"Eligible exposure {eligible_exposure:,.0f} {indication['exposure_unit']}: the scope's latest full-year "
             "earned exposure, i.e. today's book that could buy the cover.",
             "Loss & LAE per exposure comes from the rate indication (including its behavioural and credibility "
             "adjustments) and trends forward with the selected frequency and severity trends.",
             "Capital is premium / premium-to-capital ratio, a proxy for the IRDAI solvency margin (control level "
             "150%); the Appointed Actuary confirms the capital need under APS 21 §7."]
    if margin_per_pt <= 0:
        notes.append(f"Before fixed costs the cover loses money over the {p['years']} years (loss & LAE trend "
                     f"{100 * (trend - 1):+.1f}%/yr vs rate change {p['annual_rate_change_pct']:+.1f}%/yr): no take-up "
                     "breaks even. Raise the rate or the annual rate change.")
    elif breakeven is not None and breakeven > 100:
        notes.append(f"Breaking even over {p['years']} years needs {breakeven:.0f}% take-up — more than the whole eligible "
                     "book: at this volume the launch and fixed costs cannot be recovered. Revisit the costs, the "
                     "eligible market or the plan length.")
    return {
        "available": True,
        "inputs": p,
        "rate": round(rate, 2),
        "indicated_premium": indicated,
        "rate_vs_indication_pct": round(100 * (rate / indicated - 1), 1) if indicated else None,
        "eligible_exposure": round(eligible_exposure, 0),
        "loss_and_lae_per_exposure": loss,
        "projection": base["years"],
        "totals": base["totals"],
        "scenarios": scenarios,
        "breakeven_take_up_pct": breakeven,
        "exposure_unit": indication["exposure_unit"],
        "notes": notes,
    }
