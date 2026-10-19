"""backend.pricing: the rate indication, checked against hand calculations."""
from __future__ import annotations

import math
from datetime import date

import pytest

from backend import pricing

ALAE = 1.10             # analytics_input's 10% ALAE
PERMISSIBLE = 0.70      # 1 - 25% expense - 5% profit (the `flat` overrides)


def test_no_claims_experience_is_not_priced(analytics_input):
    analytics_input["summary"]["has_data"] = False
    out = pricing.rate_indication(analytics_input)
    assert out["available"] is False and "nothing to price" in out["reason"]


def test_line_baseline_basis_is_not_priced(analytics_input):
    analytics_input["basis"]["basis"] = "line_baseline"
    assert pricing.rate_indication(analytics_input)["available"] is False


def test_only_partial_years_is_not_priced(analytics_input):
    analytics_input["trend"] = [r for r in analytics_input["trend"] if r["partial_year"]]
    assert pricing.rate_indication(analytics_input)["available"] is False


def test_flat_indication_is_loss_cost_times_alae_over_permissible_loss_ratio(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, flat)
    assert out["available"] is True
    assert [r["year"] for r in out["experience"]] == [2024]            # last full year only; 2025 is partial
    assert out["pure_loss_cost"] == pytest.approx(60.0)
    assert out["loss_and_lae_per_exposure"] == pytest.approx(60.0 * ALAE, abs=0.01)
    assert out["indicated_premium"] == pytest.approx(60.0 * ALAE / PERMISSIBLE, abs=0.01)
    assert out["steps"][-1]["value"] == out["indicated_premium"]       # the worksheet ends at the indication


def test_experience_is_exposure_weighted(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, {**flat, "experience_years": 2})
    # 2023: 10,000 x $40, 2024: 30,000 x $60
    assert out["pure_loss_cost"] == pytest.approx((10_000 * 40 + 30_000 * 60) / 40_000)


def test_dates_effective_and_average_accident(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, flat)
    assert out["effective_date"] == "2026-06-30"            # valuation + 6 months, clipped to month end
    assert out["average_accident_date"] == "2027-06-30"     # annual policies written evenly: effective + 12 months


def test_trend_compounds_frequency_and_severity_to_the_average_accident_date(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, {**flat, "frequency_trend_pct": 2.0, "severity_trend_pct": 10.0})
    row = out["experience"][0]
    assert row["trend_years"] == pytest.approx(3.0, abs=0.02)   # mid-2024 to 30 Jun 2027
    years = pricing._year_fraction(date(2027, 6, 30)) - 2024.5
    expected = (1.02 * 1.10) ** years
    assert row["trend_factor"] == pytest.approx(expected, abs=1e-4)
    assert out["pure_loss_cost"] == pytest.approx(60.0 * expected, abs=0.01)


def test_expense_and_profit_divide_not_multiply(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, {**flat, "expense_ratio_pct": 30.0, "profit_pct": 10.0})
    assert out["indicated_premium"] == pytest.approx(60.0 * ALAE / 0.60, abs=0.01)


def test_ulae_applies_on_top_of_alae(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, {**flat, "ulae_pct": 5.0})
    assert out["loss_and_lae_per_exposure"] == pytest.approx(60.0 * ALAE * 1.05, abs=0.01)


def test_adverse_selection_load(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, {**flat, "adverse_selection_pct": 10.0})
    assert out["pure_loss_cost"] == pytest.approx(66.0)


def test_unreported_demand_load_only_applies_to_incremental_pricing(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, {**flat, "unreported_load_pct": 50.0})
    assert out["priced_claims"] == "whole_pattern"
    assert out["pure_loss_cost"] == pytest.approx(60.0)


# ---------------------------------------------------------------------------
# Development
# ---------------------------------------------------------------------------
def _development(cl=1.20, bf=1.10, count=1.05):
    return {"has_data": True,
            "incurred": {"rows": [{"year": 2024, "cdf": cl, "bf_factor": bf}]},
            "counts": {"rows": [{"year": 2024, "cdf": count}]}}


