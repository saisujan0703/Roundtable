"""
Claims Handling Guideline panel
===============================
Drafts the guideline Claims publishes to adjusters before launch (decision tree, FNOL questions,
documentation, reserving, authority, SIU, recoveries, communication, open decisions), lets the
reviewer edit each section, approve it, and download it as Markdown. Drafting lives in
backend/guideline.py; numbers come only from the brief's claims analytics.
"""
from __future__ import annotations

import re
from typing import Any, Callable, Dict, Optional

import streamlit as st

METHOD_LABEL = {
    "anthropic_claude": "Drafted by Claude",
    "anthropic_claude_error_fallback": "Rule-based draft (Claude call failed)",
    "offline_deterministic_fallback": "Rule-based draft (offline)",
}


def _md(text: Optional[str]) -> str:
    return (text or "").replace("$", "\\$")


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "brief"


def render_guideline(brief: Dict[str, Any], data: Optional[Dict[str, Any]],
                     draft: Callable[[], bool], save_section: Callable[[str, str], bool],
                     approve: Callable[[], bool]) -> None:
    """Render the guideline tab. The callables call the backend and return True on success."""
    st.markdown("### Claims Handling Guideline")
    st.caption("The guideline adjusters follow for this coverage: decision tree, FNOL questions, documentation, "
               "reserving, authority, SIU red flags, recoveries and customer communication. Figures come only from this "
               "brief's claims data; anything that depends on the policy wording is left as [TBD] for you to decide.")
    if data is None:
        st.error("Could not load the handling guideline from the backend.")
        return

    g = data.get("guideline")
    bid = brief["id"]
    if not g:
        if brief.get("claims_status") != "Approved":
            st.info("You can draft the guideline now; it can only be approved after the Claims finding is approved.")
        if st.button("📝 Draft handling guideline", type="primary", key=f"gl_draft_{bid}"):
            with st.spinner("Drafting the handling guideline..."):
                if draft():
                    st.rerun()
        return

    approved = g.get("status") == "Approved"
    edited = [s for s in g["sections"] if s["body"] != s.get("original_body")]

    # --- Status bar ---
    c1, c2, c3 = st.columns([1.4, 1, 1])
    c1.markdown(
        f'<span class="status-badge {"status-approved" if approved else "status-pending"}">'
        f'{"APPROVED" if approved else "DRAFT"}</span>&nbsp; '
        f'<span class="rt-chip grey">{METHOD_LABEL.get(g.get("generation_method"), g.get("generation_method"))}</span>'
        + (f'&nbsp;<span class="rt-chip indigo">{len(edited)} section(s) edited</span>' if edited else ""),
        unsafe_allow_html=True,
    )
    c2.download_button("⬇️ Download (.md)", data=data.get("markdown") or "", key=f"gl_dl_{bid}",
                       file_name=f"claims-handling-guideline-{_slug(brief['title'])}.md", mime="text/markdown",
                       use_container_width=True)
    if not approved:
        if c3.button("✅ Approve guideline", type="primary", key=f"gl_approve_{bid}", use_container_width=True,
                     disabled=brief.get("claims_status") != "Approved" or bool(g.get("stale")),
                     help="Requires the Claims finding to be approved first."):
            if approve():
                st.rerun()

    if g.get("stale"):
        st.warning("The brief's claims analysis was re-run after this guideline was drafted, so its figures may be out "
                   "of date. Redraft it before approving.")
    if g.get("basis") == "proxy":
        st.info("This product has no claims of its own: figures in the guideline are **proxy data** from related risk patterns.")
    if approved:
        st.success(f"Approved {(g.get('approved_at') or '')[:16].replace('T', ' ')} UTC. Editing any section reopens it as a Draft.")
    elif brief.get("claims_status") != "Approved":
        st.caption("Approve the Claims finding (Claims review tab) to enable guideline approval.")

    if not approved:
        with st.expander("🔄 Redraft the whole guideline"):
            st.caption("Replaces every section with a fresh draft from the current brief"
                       + (f" — your edits to {len(edited)} section(s) will be lost." if edited else "."))
            if st.button("Redraft", key=f"gl_redraft_{bid}"):
                with st.spinner("Redrafting the handling guideline..."):
                    if draft():
                        st.rerun()

    st.markdown("---")
    # --- Sections ---
    for s in g["sections"]:
        key = f"gl_{bid}_{s['key']}"
        is_edited = s["body"] != s.get("original_body")
        st.markdown(f"#### {s['heading']}" + (" &nbsp;<span class='rt-chip indigo'>edited</span>" if is_edited else ""),
                    unsafe_allow_html=True)
        # Closing the editor after a save is requested by flag: a widget's state can't change once it is drawn
        if st.session_state.pop(f"{key}_close", False):
            st.session_state[f"{key}_toggle"] = False
        if st.toggle("Edit", key=f"{key}_toggle"):
            with st.form(key=f"{key}_form", border=False):
                body = st.text_area("Section text (Markdown)", value=s["body"], height=260, key=f"{key}_body",
                                    label_visibility="collapsed")
                b1, b2 = st.columns([1, 5])
                if b1.form_submit_button("Save", type="primary"):
                    if not body.strip():
                        st.error("A section can't be empty.")
                    elif save_section(s["key"], body):
                        st.session_state[f"{key}_close"] = True
                        st.rerun()
                if is_edited and b2.form_submit_button("Restore generated text"):
                    if save_section(s["key"], s["original_body"]):
                        st.session_state[f"{key}_close"] = True
                        st.rerun()
        else:
            st.markdown(_md(s["body"]))
