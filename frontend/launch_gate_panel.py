"""
Launch Gate panel
=================
The single go / no-go decision for the coverage: criteria computed from the brief's work products
(finding, guideline, readiness, test scenarios, letters, state compliance) and one sign-off per function.
Logic lives in backend/launch_gate.py.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, Optional

import streamlit as st

STATUS_STYLE = {"GO": ("success", "🟢 GO — every criterion is met and every function has approved."),
                "NO-GO": ("error", "🔴 NO-GO — at least one function has rejected the launch."),
                "NOT READY": ("warning", "🟡 NOT READY — criteria or sign-offs outstanding.")}
DECISION_ICON = {"Approve": "✅", "Approve with conditions": "☑️", "Reject": "⛔"}


def _md(text: Optional[str]) -> str:
    return (text or "").replace("$", "\\$")


def render_launch_gate(brief: Dict[str, Any], data: Optional[Dict[str, Any]],
                       sign: Callable[[str, Dict[str, str]], bool], withdraw: Callable[[str], bool]) -> None:
    """Render the tab. *sign(function, {name, decision, note})* and *withdraw(function)* call the backend."""
    st.markdown("### Launch Gate")
    st.caption("One go / no-go decision for this coverage. The criteria are read from the other tabs and can't be "
               "ticked by hand; each function signs off once they are all met. Changing a signed-off artifact "
               "afterwards makes the approvals stale.")
    if data is None:
        st.error("Could not load the launch gate from the backend.")
        return
    bid = brief["id"]
    kind, text = STATUS_STYLE[data["status"]]
    getattr(st, kind)(text)

    c1, c2 = st.columns(2)
    c1.metric("Criteria met", f"{data['criteria_met']} / {len(data['criteria'])}")
    c2.metric("Current approvals", f"{data['approvals']} / {len(data['functions'])}")
    if data["conditions"]:
        st.info("**Launch conditions:**\n\n" + "\n".join(f"- **{c['function']}:** {_md(c['note'])}"
                                                           for c in data["conditions"]))

    st.markdown("#### Criteria")
    for c in data["criteria"]:
        st.markdown(f"{'✅' if c['passed'] else '❌'} **{c['label']}** — {_md(c['detail'])}")
    all_met = data["criteria_met"] == len(data["criteria"])

    st.markdown("#### Sign-offs")
    for s in data["signoffs"]:
        key = f"lg_{bid}_{s['function']}"
        if s["signed"]:
            stale = " · ⚠️ stale — artifacts changed since" if s["stale"] else ""
            head = f"{DECISION_ICON.get(s['decision'], '')} {s['label']} — {s['decision']} by {s['name']}{stale}"
        else:
            head = f"⚪ {s['label']} — not signed"
        with st.expander(head, expanded=False):
            if s["signed"]:
                st.caption(f"Signed {(s.get('signed_at') or '')[:16].replace('T', ' ')} UTC")
                if s.get("note"):
                    st.markdown(f"**{'Reason' if s['decision'] == 'Reject' else 'Conditions / note'}:** {_md(s['note'])}")
                if s["stale"]:
                    st.warning("The finding, guideline, scenarios, letters or compliance matrix changed after this "
                               "approval. Sign again to confirm it still stands.")
            with st.form(key=f"{key}_form", border=False):
                a, b = st.columns([1, 1])
                name = a.text_input("Name", value=s.get("name", ""), key=f"{key}_name")
                decision = b.selectbox("Decision", data["decisions"], key=f"{key}_decision",
                                       index=data["decisions"].index(s["decision"]) if s["signed"] else 0)
                note = st.text_area("Conditions / reason", value=s.get("note", ""), key=f"{key}_note", height=80,
                                    placeholder="Required for a conditional approval or a rejection")
                if not all_met:
                    st.caption("Approval is enabled once every criterion is met; a rejection can be recorded now.")
                if st.form_submit_button("Sign", type="primary"):
                    if decision != "Reject" and not all_met:
                        st.error("All criteria must be met before approving.")
                    elif sign(s["function"], {"name": name, "decision": decision, "note": note}):
                        st.rerun()
            if s["signed"] and st.button("Withdraw sign-off", key=f"{key}_withdraw"):
                if withdraw(s["function"]):
                    st.rerun()
