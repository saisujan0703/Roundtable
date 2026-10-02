"""
Roundtable Insurance Product Decision Support System
====================================================
Streamlit UI — Claims Domain Vertical Slice

Features:
- Configurable product idea title & risk tag selection
- Decision Brief generation via FastAPI backend
- Quantitative underlying data visualization (trends, claim counts, incurred losses)
- Human-in-the-loop editing for Claims findings
- Human sign-off workflow (Approve / Reject / Save Edit)
"""
from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any, Dict, List, Optional
import requests
import streamlit as st

from claims_dashboard import render_claims_dashboard
from readiness_panel import render_readiness
from guideline_panel import render_guideline
from scenarios_panel import render_scenarios
from letters_panel import render_letters
from home_page import money_short, portfolio_stats, render_home, sculpture_svg

# Backend API Base URL
API_BASE_URL = "http://127.0.0.1:8000/api"

# Known risk tags in the synthetic Guidewire database
KNOWN_TAGS = [
    "battery_fault",
    "theftentire",
    "waterdamage",
    "slipfall",
    "strain",
    "fire",
    "rollover",
    "vehcollision",
    "rearend",
]

# Set page configuration
st.set_page_config(
    page_title="Roundtable | Insurance Decision Support",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Roundtable design system: same tokens as the landing page (frontend/home_page.py)
st.markdown(f"<style>{(Path(__file__).parent / 'theme.css').read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# API Helper Functions
# ---------------------------------------------------------------------------
def api_get_tags() -> List[str]:
    try:
        r = requests.get(f"{API_BASE_URL}/tags", timeout=3)
        if r.status_code == 200 and r.json():
            return r.json()
    except Exception:
        pass
    return KNOWN_TAGS


def api_list_briefs() -> List[Dict[str, Any]]:
    try:
        r = requests.get(f"{API_BASE_URL}/briefs", timeout=4)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return []


def api_get_brief(brief_id: int) -> Optional[Dict[str, Any]]:
    try:
        r = requests.get(f"{API_BASE_URL}/briefs/{brief_id}", timeout=4)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        st.error(f"Error fetching brief #{brief_id}: {e}")
    return None


def api_create_brief(title: str, tag_value: Optional[str] = None, proxy_tags: Optional[List[str]] = None,
                     idea_context: Optional[str] = None) -> Optional[Dict[str, Any]]:
    try:
        payload: Dict[str, Any] = {"title": title, "tag_value": tag_value, "proxy_tags": proxy_tags or None,
                                   "idea_context": idea_context or None}
        r = requests.post(
            f"{API_BASE_URL}/briefs",
            json=payload,
            timeout=180,
        )
        if r.status_code in (200, 201):
            return r.json()
        st.error(f"Failed to create brief ({r.status_code}): {r.text}")
    except Exception as e:
        st.error(f"Connection error to backend: {e}. Is 'python -m uvicorn backend.main:app' running?")
    return None


def api_refine_idea(messages: List[Dict[str, str]]) -> Optional[Dict[str, Any]]:
    try:
        r = requests.post(f"{API_BASE_URL}/ideas/refine", json={"messages": messages}, timeout=60)
        if r.status_code == 200:
            return r.json()
        st.error(f"Idea assistant failed ({r.status_code}): {r.text}")
    except Exception as e:
        st.error(f"Connection error to backend: {e}. Is 'python -m uvicorn backend.main:app' running?")
    return None


def api_transcribe(audio: bytes) -> Optional[str]:
    """Speech-to-text on the backend (local Whisper). None on failure, after showing the error."""
    try:
        r = requests.post(f"{API_BASE_URL}/ideas/transcribe",
                          files={"audio": ("idea.wav", audio, "audio/wav")}, timeout=180)
        if r.status_code == 200:
            return r.json().get("text", "").strip()
        detail = r.json().get("detail", r.text) if r.headers.get("content-type", "").startswith("application/json") else r.text
        st.error(f"Voice transcription failed ({r.status_code}): {detail}")
    except Exception as e:
        st.error(f"Connection error to backend: {e}. Is 'python -m uvicorn backend.main:app' running?")
    return None


TAG_AUTO = "(Optional) Auto-detect from title"


def render_idea_assistant(available_tags: List[str]) -> None:
    """Chat where a PM describes a product idea in their own words and gets a title + risk patterns for the form."""
    ss = st.session_state
    ss.setdefault("idea_chat", [])
    ss.setdefault("idea_suggestion", None)

    def _apply(title: str, tag: Optional[str], proxies: List[str]) -> None:
        ss.new_brief_title = title[:150]
        ss.new_brief_tag = tag if tag in available_tags else TAG_AUTO
        ss.new_brief_proxies = [p for p in proxies if p in available_tags]
        # The PM's own words go to the brief as background (latest 4,000 chars, the backend's limit)
        ss.new_brief_context = "\n\n".join(m["content"] for m in ss.idea_chat if m["role"] == "user")[-4000:]

    def _reset() -> None:
        ss.idea_chat = []
        ss.idea_suggestion = None

    with st.container(border=True, key="idea_assistant"):
        head_l, head_r = st.columns([5, 1])
        head_l.markdown(
            "**💬 Not sure what to call it?** Describe the product idea in your own words — type it or press "
            "the 🎙️ mic and say it — who it's for and what loss it should cover, and I'll suggest a title and risk patterns.  \n"
            "*e.g. \"I'm thinking of launching cover for gig drivers whose personal auto policy won't pay while they're "
            "on a delivery.\"*"
        )
        if ss.idea_chat:
            head_r.button("Start over", key="idea_reset", on_click=_reset, use_container_width=True)

        history = st.container(height=320) if len(ss.idea_chat) > 4 else st.container()
        with history:
            for m in ss.idea_chat:
                with st.chat_message(m["role"]):
                    if m.get("spoken"):
                        st.caption("🎙️ Transcribed from your recording")
                    st.markdown(m["content"])

        sug = ss.idea_suggestion
        if sug and sug.get("ready") and sug.get("title_options"):
            tag, proxies = sug.get("risk_tag"), sug.get("proxy_tags") or []
            if tag:
                st.caption(f"Risk pattern: `{tag}`")
            elif proxies:
                st.caption("No direct claims pattern — proxy history: " + ", ".join(f"`{p}`" for p in proxies))
            else:
                st.caption("No related claims pattern — the brief will use the line-of-business baseline.")
            for i, title in enumerate(sug["title_options"]):
                st.button(f"Use “{title}”", key=f"idea_use_{i}", on_click=_apply, args=(title, tag, proxies),
                          use_container_width=True)

        # Keep the placeholder to one line: in Streamlit 1.64 a wrapping placeholder switches the box to its
        # multi-line layout, where the mic fails with "Record backend not initialized"
        submitted = st.chat_input("Type your idea, or press the mic and say it",
                                  key="idea_chat_input", max_chars=4000, accept_audio=True)
        prompt, spoken = "", False
        if submitted:
            prompt = (submitted.text or "").strip()
            if submitted.audio is not None:
                with st.spinner("Transcribing your recording..."):
                    transcript = api_transcribe(submitted.audio.getvalue())
                if transcript is None:
                    return
                if not transcript:
                    st.warning("I couldn't hear any speech in that recording — try again a little closer to the mic.")
                    return
                prompt, spoken = f"{prompt} {transcript}".strip()[:4000], True
        if prompt:
            ss.idea_chat.append({"role": "user", "content": prompt, "spoken": spoken})
            with st.spinner("Thinking about your idea..."):
                # Turns alternate and end on the PM's, so the last 19 always start with a user turn too
                result = api_refine_idea([{"role": m["role"], "content": m["content"]} for m in ss.idea_chat[-19:]])
            if result:
                ss.idea_chat.append({"role": "assistant", "content": result.get("reply") or "Here are some options."})
                ss.idea_suggestion = result
            else:
                ss.idea_chat.pop()  # let the PM resend instead of leaving an unanswered turn
            st.rerun()


def _guideline_call(method: str, path: str, timeout: int = 10, **kw) -> Optional[Dict[str, Any]]:
    try:
        r = requests.request(method, f"{API_BASE_URL}/briefs/{path}", timeout=timeout, **kw)
        if r.status_code == 200:
            return r.json()
        detail = r.json().get("detail", r.text) if r.headers.get("content-type", "").startswith("application/json") else r.text
        st.error(f"Request failed ({r.status_code}): {detail}")
    except Exception as e:
        st.error(f"Connection error to backend: {e}")
    return None


def api_get_guideline(brief_id: int) -> Optional[Dict[str, Any]]:
    return _guideline_call("GET", f"{brief_id}/guideline")


def api_draft_guideline(brief_id: int) -> bool:
    return _guideline_call("POST", f"{brief_id}/guideline", timeout=180) is not None


def api_save_guideline_section(brief_id: int, key: str, body: str) -> bool:
    return _guideline_call("PUT", f"{brief_id}/guideline/sections/{key}", json={"body": body}) is not None


def api_approve_guideline(brief_id: int) -> bool:
    return _guideline_call("PUT", f"{brief_id}/guideline/approve") is not None


def api_get_scenarios(brief_id: int) -> Optional[Dict[str, Any]]:
    return _guideline_call("GET", f"{brief_id}/scenarios")


def api_generate_scenarios(brief_id: int) -> bool:
    return _guideline_call("POST", f"{brief_id}/scenarios", timeout=180) is not None


def api_save_scenario(brief_id: int, scenario_id: str, fields: Dict[str, str]) -> bool:
    return _guideline_call("PUT", f"{brief_id}/scenarios/{scenario_id}", json=fields) is not None


def api_get_letters(brief_id: int) -> Optional[Dict[str, Any]]:
    return _guideline_call("GET", f"{brief_id}/letters")


def api_draft_letters(brief_id: int) -> bool:
    return _guideline_call("POST", f"{brief_id}/letters", timeout=180) is not None


def api_save_letter(brief_id: int, key: str, subject: str, body: str) -> bool:
    return _guideline_call("PUT", f"{brief_id}/letters/{key}", json={"subject": subject, "body": body}) is not None


def api_approve_letter(brief_id: int, key: str) -> bool:
    return _guideline_call("PUT", f"{brief_id}/letters/{key}/approve") is not None


def api_rerun_proxies(brief_id: int, proxy_tags: List[str]) -> bool:
    try:
        r = requests.put(f"{API_BASE_URL}/briefs/{brief_id}/proxies", json={"proxy_tags": proxy_tags}, timeout=180)
        if r.status_code == 200:
            return True
        st.error(f"Could not re-run with these proxies ({r.status_code}): {r.json().get('detail', r.text)}")
    except Exception as e:
        st.error(f"Connection error to backend: {e}")
    return False


def render_proxy_controls(brief: Dict[str, Any], brief_data: Dict[str, Any], available_tags: List[str]) -> None:
    """Let the claims reviewer choose which related risk patterns stand in for an unmatched product's history."""
    analytics = brief_data.get("claims_analytics") or {}
    basis = analytics.get("basis") or {}
    if (brief.get("tag_value") not in (None, "unmatched") or basis.get("basis", "none") not in ("proxy", "line_baseline", "none")
            or brief.get("claims_status") == "Approved"):
        return
    current = basis.get("proxy_tags") or []
    with st.expander("🔁 Proxy risk patterns — choose comparable claims history" + (f" (using {' + '.join(current)})" if current else ""),
                     expanded=not current):
        st.caption("This product has no claims of its own. Pick up to 3 existing risk patterns whose peril behaves like the new "
                   "product's (cause of loss, severity drivers, handling). Their pooled claims run the full 11-section analysis, "
                   "clearly labelled as proxy data. Re-running returns the brief to Draft; section notes and readiness progress are kept.")
        picked = st.multiselect("Proxy risk patterns", options=available_tags, default=[t for t in current if t in available_tags],
                                max_selections=3, key=f"proxy_pick_{brief['id']}",
                                placeholder="e.g. vehiclefire, battery_fault")
        if st.button("Re-run claims analysis", key=f"proxy_run_{brief['id']}", type="primary",
                     disabled=not picked or sorted(picked) == sorted(current)):
            with st.spinner("Re-running claims analysis on the proxy patterns..."):
                if api_rerun_proxies(brief["id"], picked):
                    st.rerun()


def api_update_claims(brief_id: int, new_text: str) -> bool:
    try:
        r = requests.put(
            f"{API_BASE_URL}/briefs/{brief_id}/claims",
            json={"claims_finding_text": new_text},
            timeout=4,
        )
        return r.status_code == 200
    except Exception as e:
        st.error(f"Failed to save claims text: {e}")
        return False


def api_approve_claims(brief_id: int) -> bool:
    try:
        r = requests.put(f"{API_BASE_URL}/briefs/{brief_id}/claims/approve", timeout=4)
        return r.status_code == 200
    except Exception as e:
        st.error(f"Failed to approve claims finding: {e}")
        return False


def api_save_section_note(brief_id: int, section: int, note: str) -> bool:
    try:
        r = requests.put(f"{API_BASE_URL}/briefs/{brief_id}/notes/{section}", json={"note": note}, timeout=4)
        if r.status_code == 200:
            return True
        st.error(f"Could not save note: {r.text}")
        return False
    except Exception as e:
        st.error(f"Failed to save note: {e}")
        return False


def render_edit_status(brief: Dict[str, Any]) -> None:
    """Flag reviewer edits to the finding text and show what changed from the generated version."""
    if not brief.get("claims_edited"):
        return
    import difflib

    edited_at = (brief.get("claims_edited_at") or "")[:16].replace("T", " ")
    st.warning(
        f"✏️ **Finding text edited by reviewer**{f' on {edited_at} UTC' if edited_at else ''}. "
        "The charts show the computed claims data; the edited text is the narrative that will be approved."
    )
    original = (brief.get("original_claims_text") or "").splitlines()
    current = (brief.get("claims_finding_text") or "").splitlines()
    diff = [line for line in difflib.unified_diff(original, current, "generated", "edited", lineterm="", n=1)
            if not line.startswith(("---", "+++"))]
    with st.expander(f"Show changes from generated version ({sum(1 for d in diff if d[:1] in '+-')} lines changed)"):
        st.code("\n".join(diff) or "No line changes.", language="diff")


def api_get_readiness(brief_id: int) -> Optional[Dict[str, Any]]:
    try:
        r = requests.get(f"{API_BASE_URL}/briefs/{brief_id}/readiness", timeout=6)
        return r.json() if r.status_code == 200 else None
    except Exception:
        return None


def api_update_readiness(brief_id: int, item_id: str, fields: Dict[str, str]) -> bool:
    try:
        r = requests.put(f"{API_BASE_URL}/briefs/{brief_id}/readiness/{item_id}", json=fields, timeout=6)
        if r.status_code == 200:
            return True
        st.error(f"Could not save: {r.text}")
        return False
    except Exception as e:
        st.error(f"Failed to save readiness item: {e}")
        return False


def api_reject_claims(brief_id: int) -> bool:
    try:
        r = requests.put(f"{API_BASE_URL}/briefs/{brief_id}/claims/reject", timeout=4)
        return r.status_code == 200
    except Exception as e:
        st.error(f"Failed to reject claims finding: {e}")
        return False


def render_claims_kpis(kpis: Dict[str, Any]) -> None:
    """Headline claims metrics (computed by backend.analytics, never by the LLM)."""
    if not kpis:
        return

    def money(v):
        return "n/a" if v is None else f"${v:,.0f}"

    def pct(v):
        return "n/a" if v is None else f"{v:.1f}%"

    st.markdown(f"#### Claims KPIs — valued {kpis.get('valuation_date', '')}")
    st.caption(f"Scope: {kpis.get('scope')} · frequency per 1,000 {kpis.get('exposure_unit')}")
    trend = kpis.get("frequency_trend_pct")
    trend_label = "n/a" if trend is None else f"{trend:+.1f}%/yr" + ("" if kpis.get("frequency_trend_significant") else " (n.s.)")
    rows = [
        [("Claims (open)", f"{kpis.get('claims', 0):,} ({kpis.get('open_claims', 0):,})"),
         ("Frequency / 1,000", f"{kpis.get('frequency_per_1000') or 0:.1f}"),
         ("Fitted Frequency Trend", trend_label),
         ("Avg Severity (index)", f"{money(kpis.get('avg_severity'))} ({kpis.get('severity_index') or 0:.2f}x)")],
        [("Incurred (paid / reserve)", f"{money(kpis.get('incurred_loss'))}"),
         ("Loss Ratio Points", f"{kpis.get('loss_ratio_points') or 0:.1f}"),
         ("Denied (gap exclusions)", f"{pct(kpis.get('denial_rate_pct'))} ({pct(kpis.get('gap_denial_rate_pct'))})"),
         ("Reserve Dev. (incurred ÷ FNOL)", f"{kpis.get('reserve_development_ratio') or 0:.2f}x")],
        [("Median Cycle Time", f"{kpis.get('cycle_time_median_days') or 0:.0f} days"),
         ("Litigation Rate", pct(kpis.get("litigation_rate_pct"))),
         ("Paid Loss", money(kpis.get("paid_loss"))),
         ("Case Reserves", money(kpis.get("outstanding_reserve")))],
    ]
    for row in rows:
        cols = st.columns(len(row))
        for col, (label, value) in zip(cols, row):
            with col:
                st.metric(label=label, value=value)


# ---------------------------------------------------------------------------
# Sidebar: Existing Briefs & Navigation
# ---------------------------------------------------------------------------
st.sidebar.markdown(
    '<div class="rt-side-brand"><svg width="24" height="24" viewBox="0 0 32 32" fill="none" aria-hidden="true">'
    '<circle cx="16" cy="16" r="11" stroke="#121318" stroke-width="3.2"/>'
    '<path d="M5 16a11 11 0 0 1 11-11" stroke="#3D3FE0" stroke-width="3.2" stroke-linecap="round"/>'
    '<circle cx="16" cy="16" r="3.4" fill="#3D3FE0"/></svg>Roundtable</div>'
    '<div class="rt-side-sub">Guidewire pre-APD decision support</div>',
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")
st.sidebar.markdown('<div class="rt-side-head">Decision briefs</div>', unsafe_allow_html=True)

all_briefs = api_list_briefs()

selected_brief_id: Optional[int] = None

if all_briefs:
    brief_options = {
        f"#{b['id']} - {b['title']} ({b['claims_status']})": b["id"]
        for b in all_briefs
    }
    # A brief generated on the last run opens straight away (set before the picker is drawn)
    open_id = st.session_state.pop("open_brief_id", None)
    open_label = next((lbl for lbl, bid in brief_options.items() if bid == open_id), None)
    if open_label:
        st.session_state.brief_picker = open_label
    selected_label = st.sidebar.selectbox(
        "Open a brief",
        options=list(brief_options.keys()),
        index=0,
        key="brief_picker",
    )
    if selected_label:
        selected_brief_id = brief_options[selected_label]
else:
    st.sidebar.info("No saved briefs yet. Generate your first brief on the right.")

st.sidebar.markdown("---")
st.sidebar.markdown(
    '<div class="rt-side-head">Architecture principles</div>'
    + "".join(
        f'<div class="rt-principle"><i></i><div><b>{name}</b><span>{desc}</span></div></div>'
        for name, desc in (
            ("Numbers", "Python / SQL only"),
            ("RAG", "Qualitative sources only"),
            ("Citations", "Strictly verified"),
            ("Sign-off", "Human-in-the-loop"),
        )
    ),
    unsafe_allow_html=True,
)

# ===========================================================================
# SESSION STATE & AUTHENTICATION MANAGEMENT
# ===========================================================================
if "current_view" not in st.session_state:
    st.session_state.current_view = "home"  # "home" | "claims" | "actuarial" | "login"
if "is_authenticated" not in st.session_state:
    st.session_state.is_authenticated = False
if "user_role" not in st.session_state:
    st.session_state.user_role = "Claims Lead"
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "pending_view" not in st.session_state:
    st.session_state.pending_view = "claims"

# ===========================================================================
# TOP SAAS NAVBAR (ChronoTask / Outcrowd Inspired Header)
# ===========================================================================
st.markdown("""
<style>
/* Top Navigation Bar: text links centred, pill actions on the right */
.navbar-brand {
    font-size: 1.2rem;
    font-weight: 700;
    color: #121318;
    letter-spacing: -0.02em;
    display: flex;
    align-items: center;
    gap: 8px;
}
.st-key-nav_home .stButton > button[kind], .st-key-nav_claims .stButton > button[kind], .st-key-nav_actuarial .stButton > button[kind] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: #121318 !important;
}
.st-key-nav_home .stButton > button[kind] p, .st-key-nav_claims .stButton > button[kind] p, .st-key-nav_actuarial .stButton > button[kind] p {
    font-size: 0.9rem !important;
    font-weight: 500 !important;
    color: #121318 !important;
}
.st-key-nav_home .stButton > button[kind="primary"] p, .st-key-nav_claims .stButton > button[kind="primary"] p, .st-key-nav_actuarial .stButton > button[kind="primary"] p {
    font-weight: 700 !important;
    text-decoration: underline;
    text-decoration-color: #3D3FE0;
    text-decoration-thickness: 2px;
    text-underline-offset: 6px;
}
.st-key-nav_home .stButton > button[kind]:hover p, .st-key-nav_claims .stButton > button[kind]:hover p, .st-key-nav_actuarial .stButton > button[kind]:hover p {
    color: #3D3FE0 !important;
}
.st-key-nav_signin .stButton > button[kind], .st-key-nav_signout .stButton > button[kind] {
    border-radius: 999px !important;
    font-weight: 600 !important;
}
.st-key-nav_signin .stButton > button[kind] {
    background: #121318 !important;
    border: 1px solid #121318 !important;
}
.st-key-nav_signin .stButton > button[kind] p { color: #FFFFFF !important; }
.st-key-nav_signout .stButton > button[kind] {
    background: #FFFFFF !important;
    border: 1px solid #BFC2D3 !important;
}
.user-badge {
    background: #ECEDFC;
    color: #3D3FE0;
    border: 1px solid #D6D8FA;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.76rem;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

nav_col1, nav_col2, nav_col3, nav_col4, nav_col5, nav_col6 = st.columns([2.8, 0.8, 0.8, 0.9, 2.4, 1.0])

with nav_col1:
    st.markdown('<div class="navbar-brand" style="padding-top: 6px;"><svg width="26" height="26" viewBox="0 0 32 32" fill="none" aria-hidden="true"><circle cx="16" cy="16" r="11" stroke="#121318" stroke-width="3.2"/><path d="M5 16a11 11 0 0 1 11-11" stroke="#3D3FE0" stroke-width="3.2" stroke-linecap="round"/><circle cx="16" cy="16" r="3.4" fill="#3D3FE0"/></svg>Roundtable</div>', unsafe_allow_html=True)

with nav_col2:
    if st.button("Home", key="nav_home", use_container_width=True, type=("primary" if st.session_state.current_view == "home" else "secondary")):
        st.session_state.current_view = "home"
        st.rerun()

with nav_col3:
    if st.button("Claims", key="nav_claims", use_container_width=True, type=("primary" if st.session_state.current_view == "claims" else "secondary")):
        if st.session_state.is_authenticated:
            st.session_state.current_view = "claims"
        else:
            st.session_state.pending_view = "claims"
            st.session_state.current_view = "login"
        st.rerun()

with nav_col4:
    if st.button("Actuarial", key="nav_actuarial", use_container_width=True, type=("primary" if st.session_state.current_view == "actuarial" else "secondary")):
        if st.session_state.is_authenticated:
            st.session_state.current_view = "actuarial"
        else:
            st.session_state.pending_view = "actuarial"
            st.session_state.current_view = "login"
        st.rerun()

with nav_col5:
    if st.session_state.is_authenticated:
        st.markdown(f'<div style="text-align: right; padding-top: 8px;"><span class="user-badge">👤 {st.session_state.user_role}</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="text-align: right; padding-top: 8px; color: #5B5F6E; font-size: 0.82rem; font-weight: 500;">Enterprise access</div>', unsafe_allow_html=True)

with nav_col6:
    if st.session_state.is_authenticated:
        if st.button("Sign Out", key="nav_signout", use_container_width=True):
            st.session_state.is_authenticated = False
            st.session_state.current_view = "home"
            st.rerun()
    else:
        if st.button("Sign In", key="nav_signin", type="primary", use_container_width=True):
            st.session_state.pending_view = "claims"
            st.session_state.current_view = "login"
            st.rerun()

if st.session_state.current_view != "home":
    st.markdown("<hr style='margin: 0.5rem 0 1.2rem 0; opacity: 0.5;'>", unsafe_allow_html=True)

# ===========================================================================
# VIEW: LOGIN SCREEN
# ===========================================================================
if st.session_state.current_view == "login":
    def _sign_in(email: str, role: str, view: str) -> None:
        st.session_state.is_authenticated = True
        st.session_state.user_email = email
        st.session_state.user_role = role
        st.session_state.current_view = view
        st.rerun()

    _, login_mid, _ = st.columns([0.5, 6, 0.5])
    with login_mid, st.container(key="login_card"):
        form_col, art_col = st.columns([1, 1.1], gap="large")
        with form_col:
            st.markdown(
                '<span class="rt-eyebrow"><i></i>Enterprise access</span>'
                '<div class="rt-ws-title" style="font-size:2.1rem">Sign in to Roundtable</div>'
                '<p class="rt-ws-sub" style="margin-bottom:1.4rem">Use your enterprise credentials to open the '
                'Claims and Actuarial intelligence workspaces.</p>',
                unsafe_allow_html=True,
            )
            auth_email = st.text_input("Work email", value="analyst@guidewire-carrier.com", placeholder="name@company.com")
            auth_pass = st.text_input("Password", value="••••••••••••", type="password")

            log_btn_col1, log_btn_col2 = st.columns(2)
            with log_btn_col1:
                if st.button("Sign in", type="primary", use_container_width=True):
                    _sign_in(auth_email, "Insurance Specialist", st.session_state.pending_view)
            with log_btn_col2:
                if st.button("Back to home", use_container_width=True):
                    st.session_state.current_view = "home"
                    st.rerun()

            st.markdown('<div class="rt-login-divider"><span>Quick demo access</span></div>', unsafe_allow_html=True)
            demo_c1, demo_c2 = st.columns(2)
            with demo_c1:
                if st.button("Claims Lead", use_container_width=True):
                    _sign_in("claims.lead@carrier.com", "Claims Lead", "claims")
            with demo_c2:
                if st.button("Lead Actuary", use_container_width=True):
                    _sign_in("lead.actuary@carrier.com", "Lead Actuary", "actuarial")

        with art_col:
            stats = portfolio_stats()
            art_cards = ""
            if stats.get("ok"):
                lr = stats["loss_ratio"]
                art_cards = (
                    '<div class="rt-login-card a"><div class="l">Claims analyzed</div>'
                    f'<div class="v">{stats["n_claims"]:,}</div><span class="rt-chip up">SQL verified</span></div>'
                    '<div class="rt-login-card b"><div class="l">Portfolio loss ratio</div>'
                    f'<div class="v" style="color:var(--rt-indigo)">{(f"{lr:.1%}" if lr is not None else "—")}</div></div>'
                )
            st.markdown(
                f'<div class="rt-login-art">{sculpture_svg()}{art_cards}'
                '<div class="rt-login-quote">Every number is computed in Python &amp; SQL. Every claim is cited. '
                'Every brief is signed off by a person.</div></div>',
                unsafe_allow_html=True,
            )

# ===========================================================================
# VIEW: HOME LANDING PAGE
# ===========================================================================
elif st.session_state.current_view == "home":
    def _go_workspace(view: str) -> None:
        if st.session_state.is_authenticated:
            st.session_state.current_view = view
        else:
            st.session_state.pending_view = view
            st.session_state.current_view = "login"
        st.rerun()

    render_home(_go_workspace)

# ===========================================================================
# VIEW: CLAIMS & ACTUARIAL WORKSPACES
# ===========================================================================
elif st.session_state.current_view in ("claims", "actuarial"):
    is_actuarial_view = (st.session_state.current_view == "actuarial")
    workspace_title = "Actuarial intelligence" if is_actuarial_view else "Claims intelligence"
    workspace_caption = (
        "Directional loss estimation and portfolio exposure, computed in SQL and ready for actuarial sign-off."
        if is_actuarial_view else
        "Verified ClaimCenter loss trends, competitor and regulatory evidence, and live research, with human sign-off."
    )
    st.markdown(
        f'<div class="rt-ws-head"><span class="rt-eyebrow"><i></i>{"Actuarial" if is_actuarial_view else "Claims"} workspace'
        f' · {st.session_state.user_role}</span>'
        f'<div class="rt-ws-title">{workspace_title}</div><p class="rt-ws-sub">{workspace_caption}</p></div>',
        unsafe_allow_html=True,
    )
    ws_stats = portfolio_stats()
    if ws_stats.get("ok"):
        ws_lr = ws_stats["loss_ratio"]
        stat_tiles = (
            ("Claims analyzed", f'{ws_stats["n_claims"]:,}', '<span class="rt-chip indigo">ClaimCenter</span>'),
            ("Total incurred", money_short(ws_stats["incurred"]), '<span class="rt-chip up">SQL verified</span>'),
            ("Portfolio loss ratio", f"{ws_lr:.1%}" if ws_lr is not None else "—", '<span class="rt-chip grey">incurred / earned</span>'),
            ("Decision briefs", f"{len(all_briefs):,}", '<span class="rt-chip lime">human sign-off</span>'),
        )
        st.markdown(
            '<div class="rt-stat-row">'
            + "".join(f'<div class="rt-stat"><div class="l">{lbl}{chip}</div><div class="v">{val}</div></div>'
                      for lbl, val, chip in stat_tiles)
            + "</div>",
            unsafe_allow_html=True,
        )

    # -----------------------------------------------------------------------
    # Section 1: New Brief Creation
    # -----------------------------------------------------------------------
    with st.expander("Create New Product Decision Brief", expanded=(not bool(selected_brief_id))):
        available_tags = api_get_tags()
        render_idea_assistant(available_tags)

        col_t, col_tag, col_btn = st.columns([3, 2, 1.2])

        with col_t:
            st.session_state.setdefault("new_brief_title", "EV High-Voltage Battery Coverage Gap")
            prod_title = st.text_input(
                "Product Idea Title",
                key="new_brief_title",
                max_chars=150,
                placeholder="e.g. Cyber Extortion Endorsement or Drone Hull Coverage",
                help="Maximum 150 characters.",
            )

        with col_tag:
            tag_options = [TAG_AUTO] + available_tags
            if st.session_state.get("new_brief_tag") not in tag_options:
                st.session_state.new_brief_tag = TAG_AUTO
            selected_tag_opt = st.selectbox(
                "Underlying Risk Tag",
                options=tag_options,
                key="new_brief_tag",
                help="Optional: select if this matches an existing internal risk pattern. External research will run regardless of selection.",
            )
            st.caption("Optional: select if this matches an existing internal risk pattern. External research will run regardless of selection.")

        with col_btn:
            st.write("")
            st.write("")
            generate_clicked = st.button("Generate Brief", type="primary", use_container_width=True)

        st.session_state.new_brief_proxies = [p for p in st.session_state.get("new_brief_proxies", []) if p in available_tags]
        new_proxy_tags = st.multiselect(
            "Proxy risk patterns (used only if the title matches no risk pattern of its own)",
            options=available_tags,
            key="new_brief_proxies",
            max_selections=3,
            placeholder="Optional — leave empty to auto-suggest from the title",
            help="A brand-new product has no claims history. The claims analysis then pools the claims of these related "
                 "patterns, labelled as proxy data. Leave empty to auto-suggest; if nothing related is found, the "
                 "line-of-business baseline is shown instead.",
        )

        idea_context = st.session_state.get("new_brief_context")
        if idea_context:
            preview = idea_context if len(idea_context) <= 220 else idea_context[:220] + "…"
            use_context = st.checkbox(
                "Attach my idea description as background for the brief",
                value=True, key="new_brief_use_context",
                help="Claude uses it to understand the intended customer and loss. It is never treated as evidence: "
                     "numbers and citations still come only from claims data and research.",
            )
            st.caption(f"“{preview}”")
        else:
            use_context = False

        if generate_clicked:
            if not prod_title.strip():
                st.error("Please provide a valid product title.")
            elif len(prod_title.strip()) > 150:
                st.error("Product Idea Title exceeds maximum limit of 150 characters. Please shorten it.")
            else:
                chosen_tag = None if selected_tag_opt == TAG_AUTO else selected_tag_opt
                with st.spinner("Analyzing claims database and retrieving evidence..."):
                    created = api_create_brief(prod_title.strip(), chosen_tag, new_proxy_tags,
                                               idea_context if use_context else None)
                    if created:
                        # The next idea starts fresh
                        st.session_state.new_brief_context = None
                        st.session_state.idea_chat = []
                        st.session_state.idea_suggestion = None
                        st.session_state.open_brief_id = created["id"]
                        st.success(f"Brief #{created['id']} generated successfully!")
                        st.rerun()

    # -----------------------------------------------------------------------
    # Section 2: Active Brief Review (With Domain Tabs)
    # -----------------------------------------------------------------------
    if selected_brief_id is not None:
        brief = api_get_brief(selected_brief_id)
        if brief:
            # Brief header card: title, tag match, created date and sign-off status
            tag_display = brief.get("tag_value")
            conf = brief.get("match_confidence") or (brief.get("brief_data") or {}).get("match_confidence")
            conf_pct = f"{int(conf * 100)}%" if conf is not None else "N/A"
            matched = bool(tag_display and tag_display != "unmatched")
            head_basis = ((brief.get("brief_data") or {}).get("claims_analytics") or {}).get("basis") or {}
            proxy_label = " + ".join(head_basis.get("proxy_tags") or [])
            basis_chip = (f'<span class="rt-chip warn">Proxy data · {html.escape(proxy_label)}</span>'
                          if head_basis.get("basis") == "proxy" else
                          '<span class="rt-chip warn">Line-of-business baseline only</span>'
                          if head_basis.get("basis") == "line_baseline" else "")
            status = brief.get("claims_status", "Draft")
            badge_class = "status-approved" if status == "Approved" else ("status-rejected" if status == "Rejected" else "status-pending")
            chips = (
                f'<span class="rt-chip {"indigo" if matched else "grey"}">Risk tag · {tag_display if matched else "unmatched"}</span>'
                f'<span class="rt-chip {"up" if matched else "warn"}">Match confidence {conf_pct}'
                f'{"" if matched else " · below 50%"}</span>'
                f'{basis_chip}'
                f'<span class="rt-chip grey">Created {brief["created_at"][:16].replace("T", " ")}</span>'
            )
            st.markdown(
                f'<div class="rt-brief-head"><div><div class="k">Brief #{brief["id"]}</div>'
                f'<div class="t">{html.escape(brief["title"])}</div><div class="chips">{chips}</div></div>'
                f'<div class="status"><small>Sign-off status</small><span class="status-badge {badge_class}">{status.upper()}</span></div></div>',
                unsafe_allow_html=True,
            )
            pm_context = (brief.get("brief_data") or {}).get("idea_context")
            if pm_context:
                with st.expander("PM's idea description (background, not evidence)"):
                    st.markdown(pm_context)

            # Organize tabs according to the selected workspace
            if is_actuarial_view:
                tab_primary, tab_market, tab_underwriting, tab_compliance, tab_external = st.tabs([
                    "Actuarial review",
                    "Competitor intelligence",
                    "Underwriting review",
                    "Regulatory compliance",
                    "Live web research",
                ])
                tab_readiness = tab_guideline = tab_scenarios = tab_letters = None
            else:
                (tab_primary, tab_readiness, tab_guideline, tab_scenarios, tab_letters, tab_market, tab_underwriting,
                 tab_compliance, tab_external) = st.tabs([
                    "Claims review",
                    "Claims readiness",
                    "Handling guideline",
                    "Test scenarios",
                    "Customer letters",
                    "Competitor intelligence",
                    "Underwriting review",
                    "Regulatory compliance",
                    "Live web research",
                ])

            brief_data = brief.get("brief_data") or {}
            internal_ev = brief_data.get("internal_evidence", [])
            dir_est = brief_data.get("directional_estimate", {})
            # Proxy briefs: the estimate is a loss cost per 1,000 exposure-years, not a 12-month total for this product
            is_proxy = head_basis.get("basis") == "proxy"
            proxy_unit = ((brief_data.get("claims_kpis") or {}).get("exposure_unit") or "exposure-years")
            tag_metric = f"Proxy: {proxy_label}" if is_proxy else (brief.get("tag_value") or "Unmatched")
            est_label = f"Proxy loss cost / 1,000 {proxy_unit}" if is_proxy else None

            # ---------------------------------------------------------------
            # PRIMARY TAB (Claims or Actuarial depending on current workspace)
            # ---------------------------------------------------------------
            with tab_primary:
                if is_actuarial_view:
                    st.markdown("### Actuarial Loss Distribution & Directional Exposure")
                    st.caption("Quantitative loss aggregation computed directly via pure SQL queries from verified claims data.")

                    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
                    with m_col1:
                        st.metric(
                            label="Risk Tag",
                            value=tag_metric,
                            help=f"Tag Match Confidence: {conf_pct}",
                        )
                    with m_col2:
                        st.metric(
                            label=est_label or "Directional Next-12-Month Incurred",
                            value=f"\\${dir_est.get('range_low', 0):,.0f} – \\${dir_est.get('range_high', 0):,.0f}" if dir_est else "Not available",
                            help="Directional estimate — not actuarial.",
                        )
                    with m_col3:
                        incident_count = dir_est.get("incident_count") if dir_est else None
                        st.metric(
                            label=f"Proxy claims / 1,000 {proxy_unit}" if is_proxy else "Projected Claims (12 mo)",
                            value=(f"{incident_count:,}" if is_proxy else f"{incident_count:,} claims") if incident_count is not None else "Not available",
                            help="Last-12-month reported claims projected with exposure growth and fitted frequency trend.",
                        )
                    with m_col4:
                        st.metric(
                            label="Loss Calculation Engine",
                            value="Pure SQL / Python",
                            help="Deterministic computation — LLM is NOT used for numbers.",
                        )

                    st.markdown("#### Directional Loss Projection Range")
                    if dir_est:
                        st.write(f"**Calculated Range:** \\${dir_est.get('range_low', 0):,.2f} to \\${dir_est.get('range_high', 0):,.2f}")
                        st.caption(f"**Basis:** {dir_est.get('basis', 'Historical claim volumes and severity distribution.')}")
                    else:
                        st.info("No directional estimate available for this brief.")
                    render_claims_kpis(brief_data.get("claims_kpis") or {})

                    st.markdown(
                        f'<div class="insufficient-evidence">ℹ️ <strong>Actuarial Guardrail:</strong> Numbers are calculated deterministically via SQL. Final loss ratios require Chief Actuary sign-off before APD rate book filing.</div>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown("### Claims Intelligence & Loss Trend Analysis")
                    st.caption("Grounded directly in verified Guidewire ClaimCenter claims data (roundtable.db).")

                    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
                    with m_col1:
                        st.metric(
                            label="Risk Category Tag",
                            value=tag_metric,
                            help=f"Tag Match Confidence: {conf_pct}",
                        )
                    with m_col2:
                        st.metric(
                            label=est_label or "Directional Annual Exposure",
                            value=f"\\${dir_est.get('range_low', 0):,.0f} – \\${dir_est.get('range_high', 0):,.0f}" if dir_est else "Calculated",
                            help="Directional estimate — not actuarial.",
                        )
                    with m_col3:
                        gen_method = brief_data.get("generation_method", "N/A")
                        if gen_method == "anthropic_claude":
                            gen_label = "Claude (Live Web)"
                        elif gen_method == "anthropic_claude_error_fallback":
                            gen_label = "API Error Fallback"
                        elif "offline" in gen_method or gen_method == "offline_deterministic_fallback":
                            gen_label = "Deterministic (Offline)"
                        else:
                            gen_label = gen_method

                        st.metric(
                            label="Generation Engine",
                            value=gen_label,
                        )
                    with m_col4:
                        st.metric(
                            label="Human Sign-Off Required",
                            value="Yes (Mandatory)",
                        )

                    st.markdown("#### Claims Findings")
                    render_edit_status(brief)
                    render_proxy_controls(brief, brief_data, available_tags)
                    if not render_claims_dashboard(
                        brief_data.get("claims_analytics") or {},
                        notes=brief.get("section_notes") or {},
                        save_note=lambda section, text, bid=brief["id"]: api_save_section_note(bid, section, text),
                        key_prefix=f"brief{brief['id']}",
                        locked=brief.get("claims_status") == "Approved",
                    ):
                        # No charts: briefs created before structured analytics were stored, or no internal data at all
                        if "basis" not in (brief_data.get("claims_analytics") or {}):
                            st.caption("Charts are available for briefs generated after the claims-data upgrade — regenerate this brief to see them.")
                        with st.container(border=True, key=f"rtcard_finding_{brief['id']}"):
                            st.markdown(brief["claims_finding_text"].replace("\n• ", "\n\n• "))

                    if internal_ev:
                        with st.expander(f"Verified claims source citations ({sum(len(ev.get('citations', [])) for ev in internal_ev)})"):
                            for ev in internal_ev:
                                for c in ev.get("citations", []):
                                    st.markdown(f"`{c.get('source_url', '')}` — {c.get('claim', '')}")

                    with st.expander("Edit claims finding text for sign-off", expanded=False):
                        st.caption(
                            "This text is the record that gets approved. Edit any section, then Save or Approve below."
                        )
                        edited_claims_text = st.text_area(
                            "Claims Finding Document",
                            value=brief["claims_finding_text"],
                            height=420,
                            key=f"claims_edit_{brief['id']}",
                        )

                    btn_col1, btn_col2, btn_col3, btn_col_space = st.columns([1.2, 1.2, 1.2, 3])

                    with btn_col1:
                        if st.button("Save Edit", key=f"save_{brief['id']}", use_container_width=True):
                            if api_update_claims(brief["id"], edited_claims_text):
                                st.success("Claims finding updated!")
                                st.rerun()

                    with btn_col2:
                        if st.button("Approve", key=f"app_{brief['id']}", type="primary", use_container_width=True):
                            if edited_claims_text != brief["claims_finding_text"]:
                                api_update_claims(brief["id"], edited_claims_text)
                            if api_approve_claims(brief["id"]):
                                st.success("Claims section marked as Approved!")
                                st.rerun()

                    with btn_col3:
                        if st.button("Reject", key=f"rej_{brief['id']}", use_container_width=True):
                            if api_reject_claims(brief["id"]):
                                st.error("Claims section marked as Rejected.")
                                st.rerun()

            # ---------------------------------------------------------------
            # TAB 2: COMPETITOR INTELLIGENCE (Included in both workspaces)
            # ---------------------------------------------------------------
            with tab_market:
                st.markdown("### Competitor Intelligence")
                st.caption("Qualitative market filings retrieved via RAG from verified competitor sources.")

                comp_ev = brief_data.get("competitor_comparison", [])
                if not comp_ev:
                    from backend.rag import retrieve_evidence
                    legacy_comp = retrieve_evidence(f"{brief['title']} {brief['tag_value']}", source_type="competitor", n_results=4, min_score=0.5)
                    if legacy_comp:
                        comp_ev = [
                            {
                                "statement": f"**{d['metadata'].get('source_name')}** — **{d['metadata'].get('product_name')}**\n\n{d.get('text', '').split('Summary:')[-1].strip()}",
                                "citations": [{"source_url": d["metadata"].get("source_url", ""), "claim": f"{d['metadata'].get('source_name')} offers {d['metadata'].get('product_name')}"}]
                            }
                            for d in legacy_comp
                        ]
                    else:
                        comp_ev = [{"statement": "Insufficient evidence — no matching competitor source found.", "citations": []}]

                for idx, ev in enumerate(comp_ev, 1):
                    stmt = ev.get("statement", "")
                    if stmt.startswith("Insufficient evidence"):
                        st.markdown(f'<div class="insufficient-evidence">⚠️ {stmt}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(
                            '<span class="source-badge-curated">📚 Source: Curated Corpus</span>',
                            unsafe_allow_html=True,
                        )
                        st.markdown(stmt)
                        for c in ev.get("citations", []):
                            source_url = c.get("source_url", "")
                            claim_text = c.get("claim", "")
                            st.markdown(
                                f'''<div class="citation-block">
                                    <span class="citation-label">Verified Citation:</span> 
                                    <span class="citation-source">{source_url}</span> — {claim_text}
                                </div>''',
                                unsafe_allow_html=True,
                            )
                        st.markdown("---")

            # ---------------------------------------------------------------
            # TAB 3: UNDERWRITING REVIEW
            # ---------------------------------------------------------------
            with tab_underwriting:
                st.markdown("### Underwriting Review")
                st.info("Underwriting eligibility rules and policy condition guidelines.")
                rec = brief_data.get("recommendation")
                if rec:
                    st.write(f"**Strategic Recommendation:** {rec}")
                else:
                    st.write("**Strategic Recommendation:** Establish conditional endorsement endorsement boundaries before APD line-of-business configuration.")

            # ---------------------------------------------------------------
            # TAB 4: REGULATORY COMPLIANCE
            # ---------------------------------------------------------------
            with tab_compliance:
                st.markdown("### Regulatory Compliance")
                st.caption("Insurance Department bulletins and statutory standards retrieved via RAG.")

                reg_ev = brief_data.get("regulatory_notes", [])
                if not reg_ev:
                    from backend.rag import retrieve_evidence
                    legacy_reg = retrieve_evidence(f"{brief['title']} {brief['tag_value']}", source_type="regulatory", n_results=3, min_score=0.5)
                    if legacy_reg:
                        reg_ev = [
                            {
                                "statement": f"**{d['metadata'].get('source_name')}** — **{d['metadata'].get('product_name')}**\n\n{d.get('text', '').split('Summary:')[-1].strip()}",
                                "citations": [{"source_url": d["metadata"].get("source_url", ""), "claim": f"Guidance from {d['metadata'].get('source_name')}"}]
                            }
                            for d in legacy_reg
                        ]
                    else:
                        reg_ev = [{"statement": "Insufficient evidence — no matching regulatory source found.", "citations": []}]

                for idx, ev in enumerate(reg_ev, 1):
                    stmt = ev.get("statement", "")
                    if stmt.startswith("Insufficient evidence"):
                        st.markdown(f'<div class="insufficient-evidence">⚠️ {stmt}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(
                            '<span class="source-badge-curated">📚 Source: Curated Corpus</span>',
                            unsafe_allow_html=True,
                        )
                        st.markdown(stmt)
                        for c in ev.get("citations", []):
                            source_url = c.get("source_url", "")
                            claim_text = c.get("claim", "")
                            st.markdown(
                                f'''<div class="citation-block">
                                    <span class="citation-label">Verified Citation:</span> 
                                    <span class="citation-source">{source_url}</span> — {claim_text}
                                </div>''',
                                unsafe_allow_html=True,
                            )
                        st.markdown("---")

            # ---------------------------------------------------------------
            # CLAIMS READINESS (Claims workspace only)
            # ---------------------------------------------------------------
            if tab_readiness is not None:
                with tab_readiness:
                    render_readiness(
                        brief,
                        api_get_readiness(brief["id"]),
                        save_item=lambda item_id, fields, bid=brief["id"]: api_update_readiness(bid, item_id, fields),
                    )
                with tab_guideline:
                    render_guideline(
                        brief,
                        api_get_guideline(brief["id"]),
                        draft=lambda bid=brief["id"]: api_draft_guideline(bid),
                        save_section=lambda key, body, bid=brief["id"]: api_save_guideline_section(bid, key, body),
                        approve=lambda bid=brief["id"]: api_approve_guideline(bid),
                    )
                letters_data = api_get_letters(brief["id"])
                with tab_scenarios:
                    render_scenarios(
                        brief,
                        api_get_scenarios(brief["id"]),
                        generate=lambda bid=brief["id"]: api_generate_scenarios(bid),
                        save=lambda sid, fields, bid=brief["id"]: api_save_scenario(bid, sid, fields),
                        letters=letters_data,
                    )
                with tab_letters:
                    render_letters(
                        brief,
                        letters_data,
                        draft=lambda bid=brief["id"]: api_draft_letters(bid),
                        save=lambda key, subject, body, bid=brief["id"]: api_save_letter(bid, key, subject, body),
                        approve=lambda key, bid=brief["id"]: api_approve_letter(bid, key),
                    )

            # ---------------------------------------------------------------
            # TAB 5: LIVE WEB RESEARCH (Formatted Sub-Tabs & Right-Side Reader)
            # ---------------------------------------------------------------
            with tab_external:
                st.markdown("### Live External Market & Web Intelligence")
                st.caption("Categorized external discovery across news articles, industry blogs, government safety/regulatory datasets, actuarial research papers, and competitor filings.")

                ext_status = brief_data.get("external_market_status", "offline")
                ext_err_msg = brief_data.get("external_market_error_message")
                ext_ev = brief_data.get("external_market_evidence", [])

                # No placeholder sources: surface why live research returned nothing
                if ext_status == "error":
                    st.error(ext_err_msg or "Live web research failed for this brief.")
                elif ext_status == "offline":
                    st.warning(ext_err_msg or "Live web research is offline — configure TAVILY_API_KEY in .env.")
                elif ext_err_msg:
                    st.info(ext_err_msg)

                # Categorize items into the 5 target categories
                cat_articles: List[Dict[str, Any]] = []
                cat_blogs: List[Dict[str, Any]] = []
                cat_gov: List[Dict[str, Any]] = []
                cat_research: List[Dict[str, Any]] = []
                cat_competitors: List[Dict[str, Any]] = []
                cat_all: List[Dict[str, Any]] = []

                for item in ext_ev:
                    cat = str(item.get("category", "")).lower()
                    cat_all.append(item)
                    if "blog" in cat or "opinion" in cat or "perspective" in cat:
                        cat_blogs.append(item)
                    elif "gov" in cat or "statut" in cat or "regulat" in cat or "doi" in cat or "naic" in cat or "nhtsa" in cat:
                        cat_gov.append(item)
                    elif "paper" in cat or "study" in cat or "whitepaper" in cat or "academic" in cat or "actuarial" in cat or "research" in cat:
                        cat_research.append(item)
                    elif "competitor" in cat or "offering" in cat or "product" in cat:
                        cat_competitors.append(item)
                    else:
                        cat_articles.append(item)

                # Fallback balancing if a bucket is empty
                if not cat_articles and cat_all:
                    cat_articles = [it for it in cat_all if "news" in str(it.get("source_type", "")).lower()] or cat_all[:2]
                if not cat_gov and cat_all:
                    cat_gov = [it for it in cat_all if "regulatory" in str(it.get("source_type", "")).lower()]
                if not cat_research and cat_all:
                    cat_research = [it for it in cat_all if "report" in str(it.get("source_type", "")).lower()]

                # Top Metrics Ribbon
                m_sub1, m_sub2, m_sub3, m_sub4, m_sub5 = st.columns(5)
                with m_sub1:
                    st.metric("📰 Articles", len(cat_articles), help="Recent news coverage & loss incident reports")
                with m_sub2:
                    st.metric("✍️ Blogs & Opinions", len(cat_blogs), help="Industry analysis & underwriting perspectives")
                with m_sub3:
                    st.metric("🏛️ Gov & Regulatory", len(cat_gov), help="Official safety registries, NAIC & DOI bulletins")
                with m_sub4:
                    st.metric("📑 Research Papers", len(cat_research), help="Peer-reviewed actuarial studies & loss cost models")
                with m_sub5:
                    st.metric("🏢 Competitor Intel", len(cat_competitors), help="Carrier riders, endorsements & policy terms")

                st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

                # Sub-Tabs for each categorized intelligence feed
                sub_articles, sub_blogs, sub_gov, sub_research, sub_competitors, sub_stream = st.tabs([
                    f"📰 Articles & News ({len(cat_articles)})",
                    f"✍️ Blogs & Perspectives ({len(cat_blogs)})",
                    f"🏛️ Government & Regulatory Data ({len(cat_gov)})",
                    f"📑 Research Papers ({len(cat_research)})",
                    f"🏢 Competitor Offerings ({len(cat_competitors)})",
                    f"🌐 All Sources ({len(cat_all)})",
                ])

                # Helper to render the interactive split view: Left list, Right document reader
                def _render_category_split_view(items: List[Dict[str, Any]], category_label: str, tab_key: str):
                    if not items:
                        st.info(f"No {category_label.lower()} currently retrieved for this product. You can run a broader live web search.")
                        return

                    session_selected_key = f"selected_doc_{brief['id']}_{tab_key}"
                    if session_selected_key not in st.session_state or st.session_state[session_selected_key] >= len(items):
                        st.session_state[session_selected_key] = 0

                    current_idx = st.session_state[session_selected_key]
                    selected_item = items[current_idx] if 0 <= current_idx < len(items) else items[0]

                    col_left, col_right = st.columns([1.15, 1.45], gap="medium")

                    # LEFT SIDE: Document Cards List
                    with col_left:
                        st.markdown(f"<div style='font-size: 0.85rem; font-weight: 700; color: #64748B; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.04em;'>📁 Discovered Sources ({len(items)})</div>", unsafe_allow_html=True)
                        
                        for i, it in enumerate(items):
                            s_name = it.get("source_name", "Web Source")
                            p_title = it.get("product_or_initiative_name", "Initiative")
                            summary_short = it.get("summary", "")
                            if len(summary_short) > 130:
                                summary_short = summary_short[:127] + "..."
                            is_active = (i == current_idx)
                            active_border = "border: 2px solid #0073C6; background: #F4F9FD;" if is_active else "border: 1px solid #E2E8F0; background: #FFFFFF;"
                            
                            st.markdown(f"""
                            <div style="{active_border} border-radius: 10px; padding: 12px 14px; margin-bottom: 10px; box-shadow: 0 2px 6px rgba(27,42,74,0.03);">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                                    <span style="font-size: 0.76rem; font-weight: 700; color: #0073C6; text-transform: uppercase;">🏢 {s_name}</span>
                                    <span style="font-size: 0.70rem; color: #94A3B8;">{'🟢 ACTIVE' if is_active else '📄 CITED'}</span>
                                </div>
                                <div style="font-size: 0.90rem; font-weight: 700; color: #1B2A4A; line-height: 1.35; margin-bottom: 6px;">
                                    {p_title}
                                </div>
                                <div style="font-size: 0.80rem; color: #64748B; line-height: 1.4;">
                                    {summary_short}
                                </div>
                            </div>
                            """, unsafe_allow_html=True)

                            btn_label = "📖 Currently Viewing" if is_active else f"📖 Open & Inspect #{i+1}"
                            if st.button(btn_label, key=f"btn_open_{tab_key}_{brief['id']}_{i}", use_container_width=True, type=("primary" if is_active else "secondary")):
                                st.session_state[session_selected_key] = i
                                st.rerun()

                    # RIGHT SIDE: Full Document Inspector & APD Analysis Panel
                    with col_right:
                        st.markdown("<div style='font-size: 0.85rem; font-weight: 700; color: #64748B; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.04em;'>🔍 Document Deep Inspector & APD Impact</div>", unsafe_allow_html=True)
                        
                        doc_source = selected_item.get("source_name", "Unknown Source")
                        doc_title = selected_item.get("product_or_initiative_name", "Market Discovery")
                        doc_summary = selected_item.get("summary", "")
                        doc_url = selected_item.get("url", "")
                        doc_type = selected_item.get("source_type", "market_intelligence").replace("_", " ").title()
                        doc_date = selected_item.get("date_retrieved", "")[:10] or "2026-09-29"
                        is_ins_rel = selected_item.get("is_insurance_related", True)

                        pill_class = "pill-articles"
                        cat_str = str(selected_item.get("category", "")).lower()
                        if "blog" in cat_str: pill_class = "pill-blogs"
                        elif "gov" in cat_str or "statut" in cat_str: pill_class = "pill-government"
                        elif "paper" in cat_str or "study" in cat_str: pill_class = "pill-research"
                        elif "competitor" in cat_str: pill_class = "pill-competitor"

                        st.markdown(f"""
                        <div class="research-inspector-panel">
                            <div class="research-inspector-header">
                                <div>
                                    <span class="research-category-pill {pill_class}">📌 {category_label}</span>
                                    <span style="font-size: 0.76rem; color: #64748B; margin-left: 8px;">Retrieved: {doc_date}</span>
                                </div>
                                <span style="font-size: 0.74rem; background: #EBF8F2; color: #1E7E34; border: 1px solid #C3ECD7; padding: 2px 8px; border-radius: 4px; font-weight: 600;">
                                    ✓ Verified Provenance
                                </span>
                            </div>
                            <h3 style="margin: 0 0 10px 0; color: #1B2A4A; font-size: 1.25rem; font-weight: 800; line-height: 1.3;">
                                {doc_title}
                            </h3>
                            <div style="font-size: 0.85rem; color: #0073C6; font-weight: 600; margin-bottom: 14px;">
                                🏢 Publisher / Authority: <strong>{doc_source}</strong> &nbsp;•&nbsp; Type: <em>{doc_type}</em>
                            </div>
                            <div style="font-size: 0.94rem; color: #2D3748; line-height: 1.6; margin-bottom: 16px; background: #F8FAFC; padding: 14px; border-radius: 8px; border: 1px solid #EDF2F7;">
                                <strong style="color: #1B2A4A;">Executive Abstract & Findings:</strong><br>
                                {doc_summary}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                        # APD Impact & Guidance Box
                        st.markdown(f"""
                        <div class="apd-impact-box">
                            <h5>🛡️ Underwriting & Guidewire APD Actionability</h5>
                            <ul style="margin: 0; padding-left: 18px; color: #4A5568; line-height: 1.5; font-size: 0.84rem;">
                                <li><strong>PolicyCenter Product Model:</strong> Evaluate introducing a dedicated coverage term, sub-limit, or exclusion schedule based on <em>{doc_source}</em> findings.</li>
                                <li><strong>ClaimCenter Loss Intake:</strong> Ensure loss causes and incident question sets capture telemetry/hazard points highlighted in this report.</li>
                                <li><strong>Underwriting Appetite:</strong> Review eligibility boundary thresholds for this product segment.</li>
                            </ul>
                        </div>
                        """, unsafe_allow_html=True)

                        # Direct Launch & Verified URL action
                        if doc_url:
                            st.markdown(f"""
                            <div style="display: flex; gap: 10px; align-items: center; margin-top: 12px;">
                                <a href="{doc_url}" target="_blank" style="display: inline-flex; align-items: center; gap: 6px; background: #0073C6; color: white; padding: 8px 18px; border-radius: 6px; text-decoration: none; font-size: 0.84rem; font-weight: 600; box-shadow: 0 2px 6px rgba(0,115,198,0.25);">
                                    🔗 Open Live Source Webpage ↗
                                </a>
                                <span style="font-size: 0.78rem; color: #64748B; font-family: monospace; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-width: 260px;">
                                    {doc_url}
                                </span>
                            </div>
                            """, unsafe_allow_html=True)

                        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
                        with st.expander("Copy Standard Citation String", expanded=False):
                            cite_str = f"[{doc_source}] \"{doc_title}\". Retrieved from {doc_url} on {doc_date}. Validated for Guidewire APD decision brief #{brief['id']}."
                            st.code(cite_str, language="markdown")

                # Render each sub-tab
                with sub_articles:
                    _render_category_split_view(cat_articles, "News & Industry Articles", "articles")

                with sub_blogs:
                    _render_category_split_view(cat_blogs, "Blogs & Market Perspectives", "blogs")

                with sub_gov:
                    _render_category_split_view(cat_gov, "Government & Regulatory Data", "gov")

                with sub_research:
                    _render_category_split_view(cat_research, "Research Papers & Studies", "research")

                with sub_competitors:
                    # SERFF blocks automated access, so filed rates/forms are a manual lookup
                    st.caption(
                        "Carrier web pages show marketed coverage only. For filed rates, rules and policy forms, "
                        "search competitor filings by state in [SERFF Filing Access](https://filingaccess.serff.com/sfa/home/)."
                    )
                    _render_category_split_view(cat_competitors, "Competitor Offerings & Products", "competitors")

                with sub_stream:
                    _render_category_split_view(cat_all, "All Discovered Sources", "all")
    else:
        st.info("Select or create a Product Decision Brief in the sidebar or above to view findings.")

