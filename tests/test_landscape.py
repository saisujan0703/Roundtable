"""backend.competitor_landscape: search, extraction and quote verification, with a fake search and a fake LLM."""
from __future__ import annotations

import pytest

from backend import competitor_landscape as cl
from conftest import BRIEF_ID

ACME_PAGE = ("Acme Mutual sells a gig driver endorsement that fills the gap while you deliver. "
             "The Acme gig driver endorsement costs from $12 per month and is available in 38 states. "
             "It covers liability and collision while the app is on, with a $500 deductible.")
ZEN_PAGE = ("Zen Insurance offers rideshare and delivery driver coverage as an add-on to a personal auto policy. "
            "Our survey found the average delivery driver add-on adds $25 per month to a premium.")
RATING_PAGE = ("Acme Mutual has an NAIC complaint index of 0.42, well below the industry average of 1.00. "
               "AM Best rates Acme Mutual A+ (Superior) for financial strength.")


def fake_search(params):
    q = params["query"]
    if "NAIC" in q:
        return [{"url": "https://ratings.example.com/acme", "title": "Acme ratings", "raw_content": RATING_PAGE}]
    return [{"url": "https://acme.example.com/gig", "title": "Acme gig cover", "raw_content": ACME_PAGE},
            {"url": "https://compare.example.com/delivery", "title": "Best delivery cover", "content": ZEN_PAGE}]


def fake_llm(system, user, name, schema):
    if name == "report_terms":
        return {"terms": ["rideshare delivery driver", "gig driver endorsement"], "market": "personal"}
    if name == "report_verdicts":
        return {"verdicts": []}
    if name == "report_carriers":
        return {"carriers": [
            {"carrier": "Acme Mutual", "match": "exact", "facts": [
                {"field": "product_name", "value": "Gig driver endorsement", "source": 1,
                 "quote": "Acme Mutual sells a gig driver endorsement"},
                {"field": "price", "value": "$12 per month", "price_kind": "advertised", "source": 1,
                 "quote": "costs from $12 per month"},
                {"field": "states", "value": "38 states", "source": 1, "quote": "available in 38 states"},
                {"field": "limits_deductible", "value": "$500 deductible", "source": 1, "quote": "with a $500 deductible"},
                # invented: quote not on the page
                {"field": "exclusions", "value": "Excludes food spoilage", "source": 1, "quote": "excludes food spoilage"},
            ]},
            {"carrier": "Zen Insurance", "match": "variant", "facts": [
                {"field": "coverage", "value": "Delivery driver add-on", "source": 2,
                 "quote": "rideshare and delivery driver coverage as an add-on"},
                # number not in the quote: dropped
                {"field": "price", "value": "$19 per month", "price_kind": "average", "source": 2,
                 "quote": "adds $25 per month to a premium"},
            ]},
            # every fact unverifiable: the carrier is dropped
            # sells only a broader product: dropped even though the fact is on the page
            {"carrier": "Broad Co", "match": "general", "facts": [
                {"field": "coverage", "value": "Personal auto", "source": 2, "quote": "a personal auto policy"}]},
            {"carrier": "Ghost Co", "match": "exact", "facts": [{"field": "coverage", "value": "Everything", "source": 2,
                                               "quote": "Ghost Co covers everything"}]},
        ]}
    return {"ratings": [
        {"carrier": "Acme Mutual", "rating": "naic_complaint_index", "value": "0.42", "source": 3,
         "quote": "an NAIC complaint index of 0.42"},
        {"carrier": "Acme Mutual", "rating": "am_best", "value": "A+", "source": 3, "quote": "AM Best rates Acme Mutual A+"},
        {"carrier": "Acme Mutual", "rating": "jd_power", "value": "880 out of 1,000", "source": 3,
         "quote": "J.D. Power score 880"},   # not on the page
    ]}


def test_verified_needs_the_exact_quote_and_its_numbers():
    page = "The plan costs from $12 per month in most states."
    assert cl.verified("$12 per month", "costs from $12 per month", page)
    assert cl.verified("$12 per month", "Costs   from $12 per month.", page)      # case and spacing don't matter
    assert not cl.verified("$15 per month", "costs from $12 per month", page)     # number not in the quote
    assert not cl.verified("$12 per month", "costs only $12 per month", page)     # quote not on the page
    assert not cl.verified("cheap", "costs", page)                                # quote too short


