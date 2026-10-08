"""
Verification badge
==================
Shows the deterministic post-generation check (backend/verification.py) for a brief, radar signal, guideline or
letter set: a status chip plus an expander with what was checked, what was fixed and what is still flagged.
"""
from __future__ import annotations

from typing import Any, Dict, Optional

import streamlit as st

STATUS = {
    "verified": ("lime", "✓ Verified", "Every number, citation and name in the AI text matched the computed data and sources."),
    "warnings": ("warn", "Verified with warnings", "No errors; some plain numbers couldn't be matched and are worth a look."),
    "issues": ("warn", "Issues flagged", "Some AI text still doesn't match the data. Review the flagged items before sign-off."),
    "replaced": ("indigo", "AI text replaced", "The AI write-up failed verification, so the computed write-up is shown instead."),
    "computed": ("grey", "Computed text", "Written by Python from computed data, with no AI text to check."),
}
CHECK_LABEL = {"numbers": "Number", "citations": "Citation", "trend": "Trend wording", "names": "Name",
               "letters": "Letter rule", "clauses": "Policy clause"}


def _md(text: Optional[str]) -> str:
    return (str(text) if text is not None else "").replace("$", "\\$")


def chip_html(rep: Optional[Dict[str, Any]]) -> str:
    if not rep:
        return ""
    color, label, _ = STATUS.get(rep.get("status"), ("grey", "Not checked", ""))
    if rep.get("status") in ("issues", "warnings"):
        n = rep.get("errors") or rep.get("warnings")
        label = f"{n} issue{'s' if n != 1 else ''} flagged" if rep.get("errors") else f"{n} warning{'s' if n != 1 else ''}"
    return f'<span class="rt-chip {color}">{label}</span>'


def render_verification(rep: Optional[Dict[str, Any]], what: str = "AI text") -> None:
    """Expander with the details. *what* names the artifact ("brief", "write-up", "guideline", "letters")."""
    if not rep:
        return
    _, label, explain = STATUS.get(rep.get("status"), ("grey", "Not checked", ""))
    explain = explain.replace("the AI text", f"the AI-written {what}")
    with st.expander(f"Verification · {label if rep.get('status') not in ('issues', 'warnings') else chip_text(rep)}",
                     expanded=rep.get("status") == "issues"):
        st.markdown(chip_html(rep) + f" &nbsp;{explain}", unsafe_allow_html=True)
        checked = rep.get("checked") or {}
        if checked:
            st.caption("Checked: " + ", ".join(f"{v} {k}" for k, v in checked.items())
                       + f" · rule-based, no AI · {rep.get('checked_at', '')[:16].replace('T', ' ')} UTC"
                       + (" · checked after creation against today's sources" if rep.get("checked_later") else ""))
        if rep.get("actions"):
            st.markdown("**What was fixed automatically**")
            for a in rep["actions"]:
                st.markdown(f"- {_md(a)}")
        if rep.get("issues"):
            st.markdown("**Still flagged for the reviewer**")
            for i in rep["issues"]:
                icon = "⛔" if i["severity"] == "error" else "⚠️"
                st.markdown(f"{icon} **{CHECK_LABEL.get(i['check'], i['check'])} · {_md(i['location'])}:** "
                            f"{_md(i['detail'])}")
                st.caption(_md(i["text"]))


def chip_text(rep: Dict[str, Any]) -> str:
    if rep.get("errors"):
        return f"{rep['errors']} issue{'s' if rep['errors'] != 1 else ''} flagged"
    return f"{rep.get('warnings', 0)} warning{'s' if rep.get('warnings') != 1 else ''}"
