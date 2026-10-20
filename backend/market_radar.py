"""
Market Radar: always-on news watch that proposes product opportunities, with proof.

On a schedule (and on demand) Roundtable searches recent news for each watched risk topic, then checks
the headlines against evidence it can actually verify:

Topics come from three places: a watchlist of known risks, auto-discovery (broad insurance-news searches
whose hits are matched to any claims pattern), and free-text topics a user asks to scan.

1. News attention   - distinct publishers covering the topic in the last 30 days (Tavily news search)
2. Claims momentum  - fitted frequency trend and last-12-month claim growth for the matching risk tag
3. Coverage gap     - share of the tag's claims denied for reasons that signal unmet demand
4. Competitor gap   - curated competitor sources that exclude or limit the cover

Every number and the score are computed here in Python; an LLM (if configured) only writes the
headline and rationale from those facts, and may cite only the articles it was given. A signal is
a suggestion: turning it into a decision brief, and any launch, stays with people.
"""
from __future__ import annotations

import html
import json
import os
import re
import threading
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from backend import analytics, rag, verification
from backend.database import get_connection
from backend.llm import TAG_SEMANTIC_MAP, resolve_risk_tag_with_confidence

NEWS_DAYS = 30
NEWS_PER_TOPIC = 8
RESURFACE_POINTS = 15  # a dismissed signal comes back only if its score rises this much

# Risk topics watched on every scan: news query, the claims pattern it maps to, and the product idea.
# Roundtable serves the Indian market: queries use Indian framing and every search adds NEWS_MARKET.
NEWS_MARKET = "India"
WATCHLIST: List[Dict[str, str]] = [
    {"id": "ev_battery_fire", "label": "EV battery fires", "tag": "battery_fault",
     "query": "electric scooter EV battery fire explosion",
     "idea": "EV Battery Fire & Thermal Runaway Cover"},
    {"id": "vehicle_theft", "label": "Vehicle theft wave", "tag": "theftentire",
     "query": "vehicle theft cases rise cars two-wheelers stolen", "idea": "Stolen Vehicle Replacement Cover"},
    {"id": "parts_theft", "label": "Vehicle parts & battery theft", "tag": "theftparts",
     "query": "car parts battery theft stolen from parked vehicles", "idea": "Vehicle Parts Theft Cover"},
    {"id": "water_damage", "label": "Monsoon flooding & home water damage", "tag": "waterdamage",
     "query": "monsoon flooding waterlogging water damage homes", "idea": "Home Water Damage Rider"},
    {"id": "vehicle_flood", "label": "Flooded vehicles", "tag": "vehicleflood",
     "query": "cars submerged flood waterlogging vehicles damaged", "idea": "Vehicle Flood Damage Cover"},
    {"id": "hail", "label": "Hailstorms", "tag": "hail",
     "query": "hailstorm damage cars homes", "idea": "Hail Damage Cover"},
    {"id": "mold", "label": "Seepage, dampness & mould", "tag": "mold",
     "query": "seepage dampness mold damage homes monsoon", "idea": "Home Seepage & Mould Cover"},
    {"id": "workplace_strain", "label": "Workplace strain injuries", "tag": "strain",
     "query": "workplace injuries factory workers accidents rising", "idea": "Workplace Injury Cover"},
]

# Broad searches that discover risks nobody put on the watchlist; hits are mapped to claims patterns
DISCOVERY_QUERIES = [
    "insurance claims surge rising losses",
    "insurers stop covering exclude new risk",
    "spike in incidents damage injuries reported this month",
    "insurance gap uninsured losses homes vehicles",
]
DISCOVERY_MIN_PUBLISHERS = 2
MAX_DISCOVERED = 4

# Readable names for claims patterns surfaced by discovery
TAG_LABELS = {
    "animalcollision": ("Animal collisions", "Animal Collision Vehicle Cover"),
    "burglary": ("Home burglaries", "Home Burglary Cover"),
    "fire": ("Property fires", "Property Fire Cover"),
    "glassbreakage": ("Glass breakage", "Glass Breakage Cover"),
    "rearend": ("Rear-end collisions", "Rear-End Collision Cover"),
    "rollover": ("Vehicle rollovers", "Rollover Accident Cover"),
    "slipfall": ("Slip-and-fall injuries", "Slip & Fall Liability Cover"),
    "vehcollision": ("Vehicle collisions", "Collision Damage Cover"),
    "vehiclefire": ("Vehicle fires", "Vehicle Fire Cover"),
    "vehiclehail": ("Hail-damaged vehicles", "Vehicle Hail Cover"),
    "wind": ("Windstorms", "Windstorm Damage Cover"),
    "workplace_fall": ("Workplace falls", "Workplace Fall Injury Cover"),
}

