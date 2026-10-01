"""Roundtable landing page.

Centered-hero layout: oversized headline on a white framed canvas over a lavender backdrop,
pill CTAs, and a sculptural visual wrapped in orbit lines with floating stat cards. Every number
on the cards is read live from roundtable.db (Python/SQL only, no illustrative figures).
"""

from __future__ import annotations

import math
import sqlite3
from pathlib import Path
from typing import Any, Callable, Dict, List

import streamlit as st

DB_PATH = Path(__file__).resolve().parent.parent / "roundtable.db"

ICON_STROKE = "#3D3FE0"


def _icon(body: str) -> str:
    return (
        f'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="{ICON_STROKE}" stroke-width="2" '
        f'stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-3px">{body}</svg>'
    )


ICON_SEARCH = _icon('<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>')
ICON_CHART = _icon('<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>')
ICON_SHIELD = _icon('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>')
ICON_BRIEFCASE = _icon('<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>')
ICON_SCALE = _icon('<path d="M16 16l3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1z"/><path d="M2 16l3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h18"/>')
ICON_GLOBE = _icon('<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>')


# ---------------------------------------------------------------------------
# Live stats for the floating cards
# ---------------------------------------------------------------------------
@st.cache_data(ttl=600, show_spinner=False)
def portfolio_stats() -> Dict[str, Any]:
    stats: Dict[str, Any] = {"ok": False}
    try:
        conn = sqlite3.connect(str(DB_PATH))
        try:
            n_claims, incurred = conn.execute(
                "SELECT COUNT(*), COALESCE(SUM(total_incurred), 0) FROM claims"
            ).fetchone()
            earned = conn.execute("SELECT COALESCE(SUM(earned_premium), 0) FROM policies").fetchone()[0]
            n_briefs = conn.execute("SELECT COUNT(*) FROM briefs").fetchone()[0]
            causes = conn.execute(
                "SELECT loss_cause, COUNT(*) AS n FROM claims WHERE loss_cause IS NOT NULL "
                "GROUP BY loss_cause ORDER BY n DESC LIMIT 4"
            ).fetchall()
        finally:
            conn.close()
        stats.update(
            ok=True,
            n_claims=n_claims,
            incurred=incurred,
            loss_ratio=(incurred / earned) if earned else None,
            n_briefs=n_briefs,
            causes=[(c, n / n_claims) for c, n in causes] if n_claims else [],
        )
    except Exception:
        pass
    return stats


def money_short(x: float) -> str:
    for div, suffix in ((1e9, "B"), (1e6, "M"), (1e3, "K")):
        if abs(x) >= div:
            return f"${x / div:,.1f}{suffix}"
    return f"${x:,.0f}"


# ---------------------------------------------------------------------------
# Sculpture: layered spiral of blades, generated as SVG
# ---------------------------------------------------------------------------
def _fin_path(length: float, w_base: float, w_tip: float) -> str:
    """A flat fin in local coords: narrow base at x=0, wider rounded tip at x=length."""
    hb, ht = w_base / 2, w_tip / 2
    x_tip = length - ht
    return (
        f"M0,{-hb:.1f} C{length * 0.45:.1f},{-hb:.1f} {x_tip * 0.8:.1f},{-ht:.1f} {x_tip:.1f},{-ht:.1f} "
        f"A{ht:.1f},{ht:.1f} 0 0 1 {x_tip:.1f},{ht:.1f} "
        f"C{x_tip * 0.8:.1f},{ht:.1f} {length * 0.45:.1f},{hb:.1f} 0,{hb:.1f} Z"
    )


