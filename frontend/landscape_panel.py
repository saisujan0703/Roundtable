"""
Competitor landscape panel: carriers offering this kind of cover, with coverage, price and ratings, from
GET/POST /api/briefs/{id}/competitor-landscape (backend.competitor_landscape). Every fact links to its page.
"""
from __future__ import annotations

import html
from typing import Any, Callable, Dict, Optional

import pandas as pd
import streamlit as st

Call = Callable[..., Optional[Dict[str, Any]]]
PRICE_KIND = {"advertised": "advertised by carrier", "average": "comparison-site average", "filed": "filed rate",
              "example_quote": "example quote"}
MATCH = {"exact": "Same cover", "variant": "Close variant", "unknown": "Not checked"}
RATING_HELP = {
    "US": "NAIC complaint index: 1.00 is the market average, lower is better.",
    "IN": "Claim settlement ratio: share of claims the insurer settled (IRDAI); higher is better. Incurred claim "
          "ratio: claims paid as a share of premium. Complaints per 10,000: lower is better.",
    "UK": "Defaqto: 1 to 5 stars for policy features; higher is better.",
    "GLOBAL": "AM Best and S&P grades rate financial strength; A or above is strong.",
}
FIELD_LABEL = {"product_name": "Product", "states": "Where sold", "coverage": "Coverage",
               "limits_deductible": "Limits / deductible", "exclusions": "Exclusions", "price": "Price"}


def _price(c: Dict[str, Any]) -> str:
    p = c.get("price")
    return f"{p['value']} ({PRICE_KIND.get(p['kind'], p['kind'])})" if p else ""


def _ratings(c: Dict[str, Any]) -> str:
    return " · ".join(f"{r['label']}: {r['value']}" for r in c.get("ratings") or [])


RULE_LABEL = {"broker": "Broker / comparison site", "off_topic": "Different product", "ai_review": "AI check",
              "empty": "Nothing usable", "unsafe": "Unsafe text or link", "price": "Price rejected",
              "rating": "Rating rejected"}


def _render_guard(land: Dict[str, Any]) -> None:
    g = land.get("guard")
    if not g:
        st.warning("These results were found before the checks were added. Click Refresh to scan again with them.")
        return
    dropped = len(g["removed"]) + len(g["trimmed"])
    st.caption(f"🛡️ Checked before showing: {g['kept']} of {g['checked']} carriers passed"
               + (f" · {len(g['trimmed'])} facts removed" if g["trimmed"] else "")
               + (" · AI relevance check ran" if g.get("ai_review") else " · AI relevance check did not run"))
    for n in g.get("notes") or []:
        st.caption(f"ℹ️ {n}")
    if dropped:
        with st.expander(f"What the checks removed ({dropped})"):
            st.dataframe(pd.DataFrame([{"Carrier": r["carrier"], "Check": RULE_LABEL.get(r["rule"], r["rule"]),
                                        "Why": r["reason"]} for r in g["removed"] + g["trimmed"]]),
                         hide_index=True, use_container_width=True)


def render_landscape(brief: Dict[str, Any], api: Call) -> None:
    path = f"briefs/{brief['id']}/competitor-landscape"
    data = api("GET", path)
    if data is None:
        return
    land = data.get("landscape")
    st.markdown("#### Market landscape")
    st.caption("Insurers offering this kind of cover, found on the open web: what each covers, what it costs and how "
               "the insurer is rated. A fact is shown only when its quote was found word for word on the linked page.")
    c1, c_region, c2 = st.columns([2.4, 1.1, 1])
    if land:
        c1.caption(f"Last searched {land['generated_at'].replace('T', ' ').rstrip('Z')} UTC · "
                   f"{land.get('region_label', 'India')} · "
                   f"{len(land['carriers'])} carriers · {len(land['sources'])} pages read"
                   + (f" · searched as: {', '.join(land['terms'])}" if land.get("terms") else ""))
    if not data.get("search_configured"):
        c1.info("Web search is off: set TAVILY_API_KEY in .env and restart the backend to scan the market.")
    regions = data.get("regions") or {"IN": "India"}
    current = (land or {}).get("region", "IN")
    region = c_region.selectbox("Market", list(regions), format_func=regions.get,
                                index=list(regions).index(current) if current in regions else 0,
                                key=f"land_region_{brief['id']}", label_visibility="collapsed")
    changed = bool(land) and region != current
    if c2.button("Refresh" if land and not changed else "Scan the market", key=f"land_refresh_{brief['id']}",
                 type="primary", use_container_width=True, disabled=not data.get("search_configured")):
        with st.spinner(f"Searching carriers, prices and ratings in {regions[region]} (about a minute)..."):
            res = api("POST", path, timeout=240, json={"region": region})
        if res is not None:
            st.rerun()
    if not land:
        return
    for n in land.get("notes") or []:
        st.caption(f"ℹ️ {n}")
    _render_guard(land)
    carriers = land["carriers"]
    if not carriers:
        return

    st.dataframe(pd.DataFrame([{
        "Carrier": c["carrier"], "Match": MATCH.get(c.get("match"), ""), "Product": c.get("product_name") or "",
        "Coverage": c.get("coverage") or "", "Limits / deductible": c.get("limits_deductible") or "",
        "Where sold": c.get("states") or "", "Price": _price(c), "Ratings": _ratings(c),
        "Source": "Carrier website" if c.get("carrier_site") else "Third-party only",
    } for c in carriers]), hide_index=True, use_container_width=True,
        column_config={"Coverage": st.column_config.TextColumn(width="large"),
                       "Ratings": st.column_config.TextColumn(width="medium")})
    st.caption("Source: 'Carrier website' means at least one fact comes from the insurer's own page; "
               "'Third-party only' means every fact comes from comparison or news sites, so confirm it with the "
               "carrier. Carriers that sell only a broader product are left out.")
    st.caption("Prices depend on the customer, so few carriers publish one. Each price is labelled with what it is; "
               "an empty cell means no reliable published price was found. "
               + RATING_HELP.get(land.get("region", "IN"), ""))

    for c in carriers:
        with st.expander(f"{c['carrier']} — evidence"):
            for ev in c.get("evidence") or []:
                label = FIELD_LABEL.get(ev["field"], ev["field"])
                kind = f" ({PRICE_KIND.get(ev.get('price_kind'), '')})" if ev["field"] == "price" else ""
                st.markdown(f"**{label}{kind}:** {html.escape(ev['value'])}  \n"
                            f"> {html.escape(ev['quote'])}  \n[{html.escape(ev['site'])}]({ev['url']}) · "
                            f"{ev.get('source_kind', '')}")
            for r in c.get("ratings") or []:
                st.markdown(f"**{r['label']}:** {html.escape(r['value'])}  \n"
                            f"> {html.escape(r['quote'])}  \n[{html.escape(r['site'])}]({r['url']})")
            if not c.get("evidence") and not c.get("ratings"):
                st.caption("Named on: " + ", ".join(f"[{u.split('/')[2]}]({u})" for u in c["sources"]))
    with st.expander(f"All pages read ({len(land['sources'])})"):
        for s in land["sources"]:
            st.markdown(f"{'✅' if s['cited'] else '▫️'} [{html.escape(s['title'] or s['site'])}]({s['url']}) · {s['site']}")
        st.caption("✅ = a fact in the table comes from this page.")