def test_build_keeps_only_verified_facts():
    out = cl.build("Gig Delivery Driver Auto Liability Gap Coverage", search=fake_search, llm=fake_llm, region="US")
    assert out["configured"] and out["ai_extraction"]
    by = {c["carrier"]: c for c in out["carriers"]}
    assert set(by) == {"Acme Mutual", "Zen Insurance"}                 # Ghost Co had nothing verifiable
    acme, zen = by["Acme Mutual"], by["Zen Insurance"]
    assert acme["price"] == {"value": "$12 per month", "kind": "advertised", "url": "https://acme.example.com/gig",
                             "site": "acme.example.com", "source_kind": "carrier website"}
    assert acme["states"] == "38 states" and acme["limits_deductible"] == "$500 deductible"
    assert acme["exclusions"] is None                                   # invented quote dropped
    assert zen["price"] is None and zen["coverage"] == "Delivery driver add-on"
    ratings = {r["rating"]: r["value"] for r in acme["ratings"]}
    assert ratings == {"naic_complaint_index": "0.42", "am_best": "A+"}  # unverifiable J.D. Power score dropped
    cited = {s["url"] for s in out["sources"] if s["cited"]}
    assert "https://ratings.example.com/acme" in cited
    assert out["searches"] == 4 + 2          # carrier sites, open web, price, comparison sites + 1 per rated carrier
    assert out["terms"] == ["rideshare delivery driver", "gig driver endorsement"] and out["market"] == "personal"
    assert acme["match"] == "exact" and acme["carrier_site"] and not zen["carrier_site"]
    assert [c["carrier"] for c in out["carriers"]] == ["Acme Mutual", "Zen Insurance"]   # exact + own site first


def test_without_llm_lists_named_carriers_only():
    def no_llm(*a, **k):
        raise RuntimeError("no provider")

    def search(params):
        return [{"url": "https://news.example.com/x", "title": "x",
                 "raw_content": "Progressive and GEICO both sell rideshare cover for delivery drivers in most states."}]
    out = cl.build("Gig driver cover", search=search, llm=no_llm, region="US")
    assert not out["ai_extraction"]
    names = {c["carrier"] for c in out["carriers"]}
    assert {"Progressive", "GEICO"} <= names
    assert all(c["price"] is None and not c["evidence"] for c in out["carriers"])
    assert any("No AI extraction" in n for n in out["notes"])


def test_no_published_price_is_explained():
    def llm(system, user, name, schema):
        if name == "report_carriers":
            return {"carriers": [{"carrier": "Acme Mutual", "match": "exact", "facts": [
                {"field": "product_name", "value": "Gig driver endorsement", "source": 1,
                 "quote": "Acme Mutual sells a gig driver endorsement"}]}]}
        return {"ratings": []}
    out = cl.build("Gig cover", search=fake_search, llm=llm, region="US")
    assert any("No published price" in n for n in out["notes"])


def test_search_off_without_a_key(monkeypatch):
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)
    out = cl.build("Gig cover")
    assert out["configured"] is False and "TAVILY_API_KEY" in out["message"]


# ---------------------------------------------------------------------------
# API
# ---------------------------------------------------------------------------
@pytest.mark.api
def test_landscape_api_stores_and_returns(client, claims_headers, actuary_headers, monkeypatch):
    url = f"/api/briefs/{BRIEF_ID}/competitor-landscape"
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)
    r = client.post(url, headers=claims_headers)
    assert r.status_code == 400 and "TAVILY_API_KEY" in r.json()["detail"]

    monkeypatch.setattr(cl, "build", lambda title, context="", region="US":
                        _real_build(title, context, fake_search, fake_llm, region=region))
    for headers in (claims_headers, actuary_headers):          # both workspaces may refresh it
        r = client.post(url, headers=headers)
        assert r.status_code == 200, r.text
    r = client.post(url, json={"region": "IN"}, headers=claims_headers)
    assert r.status_code == 200 and r.json()["landscape"]["region"] == "IN"
    assert client.post(url, json={"region": "XX"}, headers=claims_headers).status_code == 422
    got = client.get(url, headers=claims_headers).json()
    assert got["regions"]["IN"] == "India"
    assert {c["carrier"] for c in got["landscape"]["carriers"]} == {"Acme Mutual", "Zen Insurance"}
    assert client.get("/api/briefs/999999/competitor-landscape", headers=claims_headers).status_code == 404


_real_build = cl.build