def sculpture_svg() -> str:
    """Nautilus sculpture: fins set along a logarithmic spiral, inner turns stacked over outer ones."""
    cx, cy = 560.0, 505.0
    squash = 0.8                                # slight top-down perspective
    r_max = 400.0
    growth = math.log(2.0) / (2 * math.pi)      # radius doubles per turn
    turns, per_turn = 4.2, 30
    tilt = 0.40                                 # fins lean off the radial line, giving the swirl
    start = 2.75                                # outermost fin sits low-left; the spiral sweeps over the top

    body: List[str] = []
    step = 2 * math.pi / per_turn
    for i in range(int(turns * per_turn)):      # outermost first so inner turns paint over them
        a = start + i * step                    # screen angle (y down), increasing = over the top
        r = r_max * math.exp(-growth * i * step)
        base_r = r * 0.42
        bx = cx + base_r * math.cos(a)
        by = cy + base_r * math.sin(a) * squash
        phi = a - tilt
        rot = math.degrees(math.atan2(math.sin(phi) * squash, math.cos(phi)))
        length = r * 0.66
        d = _fin_path(length, r * 0.095, r * 0.18)
        tf = f"translate({bx:.1f},{by:.1f}) rotate({rot:.1f})"
        body.append(
            f'<path d="{d}" transform="translate(4,6) {tf}" fill="#173A04" opacity="0.38" filter="url(#rtBlur)"/>'
            f'<g transform="{tf}"><path d="{d}" fill="url(#rtFin)"/><path d="{d}" fill="url(#rtFinSide)"/></g>'
        )
    defs = (
        '<linearGradient id="rtFin" x1="0" y1="0" x2="1" y2="0">'
        '<stop offset="0" stop-color="#4E8A0E"/><stop offset="0.3" stop-color="#7DB823"/>'
        '<stop offset="0.52" stop-color="#9FCC3F"/><stop offset="0.68" stop-color="#DCEBC2"/>'
        '<stop offset="0.8" stop-color="#F5F6F2"/><stop offset="1" stop-color="#FFFFFF"/></linearGradient>'
        '<linearGradient id="rtFinSide" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0" stop-color="#FFFFFF" stop-opacity="0.3"/><stop offset="0.45" stop-color="#FFFFFF" stop-opacity="0"/>'
        '<stop offset="1" stop-color="#1F4A06" stop-opacity="0.5"/></linearGradient>'
        '<filter id="rtBlur" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3.5"/></filter>'
    )
    orbits = (
        '<ellipse cx="530" cy="420" rx="440" ry="165" fill="none" stroke="#8E93C9" stroke-width="1.6" '
        'stroke-dasharray="0.5 9" stroke-linecap="round" opacity="0.8"/>'
        '<ellipse cx="530" cy="410" rx="375" ry="112" fill="none" stroke="#A3A7D6" stroke-width="1.2" opacity="0.9"/>'
    )
    return (
        '<svg class="rt-sculpture" viewBox="60 170 940 390" preserveAspectRatio="xMidYMax meet" '
        'xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
        f'<defs>{defs}</defs>{orbits}{"".join(body)}</svg>'
    )


