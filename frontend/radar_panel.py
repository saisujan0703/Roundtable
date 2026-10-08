"""
Market Radar panel
==================
News-driven product opportunities, each with its proof: the articles that triggered it, what our own claims
data says, and competitor / regulatory sources, plus a transparent score breakdown. A signal can be turned
into a full decision brief or dismissed. Logic lives in backend/market_radar.py.
"""
from __future__ import annotations

import html
from typing import Any, Callable, Dict, Optional

import streamlit as st

from verification_badge import chip_html, render_verification

REC_CHIP = {
    "Launch opportunity": "lime",
    "Review pricing & exposure": "warn",
    "Investigate": "indigo",
    "Watch: headlines not yet in our claims": "grey",
    "Low priority": "grey",
}
ORIGIN_LABEL = {"watchlist": "Watchlist", "discovered": "Found in the news", "custom": "Your topic"}


def _md(text: Optional[str]) -> str:
    return (str(text) if text is not None else "").replace("$", "\\$")


def _pct(v: Optional[float]) -> str:
    return "—" if v is None else f"{v:+.1f}%"


def _render_proofs(sig: Dict[str, Any]) -> None:
    ev = sig["evidence"]
    st.markdown("**News that triggered it**")
    for i, a in enumerate(sig["articles"], 1):
        date = f" · {html.escape(a['published'])}" if a.get("published") else ""
        st.markdown(f"[{i}] [{_md(a['title'])}]({a['url']}) — *{html.escape(a['source'])}{date}*")
        if a.get("snippet"):
            st.caption(_md(a["snippet"]))

    if ev.get("screened_out"):
        st.caption(f"Left out as off-topic ({len(ev['screened_out'])}), checked by {ev.get('screened_by', 'screening')}:")
        for a in ev["screened_out"]:
            st.caption(f"✕ [{_md(a['title'])}]({a['url']}) — {_md(a.get('reason'))}")

    c = ev["claims"]
    st.markdown("**Our claims data** (synthetic demo data)")
    if c.get("has_data"):
        cols = st.columns(4)
        cols[0].metric("Claims on file", f"{c.get('claims') or 0:,}")
        cols[1].metric("Frequency trend", f"{_pct(c.get('annual_trend_pct'))}/yr",
                       help="Fitted ex-CAT trend. " + ("Statistically significant." if c.get("trend_significant")
                                                       else "Not statistically significant."))
        cols[2].metric("Last 12 months", _pct(c.get("last_12m_vs_prior_pct")),
                       help=f"{c.get('last_12m_claims')} claims vs {c.get('prior_12m_claims')} in the prior 12 months")
        cols[3].metric("Coverage-gap denials", f"{c.get('gap_denial_rate_pct') or 0:.1f}%",
                       help=f"{c.get('gap_denials') or 0} claims denied for reasons that signal unmet demand")
        if c.get("trend_narrative"):
            st.caption(_md(c["trend_narrative"]))
    else:
        st.warning(_md(c.get("narrative")))

    for key, title in (("competitors", "Competitor sources"), ("regulatory", "Regulatory sources")):
        if ev.get(key):
            st.markdown(f"**{title}**")
            for s in ev[key]:
                flag = " — *excludes or limits this cover*" if s.get("excludes_cover") and key == "competitors" else ""
                link = f"[{_md(s['title'] or s['source'])}]({s['url']})" if s.get("url") else _md(s["title"])
                st.markdown(f"- {_md(s['source'])}: {link}{flag}")