def test_searches_use_the_market_terms_and_skip_comparison_sites_for_commercial_cover():
    queries = []

    def search(params):
        queries.append(params)
        return []

    def llm(system, user, name, schema):
        assert name == "report_terms" and "supply chain" in user.lower()
        return {"terms": ["contingent business interruption", "supply chain insurance"], "market": "commercial"}
    cl.build("Commercial Supply Chain Disruption Cover", "Factories lose income when a supplier stops", search, llm, region="US")
    assert queries[0]["query"] == "contingent business interruption insurance"
    assert queries[0]["include_domains"] == cl.CARRIER_SITES
    assert not any(q.get("include_domains") == cl.COMPARISON_SITES for q in queries)


def test_carrier_site_fact_replaces_a_third_party_one():
    filler = " Read our full guide to rideshare and delivery driver insurance before you buy a policy."
    third = "Comparison: Acme Mutual charges about $30 per month for gig cover." + filler
    own = "Acme Mutual gig cover starts at $12 per month." + filler

    def search(params):
        return [{"url": "https://compare.example.com/a", "title": "c", "raw_content": third},
                {"url": "https://www.acmemutual.com/gig", "title": "o", "raw_content": own}]

    def llm(system, user, name, schema):
        if name == "report_terms":
            raise RuntimeError("no terms")       # falls back to the title
        if name == "report_ratings":
            return {"ratings": []}
        return {"carriers": [{"carrier": "Acme Mutual", "match": "exact", "facts": [
            {"field": "price", "value": "$30 per month", "price_kind": "average", "source": 1,
             "quote": "Acme Mutual charges about $30 per month"},
            {"field": "price", "value": "$12 per month", "price_kind": "advertised", "source": 2,
             "quote": "gig cover starts at $12 per month"}]}]}
    out = cl.build("Gig cover", search=search, llm=llm, region="US")
    price = out["carriers"][0]["price"]
    assert price["value"] == "$12 per month" and price["source_kind"] == "carrier website"
    assert out["terms"] == ["Gig"]


def test_india_market_uses_indian_insurers_and_irdai_ratings():
    queries, prompts = [], []
    page = ("HDFC ERGO offers a cyber insurance policy for individuals, available across India. "
            "The plan starts at ₹2,499 p.a. for a sum insured of ₹1 lakh.")
    rating_page = "HDFC ERGO reported a claim settlement ratio of 99.2% in FY2024-25, according to IRDAI data."

    def search(params):
        queries.append(params)
        if "claim settlement" in params["query"]:
            return [{"url": "https://www.policybazaar.com/hdfc-ergo/", "title": "r", "raw_content": rating_page}]
        return [{"url": "https://www.hdfcergo.com/cyber", "title": "p", "raw_content": page}]

    def llm(system, user, name, schema):
        prompts.append((name, system, user))
        if name == "report_terms":
            return {"terms": ["personal cyber insurance"], "market": "personal"}
        if name == "report_carriers":
            return {"carriers": [{"carrier": "HDFC ERGO", "match": "exact", "facts": [
                {"field": "product_name", "value": "Cyber insurance policy", "source": 1,
                 "quote": "HDFC ERGO offers a cyber insurance policy"},
                {"field": "price", "value": "₹2,499 p.a.", "price_kind": "advertised", "source": 1,
                 "quote": "starts at ₹2,499 p.a."}]}]}
        if name == "report_ratings":
            return {"ratings": [{"carrier": "HDFC ERGO", "rating": "claim_settlement_ratio", "value": "99.2% (FY2024-25)",
                                 "source": 2, "quote": "a claim settlement ratio of 99.2% in FY2024-25"}]}
        return {"verdicts": []}

    out = cl.build("Personal Cyber Insurance", search=search, llm=llm, region="IN")
    assert out["region"] == "IN" and out["region_label"] == "India"
    assert queries[0]["include_domains"] == cl.IN_CARRIER_SITES and queries[0]["query"].endswith(" in India")
    assert any(q.get("include_domains") == cl.REGIONS["IN"]["comparison"] for q in queries)   # Policybazaar etc.
    ratings_prompt = next(p for n, p, u in prompts if n == "report_ratings")
    assert "claim_settlement_ratio" in ratings_prompt and "naic_complaint_index" not in ratings_prompt
    assert "<market>India" in next(u for n, p, u in prompts if n == "report_carriers")
    hdfc = out["carriers"][0]
    assert hdfc["price"]["value"] == "₹2,499 p.a." and hdfc["carrier_site"]
    assert [r["label"] for r in hdfc["ratings"]] == ["Claim settlement ratio"]


def test_unknown_region_falls_back_to_india():
    out = cl.build("Gig cover", search=lambda p: [], llm=lambda *a: {"terms": ["gig"], "market": "personal"},
                   region="MARS")
    assert out["region"] == "IN"
