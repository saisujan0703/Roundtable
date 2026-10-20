"""Custom risk patterns (backend.risk_patterns) and user-added sources (backend.evidence_sources)."""
from __future__ import annotations

import pytest

from backend import risk_patterns


# ---------------------------------------------------------------------------
# Risk patterns: unit
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("fields,message", [
    ({"label": "x", "keywords": ["fire"]}, "name"),
    ({"label": "Fire", "keywords": []}, "keyword"),
    ({"label": "Fire", "keywords": ["ab"]}, "too short"),
    ({"label": "Fire", "keywords": ["fire"], "products": ["Boats"]}, "Unknown product"),
])
def test_pattern_validation(fields, message):
    with pytest.raises(risk_patterns.PatternError, match=message):
        risk_patterns.clean(fields["label"], fields["keywords"], fields.get("products"))


def test_keywords_are_normalised_and_deduplicated():
    out = risk_patterns.clean("  E-bike fire ", ["E-Bike", "e-bike", "  lithium   battery "], ["PersonalAuto"])
    assert out == {"label": "E-bike fire", "keywords": ["e-bike", "lithium battery"], "products": ["PersonalAuto"],
                   "description": ""}


def test_regex_matches_at_word_start_and_across_separators():
    rx = risk_patterns.regex(["flood", "e-bike"])
    assert rx.search("Basement flooding after storm")
    assert rx.search("E bike charger fire") and rx.search("e_bike") and rx.search("E-BIKE")
    assert not rx.search("webike") and not rx.search("antiflood")


def test_slug():
    assert risk_patterns.slug("E-bike & Scooter Fire!") == "custom_e_bike_scooter_fire"


# ---------------------------------------------------------------------------
# Risk patterns: through the API and analytics
# ---------------------------------------------------------------------------
BATTERY = {"label": "Auto battery (keyword)", "keywords": ["high-voltage battery"], "products": ["PersonalAuto", "BusinessAuto"],
           "description": "test"}


@pytest.fixture(scope="module")
def battery_pattern(client, actuary_headers):
    r = client.post("/api/risk-patterns", json=BATTERY, headers=actuary_headers)
    assert r.status_code == 201, r.text
    yield r.json()
    client.delete(f"/api/risk-patterns/{r.json()['key']}", headers=actuary_headers)


@pytest.mark.api
def test_preview_shows_what_keywords_catch(client, claims_headers):
    r = client.post("/api/risk-patterns/preview", json={"keywords": ["high-voltage battery"]}, headers=claims_headers)
    assert r.status_code == 200, r.text
    p = r.json()
    assert p["claims"] > 0 and p["samples"] and all("battery" in (s["description"] or "").lower() for s in p["samples"])
    bad = client.post("/api/risk-patterns/preview", json={"keywords": ["ab"]}, headers=claims_headers)
    assert bad.status_code == 400


@pytest.mark.api
def test_custom_pattern_is_a_usable_tag(client, claims_headers, battery_pattern):
    key = battery_pattern["key"]
    assert key.startswith("custom_") and battery_pattern["created_by"] == "Lead Actuary"
    assert key in client.get("/api/tags", headers=claims_headers).json()
    listed = {p["key"]: p for p in client.get("/api/risk-patterns", headers=claims_headers).json()["patterns"]}
    assert listed[key]["claims"] > 0


@pytest.mark.api
def test_custom_pattern_drives_the_analytics(battery_pattern):
    from backend import analytics
    custom = analytics.get_claims_summary_stats(battery_pattern["key"])
    builtin = analytics.get_claims_summary_stats("battery_fault")
    # in this data every auto claim mentioning 'battery' is tagged battery_fault, so the two must agree
    assert custom["has_data"] and custom["tag_count"] == builtin["tag_count"] > 0
    assert custom["incurred_loss"] == builtin["incurred_loss"]
    pooled = analytics.get_tag_scope(f"{battery_pattern['key']}+vehiclefire")
    assert pooled["has_data"]


@pytest.mark.api
def test_title_finds_the_custom_pattern(battery_pattern):
    from backend.llm import resolve_risk_tag_with_confidence
    tag, conf = resolve_risk_tag_with_confidence("Auto battery (keyword) top-up cover")
    assert tag == battery_pattern["key"] and conf >= 0.5