def _render_signal(sig: Dict[str, Any], act: Callable[[str, str], None]) -> None:
    tid = sig["topic_id"]
    with st.container(border=True):
        head, score_col = st.columns([5, 1])
        with head:
            origin = ORIGIN_LABEL.get(sig["evidence"].get("origin"), "Watchlist")
            status = {"briefed": '<span class="rt-chip lime">brief created</span>',
                      "dismissed": '<span class="rt-chip grey">dismissed</span>'}.get(sig["status"], "")
            st.markdown(
                f'<span class="rt-chip {REC_CHIP.get(sig["recommendation"], "grey")}">{html.escape(sig["recommendation"])}</span> '
                f'<span class="rt-chip grey">{html.escape(origin)}</span> {status} '
                f'{chip_html(sig["evidence"].get("verification"))}'
                f'<div style="font-size:1.15rem;font-weight:700;margin-top:6px">{html.escape(sig["label"])}</div>'
                f'<div style="color:var(--rt-muted);font-size:0.85rem">Proposed product: '
                f'<strong>{html.escape(sig["product_idea"])}</strong> · scanned {html.escape(sig["scanned_at"][:16].replace("T", " "))} UTC</div>',
                unsafe_allow_html=True,
            )
        score_col.metric("Opportunity", f"{sig['score']}/100")

        st.markdown(f"**{_md(sig['headline'])}**")
        st.markdown(_md(sig["rationale"]))
        if sig.get("risks"):
            st.markdown("**Watch out for:**\n" + "\n".join(f"- {_md(r)}" for r in sig["risks"]))

        render_verification(sig["evidence"].get("verification"), "write-up")
        with st.expander("Score breakdown"):
            for comp in sig["components"]:
                st.progress(comp["points"] / comp["max"] if comp["max"] else 0.0,
                            text=f"{comp['name']}: {comp['points']} / {comp['max']} — {comp['why']}")
            st.caption("Computed in Python from the news count, our claims data and curated sources. "
                       f"Write-up: {sig['generation_method']}.")
        with st.expander(f"Proofs ({len(sig['articles'])} articles + data)"):
            _render_proofs(sig)

        b1, b2, _ = st.columns([1.3, 1, 2.2])
        with b1:
            if sig.get("brief_id"):
                if st.button(f"Open brief #{sig['brief_id']}", key=f"rad_open_{tid}", use_container_width=True):
                    act("open", tid)
            elif st.button("Create decision brief", key=f"rad_brief_{tid}", type="primary", use_container_width=True):
                act("brief", tid)
        with b2:
            if sig["status"] == "dismissed":
                if st.button("Restore", key=f"rad_restore_{tid}", use_container_width=True):
                    act("restore", tid)
            elif st.button("Dismiss", key=f"rad_dismiss_{tid}", use_container_width=True):
                act("dismiss", tid)


def render_radar(data: Optional[Dict[str, Any]], scan: Callable[[Optional[str]], None],
                 act: Callable[[str, str], None], focus: Optional[str] = None) -> None:
    """*scan(topic or None)* runs a scan; *act(action, topic_id)* is brief / open / dismiss / restore."""
    st.markdown(
        '<div class="rt-ws-head"><span class="rt-eyebrow"><i></i>Market radar</span>'
        '<div class="rt-ws-title">Opportunities in the news</div>'
        '<p class="rt-ws-sub">Roundtable watches recent news across risk types, checks each story against our own '
        'claims, competitors and regulation, and suggests products with the proof attached. People decide.</p></div>',
        unsafe_allow_html=True,
    )
    if data is None:
        st.error("Could not load the market radar from the backend.")
        return
    if not data.get("news_configured"):
        st.warning("News scanning is off: set TAVILY_API_KEY in .env and restart the backend.")

    run = data.get("last_run")
    if run:
        when = (run.get("finished_at") or run["started_at"])[:16].replace("T", " ")
        st.caption(f"Last scan: {when} UTC ({run['trigger']}) — {run.get('message') or run['status']}. "
                   "The watchlist is rescanned automatically every day.")

    if data.get("scanning"):
        st.info("A news scan is running in the background (a few minutes). Refresh to see the latest signals.")
        if st.button("Refresh"):
            st.rerun()

    c1, c2, c3 = st.columns([1.1, 2.6, 1.1])
    with c1:
        if st.button("Scan now", type="primary", use_container_width=True, disabled=data.get("scanning", False),
                     help="Watchlist + auto-discovery from general news; runs in the background for a few minutes"):
            scan(None)
    with c2:
        topic = st.text_input("Scan a topic", placeholder="Any news topic, e.g. phone theft in metros, heatwave crop losses",
                              label_visibility="collapsed", key="radar_topic")
    with c3:
        if st.button("Scan topic", use_container_width=True, disabled=not (topic or "").strip()):
            scan(topic.strip())

    with st.expander("What the radar watches"):
        st.markdown("**Watchlist:** " + ", ".join(t["label"] for t in data.get("watchlist", [])))
        st.markdown("**Auto-discovery:** broad news searches whose stories are matched to any risk pattern in "
                    "our claims data, so new risks surface without being listed:\n"
                    + "\n".join(f"- *{_md(q)}*" for q in data.get("discovery_queries", [])))
        st.markdown("**Your topics:** anything typed above is scanned the same way.")

    signals = data.get("signals", [])
    # The topic the user just scanned goes first, whatever its score
    focused = next((s for s in signals if s["topic_id"] == focus), None)
    if focused:
        st.markdown(f"#### Result for your scan: {html.escape(focused['label'])}")
        _render_signal(focused, act)
        st.markdown("#### All signals")
        signals = [s for s in signals if s["topic_id"] != focus]
    show_dismissed = st.toggle("Show dismissed", key="radar_show_dismissed")
    if not show_dismissed:
        signals = [s for s in signals if s["status"] != "dismissed"]
    if not signals:
        st.info("No signals yet. Click **Scan now** to search the news.")
        return
    launch = sum(1 for s in signals if s["recommendation"] == "Launch opportunity")
    st.markdown(f"**{len(signals)} signal(s)**, {launch} launch opportunit{'y' if launch == 1 else 'ies'} — "
                "highest score first.")
    for sig in signals:
        _render_signal(sig, act)
