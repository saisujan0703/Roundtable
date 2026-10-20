"""End to end through the FastAPI app, on a temporary copy of roundtable.db (see conftest)."""
from __future__ import annotations

import pytest

from conftest import ACTUARY, BRIEF_ID, CLAIMS

pytestmark = pytest.mark.api

SOURCED = {"values": {"target_roe_pct": 12.0, "tax_rate_pct": 25.17},
           "sources": {"target_roe_pct": "2026 capital plan", "tax_rate_pct": "Income Tax Act s.115BAA"}}


# ---------------------------------------------------------------------------
# Sign-in and roles
# ---------------------------------------------------------------------------
def test_health_is_public(client):
    assert client.get("/api/health").json()["status"] == "ok"


def test_api_needs_a_session(client):
    assert client.get("/api/briefs").status_code == 401
    assert client.get("/api/briefs", headers={"Authorization": "Bearer nonsense"}).status_code == 401


def test_wrong_password_and_wrong_role(client):
    email, _, role = CLAIMS
    assert client.post("/api/auth/login", json={"email": email, "password": "nope", "role": role}).status_code == 401
    email, password, _ = ACTUARY
    r = client.post("/api/auth/login", json={"email": email, "password": password, "role": "Claims Lead"})
    assert r.status_code == 403


def test_me_and_logout(client):
    email, password, role = CLAIMS
    token = client.post("/api/auth/login", json={"email": email, "password": password, "role": role}).json()["token"]
    h = {"Authorization": f"Bearer {token}"}
    assert client.get("/api/auth/me", headers=h).json()["role"] == role
    client.post("/api/auth/logout", headers=h)
    assert client.get("/api/auth/me", headers=h).status_code == 401


def test_account_locks_after_repeated_wrong_passwords(client, test_db):
    from backend import auth
    from backend.database import get_connection
    with get_connection() as conn:
        conn.execute("INSERT OR REPLACE INTO users (email, name, role, password_hash, created_at, failed_attempts) "
                     "VALUES (?, ?, ?, ?, '2026-01-01', 0)",
                     ("lockout@test.com", "Lockout", "Claims Lead", auth.hash_password("right")))
    body = {"email": "lockout@test.com", "password": "wrong", "role": "Claims Lead"}
    codes = [client.post("/api/auth/login", json=body).status_code for _ in range(auth.MAX_FAILED_ATTEMPTS)]
    assert codes == [401] * auth.MAX_FAILED_ATTEMPTS
    r = client.post("/api/auth/login", json={**body, "password": "right"})
    assert r.status_code == 423


def test_claims_lead_cannot_change_actuarial_work(client, claims_headers):
    assert client.put("/api/actuarial/settings", json=SOURCED, headers=claims_headers).status_code == 403
    r = client.put(f"/api/briefs/{BRIEF_ID}/actuarial/assumptions", json={"assumptions": {}}, headers=claims_headers)
    assert r.status_code == 403


def test_actuary_cannot_change_claims_work(client, actuary_headers):
    r = client.put(f"/api/briefs/{BRIEF_ID}/launch-gate/claims", json={}, headers=actuary_headers)
    assert r.status_code == 403


# ---------------------------------------------------------------------------
# Company assumptions
# ---------------------------------------------------------------------------
def test_company_settings_need_a_source(client, actuary_headers):
    unsourced = {"values": {"target_roe_pct": 10.0}, "sources": {}}
    r = client.put("/api/actuarial/settings", json=unsourced, headers=actuary_headers)
    assert r.status_code == 400 and "Cite the source" in r.json()["detail"]


def test_company_settings_save_and_derive_profit(client, actuary_headers):
    r = client.put("/api/actuarial/settings", json=SOURCED, headers=actuary_headers)
    assert r.status_code == 200, r.text
    body = r.json()
    assert body["values"] == SOURCED["values"] and body["updated_by"] == "Lead Actuary"
    # 12% x 0.5 / 0.7483 - 7% x (0.5 + 0.6)
    assert body["derived"]["profit_pct"] == pytest.approx(12 * 0.5 / 0.7483 - 7 * 1.1, abs=0.01)
    assert body["derived"]["eom_limit_pct"] == 30.0


# ---------------------------------------------------------------------------
# Briefs and the actuarial workspace
# ---------------------------------------------------------------------------
def test_briefs_list_and_missing_brief(client, claims_headers):
    briefs = client.get("/api/briefs", headers=claims_headers).json()
    assert any(b["id"] == BRIEF_ID for b in briefs)
    assert client.get("/api/briefs/999999", headers=claims_headers).status_code == 404


