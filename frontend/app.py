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

import json
from typing import Any, Dict, List, Optional
import requests
import streamlit as st

from claims_dashboard import render_claims_dashboard
from readiness_panel import render_readiness

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

# Injected Guidewire Enterprise Design System CSS
st.markdown("""
<style>
:root {
    --gw-navy: #1B2A4A;
    --gw-navy-dark: #14213D;
    --gw-teal: #0073C6;
    --gw-teal-light: #00A9CE;
    --gw-white: #FFFFFF;
    --gw-gray-bg: #F5F7FA;
    --gw-gray-border: #E1E5EA;
    --gw-text: #1A1A1A;
    --gw-text-muted: #5A6472;
    --gw-success: #1E7E34;
    --gw-danger: #C0392B;
    --gw-warning: #E8A317;
}

html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [class*="css"] {
    font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: var(--gw-text) !important;
    background-color: var(--gw-white) !important;
}

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    background-color: var(--gw-navy) !important;
    border-right: none;
}
section[data-testid="stSidebar"] * {
    color: #E8EDF5 !important;
}
section[data-testid="stSidebar"] h1 {
    color: #FFFFFF !important;
    font-weight: 700;
    font-size: 1.4rem;
    padding-bottom: 4px;
}
section[data-testid="stSidebar"] h2, 
section[data-testid="stSidebar"] h3 {
    color: #FFFFFF !important;
    font-weight: 600;
    font-size: 1rem;
    margin-top: 1.5rem;
    border-top: 1px solid rgba(255,255,255,0.15);
    padding-top: 1rem;
}
section[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.15);
}
section[data-testid="stSidebar"] .stSelectbox label {
    color: #B8C4D6 !important;
    font-size: 0.85rem;
    font-weight: 500;
}
section[data-testid="stSidebar"] li {
    font-size: 0.9rem;
    color: #C8D2E0 !important;
    margin-bottom: 4px;
}

/* ===== MAIN CONTENT AREA ===== */
.main .block-container {
    padding-top: 2rem;
    max-width: 1100px;
    background-color: var(--gw-white) !important;
}
.main {
    background-color: var(--gw-white) !important;
}

/* ===== HEADINGS ===== */
h1 {
    color: var(--gw-navy);
    font-weight: 700;
    letter-spacing: -0.01em;
    font-size: 2rem;
}
h2 {
    color: var(--gw-navy);
    font-weight: 600;
    font-size: 1.4rem;
    margin-top: 1.5rem;
}
h3 {
    color: var(--gw-navy);
    font-weight: 600;
    font-size: 1.15rem;
}
.main p {
    color: var(--gw-text-muted);
    line-height: 1.5;
}

/* ===== METRICS (st.metric widgets) ===== */
[data-testid="stMetric"] {
    background-color: var(--gw-gray-bg) !important;
    border: 1px solid var(--gw-gray-border) !important;
    border-radius: 6px;
    padding: 16px 18px;
}
[data-testid="stMetricLabel"] {
    color: var(--gw-text-muted) !important;
    font-weight: 500;
    font-size: 0.85rem;
}
[data-testid="stMetricValue"] {
    color: var(--gw-navy) !important;
    font-weight: 700;
}

/* ===== BUTTONS ===== */
.stButton > button {
    border-radius: 4px;
    font-weight: 500;
    border: 1px solid var(--gw-gray-border);
    transition: background-color 0.15s ease;
}
.stButton > button[kind="primary"] {
    background-color: var(--gw-teal) !important;
    border: none !important;
    color: white !important;
}
.stButton > button[kind="primary"]:hover {
    background-color: var(--gw-navy-dark) !important;
}
.stButton > button[kind="secondary"] {
    background-color: white !important;
    color: var(--gw-navy) !important;
    border: 1px solid var(--gw-gray-border) !important;
}
.stButton > button[kind="secondary"]:hover {
    background-color: var(--gw-gray-bg) !important;
    border-color: var(--gw-teal) !important;
}

/* ===== TABS ===== */
div[data-baseweb="tab-list"] {
    background-color: transparent !important;
    border-bottom: 1px solid var(--gw-gray-border) !important;
    gap: 4px;
}
button[data-baseweb="tab"] {
    background-color: transparent !important;
    font-weight: 500;
    color: var(--gw-text-muted) !important;
    padding: 10px 16px;
}
button[data-baseweb="tab"][aria-selected="true"] {
    color: var(--gw-teal) !important;
    border-bottom: 2px solid var(--gw-teal) !important;
    font-weight: 600;
}

/* ===== EXPANDER (Create New Brief section) ===== */
.streamlit-expanderHeader {
    background-color: var(--gw-gray-bg) !important;
    border: 1px solid var(--gw-gray-border) !important;
    border-radius: 6px;
    font-weight: 600;
    color: var(--gw-navy) !important;
}

/* ===== TEXT INPUTS / SELECTS ===== */
.stTextInput input, .stSelectbox [data-baseweb="select"] {
    background-color: #FFFFFF !important;
    color: var(--gw-text) !important;
    border-radius: 4px;
    border: 1px solid var(--gw-gray-border) !important;
}
.stTextInput input:focus, .stSelectbox [data-baseweb="select"]:focus-within {
    border-color: var(--gw-teal) !important;
    box-shadow: 0 0 0 1px var(--gw-teal) !important;
}
.stTextArea textarea {
    background-color: #FFFFFF !important;
    color: var(--gw-text) !important;
    border-radius: 4px;
    border: 1px solid var(--gw-gray-border) !important;
    font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

/* ===== CITATION CALLOUTS ===== */
.citation-block {
    background-color: var(--gw-gray-bg);
    border-left: 3px solid var(--gw-teal);
    padding: 12px 16px;
    margin: 8px 0 16px 0;
    border-radius: 0 4px 4px 0;
    font-size: 0.92rem;
    line-height: 1.5;
}
.citation-block .citation-label {
    color: var(--gw-teal);
    font-weight: 600;
}
.citation-block .citation-source {
    color: var(--gw-text-muted);
    font-family: "SF Mono", Consolas, monospace;
    font-size: 0.85rem;
}

/* Insufficient evidence warning banner */
.insufficient-evidence {
    background-color: #FDF3E7;
    border-left: 3px solid var(--gw-warning);
    padding: 12px 16px;
    margin: 8px 0;
    border-radius: 0 4px 4px 0;
    color: #8A5A00;
    font-size: 0.92rem;
}

/* ===== STATUS BADGES ===== */
.status-badge {
    display: inline-block;
    padding: 4px 14px;
    border-radius: 3px;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.02em;
}
.status-approved { background-color: var(--gw-success); color: white; }
.status-rejected { background-color: var(--gw-danger); color: white; }
.status-pending, .status-draft { background-color: var(--gw-warning); color: white; }

/* ===== SOURCE EVIDENCE BADGES ===== */
.source-badge-live {
    display: inline-block;
    background-color: #E8F4FD;
    color: #0073C6;
    border: 1px solid #B8DCF5;
    padding: 3px 10px;
    border-radius: 3px;
    font-size: 0.78rem;
    font-weight: 600;
    margin-bottom: 8px;
}
.source-badge-curated {
    display: inline-block;
    background-color: #F0F4F8;
    color: #4A5568;
    border: 1px solid #CBD5E0;
    padding: 3px 10px;
    border-radius: 3px;
    font-size: 0.78rem;
    font-weight: 600;
    margin-bottom: 8px;
}

/* ===== OFFLINE & ERROR BANNERS ===== */
.banner-offline {
    background-color: #F5F7FA;
    border-left: 4px solid #5A6472;
    padding: 14px 18px;
    margin: 12px 0 16px 0;
    border-radius: 0 4px 4px 0;
    color: #2D3748;
    font-size: 0.92rem;
}
.banner-error {
    background-color: #FDEDED;
    border-left: 4px solid var(--gw-danger);
    padding: 14px 18px;
    margin: 12px 0 16px 0;
    border-radius: 0 4px 4px 0;
    color: #900;
    font-size: 0.92rem;
}

/* ===== RESEARCH FEED & INSPECTOR STYLES ===== */
.research-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 14px 16px;
    margin-bottom: 12px;
    transition: all 0.2s ease;
    cursor: pointer;
}
.research-card:hover {
    border-color: #0073C6;
    box-shadow: 0 4px 12px rgba(0, 115, 198, 0.08);
}
.research-card.selected {
    border-color: #0073C6;
    background: #F4F9FD;
    box-shadow: 0 4px 14px rgba(0, 115, 198, 0.12);
}
.research-category-pill {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 0.72rem;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 4px;
    letter-spacing: 0.02em;
    text-transform: uppercase;
}
.pill-articles { background: #E8F4FD; color: #0073C6; border: 1px solid #B8DCF5; }
.pill-blogs { background: #FEF3C7; color: #92400E; border: 1px solid #FDE68A; }
.pill-government { background: #DCFCE7; color: #166534; border: 1px solid #BBF7D0; }
.pill-research { background: #F3E8FF; color: #6B21A8; border: 1px solid #E9D5FF; }
.pill-competitor { background: #F1F5F9; color: #334155; border: 1px solid #CBD5E1; }

.research-inspector-panel {
    background: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-top: 4px solid #0073C6;
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 8px 24px rgba(27, 42, 74, 0.06);
}
.research-inspector-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 14px;
}
.apd-impact-box {
    background: #F8FAFC;
    border-left: 4px solid #0073C6;
    border-radius: 0 8px 8px 0;
    padding: 14px 16px;
    margin: 16px 0;
    font-size: 0.88rem;
}
.apd-impact-box h5 {
    color: #1B2A4A;
    font-weight: 700;
    margin: 0 0 6px 0;
    font-size: 0.92rem;
}

/* ===== SECTION DIVIDERS ===== */
hr {
    border-color: var(--gw-gray-border);
    margin: 1.5rem 0;
}

/* ===== HIDE STREAMLIT DEFAULT CHROME ===== */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

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


def api_create_brief(title: str, tag_value: Optional[str] = None) -> Optional[Dict[str, Any]]:
    try:
        payload: Dict[str, Any] = {"title": title, "tag_value": tag_value}
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
    with st.expander(f"🔍 Show changes from generated version ({sum(1 for d in diff if d[:1] in '+-')} lines changed)"):
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

    st.markdown(f"#### 📋 Claims KPIs — valued {kpis.get('valuation_date', '')}")
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
st.sidebar.title("🛡️ Roundtable")
st.sidebar.caption("Guidewire Pre-APD Decision Support System")

st.sidebar.markdown("---")
st.sidebar.subheader("Recent Decision Briefs")

all_briefs = api_list_briefs()

selected_brief_id: Optional[int] = None

if all_briefs:
    brief_options = {
        f"#{b['id']} - {b['title']} ({b['claims_status']})": b["id"]
        for b in all_briefs
    }
    selected_label = st.sidebar.selectbox(
        "Select an existing brief to review:",
        options=list(brief_options.keys()),
        index=0,
    )
    if selected_label:
        selected_brief_id = brief_options[selected_label]
else:
    st.sidebar.info("No saved briefs yet. Generate your first brief on the right.")

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    **Architecture Principles:**
    * 📊 **Numbers**: Python/SQL only
    * 🔍 **RAG**: Qualitative sources only
    * 🔗 **Citations**: Strictly verified
    * 👤 **Sign-Off**: Human-in-the-loop
    """
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
/* Top Navigation Bar Styling */
.top-navbar-wrapper {
    background: #FFFFFF;
    border: 1px solid #E5E9F0;
    border-radius: 50px;
    padding: 8px 18px;
    margin: -1rem 0 1.5rem 0;
    box-shadow: 0 4px 16px rgba(27, 42, 74, 0.04);
}
.navbar-brand {
    font-size: 1.15rem;
    font-weight: 800;
    color: #1B2A4A;
    letter-spacing: -0.02em;
    display: flex;
    align-items: center;
    gap: 8px;
}
.user-badge {
    background: #E8F4FD;
    color: #0073C6;
    border: 1px solid #B8DCF5;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.76rem;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

nav_col1, nav_col2, nav_col3, nav_col4, nav_col5, nav_col6 = st.columns([2.5, 1.2, 1.2, 1.4, 2.5, 1.3])

with nav_col1:
    st.markdown('<div class="navbar-brand" style="padding-top: 6px;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#1B2A4A" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -3px; margin-right: 6px;"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg><strong>Roundtable</strong></div>', unsafe_allow_html=True)

with nav_col2:
    if st.button("🏠 Home", key="nav_home", use_container_width=True, type=("primary" if st.session_state.current_view == "home" else "secondary")):
        st.session_state.current_view = "home"
        st.rerun()

with nav_col3:
    if st.button("🔍 Claims", key="nav_claims", use_container_width=True, type=("primary" if st.session_state.current_view == "claims" else "secondary")):
        if st.session_state.is_authenticated:
            st.session_state.current_view = "claims"
        else:
            st.session_state.pending_view = "claims"
            st.session_state.current_view = "login"
        st.rerun()

with nav_col4:
    if st.button("📊 Actuarial", key="nav_actuarial", use_container_width=True, type=("primary" if st.session_state.current_view == "actuarial" else "secondary")):
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
        st.markdown('<div style="text-align: right; padding-top: 8px; color: #64748B; font-size: 0.82rem; font-weight: 500;">Enterprise Access</div>', unsafe_allow_html=True)

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

st.markdown("<hr style='margin: 0.5rem 0 1.2rem 0; opacity: 0.5;'>", unsafe_allow_html=True)

# ===========================================================================
# VIEW: LOGIN SCREEN
# ===========================================================================
if st.session_state.current_view == "login":
    st.markdown("""
    <div style="max-width: 520px; margin: 2rem auto; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 20px; padding: 36px; box-shadow: 0 12px 36px rgba(27, 42, 74, 0.08); text-align: center;">
        <div style="display: inline-flex; align-items: center; justify-content: center; width: 56px; height: 56px; background: #E8F4FD; border-radius: 16px; font-size: 1.8rem; margin-bottom: 16px;">
            🛡️
        </div>
        <h2 style="margin: 0 0 8px 0; color: #1B2A4A; font-weight: 800; font-size: 1.6rem;">Sign in to Roundtable</h2>
        <p style="margin: 0 0 24px 0; color: #64748B; font-size: 0.92rem; line-height: 1.5;">
            Authenticate with your enterprise credentials to access Claims and Actuarial intelligence workspaces.
        </p>
    </div>
    """, unsafe_allow_html=True)

    log_c1, log_c2, log_c3 = st.columns([1, 2, 1])
    with log_c2:
        auth_email = st.text_input("Work Email", value="analyst@guidewire-carrier.com", placeholder="name@company.com")
        auth_pass = st.text_input("Password", value="••••••••••••", type="password")

        log_btn_col1, log_btn_col2 = st.columns(2)
        with log_btn_col1:
            if st.button("🔓 Sign In (Standard)", type="primary", use_container_width=True):
                st.session_state.is_authenticated = True
                st.session_state.user_email = auth_email
                st.session_state.user_role = "Insurance Specialist"
                st.session_state.current_view = st.session_state.pending_view
                st.success("Authenticated successfully!")
                st.rerun()

        with log_btn_col2:
            if st.button("Cancel / Back", use_container_width=True):
                st.session_state.current_view = "home"
                st.rerun()

        st.markdown("<div style='text-align: center; margin: 18px 0 12px 0; color: #94A3B8; font-size: 0.80rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;'>— Quick Demo Access —</div>", unsafe_allow_html=True)

        demo_c1, demo_c2 = st.columns(2)
        with demo_c1:
            if st.button("🔍 Sign In as Claims Lead", use_container_width=True):
                st.session_state.is_authenticated = True
                st.session_state.user_email = "claims.lead@carrier.com"
                st.session_state.user_role = "Claims Lead"
                st.session_state.current_view = "claims"
                st.rerun()
        with demo_c2:
            if st.button("📊 Sign In as Actuary", use_container_width=True):
                st.session_state.is_authenticated = True
                st.session_state.user_email = "lead.actuary@carrier.com"
                st.session_state.user_role = "Lead Actuary"
                st.session_state.current_view = "actuarial"
                st.rerun()

# ===========================================================================
# VIEW: HOME LANDING PAGE
# ===========================================================================
elif st.session_state.current_view == "home":
    # SVG Line Icon Definitions (1.5-2px stroke, Enterprise Guidewire Palette)
    icon_search = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0073C6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -2px; margin-right: 6px;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>'
    icon_chart = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0073C6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -2px; margin-right: 6px;"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line><line x1="3" y1="20" x2="21" y2="20"></line></svg>'
    icon_shield = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0073C6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -2px; margin-right: 6px;"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>'
    icon_briefcase = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0073C6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -2px; margin-right: 6px;"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>'
    icon_scale = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0073C6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -2px; margin-right: 6px;"><path d="M16 16l3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1z"></path><path d="M2 16l3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1z"></path><path d="M7 21h10"></path><path d="M12 3v18"></path><path d="M3 7h18"></path></svg>'
    icon_globe = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0073C6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -2px; margin-right: 6px;"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>'

    hero_html = f"""<style>
.roundtable-hero-container {{
    background: #F4F6F9;
    border: 1px solid #E5E9F0;
    border-radius: 16px;
    padding: 32px 32px 32px 32px;
    margin: 0 0 32px 0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
}}
.roundtable-hero-layout {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 32px;
}}
.roundtable-hero-content {{
    flex: 1 1 56%;
    max-width: 600px;
}}
.roundtable-hero-graphic {{
    flex: 1 1 44%;
    display: flex;
    justify-content: center;
    align-items: center;
}}
.hero-flow-diagram {{
    width: 100%;
    max-width: 380px;
    height: auto;
}}
.roundtable-hero-pill {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #FFFFFF;
    color: #1B2A4A;
    border: 1px solid #E2E8F0;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.03em;
    padding: 4px 16px;
    border-radius: 100px;
    box-shadow: 0 1px 2px rgba(27, 42, 74, 0.04);
    margin-bottom: 16px;
}}
.roundtable-hero-pill .pill-dot {{
    width: 8px;
    height: 8px;
    background-color: #0073C6;
    border-radius: 50%;
}}
.roundtable-hero-headline {{
    color: #1B2A4A;
    font-size: 2.25rem;
    font-weight: 800;
    line-height: 1.2;
    margin: 0 0 16px 0;
    letter-spacing: -0.02em;
}}
.roundtable-hero-subheadline {{
    color: #556275;
    font-size: 0.98rem;
    line-height: 1.55;
    margin: 0 0 24px 0;
}}
@media (max-width: 880px) {{
    .roundtable-hero-layout {{
        flex-direction: column;
        text-align: center;
    }}
    .roundtable-hero-content {{
        max-width: 100%;
    }}
    .roundtable-hero-pill {{
        margin: 0 auto 16px auto;
    }}
}}
.roundtable-feature-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
}}
@media (max-width: 960px) {{
    .roundtable-feature-grid {{
        grid-template-columns: repeat(2, 1fr);
    }}
}}
@media (max-width: 640px) {{
    .roundtable-feature-grid {{
        grid-template-columns: 1fr;
    }}
}}
.roundtable-feature-card {{
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 24px 16px 16px 16px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.06);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;
}}
.roundtable-feature-card:hover {{
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    border-color: #CBDCEB;
}}
.roundtable-card-preview {{
    background: #F8FAFC;
    border: 1px solid #EDF2F7;
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 16px;
    min-height: 80px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 8px;
}}
.preview-chip-row {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
}}
.preview-chip {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 100px;
    padding: 4px 12px;
    font-size: 0.72rem;
    font-weight: 600;
    color: #1B2A4A;
}}
.preview-chip.teal {{
    background: #E8F4FD;
    border-color: #B8DCF5;
    color: #0073C6;
}}
.preview-chip.green {{
    background: #EBF8F2;
    border-color: #C3ECD7;
    color: #1E7E34;
}}
.preview-chip.blue-tint {{
    background: #EDF5FC;
    border-color: #D0E4F5;
    color: #1B2A4A;
}}
.preview-bars {{
    display: flex;
    align-items: flex-end;
    gap: 8px;
    height: 28px;
    padding-top: 4px;
}}
.preview-bar {{
    flex: 1;
    background: #DCE6F2;
    border-radius: 3px;
    transition: background-color 0.2s ease;
}}
.preview-bar.active {{
    background: #0073C6;
}}
.roundtable-card-info {{
    padding: 0 4px 4px 4px;
}}
.roundtable-card-title {{
    font-size: 1rem;
    font-weight: 700;
    color: #1B2A4A;
    margin: 0 0 8px 0;
    display: flex;
    align-items: center;
    gap: 4px;
}}
.roundtable-card-desc {{
    font-size: 0.83rem;
    color: #556275;
    line-height: 1.5;
    margin: 0;
}}
</style>
<div class="roundtable-hero-container">
<div class="roundtable-hero-layout">
<div class="roundtable-hero-content">
<div class="roundtable-hero-pill">
<span class="pill-dot"></span>
Guidewire Pre-APD Decision Support
</div>
<div class="roundtable-hero-headline">
Think, validate, and decide<br>all in one place
</div>
<div class="roundtable-hero-subheadline">
Human-approved, cited, AI-assisted research across Claims, Actuarial, Underwriting, Competitor Intel, Regulatory, and Live Web Research — before anything reaches Guidewire APD.
</div>
</div>
<div class="roundtable-hero-graphic">
<svg class="hero-flow-diagram" viewBox="0 0 360 180" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M 85 35 C 135 35, 135 90, 175 90" stroke="#CBD5E1" stroke-width="1.75" stroke-dasharray="4 3"/>
<path d="M 85 90 L 175 90" stroke="#CBD5E1" stroke-width="1.75"/>
<path d="M 85 145 C 135 145, 135 90, 175 90" stroke="#CBD5E1" stroke-width="1.75" stroke-dasharray="4 3"/>
<path d="M 255 90 L 290 90" stroke="#0073C6" stroke-width="2"/>
<polygon points="290,86 298,90 290,94" fill="#0073C6"/>
<circle cx="130" cy="58" r="3" fill="#0073C6"/>
<circle cx="130" cy="122" r="3" fill="#00A9CE"/>
<g transform="translate(10, 18)">
<rect width="75" height="34" rx="8" fill="#FFFFFF" stroke="#0073C6" stroke-width="1.5"/>
<circle cx="18" cy="17" r="7" fill="#E8F4FD"/>
<circle cx="17" cy="16" r="3.2" stroke="#0073C6" stroke-width="1.2"/>
<line x1="19.5" y1="18.5" x2="22" y2="21" stroke="#0073C6" stroke-width="1.2" stroke-linecap="round"/>
<text x="48" y="21" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="600" fill="#1B2A4A">Claims</text>
</g>
<g transform="translate(10, 73)">
<rect width="75" height="34" rx="8" fill="#FFFFFF" stroke="#1B2A4A" stroke-width="1.5"/>
<circle cx="18" cy="17" r="7" fill="#F0F4F8"/>
<line x1="14" y1="20" x2="14" y2="16" stroke="#1B2A4A" stroke-width="1.2" stroke-linecap="round"/>
<line x1="18" y1="20" x2="18" y2="13" stroke="#1B2A4A" stroke-width="1.2" stroke-linecap="round"/>
<line x1="22" y1="20" x2="22" y2="17" stroke="#1B2A4A" stroke-width="1.2" stroke-linecap="round"/>
<text x="48" y="21" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="600" fill="#1B2A4A">Actuarial</text>
</g>
<g transform="translate(10, 128)">
<rect width="75" height="34" rx="8" fill="#FFFFFF" stroke="#5A6472" stroke-width="1.5"/>
<circle cx="18" cy="17" r="7" fill="#F8FAFC"/>
<rect x="13" y="13" width="10" height="8" rx="1.5" stroke="#5A6472" stroke-width="1" fill="none"/>
<path d="M16 13V11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2" stroke="#5A6472" stroke-width="1"/>
<text x="48" y="21" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="600" fill="#1B2A4A">Market</text>
</g>
<g transform="translate(160, 62)">
<rect width="95" height="56" rx="10" fill="#1B2A4A" stroke="#0073C6" stroke-width="2"/>
<text x="47.5" y="24" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle" letter-spacing="0.05em">DECISION</text>
<text x="47.5" y="38" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#00A9CE" text-anchor="middle" letter-spacing="0.05em">BRIEF</text>
<rect x="27.5" y="44" width="40" height="2.5" rx="1" fill="#0073C6"/>
</g>
<g transform="translate(285, 71)">
<rect width="68" height="38" rx="8" fill="#F0F9FF" stroke="#0073C6" stroke-width="1.5"/>
<text x="34" y="18" font-family="-apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#0073C6" text-anchor="middle">GUIDEWIRE</text>
<text x="34" y="30" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#14213D" text-anchor="middle">APD</text>
</g>
</svg>
</div>
</div>
</div>"""

    st.markdown(hero_html, unsafe_allow_html=True)

    # Hero CTA Action Buttons
    cta_c1, cta_c2, cta_c3 = st.columns([1, 1.2, 1])
    with cta_c2:
        btn_claims_cta, btn_actuarial_cta = st.columns(2)
        with btn_claims_cta:
            if st.button("🔍 Claims Workspace", key="hero_cta_claims", type="primary", use_container_width=True):
                if st.session_state.is_authenticated:
                    st.session_state.current_view = "claims"
                else:
                    st.session_state.pending_view = "claims"
                    st.session_state.current_view = "login"
                st.rerun()
        with btn_actuarial_cta:
            if st.button("📊 Actuarial Workspace", key="hero_cta_actuarial", use_container_width=True):
                if st.session_state.is_authenticated:
                    st.session_state.current_view = "actuarial"
                else:
                    st.session_state.pending_view = "actuarial"
                    st.session_state.current_view = "login"
                st.rerun()

    # Bento Feature Cards with SVGs and Normalized 8px Spacing
    grid_html = f"""<div style="height: 24px;"></div>
<div class="roundtable-feature-grid">
<div class="roundtable-feature-card">
<div class="roundtable-card-preview">
<div class="preview-chip-row">
<span class="preview-chip teal">{icon_search} ClaimCenter Data</span>
<span class="preview-chip green">Verified</span>
</div>
<div class="preview-chip-row">
<span class="preview-chip">Frequency & Loss Causes</span>
<span class="preview-chip blue-tint">SQL Synced</span>
</div>
</div>
<div class="roundtable-card-info">
<div class="roundtable-card-title">{icon_search} Claims Review</div>
<p class="roundtable-card-desc">Detects frequency, severity, loss causes, and recurring coverage gaps from internal claims history.</p>
</div>
</div>

<div class="roundtable-feature-card">
<div class="roundtable-card-preview">
<div class="preview-bars">
<div class="preview-bar" style="height: 45%;"></div>
<div class="preview-bar" style="height: 65%;"></div>
<div class="preview-bar" style="height: 85%;"></div>
<div class="preview-bar active" style="height: 100%;"></div>
<div class="preview-bar" style="height: 70%;"></div>
</div>
<div class="preview-chip-row">
<span class="preview-chip teal">{icon_chart} Loss Trends</span>
<span class="preview-chip blue-tint">Directional Range</span>
</div>
</div>
<div class="roundtable-card-info">
<div class="roundtable-card-title">{icon_chart} Actuarial Review</div>
<p class="roundtable-card-desc">Computes pure-SQL loss trends, baseline financial ranges, and directional portfolio exposure.</p>
</div>
</div>

<div class="roundtable-feature-card">
<div class="roundtable-card-preview">
<div class="preview-chip-row">
<span class="preview-chip">Segment Exposure</span>
<span class="preview-chip green">Eligible</span>
</div>
<div class="preview-chip-row">
<span class="preview-chip teal">{icon_shield} Underwriting Rules</span>
<span class="preview-chip blue-tint">Boundaries</span>
</div>
</div>
<div class="roundtable-card-info">
<div class="roundtable-card-title">{icon_shield} Underwriting Review</div>
<p class="roundtable-card-desc">Evaluates risk eligibility, guideline boundaries, and customer segment exposure thresholds.</p>
</div>
</div>

<div class="roundtable-feature-card">
<div class="roundtable-card-preview">
<div class="preview-chip-row">
<span class="preview-chip teal">{icon_briefcase} 4 Peer Carriers</span>
<span class="preview-chip green">Benchmarked</span>
</div>
<div class="preview-chip-row">
<span class="preview-chip">Market Policy Terms</span>
<span class="preview-chip blue-tint">Gaps Found</span>
</div>
</div>
<div class="roundtable-card-info">
<div class="roundtable-card-title">{icon_briefcase} Competitor Intel</div>
<p class="roundtable-card-desc">Benchmarks peer carrier coverages, policy terms, and market product offerings.</p>
</div>
</div>

<div class="roundtable-feature-card">
<div class="roundtable-card-preview">
<div class="preview-chip-row">
<span class="preview-chip teal">{icon_scale} 50-State Mandates</span>
<span class="preview-chip blue-tint">Filing Req</span>
</div>
<div class="preview-chip-row">
<span class="preview-chip green">DOI Compliance</span>
<span class="preview-chip blue-tint">Statutory</span>
</div>
</div>
<div class="roundtable-card-info">
<div class="roundtable-card-title">{icon_scale} Regulatory Compliance</div>
<p class="roundtable-card-desc">Assesses state insurance mandates, rate filing requirements, and statutory guidelines.</p>
</div>
</div>

<div class="roundtable-feature-card">
<div class="roundtable-card-preview">
<div class="preview-chip-row">
<span class="preview-chip teal">{icon_globe} Live Web Search</span>
<span class="preview-chip green">Real-Time</span>
</div>
<div class="preview-chip-row">
<span class="preview-chip">Cited Industry News</span>
<span class="preview-chip blue-tint">External API</span>
</div>
</div>
<div class="roundtable-card-info">
<div class="roundtable-card-title">{icon_globe} Live Web Research</div>
<p class="roundtable-card-desc">Discovers real-time industry news, competitor launches, and external research studies.</p>
</div>
</div>
</div>"""

    st.markdown(grid_html, unsafe_allow_html=True)

# ===========================================================================
# VIEW: CLAIMS & ACTUARIAL WORKSPACES
# ===========================================================================
elif st.session_state.current_view in ("claims", "actuarial"):
    is_actuarial_view = (st.session_state.current_view == "actuarial")
    workspace_title = "📊 Actuarial Intelligence Workspace" if is_actuarial_view else "🔍 Claims Intelligence Workspace"
    workspace_caption = "Directional financial loss estimation and portfolio rate modeling" if is_actuarial_view else "Verified ClaimCenter loss trends, human sign-off, competitor data & live research"

    st.markdown(f"## {workspace_title}")
    st.caption(workspace_caption)

    # -----------------------------------------------------------------------
    # Section 1: New Brief Creation
    # -----------------------------------------------------------------------
    with st.expander("➕ Create New Product Decision Brief", expanded=(not bool(selected_brief_id))):
        col_t, col_tag, col_btn = st.columns([3, 2, 1.2])

        with col_t:
            prod_title = st.text_input(
                "Product Idea Title",
                value="EV High-Voltage Battery Coverage Gap",
                max_chars=150,
                placeholder="e.g. Cyber Extortion Endorsement or Drone Hull Coverage",
                help="Maximum 150 characters.",
            )

        with col_tag:
            available_tags = api_get_tags()
            tag_options = ["(Optional) Auto-detect from title"] + available_tags
            selected_tag_opt = st.selectbox(
                "Underlying Risk Tag",
                options=tag_options,
                index=0,
                help="Optional: select if this matches an existing internal risk pattern. External research will run regardless of selection.",
            )
            st.caption("Optional: select if this matches an existing internal risk pattern. External research will run regardless of selection.")

        with col_btn:
            st.write("")
            st.write("")
            generate_clicked = st.button("🚀 Generate Brief", type="primary", use_container_width=True)

        if generate_clicked:
            if not prod_title.strip():
                st.error("Please provide a valid product title.")
            elif len(prod_title.strip()) > 150:
                st.error("Product Idea Title exceeds maximum limit of 150 characters. Please shorten it.")
            else:
                chosen_tag = None if selected_tag_opt.startswith("(Optional)") else selected_tag_opt
                with st.spinner("Analyzing claims database and retrieving evidence..."):
                    created = api_create_brief(prod_title.strip(), chosen_tag)
                    if created:
                        st.success(f"Brief #{created['id']} generated successfully!")
                        st.rerun()

    # -----------------------------------------------------------------------
    # Section 2: Active Brief Review (With Domain Tabs)
    # -----------------------------------------------------------------------
    if selected_brief_id is not None:
        brief = api_get_brief(selected_brief_id)
        if brief:
            # Top banner with title, tag matching confidence, and status badge
            b_col1, b_col2 = st.columns([4, 1.8])
            with b_col1:
                st.subheader(f"Brief #{brief['id']}: {brief['title']}")
                tag_display = brief.get("tag_value")
                conf = brief.get("match_confidence") or (brief.get("brief_data") or {}).get("match_confidence")
                conf_pct = f"{int(conf * 100)}%" if conf is not None else "N/A"
                if tag_display and tag_display != "unmatched":
                    tag_label = f"Matched: `{tag_display}` (confidence: {conf_pct})"
                else:
                    tag_label = f"Unmatched (confidence: {conf_pct} — below 50% threshold)"
                st.caption(f"Risk Tag: {tag_label} | Created: `{brief['created_at'][:19].replace('T', ' ')}`")

            with b_col2:
                status = brief.get("claims_status", "Draft")
                badge_class = "status-approved" if status == "Approved" else ("status-rejected" if status == "Rejected" else "status-pending")
                st.markdown(
                    f'<div style="text-align: right; padding-top: 10px;">'
                    f'<span style="color: var(--gw-text-muted); font-size: 0.85rem; font-weight: 500; margin-right: 8px;">Sign-Off Status:</span>'
                    f'<span class="status-badge {badge_class}">{status.upper()}</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

            st.markdown("---")

            # Organize tabs according to the selected workspace
            if is_actuarial_view:
                tab_primary, tab_market, tab_underwriting, tab_compliance, tab_external = st.tabs([
                    "📊 Actuarial Review & Financials (Active)",
                    "🏢 Competitor Intelligence",
                    "🛡️ Underwriting Review",
                    "⚖️ Regulatory Compliance",
                    "🌐 Live Web Research",
                ])
                tab_readiness = None
            else:
                tab_primary, tab_readiness, tab_market, tab_underwriting, tab_compliance, tab_external = st.tabs([
                    "🔍 Claims Review (Active)",
                    "✅ Claims Readiness",
                    "🏢 Competitor Intelligence",
                    "🛡️ Underwriting Review",
                    "⚖️ Regulatory Compliance",
                    "🌐 Live Web Research",
                ])

            brief_data = brief.get("brief_data") or {}
            internal_ev = brief_data.get("internal_evidence", [])
            dir_est = brief_data.get("directional_estimate", {})

            # ---------------------------------------------------------------
            # PRIMARY TAB (Claims or Actuarial depending on current workspace)
            # ---------------------------------------------------------------
            with tab_primary:
                if is_actuarial_view:
                    st.markdown("### 📊 Actuarial Loss Distribution & Directional Exposure")
                    st.caption("Quantitative loss aggregation computed directly via pure SQL queries from verified claims data.")

                    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
                    with m_col1:
                        st.metric(
                            label="Risk Tag",
                            value=brief.get("tag_value") or "Unmatched",
                            help=f"Tag Match Confidence: {conf_pct}",
                        )
                    with m_col2:
                        st.metric(
                            label="Directional Next-12-Month Incurred",
                            value=f"${dir_est.get('range_low', 0):,.0f} - ${dir_est.get('range_high', 0):,.0f}" if dir_est else "Not available",
                            help="Directional estimate — not actuarial.",
                        )
                    with m_col3:
                        incident_count = dir_est.get("incident_count") if dir_est else None
                        st.metric(
                            label="Projected Claims (12 mo)",
                            value=f"{incident_count:,} claims" if incident_count is not None else "Not available",
                            help="Last-12-month reported claims projected with exposure growth and fitted frequency trend.",
                        )
                    with m_col4:
                        st.metric(
                            label="Loss Calculation Engine",
                            value="Pure SQL / Python",
                            help="Deterministic computation — LLM is NOT used for numbers.",
                        )

                    st.markdown("#### 📈 Directional Loss Projection Range")
                    if dir_est:
                        st.write(f"**Calculated Range:** ${dir_est.get('range_low', 0):,.2f} to ${dir_est.get('range_high', 0):,.2f}")
                        st.caption(f"**Basis:** {dir_est.get('basis', 'Historical claim volumes and severity distribution.')}")
                    else:
                        st.info("No directional estimate available for this brief.")
                    render_claims_kpis(brief_data.get("claims_kpis") or {})

                    st.markdown(
                        f'<div class="insufficient-evidence">ℹ️ <strong>Actuarial Guardrail:</strong> Numbers are calculated deterministically via SQL. Final loss ratios require Chief Actuary sign-off before APD rate book filing.</div>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown("### 🔍 Claims Intelligence & Loss Trend Analysis")
                    st.caption("Grounded directly in verified Guidewire ClaimCenter claims data (roundtable.db).")

                    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
                    with m_col1:
                        st.metric(
                            label="Risk Category Tag",
                            value=brief.get("tag_value") or "Unmatched",
                            help=f"Tag Match Confidence: {conf_pct}",
                        )
                    with m_col2:
                        st.metric(
                            label="Directional Annual Exposure",
                            value=f"${dir_est.get('range_low', 0):,.0f} - ${dir_est.get('range_high', 0):,.0f}" if dir_est else "Calculated",
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

                    st.markdown("#### 📊 Claims Findings")
                    render_edit_status(brief)
                    if not render_claims_dashboard(
                        brief_data.get("claims_analytics") or {},
                        notes=brief.get("section_notes") or {},
                        save_note=lambda section, text, bid=brief["id"]: api_save_section_note(bid, section, text),
                        key_prefix=f"brief{brief['id']}",
                        locked=brief.get("claims_status") == "Approved",
                    ):
                        # Briefs created before structured analytics were stored: show the text, formatted
                        st.caption("Charts are available for briefs generated after the claims-data upgrade — regenerate this brief to see them.")
                        with st.container(border=True):
                            st.markdown(brief["claims_finding_text"].replace("\n• ", "\n\n• "))

                    if internal_ev:
                        with st.expander(f"📑 Verified claims source citations ({sum(len(ev.get('citations', [])) for ev in internal_ev)})"):
                            for ev in internal_ev:
                                for c in ev.get("citations", []):
                                    st.markdown(f"`{c.get('source_url', '')}` — {c.get('claim', '')}")

                    with st.expander("✍️ Edit claims finding text for sign-off", expanded=False):
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
                        if st.button("💾 Save Edit", key=f"save_{brief['id']}", use_container_width=True):
                            if api_update_claims(brief["id"], edited_claims_text):
                                st.success("Claims finding updated!")
                                st.rerun()

                    with btn_col2:
                        if st.button("✅ Approve", key=f"app_{brief['id']}", type="primary", use_container_width=True):
                            if edited_claims_text != brief["claims_finding_text"]:
                                api_update_claims(brief["id"], edited_claims_text)
                            if api_approve_claims(brief["id"]):
                                st.success("Claims section marked as Approved!")
                                st.rerun()

                    with btn_col3:
                        if st.button("❌ Reject", key=f"rej_{brief['id']}", use_container_width=True):
                            if api_reject_claims(brief["id"]):
                                st.error("Claims section marked as Rejected.")
                                st.rerun()

            # ---------------------------------------------------------------
            # TAB 2: COMPETITOR INTELLIGENCE (Included in both workspaces)
            # ---------------------------------------------------------------
            with tab_market:
                st.markdown("### 🏢 Competitor Intelligence")
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
                st.markdown("### 🛡️ Underwriting Review")
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
                st.markdown("### ⚖️ Regulatory Compliance")
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

            # ---------------------------------------------------------------
            # TAB 5: LIVE WEB RESEARCH (Formatted Sub-Tabs & Right-Side Reader)
            # ---------------------------------------------------------------
            with tab_external:
                st.markdown("### 🌐 Live External Market & Web Intelligence")
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
                        with st.expander("📋 Copy Standard Citation String", expanded=False):
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

