"""
Customer Letters panel
======================
Letter templates a new coverage needs before launch (acknowledgement, documents request, reservation of
rights, denials, approval), drafted from the handling guideline. Each letter is edited and approved on its
own; merge fields like {{claim_number}} are filled by ClaimCenter when sent. Drafting lives in backend/letters.py.
"""
from __future__ import annotations

import re
from typing import Any, Callable, Dict, Optional

import streamlit as st

METHOD_LABEL = {
    "anthropic_claude": "Drafted by Claude",
    "anthropic_claude_error_fallback": "Template draft (Claude call failed)",
    "google_gemini": "Drafted by Gemini",
    "google_gemini_error_fallback": "Template draft (Gemini call failed)",
    "offline_deterministic_fallback": "Template draft (offline)",
}
SCENARIO_NAMES = {
    "covered": "Covered", "not_purchased": "Not purchased", "excluded": "Excluded", "ambiguous": "Unclear cause",
    "late_notice": "Late notice", "incomplete_proof": "Incomplete proof", "fraud": "SIU red flag",
    "large_loss": "Large loss", "recovery": "Subrogation / salvage",
}


def _md(text: Optional[str]) -> str:
    return (text or "").replace("$", "\\$")


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "brief"


def render_letters(brief: Dict[str, Any], data: Optional[Dict[str, Any]], draft: Callable[[], bool],
                   save: Callable[[str, str, str], bool], approve: Callable[[str], bool]) -> None:
    """Render the letters tab. The callables call the backend and return True on success."""
    st.markdown("### Customer Letter Templates")
    st.caption("The letters adjusters send on this coverage, drafted from the handling guideline. Customer details are "
               "merge fields ClaimCenter fills in when sending; policy clauses and state deadlines are left as [TBD] "
               "for Legal and Compliance. Each letter is approved on its own.")
    if data is None:
        st.error("Could not load the letter templates from the backend.")
        return
    bid = brief["id"]
    if not data["has_guideline"]:
        st.info("Draft the handling guideline first (Handling guideline tab) — the letters follow its decision tree "
                "and documentation list.")
        return

    record = data.get("letters")
    if not record:
        if st.button("✉️ Draft customer letters", type="primary", key=f"lt_draft_{bid}"):
            with st.spinner("Drafting the letter templates..."):
                if draft():
                    st.rerun()
        return

    letters = record["letters"]
    approved = sum(l["status"] == "Approved" for l in letters)
    tbds = sum(l.get("tbd_count", 0) for l in letters)
    c1, c2, c3 = st.columns(3)
    c1.metric("Letters approved", f"{approved} / {len(letters)}")
    c2.metric("Open [TBD] items", tbds)
    c3.markdown(f'<br><span class="rt-chip grey">{METHOD_LABEL.get(record.get("generation_method"), "")}</span>',
                unsafe_allow_html=True)
    if data["stale"]:
        st.warning("The handling guideline changed after these letters were drafted. Redraft them (or edit each one) "
                   "before approving.")
    if not data["guideline_approved"]:
        st.caption("Approve the handling guideline to enable letter approval.")
    if approved == len(letters) and tbds == 0:
        st.success("All letters approved with no open [TBD] items: ready to load into ClaimCenter.")
    elif approved == len(letters):
        st.warning(f"All letters approved, but {tbds} [TBD] item(s) remain — fill them before loading into ClaimCenter.")

    d1, d2 = st.columns([1, 2])
    d1.download_button("⬇️ Download (.md)", data=data.get("markdown") or "", key=f"lt_dl_{bid}", mime="text/markdown",
                       file_name=f"customer-letters-{_slug(brief['title'])}.md", use_container_width=True)
    with d2.expander("🔄 Redraft all letters"):
        if approved and not data["stale"]:
            st.caption("Some letters are approved, so redrafting everything is disabled — edit letters one by one.")
        else:
            st.caption("Replaces every letter with a fresh draft from the current guideline; your edits"
                       + (f" and the {approved} approval(s) given against the old guideline" if approved else "")
                       + " will be lost.")
            if st.button("Redraft", key=f"lt_redraft_{bid}"):
                with st.spinner("Redrafting the letter templates..."):
                    if draft():
                        st.rerun()
    with st.expander("ℹ️ Merge fields ClaimCenter fills in"):
        st.markdown("\n".join(f"- `{{{{{k}}}}}` — {v}" for k, v in data["merge_fields"].items()))

    st.markdown("---")
    for l in letters:
        key = f"lt_{bid}_{l['key']}"
        icon = "✅" if l["status"] == "Approved" else "📝"
        tbd = f" · {l.get('tbd_count', 0)} [TBD]" if l.get("tbd_count") else ""
        with st.expander(f"{icon} {l['name']} — {l['status']}{tbd}"):
            st.caption(f"**When to send:** {_md(l['purpose'])}")
            if l.get("used_in"):
                st.caption("Checked by test scenarios: " + ", ".join(SCENARIO_NAMES.get(c, c) for c in l["used_in"]))

            if st.session_state.pop(f"{key}_close", False):
                st.session_state[f"{key}_toggle"] = False
            if st.toggle("Edit", key=f"{key}_toggle"):
                with st.form(key=f"{key}_form", border=False):
                    subject = st.text_input("Subject", value=l["subject"], key=f"{key}_subject")
                    body = st.text_area("Letter (Markdown)", value=l["body"], height=360, key=f"{key}_body")
                    b1, b2 = st.columns([1, 4])
                    if b1.form_submit_button("Save", type="primary"):
                        if not subject.strip() or not body.strip():
                            st.error("Subject and letter can't be empty.")
                        elif save(l["key"], subject, body):
                            st.session_state[f"{key}_close"] = True
                            st.rerun()
                    if (l["body"] != l["original_body"] or l["subject"] != l["original_subject"]) and \
                            b2.form_submit_button("Restore drafted text"):
                        if save(l["key"], l["original_subject"], l["original_body"]):
                            st.session_state[f"{key}_close"] = True
                            st.rerun()
            else:
                with st.container(border=True):
                    st.markdown(f"**Subject:** {_md(l['subject'])}")
                    st.markdown(_md(l["body"]))

            if l["status"] == "Approved":
                st.success(f"Approved {(l.get('approved_at') or '')[:16].replace('T', ' ')} UTC — editing reopens it.")
            elif st.button("✅ Approve letter", key=f"{key}_approve", type="primary",
                           disabled=not data["guideline_approved"] or data["stale"]):
                if approve(l["key"]):
                    st.rerun()