@pytest.fixture(scope="module")
def pricing_response(client, actuary_headers):
    r = client.get(f"/api/briefs/{BRIEF_ID}/pricing", headers=actuary_headers)
    assert r.status_code == 200, r.text
    body = r.json()
    if not body.get("available"):
        pytest.skip(f"brief {BRIEF_ID} has no indication: {body.get('reason')}")
    return body


def test_indication_is_internally_consistent(pricing_response):
    p = pricing_response
    assert p["indicated_premium"] > 0
    assert p["steps"][-1]["value"] == p["indicated_premium"]
    a = p["assumptions"]
    permissible = 1 - (a["expense_ratio_pct"] + a["profit_pct"]) / 100
    assert p["indicated_premium"] == pytest.approx(p["loss_and_lae_per_exposure"] / permissible, rel=1e-3)
    if p["range"]["low"] is not None:
        assert p["range"]["low"] <= p["indicated_premium"] <= p["range"]["high"]


def test_what_if_does_not_persist(client, actuary_headers, pricing_response):
    base = pricing_response["indicated_premium"]
    hi = client.get(f"/api/briefs/{BRIEF_ID}/pricing", params={"profit_pct": 15}, headers=actuary_headers).json()
    assert hi["what_if"] is True and hi["indicated_premium"] > base
    again = client.get(f"/api/briefs/{BRIEF_ID}/pricing", headers=actuary_headers).json()
    assert again["indicated_premium"] == base


def test_saved_assumptions_change_the_indication(client, actuary_headers, pricing_response):
    url = f"/api/briefs/{BRIEF_ID}/actuarial/assumptions"
    try:
        r = client.put(url, json={"assumptions": {"expense_ratio_pct": 35.0}}, headers=actuary_headers)
        assert r.status_code == 200
        changed = client.get(f"/api/briefs/{BRIEF_ID}/pricing", headers=actuary_headers).json()
        assert changed["assumptions"]["expense_ratio_pct"] == 35.0
        assert changed["indicated_premium"] != pricing_response["indicated_premium"]
    finally:
        client.put(url, json={"assumptions": pricing_response["saved_assumptions"]}, headers=actuary_headers)


def test_bad_dev_method_is_rejected(client, actuary_headers):
    r = client.put(f"/api/briefs/{BRIEF_ID}/actuarial/assumptions",
                   json={"assumptions": {"dev_method": "guess"}}, headers=actuary_headers)
    assert r.status_code == 400


def test_approval_flow_and_staleness(client, actuary_headers, pricing_response):
    url = f"/api/briefs/{BRIEF_ID}/actuarial/approval"
    r = client.put(url, json={"name": "Test Actuary", "note": ""}, headers=actuary_headers)
    assert r.status_code == 200, r.text
    status = client.get(f"/api/briefs/{BRIEF_ID}/pricing", headers=actuary_headers).json()["approval_status"]
    assert status["approved"] is True
    a_url = f"/api/briefs/{BRIEF_ID}/actuarial/assumptions"
    try:
        client.put(a_url, json={"assumptions": {**pricing_response["saved_assumptions"], "profit_pct": 9.0}},
                   headers=actuary_headers)
        status = client.get(f"/api/briefs/{BRIEF_ID}/pricing", headers=actuary_headers).json()["approval_status"]
        assert status["approved"] is False and status["stale"] is True
    finally:
        client.put(a_url, json={"assumptions": pricing_response["saved_assumptions"]}, headers=actuary_headers)
        client.delete(url, headers=actuary_headers)


def test_rating_plan_reproduces_the_indicated_premium(client, actuary_headers, pricing_response):
    r = client.get(f"/api/briefs/{BRIEF_ID}/rating-plan", headers=actuary_headers)
    assert r.status_code == 200, r.text
    plan = r.json()
    if not plan.get("available", True) or "base_rate" not in plan:
        pytest.skip("no rating plan for this brief")
    assert plan["base_rate"] * plan["off_balance"] == pytest.approx(plan["indicated_premium"], rel=1e-3)


@pytest.mark.parametrize("section", ["loss-development", "business-plan", "monitoring", "actuarial-memo",
                                     "rating-tests", "covered-claims", "parametric"])
def test_actuarial_sections_load(client, actuary_headers, section):
    r = client.get(f"/api/briefs/{BRIEF_ID}/{section}", headers=actuary_headers)
    assert r.status_code == 200, f"{section}: {r.text[:300]}"


@pytest.mark.parametrize("section", ["readiness", "guideline", "scenarios", "letters", "operations", "compliance",
                                     "launch-gate", "policy-form", "workflow", "verification"])
def test_claims_sections_load(client, claims_headers, section):
    r = client.get(f"/api/briefs/{BRIEF_ID}/{section}", headers=claims_headers)
    assert r.status_code == 200, f"{section}: {r.text[:300]}"
