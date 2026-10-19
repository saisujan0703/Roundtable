"""backend.actuarial (assumptions, benchmarks, approval) and backend.actuarial_settings (company assumptions)."""
from __future__ import annotations

import pytest

from backend import actuarial, actuarial_settings, monitoring, pricing


@pytest.fixture
def indication(analytics_input, flat):
    return pricing.rate_indication(analytics_input, flat)


# ---------------------------------------------------------------------------
# Assumptions and benchmarks
# ---------------------------------------------------------------------------
def test_save_assumptions_keeps_known_keys_only():
    state = actuarial.save_assumptions(actuarial.empty(), {"profit_pct": "4", "apply_complement": 0, "bogus": 1,
                                                           "ulae_pct": None})
    assert state["assumptions"] == {"profit_pct": 4.0, "apply_complement": False}


def test_save_assumptions_rejects_an_unknown_development_method():
    with pytest.raises(ValueError):
        actuarial.save_assumptions(actuarial.empty(), {"dev_method": "guess"})


GOOD_BENCHMARK = {"kind": "loss_cost", "source": "ISO 2025", "value": 50, "as_of": "2025-01-01"}


@pytest.mark.parametrize("change,message", [
    ({"kind": "rumour"}, "kind"), ({"source": "  "}, "source"), ({"value": 0}, "positive"),
    ({"value": "abc"}, "value"), ({"as_of": "soon"}, "date"),
    ({"kind": "premium", "permissible_loss_ratio_pct": 10}, "permissible"),
])
def test_benchmark_validation(change, message):
    with pytest.raises(ValueError, match=message):
        actuarial.add_benchmark(actuarial.empty(), {**GOOD_BENCHMARK, **change}, "tester")


def test_benchmark_add_toggle_remove():
    state = actuarial.add_benchmark(actuarial.empty(), GOOD_BENCHMARK, "tester")
    bid = state["benchmarks"][0]["id"]
    actuarial.set_benchmark_included(state, bid, False)
    assert state["benchmarks"][0]["include"] is False
    actuarial.remove_benchmark(state, bid)
    assert state["benchmarks"] == []
    with pytest.raises(KeyError):
        actuarial.remove_benchmark(state, bid)


def test_benchmark_limit():
    state = actuarial.empty()
    for _ in range(actuarial.MAX_BENCHMARKS):
        actuarial.add_benchmark(state, GOOD_BENCHMARK, "tester")
    with pytest.raises(ValueError, match="At most"):
        actuarial.add_benchmark(state, GOOD_BENCHMARK, "tester")


# ---------------------------------------------------------------------------
# Approval
# ---------------------------------------------------------------------------
def test_approval_needs_a_name(indication):
    with pytest.raises(ValueError, match="name"):
        actuarial.approve(actuarial.empty(), indication, " ", "", None)


def test_selection_far_from_the_indication_needs_a_reason(indication):
    far = indication["indicated_premium"] * 1.10
    with pytest.raises(ValueError, match="reason"):
        actuarial.approve(actuarial.empty(), indication, "A. Actuary", "", far)
    state = actuarial.approve(actuarial.empty(), indication, "A. Actuary", "Market position", far)
    assert state["approval"]["deviation_pct"] == pytest.approx(10.0, abs=0.01)


def test_approval_goes_stale_when_inputs_change(analytics_input, flat, indication):
    state = actuarial.approve(actuarial.empty(), indication, "A. Actuary", "", None)
    assert actuarial.status(state, indication)["approved"] is True
    changed = pricing.rate_indication(analytics_input, {**flat, "profit_pct": 6.0})
    st = actuarial.status(state, changed)
    assert st["approved"] is False and st["stale"] is True and "re-approve" in st["detail"]


def test_selected_rate_uses_a_current_approval_only(analytics_input, flat, indication):
    selected = round(indication["indicated_premium"] * 1.02, 2)
    state = actuarial.approve(actuarial.empty(), indication, "A. Actuary", "", selected)
    assert actuarial.selected_rate(state, indication) == selected
    changed = pricing.rate_indication(analytics_input, {**flat, "profit_pct": 6.0})
    assert actuarial.selected_rate(state, changed) == changed["indicated_premium"]


def test_status_without_approval():
    assert actuarial.status(actuarial.empty(), None)["approved"] is False


# ---------------------------------------------------------------------------
# Company settings: expense ratio and profit derived from ROE
# ---------------------------------------------------------------------------
def _settings(**values):
    return {"values": values, "sources": {k: "test" for k in values}}


def test_expense_ratio_is_the_sum_of_components():
    s = _settings(commission_pct=15, premium_tax_pct=2, other_acquisition_pct=3, general_expense_pct=5)
    assert actuarial_settings.expense_ratio_pct(s) == 25


def test_profit_from_target_roe_by_hand():
    # S = 1/2 = 0.5, R = 0.6; 10% x 0.5 / 0.79 - 3% x 1.1 = 6.329% - 3.3% = 3.03%
    assert actuarial_settings.profit_pct(_settings()) == pytest.approx(3.03, abs=0.01)
    higher = actuarial_settings.profit_pct(_settings(target_roe_pct=15))
    assert higher > actuarial_settings.profit_pct(_settings())


def test_pricing_defaults_only_for_what_is_set():
    assert actuarial_settings.pricing_defaults(_settings()) == {}
    out = actuarial_settings.pricing_defaults(_settings(tax_rate_pct=21, ulae_pct=6))
    assert set(out) == {"profit_pct", "ulae_pct"} and out["ulae_pct"] == 6


def test_provenance_cites_sources():
    prov = actuarial_settings.provenance(_settings(commission_pct=12))
    assert "Commission %: test" in prov["expense_ratio_pct"] and "profit_pct" not in prov


def test_save_rejects_out_of_range_and_unsourced(test_db):
    actuarial_settings.init_table()
    with pytest.raises(ValueError, match="between"):
        actuarial_settings.save({"tax_rate_pct": 80}, {"tax_rate_pct": "x"}, "tester")
    with pytest.raises(ValueError, match="Cite the source"):
        actuarial_settings.save({"tax_rate_pct": 21}, {"tax_rate_pct": "  "}, "tester")
    saved = actuarial_settings.save({"tax_rate_pct": 21, "unknown": 3}, {"tax_rate_pct": "Federal rate"}, "tester")
    assert saved["values"] == {"tax_rate_pct": 21.0} and saved["updated_by"] == "tester"


# ---------------------------------------------------------------------------
# Monitoring
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("ae,expected", [(None, "no data"), (1.0, "green"), (0.90, "green"), (1.10, "green"),
                                         (0.85, "amber"), (1.25, "amber"), (0.79, "red"), (1.30, "red")])
def test_actual_to_expected_status_bands(ae, expected):
    assert monitoring._status(ae) == expected


def test_expected_matches_the_indication(analytics_input, flat):
    ind = pricing.rate_indication(analytics_input, {**flat, "adverse_selection_pct": 10.0})
    exp = monitoring._expected(ind)
    assert exp["loss_cost"] == ind["pure_loss_cost"]
    assert exp["frequency_per_1000"] == pytest.approx(10.0 * 1.10)      # 300 claims / 30,000, plus the 10% load
    assert exp["severity"] == pytest.approx(1000 * exp["loss_cost"] / exp["frequency_per_1000"])
