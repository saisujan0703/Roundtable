"""
Audit log panel: who changed what and when, from GET /api/audit (backend.audit).
"""
from __future__ import annotations

from typing import Any, Callable, Dict, Optional

import pandas as pd
import streamlit as st

Call = Callable[..., Optional[Dict[str, Any]]]

OUTCOMES = {"All": None, "Done": "ok", "Refused": "refused"}


def _result(status: int) -> str:
    if status < 300:
        return "Done"
    return {400: "Refused: invalid", 401: "Refused: bad sign-in", 403: "Refused: not allowed",
            404: "Refused: not found", 423: "Refused: locked"}.get(status, f"Failed ({status})")


def render_audit_log(brief: Dict[str, Any], api: Call) -> None:
    st.markdown("### Audit log")
    st.caption("Every change made through Roundtable, done or refused: who, their role, when, what and the values "
               "they sent. Passwords and tokens are never recorded. Entries cannot be edited or deleted.")
    c1, c2, c3 = st.columns([1.4, 1.2, 1])
    scope = c1.radio("Show", [f"This brief (#{brief['id']})", "All activity"], horizontal=True, key="audit_scope")
    outcome = c2.radio("Result", list(OUTCOMES), horizontal=True, key="audit_outcome")
    limit = c3.selectbox("Entries", [100, 500, 1000], key="audit_limit")
    params: Dict[str, Any] = {"limit": limit}
    if OUTCOMES[outcome]:
        params["outcome"] = OUTCOMES[outcome]
    path = f"briefs/{brief['id']}/audit" if scope.startswith("This brief") else "audit"
    data = api("GET", path, params=params)
    if data is None:
        return
    entries = data["entries"]
    if not entries:
        st.info("Nothing recorded yet for this view.")
        return
    df = pd.DataFrame([{
        "When (UTC)": e["at"].replace("T", " ").rstrip("Z"),
        "Who": e.get("name") or e.get("email") or "—",
        "Role": e.get("role") or "—",
        "Action": (e["action"] or "").capitalize(),
        "Brief": f"#{e['brief_id']}" if e.get("brief_id") else "",
        "Result": _result(e["status"]),
        "Details": e.get("detail") or "",
    } for e in entries])
    st.dataframe(df, hide_index=True, use_container_width=True,
                 column_config={"Details": st.column_config.TextColumn(width="large")})
    st.caption(f"{len(entries)} most recent entr{'y' if len(entries) == 1 else 'ies'} shown."
               + (" Older entries exist; raise the number shown to see them." if data.get("next_before_id") else ""))
    st.download_button("Download as CSV", df.to_csv(index=False).encode("utf-8"),
                       file_name=f"roundtable-audit-{'brief-' + str(brief['id']) if path != 'audit' else 'all'}.csv",
                       mime="text/csv", key="audit_csv")
