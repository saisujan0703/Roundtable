"""
India sources: curated Indian competitor and regulatory sources, Indian sites and framing in live research,
Library search and Market Radar, Indian names in the name check, and India as the competitor-scan default.
"""
from __future__ import annotations

import json
import sys
import types
from pathlib import Path

import pytest

from backend import competitor_landscape, evidence_sources, llm, market_radar, rag, verification

SOURCES = Path(__file__).resolve().parent.parent / "sources"
US_TERMS = ("NAIC", "NHTSA", "FAA", "Medicare", "Department of Insurance", "SERFF", "CFR", "NFPA")


def _load(name):
    return json.loads((SOURCES / name).read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Curated sources
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("name, key, title", [("competitors.json", "competitor_name", "product_name"),
                                              ("regulatory.json", "regulatory_body", "regulation_title")])
def test_curated_sources_are_indian_and_complete(name, key, title):
    items = _load(name)
    assert len(items) >= 8
    for i in items:
        text = json.dumps(i, ensure_ascii=False)
        assert i[key] and i[title] and len(i.get("summary") or i.get("coverage_summary")) > 150
        assert i["source_url"].startswith("https://") and i["date_collected"] == "2026-10-20"
        assert not any(t in text for t in US_TERMS), (i[key], [t for t in US_TERMS if t in text])


def test_regulators_cover_claims_products_motor_and_cyber():
    bodies = " ".join(i["regulatory_body"] + " " + i["regulation_title"] for i in _load("regulatory.json"))
    for expected in ("IRDAI", "Motor Vehicles Act", "Employee's Compensation Act", "AIS-156", "Drone Rules",
                     "CERT-In", "Digital Personal Data Protection"):
        assert expected in bodies


@pytest.mark.parametrize("query, kind, expected", [
    ("EV battery water ingress short circuit add-on", "competitor", ("Zurich Kotak", "ICICI Lombard", "Royal Sundaram")),
    ("engine hydrostatic lock flood waterlogging", "competitor", ("Tata AIG",)),
    ("surveyor claim settlement rejection Ombudsman", "regulatory", ("IRDAI",)),
    ("drone third party insurance", "regulatory", ("Ministry of Civil Aviation",)),
])
def test_retrieval_finds_indian_sources(query, kind, expected):
    hits = rag.retrieve_evidence(query, source_type=kind, n_results=3)
    assert hits and any(e in hits[0]["metadata"]["source_name"] for e in expected)


# ---------------------------------------------------------------------------
# Live research, Library search and Market Radar ask for Indian results
# ---------------------------------------------------------------------------
@pytest.fixture
def fake_tavily(monkeypatch):
    calls = []

    class Client:
        def __init__(self, api_key):
            pass

        def search(self, **params):
            calls.append(params)
            return {"results": []}

    monkeypatch.setitem(sys.modules, "tavily", types.SimpleNamespace(TavilyClient=Client))
    monkeypatch.setenv("TAVILY_API_KEY", "test-key")
    return calls


def test_live_research_searches_indian_sites(fake_tavily):
    llm._external_cache.clear()
    llm.generate_external_market_evidence("EV Battery Cover")
    # six searches, and the domain-restricted ones are retried on the open web when they come back empty
    assert len(fake_tavily) >= 6 and all("India" in c["query"] for c in fake_tavily)
    domains = {d for c in fake_tavily for d in c.get("include_domains", [])}
    assert {"irdai.gov.in", "icicilombard.com", "economictimes.indiatimes.com", "actuariesindia.org"} <= domains
    assert not domains & {"naic.org", "nhtsa.gov", "statefarm.com", "insurancejournal.com"}


@pytest.mark.parametrize("kind, word", [("competitor", "add-on"), ("regulatory", "IRDAI")])
def test_library_search_is_framed_for_india(fake_tavily, kind, word):
    evidence_sources.search_web("EV battery cover", kind, [])
    q = fake_tavily[-1]["query"]
    assert "India" in q and word in q and "NAIC" not in q


def test_market_radar_searches_indian_news(fake_tavily):
    topic = next(t for t in market_radar.WATCHLIST if t["id"] == "water_damage")
    market_radar.fetch_news(topic)
    assert fake_tavily[-1]["query"].endswith(" India") and "monsoon" in fake_tavily[-1]["query"]
    assert not any("catalytic" in t["query"] for t in market_radar.WATCHLIST)


# ---------------------------------------------------------------------------
# Name check and competitor-scan default
# ---------------------------------------------------------------------------
def test_unsourced_indian_insurer_is_flagged():
    issues = verification.check_names("HDFC ERGO already sells this add-on.", "Tata AIG Engine Secure", "s1")
    assert any("HDFC ERGO" in json.dumps(i) for i in issues)
    assert not verification.check_names("Tata AIG sells Engine Secure.", "Tata AIG Engine Secure", "s1")


def test_competitor_scan_defaults_to_india():
    assert competitor_landscape.DEFAULT_REGION == "IN"
    out = competitor_landscape.build("Gig cover", search=lambda p: [],
                                     llm=lambda *a: {"terms": ["gig"], "market": "personal"})
    assert out["region"] == "IN"
