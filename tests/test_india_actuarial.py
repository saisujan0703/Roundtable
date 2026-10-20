"""
India actuarial: IRDAI Use & File and IAI APS 21 in the actuarial memorandum, the expenses-of-management limit,
Indian tax and yield defaults, and competitor product leads instead of SERFF.
"""
from __future__ import annotations

import pytest

from backend import actuarial_memo, actuarial_settings, business_plan, filing_research
from tests.conftest import BRIEF_ID

US_TERMS = ("ASOP", "SERFF", "NAIC", "Department of Insurance")


# ---------------------------------------------------------------------------
# Standards and the expenses-of-management check
# ---------------------------------------------------------------------------
def test_standards_are_indian():
    refs = " ".join(r[0] for r in actuarial_memo.STANDARDS)
    assert "APS 21" in refs and "APS 34" in refs and "Master Circular" in refs and "EoM" in refs
    assert not any(t in refs for t in US_TERMS)


@pytest.mark.parametrize("expense, within", [(25.0, True), (30.0, True), (32.5, False)])
def test_eom_check_against_30_pct(expense, within):
    text = actuarial_memo.eom_check(expense, 5.0)
    assert ("within" in text) is within and ("**above**" in text) is (not within)
    assert "GST" in text
    assert ("Finance must show" in text) is (not within)


# ---------------------------------------------------------------------------
# Company settings and business plan defaults
# ---------------------------------------------------------------------------
def test_indian_tax_and_yield_defaults():
    f = actuarial_settings.FIELDS
    assert f["tax_rate_pct"][1] == 25.17 and f["investment_yield_pct"][1] == 7.0
    assert "GST" in f["premium_tax_pct"][0] and f["premium_tax_pct"][1] == 0.0
    assert business_plan.DEFAULTS["tax_rate_pct"] == 25.17 and business_plan.DEFAULTS["investment_yield_pct"] == 7.0


def test_profit_can_be_negative_with_indian_yields():
    # 10% x 0.5 / 0.7483 - 7% x 1.1 = 6.68% - 7.7% = -1.02%: investment income carries the return
    s = {"values": {"target_roe_pct": 10.0}, "sources": {"target_roe_pct": "test"}}
    assert actuarial_settings.profit_pct(s) == pytest.approx(-1.02, abs=0.01)


# ---------------------------------------------------------------------------
# Competitor product leads and industry CSV
# ---------------------------------------------------------------------------
def test_product_leads_point_to_indian_sources(monkeypatch):
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)
    out = filing_research.filing_leads("EV battery cover", "private car")
    labels = {r["label"] for r in out["registers"]}
    assert {"IRDAI", "Insurance Information Bureau of India", "GIC Re"} <= labels
    assert "serff" not in out and "NL-27" in out["how_to"] and out["web"] == []


@pytest.mark.parametrize("value", ["₹1,250", "Rs. 1,250", "Rs 1,250", "1250"])
def test_csv_import_accepts_rupee_values(value):
    state = {"benchmarks": []}
    text = f'source,kind,value,as_of\nIIB motor OD,loss_cost,"{value}",2025-03-31\n'
    res = filing_research.import_csv(state, text, "tester")
    assert res["added"] == 1 and not res["errors"] and state["benchmarks"][0]["value"] == 1250


# ---------------------------------------------------------------------------
# Through the API
# ---------------------------------------------------------------------------
@pytest.mark.api
def test_memo_is_for_use_and_file(client, actuary_headers):
    r = client.get(f"/api/briefs/{BRIEF_ID}/actuarial-memo", headers=actuary_headers)
    assert r.status_code == 200, r.text
    m = r.json()
    if not m.get("available"):
        pytest.skip("no indication for this brief")
    md = m["markdown"]
    assert "Use & File" in md and "APS 21" in md and "Expenses of management" in md and "Motor Vehicles Act" in md
    assert not any(t in md for t in US_TERMS)
    assert any("UIN" in t for t in m["tbd"]) and any("Appointed Actuary" in t for t in m["tbd"])


@pytest.mark.api
def test_filing_leads_endpoint(client, actuary_headers, monkeypatch):
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)
    r = client.get(f"/api/briefs/{BRIEF_ID}/filing-leads", headers=actuary_headers)
    assert r.status_code == 200, r.text
    assert r.json()["registers"][0]["label"] == "IRDAI"