# Low-signal sites: social media, headline recyclers and market-report sellers
_EXCLUDED_DOMAINS = ["facebook.com", "instagram.com", "tiktok.com", "youtube.com", "x.com", "twitter.com",
                     "threads.net", "pinterest.com", "quora.com", "reddit.com", "linkedin.com", "openpr.com",
                     "globenewswire.com", "marketresearchfuture.com", "grandviewresearch.com"]
# An article must mention a loss, hazard or insurance to count as evidence
_RISK_WORDS = ("insur", "claim", "damage", "loss", "risk", "fire", "theft", "stolen", "injur", "accident", "crash",
               "flood", "storm", "hazard", "liabil", "coverage", "premium", "lawsuit", "explo", "collapse", "recall",
               "burglar", "vandal", "leak", "mold", "hail", "wind", "death", "killed", "fraud", "cyber", "breach")
_EXCLUSION_WORDS = ("not cover", "does not cover", "doesn't cover", "exclud", "excluded", "gap", "not include",
                    "outside", "limited to", "consumable")

_scan_lock = threading.Lock()
_scheduler_started = False


# ---------------------------------------------------------------------------
# Storage
# ---------------------------------------------------------------------------
def init_radar_tables() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS market_signals (
                topic_id TEXT PRIMARY KEY,
                label TEXT NOT NULL,
                tag_value TEXT,
                product_idea TEXT NOT NULL,
                score INTEGER NOT NULL,
                recommendation TEXT NOT NULL,
                headline TEXT NOT NULL,
                rationale TEXT NOT NULL,
                risks TEXT NOT NULL DEFAULT '[]',
                components TEXT NOT NULL,
                evidence TEXT NOT NULL,
                articles TEXT NOT NULL,
                generation_method TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'new',
                dismissed_score INTEGER,
                brief_id INTEGER,
                first_seen TEXT NOT NULL,
                scanned_at TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS market_radar_runs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                started_at TEXT NOT NULL,
                finished_at TEXT,
                trigger TEXT NOT NULL,
                status TEXT NOT NULL,
                message TEXT
            )
        """)
        # A run still "running" at startup was cut off by a restart
        conn.execute("UPDATE market_radar_runs SET status = 'interrupted', message = 'Stopped by a server restart.' "
                     "WHERE status = 'running'")


def _row_to_signal(row) -> Dict[str, Any]:
    d = dict(row)
    for key in ("risks", "components", "evidence", "articles"):
        d[key] = json.loads(d[key] or "[]")
    return d


def list_signals(include_dismissed: bool = False) -> Dict[str, Any]:
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM market_signals ORDER BY score DESC, scanned_at DESC").fetchall()
        last = conn.execute("SELECT * FROM market_radar_runs ORDER BY id DESC LIMIT 1").fetchone()
    signals = [_row_to_signal(r) for r in rows]
    if not include_dismissed:
        signals = [s for s in signals if s["status"] != "dismissed"]
    return {"signals": signals, "last_run": dict(last) if last else None, "scanning": _scan_lock.locked(),
            "watchlist": [{"id": t["id"], "label": t["label"]} for t in WATCHLIST],
            "discovery_queries": DISCOVERY_QUERIES,
            "news_configured": _tavily_key() is not None}


def get_signal(topic_id: str) -> Optional[Dict[str, Any]]:
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM market_signals WHERE topic_id = ?", (topic_id,)).fetchone()
    return _row_to_signal(row) if row else None


def set_status(topic_id: str, status: str, brief_id: Optional[int] = None) -> Optional[Dict[str, Any]]:
    with get_connection() as conn:
        if status == "dismissed":
            conn.execute("UPDATE market_signals SET status = 'dismissed', dismissed_score = score WHERE topic_id = ?",
                         (topic_id,))
        else:
            conn.execute("UPDATE market_signals SET status = ?, brief_id = COALESCE(?, brief_id) WHERE topic_id = ?",
                         (status, brief_id, topic_id))
    return get_signal(topic_id)


def _save_signal(sig: Dict[str, Any]) -> None:
    now = datetime.utcnow().isoformat()
    with get_connection() as conn:
        old = conn.execute("SELECT status, dismissed_score, first_seen FROM market_signals WHERE topic_id = ?",
                           (sig["topic_id"],)).fetchone()
        status = "new"
        if old:
            status = old["status"]
            if status == "dismissed" and sig["score"] >= (old["dismissed_score"] or 0) + RESURFACE_POINTS:
                status = "new"  # the story grew materially since it was dismissed
        conn.execute("""
            INSERT INTO market_signals (topic_id, label, tag_value, product_idea, score, recommendation, headline,
                rationale, risks, components, evidence, articles, generation_method, status, first_seen, scanned_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(topic_id) DO UPDATE SET label = excluded.label, tag_value = excluded.tag_value,
                product_idea = excluded.product_idea, score = excluded.score,
                recommendation = excluded.recommendation, headline = excluded.headline,
                rationale = excluded.rationale, risks = excluded.risks, components = excluded.components,
                evidence = excluded.evidence, articles = excluded.articles,
                generation_method = excluded.generation_method, status = excluded.status,
                scanned_at = excluded.scanned_at
        """, (sig["topic_id"], sig["label"], sig["tag_value"], sig["product_idea"], sig["score"],
              sig["recommendation"], sig["headline"], sig["rationale"], json.dumps(sig["risks"]),
              json.dumps(sig["components"]), json.dumps(sig["evidence"]), json.dumps(sig["articles"]),
              sig["generation_method"], status, old["first_seen"] if old else now, now))


# ---------------------------------------------------------------------------
# 1. News
# ---------------------------------------------------------------------------
def _tavily_key() -> Optional[str]:
    key = (os.environ.get("TAVILY_API_KEY") or "").strip()
    return key if key and key != "your_tavily_api_key_here" else None


def _domain(url: str) -> str:
    netloc = urllib.parse.urlparse(url).netloc.lower()
    return netloc[4:] if netloc.startswith("www.") else netloc


def _keywords(topic: Dict[str, str]) -> List[str]:
    words = [w for w in re.findall(r"[a-z][a-z\-]{2,}", topic["query"].lower())
             if w not in {"the", "and", "from", "after", "rising", "surge", "homes", "cars", "damage", "damaged"}]
    return list(dict.fromkeys(words + TAG_SEMANTIC_MAP.get(topic.get("tag") or "", [])))


def fetch_news(topic: Dict[str, str]) -> List[Dict[str, Any]]:
    """Recent news articles for the topic: deduplicated by URL and headline, filtered for relevance."""
    from tavily import TavilyClient

    client = TavilyClient(api_key=_tavily_key())
    response = client.search(query=f"{topic['query']} {NEWS_MARKET}", topic="news", days=NEWS_DAYS, max_results=NEWS_PER_TOPIC,
                             search_depth="basic", include_answer=False, exclude_domains=_EXCLUDED_DOMAINS,
                             timeout=20)
    keywords = _keywords(topic)
    seen_urls, seen_titles, out = set(), set(), []
    for res in (response.get("results", []) if isinstance(response, dict) else []):
        url = (res.get("url") or "").strip()
        title = html.unescape(res.get("title") or "").strip()
        content = html.unescape(res.get("content") or "").strip()
        norm_title = re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()
        if not url.startswith("http") or url in seen_urls or (norm_title and norm_title in seen_titles):
            continue
        text = f"{title} {content}".lower()
        if not any(k in text for k in keywords):
            continue  # off-topic hit
        if not any(w in text for w in _RISK_WORDS):
            continue  # on-topic but not about a loss or insurance (e.g. property listings)
        seen_urls.add(url)
        seen_titles.add(norm_title)
        snippet = content if len(content) <= 320 else content[:317].rsplit(" ", 1)[0] + "..."
        out.append({"title": title or url, "url": url, "source": _domain(url),
                    "published": (res.get("published_date") or "")[:16], "snippet": snippet})
    return out


# ---------------------------------------------------------------------------
# 2-4. Evidence and score
# ---------------------------------------------------------------------------
def _claims_evidence(tag: Optional[str]) -> Dict[str, Any]:
    if not tag or tag not in analytics.list_tags():
        return {"has_data": False, "narrative": "No matching claims pattern in our data, so the headlines can't be "
                                                "checked against our own losses."}
    trend = analytics.fit_frequency_trend(tag)
    emerging = analytics.get_emerging_signals(tag)
    gap = analytics.get_coverage_gap_signals(tag)
    stats = analytics.get_claims_summary_stats(tag)
    return {
        "has_data": True, "tag_value": tag,
        "claims": gap.get("claims"),
        "annual_trend_pct": trend.get("annual_trend_pct"), "trend_significant": trend.get("significant", False),
        "trend_narrative": trend.get("narrative"),
        "last_12m_claims": emerging.get("last_12m_claims"), "prior_12m_claims": emerging.get("prior_12m_claims"),
        "last_12m_vs_prior_pct": emerging.get("last_12m_vs_prior_pct"),
        "gap_denial_rate_pct": gap.get("gap_denial_rate_pct"), "gap_denials": gap.get("gap_denials"),
        "gap_denial_estimated_loss": gap.get("gap_denial_estimated_loss"),
        "baseline_denial_rate_pct": gap.get("baseline_denial_rate_pct"),
        "avg_severity": stats.get("avg_severity") if isinstance(stats, dict) else None,
    }


def _market_evidence(topic: Dict[str, str]) -> Dict[str, Any]:
    query = f"{topic['label']} {topic['idea']} {topic['query']}"
    def _pack(hits):
        return [{"source": h["metadata"].get("source_name") or h["metadata"].get("regulatory_body") or "Source",
                 "title": h["metadata"].get("product_name") or h["metadata"].get("regulation_title") or "",
                 "url": h["metadata"].get("source_url"),
                 "excludes_cover": any(w in h["text"].lower() for w in _EXCLUSION_WORDS)}
                for h in hits]
    return {"competitors": _pack(rag.retrieve_evidence(query, source_type="competitor", n_results=3, min_score=1.0)),
            "regulatory": _pack(rag.retrieve_evidence(query, source_type="regulatory", n_results=2, min_score=1.0))}


def _clamp(x: float, hi: float) -> float:
    return max(0.0, min(hi, x))


def score_signal(articles: List[Dict[str, Any]], claims: Dict[str, Any], market: Dict[str, Any]) -> Dict[str, Any]:
    """Deterministic 0-100 opportunity score and recommendation; each component says why it scored."""
    publishers = len({a["source"] for a in articles})
    news = round(_clamp(publishers / 8 * 25, 25))
    comps = [{"name": "News attention", "points": news, "max": 25,
              "why": f"{publishers} distinct publisher(s) in the last {NEWS_DAYS} days."}]

    if claims["has_data"]:
        t = claims["annual_trend_pct"] or 0
        g12 = claims["last_12m_vs_prior_pct"] or 0
        trend_pts = _clamp(t, 20) / 20 * (20 if claims["trend_significant"] else 10)
        momentum = round(trend_pts + _clamp(g12, 60) / 60 * 10)
        comps.append({"name": "Claims momentum", "points": momentum, "max": 30,
                      "why": f"Frequency trend {t:+.1f}%/yr ({'significant' if claims['trend_significant'] else 'not significant'}); "
                             f"last 12 months {g12:+.1f}% vs the prior 12."})
        gap_rate = claims["gap_denial_rate_pct"] or 0
        gap = round(_clamp(gap_rate, 30) / 30 * 30)
        comps.append({"name": "Coverage gap", "points": gap, "max": 30,
                      "why": f"{gap_rate:.1f}% of these claims were denied for reasons that signal unmet demand "
                             f"({claims['gap_denials'] or 0} claims)."})
    else:
        momentum = gap = 0
        comps.append({"name": "Claims momentum", "points": 0, "max": 30, "why": claims["narrative"]})
        comps.append({"name": "Coverage gap", "points": 0, "max": 30, "why": "No claims pattern to measure."})

    comp_hits = market["competitors"]
    excluding = [c for c in comp_hits if c["excludes_cover"]]
    competitor = 15 if excluding else (5 if comp_hits else 7)
    comps.append({"name": "Competitor gap", "points": competitor, "max": 15,
                  "why": (f"{len(excluding)} competitor source(s) exclude or limit this cover." if excluding else
                          f"{len(comp_hits)} competitor source(s) found; none show an exclusion." if comp_hits else
                          "No competitor source on file; unknown.")})

    total = sum(c["points"] for c in comps)
    rising = claims["has_data"] and ((claims["annual_trend_pct"] or 0) >= 5 or (claims["last_12m_vs_prior_pct"] or 0) >= 20)
    if total >= 60 and gap >= 10:
        rec = "Launch opportunity"
    elif rising and gap < 10:
        rec = "Review pricing & exposure"
    elif news >= 12 and momentum < 10 and gap < 5:
        rec = "Watch: headlines not yet in our claims"
    elif total >= 40:
        rec = "Investigate"
    else:
        rec = "Low priority"
    return {"score": int(total), "recommendation": rec, "components": comps}


# ---------------------------------------------------------------------------
# Narrative (LLM optional, always grounded in the computed facts)
# ---------------------------------------------------------------------------
_SCREEN_SCHEMA = {
    "type": "object",
    "properties": {
        "verdicts": {"type": "array", "items": {
            "type": "object",
            "properties": {
                "n": {"type": "integer"},
                "relevant": {"type": "boolean"},
                "reason": {"type": "string", "description": "At most 12 words."},
            },
            "required": ["n", "relevant", "reason"],
        }},
    },
    "required": ["verdicts"],
}
_SCREEN_SYSTEM = (
    "You screen news for an insurance product team. For each numbered article decide whether it is evidence about "
    "the losses, incidents, claims, demand or coverage for the PROPOSED PRODUCT's peril. Mark it NOT relevant when "
    "it is about a different line of insurance or peril (e.g. cyber attacks when the product covers physical "
    "property damage), company news (appointments, results, partnerships, marketing, sponsorships), adverts, "
    "listings, law-firm or repair/restoration service pages, glossaries and evergreen how-to guides, or only shares "
    "a word with the topic. When unsure, mark it not relevant."
)
_GENERIC_WORDS = {"new", "the", "and", "for", "with", "latest", "recent", "rising", "insurance", "cover", "coverage",
                  "risk", "risks", "claims", "losses", "india", "news"}


# Service providers and evergreen pages that news search returns but that aren't news
_MARKETING_DOMAIN = re.compile(r"(law|legal|attorney|lawyer|injury|restor|clean|plumb|roofing|waterdamage|adjuster|"
                               r"glossary|realty|realtor|realestate|propert(y|ies)forsale)")
_MARKETING_TITLE = re.compile(r"\b(faqs?|glossary|award-winning|how to|guide to|tips|near me|services?|"
                              r"for sale|for lease|listings?|what (is|to expect)|common (causes|sources))\b", re.I)


def _rule_out_marketing(articles) -> tuple:
    kept, dropped = [], []
    for a in articles:
        if _MARKETING_DOMAIN.search(a["source"].split(".")[0]):
            dropped.append({**a, "reason": "Service provider's page, not news"})
        elif _MARKETING_TITLE.search(a["title"]):
            dropped.append({**a, "reason": "Guide, FAQ or advert, not news"})
        else:
            kept.append(a)
    return kept, dropped


def _screen_articles(topic, articles) -> tuple:
    kept, ruled_out = _rule_out_marketing(articles)
    kept, dropped, method = _screen_relevance(topic, kept)
    return kept, ruled_out + dropped, method


def _screen_relevance(topic, articles) -> tuple:
    """Keep only articles that are really about the product's peril. Returns (kept, screened_out, method).

    Uses the LLM as a relevance judge; without one, an article's headline must contain the topic's own words.
    """
    from backend import llm_client

    if llm_client.provider() is not None:
        listing = [{"n": i, "title": a["title"], "snippet": a["snippet"]} for i, a in enumerate(articles, 1)]
        try:
            out = llm_client.structured_call(
                _SCREEN_SYSTEM,
                [{"role": "user", "content": json.dumps({"topic": topic["label"], "proposed_product": topic["idea"],
                                                         "articles": listing})}],
                "screen_articles", "Relevance verdict per article", _SCREEN_SCHEMA, max_tokens=1500)
            verdicts = {int(v["n"]): v for v in out.get("verdicts", []) if isinstance(v, dict) and "n" in v}
            kept, dropped = [], []
            for i, a in enumerate(articles, 1):
                v = verdicts.get(i)
                (kept if v and v.get("relevant") else dropped).append(
                    a if v and v.get("relevant") else {**a, "reason": (v or {}).get("reason") or "No verdict"})
            return kept, dropped, llm_client.method_name()
        except Exception as e:
            print(f"[NOTE: market radar screening fell back]: {type(e).__name__}: {e}")
    words = [w for w in re.findall(r"[a-z]{3,}", topic["label"].lower()) if w not in _GENERIC_WORDS]
    words += [k for k in TAG_SEMANTIC_MAP.get(topic.get("tag") or "", []) if len(k) > 3]
    kept, dropped = [], []
    for a in articles:
        title = a["title"].lower()
        (kept if any(w in title for w in words) else dropped).append(
            a if any(w in title for w in words) else {**a, "reason": "Headline doesn't mention the topic"})
    return kept, dropped, "keyword_rule"


_NARRATIVE_SCHEMA = {
    "type": "object",
    "properties": {
        "headline": {"type": "string", "description": "One sentence, at most 20 words."},
        "rationale": {"type": "string", "description": "2-4 sentences. Cite articles as [1], [2] and only use the given facts."},
        "risks": {"type": "array", "items": {"type": "string"}, "description": "2-3 short risks or caveats."},
    },
    "required": ["headline", "rationale", "risks"],
}
_NARRATIVE_SYSTEM = (
    "You are an insurance product strategist. Using ONLY the facts provided, explain whether this news-driven "
    "signal is a product opportunity. Never invent numbers, sources or events. Cite news articles only by their "
    "bracketed numbers. Always mention adverse-selection or accumulation risk where relevant, and say plainly when "
    "the claims data does not support the headlines."
)


def _fallback_narrative(topic, articles, claims, scored) -> Dict[str, Any]:
    cites = " ".join(f"[{i}]" for i in range(1, min(3, len(articles)) + 1))
    parts = [f"{len(articles)} recent article(s) cover {topic['label'].lower()} {cites}".strip() + "."]
    if claims["has_data"]:
        parts.append(f"In our claims, {claims['trend_narrative']} Claims in the last 12 months are "
                     f"{(claims['last_12m_vs_prior_pct'] or 0):+.1f}% vs the prior 12, and "
                     f"{(claims['gap_denial_rate_pct'] or 0):.1f}% were denied for coverage-gap reasons.")
    else:
        parts.append(claims["narrative"])
    risks = ["Buyers who sign up because of the headlines may be the riskiest (adverse selection).",
             "One defect or recall can trigger many claims at once (accumulation)."]
    rep = verification.report([], verification.checked_counts(parts), [], "offline_deterministic")
    rep["status"] = "computed"
    return {"headline": f"{scored['recommendation']}: {topic['idea']}", "rationale": " ".join(parts),
            "risks": risks, "generation_method": "offline_deterministic", "verification": rep}


def _narrative(topic, articles, claims, market, scored) -> Dict[str, Any]:
    from backend import llm_client

    if llm_client.provider() is None or not articles:
        return _fallback_narrative(topic, articles, claims, scored)
    facts = {
        "topic": topic["label"], "proposed_product": topic["idea"],
        "recommendation": scored["recommendation"], "score": scored["score"],
        "score_components": scored["components"], "claims_evidence": claims,
        "competitor_sources": market["competitors"], "regulatory_sources": market["regulatory"],
        "news_articles": [{"n": i, "title": a["title"], "source": a["source"], "published": a["published"],
                           "snippet": a["snippet"]} for i, a in enumerate(articles, 1)],
    }
    fact_numbers = verification.FactNumbers(facts)
    source_text = json.dumps(facts)

    def _check(story) -> List[Dict[str, str]]:
        issues = []
        for loc, text in (("Headline", story["headline"]), ("Rationale", story["rationale"]),
                          *((f"Risk #{n}", r) for n, r in enumerate(story["risks"], 1))):
            issues += verification.check_numbers(text, fact_numbers, loc)
            issues += verification.check_bracket_citations(text, len(articles), loc)
            issues += verification.check_names(text, source_text, loc)
            if claims.get("has_data"):
                issues += verification.check_trend_wording(text, claims.get("annual_trend_pct"),
                                                           claims.get("trend_significant"), loc)
        return issues

    def _errors(issues):
        return sum(1 for i in issues if i["severity"] == verification.ERROR)

    messages = [{"role": "user", "content": json.dumps(facts)}]
    actions: List[str] = []
    try:
        out = llm_client.structured_call(_NARRATIVE_SYSTEM, messages, "market_signal", "Explain a market signal",
                                         _NARRATIVE_SCHEMA, max_tokens=1200)
        story = {"headline": html.unescape(str(out["headline"]))[:200],
                 "rationale": html.unescape(str(out["rationale"])),
                 "risks": [html.unescape(str(r)) for r in out.get("risks", [])][:3],
                 "generation_method": llm_client.method_name()}
        issues = _check(story)
        if _errors(issues):
            out2 = llm_client.structured_call(
                _NARRATIVE_SYSTEM, messages + [{"role": "assistant", "content": json.dumps(out)},
                                               {"role": "user", "content": verification.feedback(issues)}],
                "market_signal", "Explain a market signal", _NARRATIVE_SCHEMA, max_tokens=1200)
            story2 = {**story, "headline": html.unescape(str(out2["headline"]))[:200],
                      "rationale": html.unescape(str(out2["rationale"])),
                      "risks": [html.unescape(str(r)) for r in out2.get("risks", [])][:3]}
            issues2 = _check(story2)
            actions.append(f"Retried once after {_errors(issues)} issue(s); the retry had {_errors(issues2)}.")
            if _errors(issues2) < _errors(issues):
                story, issues = story2, issues2
        if _errors(issues):
            fallback = _fallback_narrative(topic, articles, claims, scored)
            actions.append("The AI write-up still failed verification; replaced it with the computed write-up.")
            fallback["verification"] = verification.report(issues, verification.checked_counts(
                [story["headline"], story["rationale"], *story["risks"]]), actions, story["generation_method"])
            fallback["verification"]["status"] = "replaced"
            return fallback
        story["verification"] = verification.report(issues, verification.checked_counts(
            [story["headline"], story["rationale"], *story["risks"]]), actions, story["generation_method"])
        return story
    except Exception as e:
        print(f"[NOTE: market radar narrative fell back]: {type(e).__name__}: {e}")
        return _fallback_narrative(topic, articles, claims, scored)


# ---------------------------------------------------------------------------
# Scan
# ---------------------------------------------------------------------------
def discover_topics() -> List[Dict[str, Any]]:
    """Find risks trending in general news that aren't on the watchlist.

    Each discovery hit is matched to a claims pattern by keywords; a pattern becomes a topic when at least
    DISCOVERY_MIN_PUBLISHERS different publishers cover it. Returns the strongest MAX_DISCOVERED.
    """
    from tavily import TavilyClient

    client = TavilyClient(api_key=_tavily_key())
    watched = {t["tag"] for t in WATCHLIST}

    def _search(q):
        try:
            r = client.search(query=f"{q} {NEWS_MARKET}", topic="news", days=NEWS_DAYS, max_results=10, search_depth="basic",
                              include_answer=False, exclude_domains=_EXCLUDED_DOMAINS, timeout=20)
            return r.get("results", []) if isinstance(r, dict) else []
        except Exception as e:
            print(f"[NOTE: market radar discovery '{q}' failed]: {type(e).__name__}: {e}")
            return []

    with ThreadPoolExecutor(max_workers=len(DISCOVERY_QUERIES)) as pool:
        hits = [h for batch in pool.map(_search, DISCOVERY_QUERIES) for h in batch]
    publishers: Dict[str, set] = {}
    for h in hits:
        url = h.get("url") or ""
        tag, conf = resolve_risk_tag_with_confidence(f"{h.get('title') or ''} {(h.get('content') or '')[:300]}")
        if tag and conf >= 0.6 and tag not in watched and url.startswith("http"):
            publishers.setdefault(tag, set()).add(_domain(url))
    trending = sorted((t for t, pubs in publishers.items() if len(pubs) >= DISCOVERY_MIN_PUBLISHERS),
                      key=lambda t: -len(publishers[t]))[:MAX_DISCOVERED]
    topics = []
    for tag in trending:
        label, idea = TAG_LABELS.get(tag, (tag.replace("_", " ").title(), f"{tag.replace('_', ' ').title()} Cover"))
        keywords = [k for k in TAG_SEMANTIC_MAP.get(tag, []) if len(k) > 3][:3]
        topics.append({"id": f"auto_{tag}", "label": label, "tag": tag, "idea": idea, "discovered": True,
                       "query": f"{label} {' '.join(keywords)}".strip()})
    return topics


def custom_topic(text: str) -> Dict[str, str]:
    text = re.sub(r"\s+", " ", text).strip()[:120]
    tag, conf = resolve_risk_tag_with_confidence(text)
    slug = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")[:40]
    # Frame the search around losses and insurance so it doesn't return listings or adverts
    return {"id": f"custom_{slug}", "label": text, "tag": tag if conf >= 0.5 else None,
            "query": f"{text} damage losses claims", "idea": f"{text.title()} Cover"[:150]}


def _analyse(topic: Dict[str, str]) -> Optional[Dict[str, Any]]:
    articles, screened_out, screened_by = _screen_articles(topic, fetch_news(topic) or [])
    if not articles:
        return None
    claims = _claims_evidence(topic.get("tag"))
    market = _market_evidence(topic)
    scored = score_signal(articles, claims, market)
    story = _narrative(topic, articles, claims, market, scored)
    checked = story.pop("verification", None)
    origin = "custom" if topic["id"].startswith("custom_") else "discovered" if topic.get("discovered") else "watchlist"
    return {"topic_id": topic["id"], "label": topic["label"], "tag_value": topic.get("tag"),
            "product_idea": topic["idea"], **scored, **story,
            "evidence": {"claims": claims, **market, "origin": origin, "screened_out": screened_out,
                         "screened_by": screened_by, "verification": checked}, "articles": articles}


def run_scan(trigger: str = "manual", topics: Optional[List[Dict[str, str]]] = None) -> Dict[str, Any]:
    """Scan the given topics (default: the watchlist). Returns a run summary; never runs two scans at once."""
    if _tavily_key() is None:
        return {"status": "offline", "message": "News scanning is off: TAVILY_API_KEY is not configured."}
    if not _scan_lock.acquire(blocking=False):
        return {"status": "busy", "message": "A scan is already running."}
    started = datetime.utcnow().isoformat()
    try:
        with get_connection() as conn:
            run_id = conn.execute("INSERT INTO market_radar_runs (started_at, trigger, status) VALUES (?, ?, 'running')",
                                  (started, trigger)).lastrowid
        discovered: List[Dict[str, Any]] = []
        if topics is None:
            discovered = discover_topics()
            topics = WATCHLIST + discovered

        def _safe(topic):
            try:
                return _analyse(topic)
            except Exception as e:
                print(f"[NOTE: market radar topic '{topic['id']}' failed]: {type(e).__name__}: {e}")
                return "error"

        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(_safe, topics))
        saved = [r for r in results if isinstance(r, dict)]
        for sig in saved:
            _save_signal(sig)
        errors = sum(1 for r in results if r == "error")
        status = "error" if errors == len(topics) else "ok"
        if trigger == "custom" and not saved and not errors:
            message = (f"No recent news about losses or claims for '{topics[0]['label']}' in the last {NEWS_DAYS} days "
                       "(off-topic articles are left out). Try naming the risk itself, e.g. 'warehouse fires' or "
                       "'office flooding'.")
        else:
            message = (f"Scanned {len(topics)} topic(s)"
                   + (f" ({len(discovered)} discovered in the news)" if discovered else "")
                       + f": {len(saved)} with recent news" + (f", {errors} failed." if errors else "."))
        with get_connection() as conn:
            conn.execute("UPDATE market_radar_runs SET finished_at = ?, status = ?, message = ? WHERE id = ?",
                         (datetime.utcnow().isoformat(), status, message, run_id))
        return {"status": status, "message": message, "topic_ids": [s["topic_id"] for s in saved]}
    finally:
        _scan_lock.release()


def start_scan_in_background(trigger: str = "manual") -> Dict[str, Any]:
    """Kick off a full watchlist + discovery scan without blocking the caller."""
    if _tavily_key() is None:
        return {"status": "offline", "message": "News scanning is off: TAVILY_API_KEY is not configured."}
    if _scan_lock.locked():
        return {"status": "busy", "message": "A scan is already running."}
    threading.Thread(target=run_scan, args=(trigger,), daemon=True, name="market-radar-scan").start()
    return {"status": "started", "message": "Scan started. It takes a few minutes; refresh to see new signals."}


def _last_auto_scan() -> Optional[datetime]:
    with get_connection() as conn:
        row = conn.execute("SELECT started_at FROM market_radar_runs WHERE status = 'ok' "
                           "AND trigger IN ('scheduled', 'manual') ORDER BY id DESC LIMIT 1").fetchone()
    return datetime.fromisoformat(row["started_at"]) if row else None


def start_scheduler() -> None:
    """Background loop: rescan the watchlist every RADAR_SCAN_HOURS (default 24). RADAR_AUTO_SCAN=0 turns it off."""
    global _scheduler_started
    if _scheduler_started or os.environ.get("RADAR_AUTO_SCAN", "1") == "0":
        return
    _scheduler_started = True
    interval = timedelta(hours=float(os.environ.get("RADAR_SCAN_HOURS", "24")))

    def _loop():
        time.sleep(30)  # let the API finish starting
        while True:
            try:
                last = _last_auto_scan()
                if _tavily_key() and (last is None or datetime.utcnow() - last >= interval):
                    print("[market radar] " + run_scan("scheduled")["message"])
            except Exception as e:
                print(f"[NOTE: market radar scheduler]: {type(e).__name__}: {e}")
            time.sleep(15 * 60)

    threading.Thread(target=_loop, daemon=True, name="market-radar").start()