# ---------------------------------------------------------------------------
# Page
# ---------------------------------------------------------------------------
HOME_CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
:root {
  --rt-ink: #121318;
  --rt-muted: #5B5F6E;
  --rt-backdrop: #D3D6EA;
  --rt-canvas: #FFFFFF;
  --rt-line: #E6E8F1;
  --rt-indigo: #3D3FE0;
  --rt-indigo-soft: #ECEDFC;
  --rt-up: #1E8E4E;
  --rt-up-soft: #E3F5EA;
  --rt-down: #D2453B;
  --rt-down-soft: #FCE8E6;
}
/* Full-bleed canvas like the other pages; hero is sized to the viewport so it fits above the fold */
.stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"], [data-testid="stHeader"] {
  background: var(--rt-canvas) !important;
}
section[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { display: none !important; }
[data-testid="stMainBlockContainer"] {
  padding-top: 2rem !important;
  padding-bottom: 3rem !important;
}
[data-testid="stMainBlockContainer"] * { font-family: 'Plus Jakarta Sans', -apple-system, 'Segoe UI', sans-serif; }

.rt-hero { text-align: center; padding: 2.2vh 0 0 0; }
.rt-eyebrow {
  display: inline-flex; align-items: center; gap: 8px;
  border: 1px solid var(--rt-line); border-radius: 999px; padding: 5px 14px;
  font-size: 0.78rem; font-weight: 600; color: var(--rt-muted); background: #FAFAFD;
}
.rt-eyebrow i { width: 7px; height: 7px; border-radius: 50%; background: var(--rt-indigo); display: inline-block; }
.rt-title {
  font-size: clamp(2.1rem, min(5.2vw, 7.4vh), 4.6rem); line-height: 1.04; letter-spacing: -0.035em;
  font-weight: 600; color: var(--rt-ink) !important; margin: 1.8vh auto 1.6vh auto; max-width: 900px;
}
.rt-sub {
  font-size: clamp(0.92rem, 1.9vh, 1.05rem); line-height: 1.55; color: var(--rt-muted) !important;
  max-width: 660px; margin: 0 auto 0.6vh auto !important; text-align: center;
}

/* Pill CTAs (real Streamlit buttons, keyed) */
.st-key-hero_cta_claims .stButton > button[kind], .st-key-hero_cta_actuarial .stButton > button[kind] {
  border-radius: 999px !important; height: 3rem; font-weight: 600 !important; font-size: 0.92rem !important;
  transition: transform .15s ease, box-shadow .15s ease;
}
.st-key-hero_cta_claims .stButton > button[kind] {
  background: var(--rt-ink) !important; color: #FFF !important; border: 1px solid var(--rt-ink) !important;
  box-shadow: 0 8px 18px -8px rgba(18, 19, 24, 0.55);
}
.st-key-hero_cta_claims .stButton > button[kind] p { color: #FFF !important; }
.st-key-hero_cta_actuarial .stButton > button[kind] {
  background: #FFF !important; color: var(--rt-ink) !important; border: 1px solid #BFC2D3 !important;
}
.st-key-hero_cta_claims .stButton > button[kind]:hover, .st-key-hero_cta_actuarial .stButton > button[kind]:hover { transform: translateY(-1px); }

/* Visual stage */
/* Stage takes whatever height is left in the viewport under the hero copy */
.rt-stage { position: relative; margin: 2vh 0 0 0; height: clamp(220px, calc(100vh - 515px), 560px); overflow: hidden; }
.rt-sculpture { position: absolute; inset: 0; width: 100%; height: 100%; }
.rt-card {
  position: absolute; background: rgba(255,255,255,0.94); border-radius: 16px; padding: 14px 16px;
  box-shadow: 0 18px 40px -16px rgba(40, 44, 90, 0.35), 0 2px 6px rgba(40, 44, 90, 0.06);
  border: 1px solid rgba(230, 232, 241, 0.9); color: var(--rt-ink); min-width: 150px;
}
.rt-card .lbl { font-size: 0.68rem; color: var(--rt-muted); font-weight: 500; }
.rt-card .val { font-size: 1.05rem; font-weight: 700; letter-spacing: -0.01em; }
.rt-card .big { font-size: 1.9rem; font-weight: 600; letter-spacing: -0.03em; line-height: 1.1; }
.rt-card .row { display: flex; justify-content: space-between; align-items: center; gap: 14px; }
.rt-card .row + .row { margin-top: 10px; padding-top: 10px; border-top: 1px dashed var(--rt-line); }
.rt-chip { font-size: 0.62rem; font-weight: 700; border-radius: 999px; padding: 2px 7px; }
.rt-chip.indigo { background: var(--rt-indigo-soft); color: var(--rt-indigo); }
.rt-chip.up { background: var(--rt-up-soft); color: var(--rt-up); }
.rt-card.c1 { left: 13%; top: 6%; transform: rotate(-9deg); }
.rt-card.c2 { right: 13%; top: 3%; transform: rotate(3deg); min-width: 170px; }
.rt-card.c3 { left: 6%; bottom: 14%; transform: rotate(14deg); }
.rt-card.c4 { right: 6%; bottom: 10%; transform: rotate(-13deg); }
.rt-bars { display: flex; align-items: flex-end; gap: 8px; height: 76px; margin-top: 8px; }
.rt-bars div { flex: 1; display: flex; flex-direction: column; justify-content: flex-end; align-items: center; gap: 3px; height: 100%; }
.rt-bars span.b { width: 100%; border-radius: 5px; background: #DADCF6; }
.rt-bars div:first-child span.b { background: linear-gradient(180deg, #5759F0, var(--rt-indigo)); }
.rt-bars span.t { font-size: 0.55rem; color: var(--rt-muted); max-width: 44px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.rt-goal { height: 4px; border-radius: 4px; background: var(--rt-indigo-soft); margin: 6px 0 4px 0; }
.rt-goal span { display: block; height: 100%; border-radius: 4px; background: var(--rt-indigo); }
@media (max-height: 760px) {
  .rt-card { padding: 10px 12px; min-width: 130px; }
  .rt-card.c3, .rt-card.c4 { display: none; }
  .rt-bars { height: 52px; }
}
@media (max-width: 900px) {
  .rt-card.c2, .rt-card.c4 { display: none; }
  .rt-card.c1 { left: 4%; } .rt-card.c3 { left: auto; right: 4%; bottom: auto; top: 6%; }
}

/* Feature section */
.rt-section-head { text-align: center; margin: 3.4rem 0 1.6rem 0; }
.rt-section-head .k { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--rt-indigo); }
.rt-section-head .h { font-size: clamp(1.6rem, 3vw, 2.3rem); font-weight: 600; letter-spacing: -0.03em; color: var(--rt-ink); margin-top: 6px; }
.rt-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
@media (max-width: 960px) { .rt-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 640px) { .rt-grid { grid-template-columns: 1fr; } }
.rt-feature {
  border: 1px solid var(--rt-line); border-radius: 20px; padding: 10px 10px 18px 10px; background: #FFF;
  transition: transform .18s ease, box-shadow .18s ease;
}
.rt-feature:hover { transform: translateY(-3px); box-shadow: 0 20px 40px -24px rgba(40, 44, 90, 0.35); }
.rt-feature .pv {
  background: #F5F6FC; border-radius: 14px; padding: 16px; min-height: 92px;
  display: flex; flex-direction: column; justify-content: center; gap: 8px;
}
.rt-feature .pv .r { display: flex; gap: 8px; flex-wrap: wrap; }
.rt-pchip { background: #FFF; border: 1px solid var(--rt-line); border-radius: 999px; padding: 4px 11px; font-size: 0.72rem; font-weight: 600; color: var(--rt-ink); }
.rt-pchip.i { background: var(--rt-indigo-soft); border-color: #D6D8FA; color: var(--rt-indigo); }
.rt-pchip.g { background: var(--rt-up-soft); border-color: #C9EBD6; color: var(--rt-up); }
.rt-feature .t { font-size: 1rem; font-weight: 700; color: var(--rt-ink); margin: 16px 8px 6px 8px; display: flex; gap: 8px; align-items: center; }
.rt-feature .d { font-size: 0.84rem; line-height: 1.55; color: var(--rt-muted); margin: 0 8px; }
</style>"""


def _cards_html(s: Dict[str, Any]) -> str:
    if not s.get("ok"):
        return ""
    bars = ""
    top = s["causes"][0][1] if s["causes"] else 1
    for cause, share in s["causes"]:
        h = max(12, int(100 * share / top))
        bars += f'<div><span class="t">{share:.0%}</span><span class="b" style="height:{h}%"></span><span class="t">{cause}</span></div>'
    lr = s["loss_ratio"]
    lr_txt = f"{lr:.1%}" if lr is not None else "—"
    lr_bar = min(100, int((lr or 0) * 100))
    return (
        '<div class="rt-card c1">'
        f'<div class="row"><div><div class="val">{money_short(s["incurred"])}</div><div class="lbl">Total incurred</div></div>'
        '<span class="rt-chip indigo">ClaimCenter</span></div>'
        f'<div class="row"><div><div class="val">{s["n_claims"]:,}</div><div class="lbl">Claims analyzed</div></div>'
        '<span class="rt-chip up">SQL verified</span></div></div>'
        '<div class="rt-card c2"><div class="row" style="border:0;padding:0;margin:0">'
        '<div class="lbl">Top loss causes</div><span class="rt-chip indigo">share</span></div>'
        f'<div class="rt-bars">{bars}</div></div>'
        f'<div class="rt-card c3"><div class="lbl">Decision briefs</div><div class="big">{s["n_briefs"]:,}</div>'
        '<div class="lbl">human-approved &amp; cited</div></div>'
        f'<div class="rt-card c4"><div class="lbl">Portfolio loss ratio</div><div class="big" style="color:var(--rt-indigo)">{lr_txt}</div>'
        f'<div class="rt-goal"><span style="width:{lr_bar}%"></span></div><div class="lbl">incurred / earned premium</div></div>'
    )


FEATURES = [
    (ICON_SEARCH, "Claims Review", "Frequency, severity, loss causes and recurring coverage gaps from internal claims history.",
     [("ClaimCenter data", "i"), ("Verified", "g")], [("Loss causes", ""), ("SQL synced", "")]),
    (ICON_CHART, "Actuarial Review", "Pure-SQL loss trends, baseline financial ranges and directional portfolio exposure.",
     [("Loss trends", "i"), ("Directional range", "")], [("Earned exposure", ""), ("Severity", "")]),
    (ICON_SHIELD, "Underwriting Review", "Risk eligibility, guideline boundaries and customer segment exposure thresholds.",
     [("Segment exposure", ""), ("Eligible", "g")], [("Underwriting rules", "i")]),
    (ICON_BRIEFCASE, "Competitor Intel", "Peer carrier coverages, endorsements and marketed product terms, with SERFF filings a click away.",
     [("Carrier products", "i"), ("Benchmarked", "g")], [("Policy terms", "")]),
    (ICON_SCALE, "Regulatory Compliance", "State insurance mandates, rate filing requirements and statutory guidance.",
     [("State mandates", "i"), ("Filing reqs", "")], [("DOI compliance", "g")]),
    (ICON_GLOBE, "Live Web Research", "Cited news, regulator data, actuarial research and carrier pages from trusted sources.",
     [("Live search", "i"), ("Cited", "g")], [("Trusted domains", "")]),
]


def _features_html() -> str:
    cards = []
    for icon, title, desc, row1, row2 in FEATURES:
        r1 = "".join(f'<span class="rt-pchip {c}">{t}</span>' for t, c in row1)
        r2 = "".join(f'<span class="rt-pchip {c}">{t}</span>' for t, c in row2)
        cards.append(
            f'<div class="rt-feature"><div class="pv"><div class="r">{r1}</div><div class="r">{r2}</div></div>'
            f'<div class="t">{icon} {title}</div><p class="d">{desc}</p></div>'
        )
    return (
        '<div class="rt-section-head"><div class="k">One brief, six reviews</div>'
        '<div class="h">Everything a product decision needs</div></div>'
        f'<div class="rt-grid">{"".join(cards)}</div>'
    )


def render_home(go: Callable[[str], None]) -> None:
    """Render the landing page. `go(view)` navigates to a workspace (handles sign-in)."""
    st.markdown(HOME_CSS, unsafe_allow_html=True)
    st.markdown(
        '<section class="rt-hero">'
        '<span class="rt-eyebrow"><i></i>Guidewire pre-APD decision support</span>'
        '<div class="rt-title">Decision intelligence for insurance products</div>'
        '<p class="rt-sub">Roundtable turns ClaimCenter history, actuarial trends and cited market research '
        'into human-approved decision briefs, before anything reaches Guidewire APD.</p>'
        '</section>',
        unsafe_allow_html=True,
    )

    _, c1, c2, _ = st.columns([3, 1.15, 1.15, 3], gap="small")
    with c1:
        if st.button("Get started", key="hero_cta_claims", use_container_width=True):
            go("claims")
    with c2:
        if st.button("Actuarial view", key="hero_cta_actuarial", use_container_width=True):
            go("actuarial")

    st.markdown(
        f'<div class="rt-stage">{sculpture_svg()}{_cards_html(portfolio_stats())}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(_features_html(), unsafe_allow_html=True)