@pytest.mark.api
def test_edit_and_refused_delete_while_in_use(client, actuary_headers, battery_pattern, test_db):
    key = battery_pattern["key"]
    r = client.put(f"/api/risk-patterns/{key}", json={**BATTERY, "keywords": ["high-voltage battery", "charging"]},
                   headers=actuary_headers)
    assert r.status_code == 200 and r.json()["keywords"] == ["high-voltage battery", "charging"]
    from backend.database import get_connection
    with get_connection() as conn:
        bid = conn.execute("INSERT INTO briefs (title, tag_value, claims_finding_text, claims_status, created_at, brief_json) "
                           "VALUES ('t', ?, '', 'draft', '2026-01-01', '{}')", (key,)).lastrowid
    try:
        r = client.delete(f"/api/risk-patterns/{key}", headers=actuary_headers)
        assert r.status_code == 409 and f"#{bid}" in r.json()["detail"]
    finally:
        with get_connection() as conn:
            conn.execute("DELETE FROM briefs WHERE id = ?", (bid,))
    assert client.put("/api/risk-patterns/custom_nope", json=BATTERY, headers=actuary_headers).status_code == 404


# ---------------------------------------------------------------------------
# Sources
# ---------------------------------------------------------------------------
SOURCE = {"source_type": "competitor", "name": "Zebra Mutual", "title": "Quokka e-scooter theft endorsement",
          "summary": "Zebra Mutual sells a quokka e-scooter theft endorsement covering scooters stolen from a locked rack.",
          "url": "https://example.com/zebra/quokka", "date_collected": "2026-10-01"}


@pytest.mark.api
@pytest.mark.parametrize("change,message", [
    ({"url": "example.com/x"}, "web address"), ({"summary": "too short"}, "Summarise"), ({"name": " "}, "Name the"),
])
def test_source_validation(client, claims_headers, change, message):
    r = client.post("/api/sources", json={**SOURCE, **change}, headers=claims_headers)
    assert r.status_code == 400 and message in r.json()["detail"]


@pytest.mark.api
def test_added_source_becomes_citable_evidence(client, claims_headers):
    r = client.post("/api/sources", json=SOURCE, headers=claims_headers)
    assert r.status_code == 201, r.text
    sid = r.json()["id"]
    try:
        assert client.post("/api/sources", json=SOURCE, headers=claims_headers).status_code == 400   # duplicate
        from backend import rag, verification
        hits = rag.retrieve_evidence("quokka scooter theft", source_type="competitor")
        assert hits and hits[0]["metadata"]["source_url"] == SOURCE["url"]
        assert "Zebra Mutual" in verification._known_names()
        listing = client.get("/api/sources", headers=claims_headers).json()
        assert any(s["id"] == sid for s in listing["added"]) and len(listing["builtin"]) == 18

        r = client.put(f"/api/sources/{sid}", json={**SOURCE, "title": "Quokka endorsement v2"}, headers=claims_headers)
        assert r.status_code == 200 and r.json()["title"] == "Quokka endorsement v2"
    finally:
        assert client.delete(f"/api/sources/{sid}", headers=claims_headers).status_code == 200
    from backend import rag
    assert not any(h["metadata"]["source_url"] == SOURCE["url"]
                   for h in rag.retrieve_evidence("quokka scooter theft", source_type="competitor"))
    assert client.delete(f"/api/sources/{sid}", headers=claims_headers).status_code == 404


@pytest.mark.api
def test_web_search_without_a_key_says_so(client, claims_headers, monkeypatch):
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)
    r = client.post("/api/sources/search", json={"query": "ev battery cover", "source_type": "competitor"},
                    headers=claims_headers)
    assert r.status_code == 200 and r.json()["configured"] is False


# ---------------------------------------------------------------------------
# The claims cache survives writes that don't touch claims
# ---------------------------------------------------------------------------
@pytest.mark.api
def test_claims_cache_key_ignores_unrelated_writes(client, actuary_headers):
    from backend import analytics
    before = analytics._db_version()
    client.put("/api/actuarial/settings", json={"values": {"tax_rate_pct": 21.0},
                                               "sources": {"tax_rate_pct": "US federal rate"}}, headers=actuary_headers)
    assert analytics._db_version() == before
