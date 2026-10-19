"""backend.conflicts: favourable claims vs carriers withdrawing from or losing money on the cover."""
from __future__ import annotations

import pytest

from backend import conflicts


def _analytics(verdict="BUILD / ENDORSE", scope_lr=55.0):
    return {"summary": {"has_data": True},
            "recommendation": {"verdict": verdict, "finding": "Claims evidence supports a new coverage."},
            "loss_ratio": {"has_data": True, "scope_loss_ratio_pct": scope_lr, "earned_premium": 12_000_000},
            "coverage_gaps": {"gap_denial_rate_pct": 12.0}}


def _curated(summary, name="Acme Mutual"):
    return {"text": f"Competitor: {name}\nProduct: Gig driver endorsement\nSummary: {summary}",
            "metadata": {"source_name": name, "product_name": "Gig driver endorsement", "source_type": "competitor",
                         "source_url": "https://example.com/acme"}}


def _web(summary, name="Insurance Journal"):
    return {"source_name": name, "product_or_initiative_name": "Market update", "summary": summary,
            "url": "https://example.com/ij", "category": "articles", "is_insurance_related": True}


BRIEF = {"title": "Gig Delivery Driver Auto Liability Gap Coverage", "tag_value": None, "proxy_tags": []}
RISK = conflicts._risk_words(BRIEF)


@pytest.mark.parametrize("text,expected", [
    ("Acme withdrew its gig driver product in 2023 after heavy losses", "exit_and_losses"),
    ("The carrier discontinued the endorsement last year", "exit"),
    ("Several carriers exited the market", "exit"),
    ("We no longer offer this cover", "exit"),
    ("Loss ratio of 112% on delivery drivers", "losses"),
    ("Combined ratio above 115 for the programme", "losses"),
    ("The exit ramp was closed", None),
    ("Drivers who exit the vehicle are covered", None),
    ("Acme offers an optional endorsement", None),
])
def test_bad_experience_detection(text, expected):
    hit = conflicts._bad_experience(text)
    assert (hit[0] if hit else None) == expected


def test_favourable_claims_vs_withdrawal_after_losses_is_high():
    out = conflicts.check_market_experience(
        _analytics(), _analytics()["recommendation"], False,
        [_curated("Acme withdrew its gig delivery driver endorsement in 2023 after heavy losses on rideshare claims.")],
        [], RISK)
    assert len(out) == 1
    c = out[0]
    assert c["kind"] == "claims_vs_market_experience" and c["severity"] == "high"
    assert c["sides"][0]["label"] == "Claims data" and "55.0%" in c["sides"][0]["text"]
    assert "withdrew" in c["sides"][1]["text"] and c["sides"][1]["url"] == "https://example.com/acme"


def test_healthy_loss_ratio_alone_counts_as_favourable():
    a = _analytics(verdict="MONITOR", scope_lr=50.0)
    out = conflicts.check_market_experience(a, a["recommendation"], False,
                                            [_curated("Acme discontinued its delivery driver cover.")], [], RISK)
    assert out and out[0]["severity"] == "medium"


def test_no_conflict_when_claims_are_not_favourable():
    a = _analytics(verdict="MONITOR", scope_lr=92.0)
    out = conflicts.check_market_experience(a, a["recommendation"], False,
                                            [_curated("Acme withdrew the product after heavy losses.")], [], RISK)
    assert out == []


def test_no_conflict_without_bad_market_news():
    a = _analytics()
    out = conflicts.check_market_experience(a, a["recommendation"], False,
                                            [_curated("Acme sells an optional gig driver endorsement.")], [], RISK)
    assert out == []


def test_live_research_must_be_about_this_risk():
    a = _analytics()
    off_topic = _web("Insurer exited the market for coastal homeowners after hurricane losses.")
    on_topic = _web("Insurer exited the market for gig delivery drivers after mounting losses.", name="Carrier Mgmt")
    assert conflicts.check_market_experience(a, a["recommendation"], False, [], [off_topic], RISK) == []
    out = conflicts.check_market_experience(a, a["recommendation"], False, [], [on_topic], RISK)
    assert out and out[0]["sides"][1]["label"] == "Carrier Mgmt (live research)"


def test_proxy_claims_cap_severity_at_medium():
    a = _analytics()
    out = conflicts.check_market_experience(a, a["recommendation"], True,
                                            [_curated("Acme withdrew the gig product after heavy losses.")], [], RISK)
    assert out[0]["severity"] == "medium" and out[0]["sides"][0]["label"] == "Claims data (proxy patterns)"


def test_detect_conflicts_runs_the_check():
    brief = {**BRIEF, "claims_analytics": _analytics(), "analysis_basis": "direct", "external_market_evidence": []}
    found, checks = conflicts.detect_conflicts(
        brief, [_curated("Acme withdrew its gig driver endorsement after heavy losses.")])
    assert "favourable claims vs market withdrawals and losses" in checks
    assert any(c["kind"] == "claims_vs_market_experience" for c in found)


def test_ai_cross_check_gets_the_claims_outlook():
    brief = {**BRIEF, "claims_analytics": _analytics(), "analysis_basis": "direct"}
    sources = conflicts._cross_check_sources(brief, [])
    assert sources[0]["label"] == "Roundtable claims analysis (computed)" and "BUILD" in sources[0]["text"]
