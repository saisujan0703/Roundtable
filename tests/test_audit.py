"""backend.audit and its wiring in the API middleware."""
from __future__ import annotations

import json

import pytest

from backend import audit
from conftest import ACTUARY, BRIEF_ID, CLAIMS


# ---------------------------------------------------------------------------
# Unit
# ---------------------------------------------------------------------------
def test_redact_masks_secrets_at_any_depth():
    out = audit.redact({"email": "a@b.com", "password": "x", "nested": [{"api_key": "k", "Token": "t", "ok": 1}]})
    assert out == {"email": "a@b.com", "password": "***", "nested": [{"api_key": "***", "Token": "***", "ok": 1}]}


def test_long_strings_are_cut():
    out = audit.redact({"note": "a" * 2_000})
    assert len(out["note"]) < 600 and "more characters" in out["note"]


def test_describe_body_json_and_uploads():
    assert json.loads(audit.describe_body(b'{"b": 1, "a": 2}', "application/json")) == {"a": 2, "b": 1}
    assert audit.describe_body(b"\x00" * 2048, "multipart/form-data; boundary=x") == "[multipart/form-data body, 2,048 bytes]"
    assert audit.describe_body(b"{not json", "application/json") == "[unreadable JSON body]"
    assert audit.describe_body(b"", "application/json") is None


def test_brief_id_and_action_name():
    assert audit.brief_id_of("/api/briefs/76/actuarial/approval") == 76
    assert audit.brief_id_of("/api/briefs/76") == 76
    assert audit.brief_id_of("/api/actuarial/settings") is None

    def save_actuarial_settings():
        pass
    assert audit.action_name(save_actuarial_settings, "PUT", "/x") == "save actuarial settings"
    assert audit.action_name(None, "PUT", "/x") == "PUT /x"


# ---------------------------------------------------------------------------
# Through the API
# ---------------------------------------------------------------------------
pytestmark_api = pytest.mark.api


def _latest(client, headers, **params):
    r = client.get("/api/audit", params={"limit": 20, **params}, headers=headers)
    assert r.status_code == 200, r.text
    return r.json()["entries"]


@pytestmark_api
def test_a_change_is_recorded_with_who_and_what(client, actuary_headers):
    body = {"values": {"tax_rate_pct": 21.0}, "sources": {"tax_rate_pct": "US federal rate"}}
    assert client.put("/api/actuarial/settings", json=body, headers=actuary_headers).status_code == 200
    e = _latest(client, actuary_headers)[0]
    assert e["email"] == ACTUARY[0] and e["role"] == "Lead Actuary" and e["name"] == "Lead Actuary"
    assert e["action"] == "save actuarial settings" and e["status"] == 200 and e["brief_id"] is None
    assert json.loads(e["detail"]) == body
    assert e["at"].endswith("Z")


@pytestmark_api
def test_refused_change_is_recorded_too(client, actuary_headers):
    client.put("/api/actuarial/settings", json={"values": {"tax_rate_pct": 21.0}, "sources": {}}, headers=actuary_headers)
    e = _latest(client, actuary_headers)[0]
    assert e["status"] == 400 and e["action"] == "save actuarial settings"


@pytestmark_api
def test_role_denial_is_recorded(client, claims_headers):
    client.put("/api/actuarial/settings", json={"values": {}}, headers=claims_headers)
    e = _latest(client, claims_headers)[0]
    assert e["status"] == 403 and e["email"] == CLAIMS[0] and e["role"] == "Claims Lead"


@pytestmark_api
def test_sign_in_attempts_are_recorded_without_the_password(client, claims_headers):
    client.post("/api/auth/login", json={"email": "Nobody@Example.com", "password": "hunter2", "role": "Claims Lead"})
    e = _latest(client, claims_headers)[0]
    assert e["email"] == "nobody@example.com" and e["status"] == 401 and e["action"] == "auth login"
    assert "hunter2" not in (e["detail"] or "") and '"password": "***"' in e["detail"]


@pytestmark_api
def test_reads_are_not_recorded(client, actuary_headers):
    before = _latest(client, actuary_headers)[0]["id"]
    client.get("/api/actuarial/settings", headers=actuary_headers)
    client.get(f"/api/briefs/{BRIEF_ID}/pricing", headers=actuary_headers)
    assert _latest(client, actuary_headers)[0]["id"] == before


@pytestmark_api
def test_brief_log_and_filters(client, actuary_headers):
    url = f"/api/briefs/{BRIEF_ID}/actuarial/assumptions"
    saved = client.get(f"/api/briefs/{BRIEF_ID}/pricing", headers=actuary_headers).json()["saved_assumptions"]
    client.put(url, json={"assumptions": {"dev_method": "guess"}}, headers=actuary_headers)      # 400
    client.put(url, json={"assumptions": saved}, headers=actuary_headers)                         # 200
    entries = client.get(f"/api/briefs/{BRIEF_ID}/audit", headers=actuary_headers).json()["entries"]
    assert entries and all(e["brief_id"] == BRIEF_ID for e in entries)
    assert entries[0]["action"] == "save actuarial assumptions" and entries[0]["status"] == 200
    refused = client.get(f"/api/briefs/{BRIEF_ID}/audit", params={"outcome": "refused"}, headers=actuary_headers).json()
    assert refused["entries"] and all(e["status"] >= 400 for e in refused["entries"])
    mine = _latest(client, actuary_headers, email=ACTUARY[0].upper())
    assert mine and all(e["email"] == ACTUARY[0] for e in mine)


@pytestmark_api
def test_paging_and_missing_brief(client, actuary_headers):
    page1 = client.get("/api/audit", params={"limit": 2}, headers=actuary_headers).json()
    assert len(page1["entries"]) == 2 and page1["next_before_id"] == page1["entries"][-1]["id"]
    page2 = client.get("/api/audit", params={"limit": 2, "before_id": page1["next_before_id"]},
                       headers=actuary_headers).json()
    assert all(e["id"] < page1["next_before_id"] for e in page2["entries"])
    assert client.get("/api/briefs/999999/audit", headers=actuary_headers).status_code == 404


@pytestmark_api
def test_audit_log_needs_a_session(client):
    assert client.get("/api/audit").status_code == 401
