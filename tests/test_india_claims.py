"""
India claims and compliance: IRDAI claim-settlement rules in the compliance matrix, IRDAI reporting lines,
MACT / EC claims, rupee amounts and IRDAI-compliant letters.
"""
from __future__ import annotations

import pytest

from backend import compliance, letters, operations, readiness, verification
from tests.conftest import BRIEF_ID

IRDAI = "IRDAI Master Circular"
EC_ACT = "Employee's Compensation Act"


# ---------------------------------------------------------------------------
# Compliance matrix rules
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("products", [["PersonalAuto"], ["PersonalAuto", "BusinessAuto"], ["HOPHomeowners"],
                                      ["PersonalAuto", "WorkersComp"]])
def test_irdai_rule_applies_in_every_state(products):
    for state in ("MH", "TN", "GA", "OR"):
        r = compliance.rule_for(state, products)
        assert r["source"].startswith(IRDAI) and not r["placeholder"]
        assert (r["acknowledge_days"], r["decision_days"]) == (1, 7)


def test_employees_compensation_has_its_own_rule():
    r = compliance.rule_for("MH", ["WorkersComp"])
    assert r["source"].startswith(EC_ACT) and r["payment_days"] == 30 and "12%" in r["extension_rule"]


def _matrix(products=("PersonalAuto",)):
    plan = {"states": [{"state": "MH", "exposure_share_pct": 60.0, "claims": 50},
                       {"state": "KA", "exposure_share_pct": 40.0, "claims": 30}]}
    return compliance.build_matrix(plan, list(products))


def test_confirm_needs_payment_days_and_no_tbd():
    m = _matrix()
    compliance.update_state(m, "MH", {"confirmed_by": "A. Rao"})
    with pytest.raises(ValueError, match="payment"):
        compliance.update_state(m, "MH", {"status": "Confirmed"})
    compliance.update_state(m, "MH", {"payment_days": 7})
    with pytest.raises(ValueError, match=r"\[TBD\]"):
        compliance.update_state(m, "MH", {"status": "Confirmed"})
    compliance.update_state(m, "MH", {"denial_notice": "Grievance Redressal Officer: G. Iyer, gro@insurer.in. "
                                                       "Ombudsman: Mumbai office."})
    compliance.update_state(m, "MH", {"status": "Confirmed"})
    assert compliance.summarize(m)["confirmed"] == 1


def test_old_us_matrix_is_upgraded_keeping_launch_flags():
    old = _matrix()
    for r in old["states"]:
        r.update(source="Georgia Comp. R. & Regs.", status="Confirmed", confirmed_by="X", decision_days=40)
    old["states"][1]["launch"] = False
    assert compliance.needs_upgrade(old) and not compliance.needs_upgrade(_matrix())
    new = compliance.carry_over(_matrix(), old)
    assert all(r["source"].startswith(IRDAI) and r["status"] == "Not confirmed" and r["decision_days"] == 7
               for r in new["states"])
    assert [r["launch"] for r in new["states"]] == [True, False]


def test_state_notices_show_what_starts_the_clock():
    n = compliance.state_notices(_matrix())[0]
    assert n["acknowledge"].startswith("1 calendar day: surveyor allocated") and n["payment"] == "[TBD]"
    assert "bimabharosa.irdai.gov.in" in n["denial_notice"] and "Ombudsman" in n["denial_notice"]


# ---------------------------------------------------------------------------
# Operations plan and readiness
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("product,exposure,line", [
    ("PersonalAuto", "VehicleDamage", "Motor OD (own damage)"),
    ("BusinessAuto", "BodilyInjuryDamage", "Motor TP (third-party liability)"),
    ("PersonalAuto", "MedPay", "Personal Accident"),
    ("HOPHomeowners", "Dwelling", "Fire"),
    ("CommercialProperty", "BodilyInjuryDamage", "Liability (public / product)"),
    ("WorkersComp", "WCInjuryDamage", "Workmen's Compensation / Employer's Liability"),
])
def test_irdai_reporting_lines(product, exposure, line):
    assert operations._statement_line(product, exposure)["line"] == line


def test_rupees_use_indian_grouping():
    assert readiness._money(1234567) == "₹12,34,567"
    assert readiness._money(10_000_000) == "₹1,00,00,000"
    assert readiness._money(999) == "₹999" and readiness._money(None) == "n/a"


def test_checklist_has_indian_regulatory_items():
    items = {i["id"]: i for i in readiness.build_checklist({"title": "Engine protect"})}
    assert "medicare_reporting" not in items and "injury_claims_statutory" in items
    text = " ".join(i["guidance"] for i in items.values())
    for term in ("IRDAI", "Bima Bharosa", "Ombudsman", "surveyor", "Late intimation"):
        assert term in text
    for us in ("Medicare", "NAIC", "OFAC", "1099", "Department of Insurance", "$"):
        assert us not in text


# ---------------------------------------------------------------------------
# Letters
# ---------------------------------------------------------------------------
def test_no_late_notice_rejection_letter():
    reasons = letters._denial_reasons({"denials": {"top_reasons": ["Late notice / prejudice: 40", "Flood: 12"]}})
    assert [r["key"] for r in reasons] == ["denial_not_purchased", "denial_exclusion"]
    assert letters.SCENARIO_LETTERS["late_notice"] == ["acknowledgement"]


def test_template_letters_are_irdai_compliant():
    reasons = letters._denial_reasons({})
    out = {l["key"]: l for l in letters._fallback({"title": "Engine protect"}, {"sections": []}, reasons)}
    ack = out["acknowledgement"]["body"]
    assert "{{surveyor_name}}" in ack and "{{surveyor_licence_number}}" in ack
    assert "will not be rejected only because a document is missing" in out["documents_request"]["body"]
    assert all("{{state_required_notice}}" in l["body"] for l in out.values() if l["type"] == "denial")
    for l in out.values():
        assert "[TBD — unknown merge field" not in l["body"]
        assert verification.check_letter_rules(l["subject"] + "\n" + l["body"], l["name"]) == []


@pytest.mark.parametrize("text", ["call +91 98765 43210", "call 9876543210", "toll-free 1800 266 7780",
                                  "call (555) 123-4567"])
def test_letter_check_catches_phone_numbers(text):
    assert verification.check_letter_rules(text, "x")


# ---------------------------------------------------------------------------
# Through the API
# ---------------------------------------------------------------------------
@pytest.mark.api
def test_compliance_matrix_is_irdai(client, claims_headers):
    r = client.get(f"/api/briefs/{BRIEF_ID}/compliance", headers=claims_headers)
    assert r.status_code == 200, r.text
    rows = r.json()["matrix"]["states"]
    assert rows and all(row["source"].startswith(IRDAI) for row in rows)
    assert "IRDAI" in r.json()["rules_note"]


@pytest.mark.api
def test_operations_plan_has_injury_claims_not_medicare(client, claims_headers):
    r = client.get(f"/api/briefs/{BRIEF_ID}/operations", headers=claims_headers)
    assert r.status_code == 200, r.text
    plan = r.json()
    assert "medicare" not in plan and "injury_claims" in plan
    assert all("Annual Statement" not in row["statement_line"] for row in plan["statutory_reporting"]["rows"])