def test_chain_ladder_development(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, {**flat, "apply_development": True},
                                  context={"development": _development()})
    assert out["experience"][0]["development_factor"] == pytest.approx(1.20)
    assert out["pure_loss_cost"] == pytest.approx(72.0)


def test_bornhuetter_ferguson_development(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, {**flat, "apply_development": True,
                                                    "dev_method": "bornhuetter_ferguson"},
                                  context={"development": _development()})
    assert out["experience"][0]["development_factor"] == pytest.approx(1.10)


def test_without_a_triangle_the_heuristic_is_used(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, {**flat, "apply_development": True})
    assert out["development"]["method"] == "heuristic"


# ---------------------------------------------------------------------------
# CAT and large losses
# ---------------------------------------------------------------------------
def _composition(cat_share=10.0, ratio=0.20, excess=1.10):
    return {"has_data": True, "cat": {"cat_share_pct": cat_share, "ratio_to_noncat": ratio},
            "excess": {"factor": excess, "source": "pattern"},
            "by_year": [{"year": 2024, "noncat_capped": 40.0, "incurred": 50.0}]}


def test_cat_removed_large_capped_then_loaded_back(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, flat, context={"composition": _composition()})
    # 80% of the loss is non-CAT below the cap; x1.10 excess; +20% CAT provision (the data's ratio by default)
    assert out["cat_large"]["applied"] is True
    assert out["assumptions"]["cat_load_pct"] == pytest.approx(20.0)
    assert out["pure_loss_cost"] == pytest.approx(60.0 * 0.8 * 1.10 * 1.20)


def test_cat_driven_pattern_is_priced_with_cat_in(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, flat, context={"composition": _composition(cat_share=60.0)})
    assert out["cat_large"]["applied"] is False and out["cat_large"]["cat_driven"] is True
    assert out["pure_loss_cost"] == pytest.approx(60.0)
    assert any("catastrophe model" in n for n in out["notes"])


# ---------------------------------------------------------------------------
# Credibility
# ---------------------------------------------------------------------------
def test_credibility_weights_experience_against_the_benchmark(analytics_input, flat):
    bench = {"kind": "loss_cost", "value": 100.0, "as_of": "2027-06-30"}   # at the target date: no trending
    out = pricing.rate_indication(analytics_input, flat, context={"benchmarks": [bench]})
    z = math.sqrt(300 / pricing.FULL_CREDIBILITY_CLAIMS)
    assert out["credibility"]["z"] == pytest.approx(z, abs=1e-3)
    assert out["credibility"]["complement"] == pytest.approx(100.0, abs=0.1)
    assert out["pure_loss_cost"] == pytest.approx(z * 60.0 + (1 - z) * 100.0, abs=0.05)


def test_premium_benchmark_is_converted_to_a_loss_cost(analytics_input, flat):
    bench = {"kind": "premium", "value": 200.0, "as_of": "2027-06-30", "permissible_loss_ratio_pct": 65.0}
    out = pricing.rate_indication(analytics_input, flat, context={"benchmarks": [bench]})
    assert out["credibility"]["complement"] == pytest.approx(200.0 * 0.65 / ALAE, abs=0.1)


def test_excluded_benchmark_and_complement_switch(analytics_input, flat):
    bench = {"kind": "loss_cost", "value": 100.0, "as_of": "2027-06-30"}
    off = pricing.rate_indication(analytics_input, {**flat, "apply_complement": False}, context={"benchmarks": [bench]})
    excluded = pricing.rate_indication(analytics_input, flat, context={"benchmarks": [{**bench, "include": False}]})
    assert off["pure_loss_cost"] == pytest.approx(60.0)
    assert excluded["credibility"]["complement"] is None


