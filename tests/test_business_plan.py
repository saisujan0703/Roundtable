"""backend.business_plan: the projection, reinsurance, capital and break-even take-up."""
from __future__ import annotations

import pytest

from backend import business_plan

INDICATION = {"available": True, "indicated_premium": 100.0, "loss_and_lae_per_exposure": 60.0,
              "exposure_unit": "vehicle-years",
              "assumptions": {"frequency_trend_pct": 0.0, "severity_trend_pct": 0.0, "expense_ratio_pct": 25.0}}
SIMPLE = {"take_up_pct": 10, "growth_pct": 0, "years": 1, "launch_cost": 0, "fixed_expense_per_year": 0,
          "annual_rate_change_pct": 0}


def test_one_year_by_hand():
    out = business_plan.build(INDICATION, eligible_exposure=10_000, rate=100.0, values=SIMPLE)
    y = out["projection"][0]
    assert y["exposures"] == 1_000
    assert y["written_premium"] == 100_000 and y["loss_and_lae"] == 60_000 and y["expenses"] == 25_000
    assert y["underwriting_result"] == 15_000
    assert y["capital"] == 50_000                                  # premium / 2.0 premium-to-surplus
    assert y["investment_income"] == 5_600                         # 7% x (50,000 + 60,000 x 1 yr / 2)
    assert y["after_tax_result"] == round((15_000 + 5_600) * 0.7483)   # 25.17% tax
    assert y["combined_ratio_pct"] == 85.0


def test_quota_share_cedes_premium_and_losses_and_earns_commission():
    out = business_plan.build(INDICATION, 10_000, 100.0, {**SIMPLE, "quota_share_pct": 40, "ceding_commission_pct": 30})
    y = out["projection"][0]
    assert y["ceded_premium"] == 40_000 and y["ceded_losses"] == 24_000 and y["ceding_commission"] == 12_000
    assert y["underwriting_result"] == 60_000 - 36_000 - 25_000 + 12_000


def test_growth_and_rate_change_compound():
    out = business_plan.build(INDICATION, 10_000, 100.0,
                              {**SIMPLE, "years": 3, "growth_pct": 10, "annual_rate_change_pct": 5})
    y3 = out["projection"][2]
    assert y3["exposures"] == pytest.approx(1_000 * 1.1 ** 2, abs=0.1)
    assert y3["written_premium"] == pytest.approx(1_000 * 1.1 ** 2 * 100 * 1.05 ** 2, abs=1)


def test_rate_change_defaults_to_the_loss_trend():
    ind = {**INDICATION, "assumptions": {**INDICATION["assumptions"], "frequency_trend_pct": 2.0, "severity_trend_pct": 5.0}}
    out = business_plan.build(ind, 10_000, 100.0, {k: v for k, v in SIMPLE.items() if k != "annual_rate_change_pct"})
    assert out["inputs"]["annual_rate_change_pct"] == pytest.approx(100 * (1.02 * 1.05 - 1), abs=0.01)


def test_break_even_take_up():
    # 1 pt of take-up = 100 exposures x $15 margin = $1,500; fixed costs $300,000 -> 200% take-up
    out = business_plan.build(INDICATION, 10_000, 100.0,
                              {**SIMPLE, "launch_cost": 250_000, "fixed_expense_per_year": 50_000})
    assert out["breakeven_take_up_pct"] == pytest.approx(200.0)
    assert any("more than the whole eligible book" in n for n in out["notes"])


def test_loss_making_cover_has_no_break_even():
    out = business_plan.build(INDICATION, 10_000, 60.0, SIMPLE)       # rate equals loss cost: expenses make it negative
    assert out["breakeven_take_up_pct"] is None
    assert any("no take-up breaks even" in n for n in out["notes"])


def test_stress_scenarios_are_worse_than_base():
    out = business_plan.build(INDICATION, 10_000, 100.0, {**SIMPLE, "years": 3})
    by = {s["scenario"]: s for s in out["scenarios"]}
    base = by["Base plan"]["after_tax_result"]
    for name in ("Losses +25%", "Rate 10% below plan (competitive pressure)", "Shock year: losses +50% in year 1"):
        assert by[name]["after_tax_result"] < base


def test_inputs_are_clamped():
    p = business_plan.inputs({"take_up_pct": 500, "years": 9, "quota_share_pct": -5})
    assert p["take_up_pct"] == 100.0 and p["years"] == 5 and p["quota_share_pct"] == 0.0


def test_unavailable_indication_passes_through():
    assert business_plan.build({"available": False, "reason": "x"}, 1, 1)["available"] is False