def test_full_credibility_ignores_the_benchmark(analytics_input, flat):
    for r in analytics_input["trend"]:
        r["claims"] = 5_000
    bench = {"kind": "loss_cost", "value": 100.0, "as_of": "2027-06-30"}
    out = pricing.rate_indication(analytics_input, flat, context={"benchmarks": [bench]})
    assert out["credibility"]["z"] == 1.0 and out["pure_loss_cost"] == pytest.approx(60.0)


# ---------------------------------------------------------------------------
# Incremental pricing (the covered-claims set)
# ---------------------------------------------------------------------------
def _covered(claims=30, cost=90_000.0):
    return {"has_data": True,
            "newly_covered": {"by_year": [{"year": 2024, "claims": claims, "estimated_cost": cost}],
                              "items": [(2024, cost, False)]}}


def test_incremental_prices_only_newly_covered_claims(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, flat, covered=_covered())
    assert out["priced_claims"] == "newly_covered"
    assert out["pure_loss_cost"] == pytest.approx(90_000 / 30_000)       # $3 per exposure, not the pattern's $60
    assert out["pattern_loss_cost"] == pytest.approx(60.0)


def test_incremental_applies_unreported_demand(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, {**flat, "unreported_load_pct": 50.0}, covered=_covered())
    assert out["pure_loss_cost"] == pytest.approx(3.0 * 1.5)


def test_standalone_switch_prices_the_whole_pattern(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, {**flat, "price_whole_pattern": True}, covered=_covered())
    assert out["priced_claims"] == "whole_pattern" and out["pure_loss_cost"] == pytest.approx(60.0)


def test_no_newly_covered_claims_gives_zero_and_says_so(analytics_input, flat):
    out = pricing.rate_indication(analytics_input, flat, covered=_covered(claims=0, cost=0.0))
    assert out["indicated_premium"] == 0.0
    assert any("no incremental cost" in n for n in out["notes"])


# ---------------------------------------------------------------------------
# Assumptions, range, sensitivity
# ---------------------------------------------------------------------------
def test_assumptions_are_clamped_and_parsed():
    a = pricing.assumptions({}, {"expense_ratio_pct": 99, "experience_years": 0, "apply_development": "false",
                                 "dev_method": "made_up", "unknown_key": 5})
    assert a["expense_ratio_pct"] == 60.0 and a["experience_years"] == 1
    assert a["apply_development"] is False and a["dev_method"] == "chain_ladder"
    assert "unknown_key" not in a


def test_fitted_trend_used_only_when_significant():
    fit = {"has_data": True, "annual_trend_pct": 8.0, "significant": False}
    assert pricing.assumptions({"frequency_trend_fit": fit})["frequency_trend_pct"] == 0.0
    assert pricing.assumptions({"frequency_trend_fit": {**fit, "significant": True}})["frequency_trend_pct"] == 8.0


def test_range_follows_the_trend_interval(analytics_input, flat):
    analytics_input["frequency_trend_fit"] = {"has_data": True, "annual_trend_pct": 3.0, "significant": True,
                                              "ci95_low_pct": -2.0, "ci95_high_pct": 8.0}
    out = pricing.rate_indication(analytics_input, {k: v for k, v in flat.items() if k != "frequency_trend_pct"})
    assert out["range"]["low"] < out["indicated_premium"] < out["range"]["high"]


def test_sensitivity_sorted_by_swing(analytics_input, flat):
    swings = [s["swing"] for s in pricing.rate_indication(analytics_input, flat)["sensitivity"]]
    assert swings == sorted(swings, reverse=True) and len(swings) >= 5


@pytest.mark.parametrize("start,months,expected", [
    (date(2025, 1, 31), 1, date(2025, 2, 28)), (date(2024, 1, 31), 1, date(2024, 2, 29)),
    (date(2025, 12, 31), 6, date(2026, 6, 30)), (date(2025, 11, 15), 3, date(2026, 2, 15)),
])
def test_add_months_clips_to_month_end(start, months, expected):
    assert pricing._add_months(start, months) == expected
