"""
Idea Workflow panels
====================
The PM -> Claims + Actuarial -> PM decision loop:

- render_team_recommendation  in the Claims / Actuarial workspace: the team's recommendation to the PM
- render_pm_board             in the Product workspace: every idea and where it is
- render_pm_decision          in the Product workspace: both recommendations side by side, then Proceed / Revise / Stop

Rules live in backend/workflow.py.
"""
from __future__ import annotations

import html
from typing import Any, Callable, Dict, List, Optional

import pandas as pd
import streamlit as st

STATUS_CHIP = {"In review": "warn", "Ready for decision": "indigo", "Proceed": "up", "Stopped": "grey"}
REC_ICON = {"Support": "✅", "Support with conditions": "☑️", "Do not support": "⛔", None: "⏳"}
DECISION_ICON = {"Proceed": "🟢", "Revise": "🔁", "Stop": "🔴"}


def _md(text: Optional[str]) -> str:
    return (text or "").replace("$", "\\$")


def status_chip(status: str) -> str:
    return f'<span class="rt-chip {STATUS_CHIP.get(status, "grey")}">{html.escape(status)}</span>'


def _review_card(label: str, r: Optional[Dict[str, Any]]) -> None:
    with st.container(border=True):
        if not r:
            st.markdown(f"**{label}** — ⏳ awaiting recommendation")
            return
        st.markdown(f"**{label}** — {REC_ICON.get(r['recommendation'], '')} **{r['recommendation']}**")
        st.caption(f"by {r['reviewer']} · {r['at'][:16].replace('T', ' ')} UTC")
        st.markdown(_md(r["rationale"]))


def _history(wf: Dict[str, Any], teams: Dict[str, str]) -> None:
    if not wf.get("history"):
        return
    with st.expander(f"🕘 Decision history ({len(wf['history'])} round(s))"):
        for h in reversed(wf["history"]):
            d = h["decision"]
            st.markdown(f"**Round {h['round']}** — {DECISION_ICON.get(d['decision'], '')} PM decided **{d['decision']}** "
                        f"({d['by']}, {d['at'][:10]})" + (f": {_md(d['note'])}" if d.get("note") else ""))
            if h.get("revise_notes"):
                st.caption(f"Revision asked for in this round: {_md(h['revise_notes'])}")
            for t, label in teams.items():
                r = h["reviews"].get(t)
                if r:
                    st.caption(f"{label}: {r['recommendation']} ({r['reviewer']}) — {_md(r['rationale'][:300])}")


# ---------------------------------------------------------------------------
# Team workspace
# ---------------------------------------------------------------------------
def render_team_recommendation(brief: Dict[str, Any], team: str, data: Optional[Dict[str, Any]],
                               submit: Callable[[Dict[str, str]], bool]) -> None:
    """The team's recommendation to the PM. *submit({recommendation, reviewer, rationale})* calls the backend."""
    if data is None:
        st.error("Could not load the idea's workflow from the backend.")
        return
    wf, label = data["workflow"], data["teams"][team]
    mine, decided = wf["reviews"].get(team), data["status"] in ("Proceed", "Stopped")
    head = (f"{REC_ICON.get(mine['recommendation'])} {label} recommendation: {mine['recommendation']}" if mine
            else f"⏳ {label} recommendation to the PM — not given yet")
    with st.expander(f"{head} · idea status: {data['status']} (round {data['round']})", expanded=not mine and not decided):
        d = wf.get("decision")
        if d:
            st.info(f"{DECISION_ICON.get(d['decision'], '')} The PM decided **{d['decision']}** "
                    f"({d['by']}, {d['at'][:10]})" + (f": {_md(d['note'])}" if d.get("note") else "."))
        if wf.get("revise_notes") and not decided:
            st.warning(f"🔁 The PM sent this idea back for revision (round {wf['round']}): {_md(wf['revise_notes'])}")
        if decided:
            if mine:
                st.caption(f"Your recommendation: {mine['recommendation']} — {_md(mine['rationale'])}")
            _history(wf, data["teams"])
            return
        st.caption("Review the brief in the tabs below, then tell the PM whether you support the idea and why. You can "
                   "change your recommendation until the PM decides."
                   + (" Supporting it needs the Claims finding approved first (Claims review tab)." if team == "claims"
                      else ""))
        key = f"wf_{brief['id']}_{team}"
        with st.form(key=f"{key}_form", border=False):
            opts = data["recommendations_allowed"]
            a, b = st.columns([1, 1])
            rec = a.selectbox("Recommendation", opts, key=f"{key}_rec",
                              index=opts.index(mine["recommendation"]) if mine else 0)
            reviewer = b.text_input("Reviewer", value=(mine or {}).get("reviewer", ""), key=f"{key}_who",
                                    placeholder=f"e.g. {label} lead")
            rationale = st.text_area("Reasons and any conditions", value=(mine or {}).get("rationale", ""),
                                     key=f"{key}_why", height=110,
                                     placeholder="What the evidence shows, risks, and conditions for supporting it")
            if st.form_submit_button("Send recommendation to PM", type="primary"):
                if submit({"recommendation": rec, "reviewer": reviewer, "rationale": rationale}):
                    st.rerun()
        _history(wf, data["teams"])


# ---------------------------------------------------------------------------
# Product (PM) workspace
# ---------------------------------------------------------------------------
def render_pm_board(briefs: List[Dict[str, Any]]) -> None:
    """Every idea and where it is in the loop."""
    if not briefs:
        st.info("No ideas yet. Submit one above.")
        return
    counts = {s: sum((b.get("workflow") or {}).get("status") == s for b in briefs) for s in STATUS_CHIP}
    cols = st.columns(len(counts))
    for col, (s, n) in zip(cols, counts.items()):
        col.metric(s, n)
    rows = []
    for b in briefs:
        w = b.get("workflow") or {}
        recs = w.get("recommendations") or {}
        rows.append({"#": b["id"], "Idea": b["title"], "Status": w.get("status", "In review"), "Round": w.get("round", 1),
                     "Claims": f"{REC_ICON.get(recs.get('claims'))} {recs.get('claims') or 'awaiting'}",
                     "Actuarial": f"{REC_ICON.get(recs.get('actuarial'))} {recs.get('actuarial') or 'awaiting'}"})
    st.dataframe(pd.DataFrame(rows), hide_index=True, width="stretch")
    st.caption("Open an idea from the sidebar to see both teams' recommendations and decide.")


def render_pm_decision(brief: Dict[str, Any], data: Optional[Dict[str, Any]],
                       decide: Callable[[Dict[str, str]], bool]) -> None:
    """Both recommendations side by side, then the PM's decision. *decide({decision, by, note})* calls the backend."""
    if data is None:
        st.error("Could not load the idea's workflow from the backend.")
        return
    wf, teams, status = data["workflow"], data["teams"], data["status"]
    st.markdown(f"#### Decision — round {data['round']} &nbsp; {status_chip(status)}", unsafe_allow_html=True)
    if wf.get("revise_notes") and status in ("In review", "Ready for decision"):
        st.caption(f"🔁 You asked for a revision: {_md(wf['revise_notes'])}")
    c1, c2 = st.columns(2)
    for col, (t, label) in zip((c1, c2), teams.items()):
        with col:
            _review_card(label, wf["reviews"].get(t))

    d = wf.get("decision")
    if d:
        (st.success if d["decision"] == "Proceed" else st.error)(
            f"{DECISION_ICON.get(d['decision'], '')} You decided **{d['decision']}** ({d['by']}, "
            f"{d['at'][:16].replace('T', ' ')} UTC)" + (f": {_md(d['note'])}" if d.get("note") else "."))
        if d["decision"] == "Proceed":
            st.caption("Launch readiness is now open in the Claims workspace (guideline, letters, test scenarios, "
                       "launch operations); the launch gate decides go-live.")
    elif status == "In review":
        st.info("Waiting for " + " and ".join(teams[t] for t in data["awaiting"]) + " to recommend. You can decide "
                "once both teams have responded.")
    else:
        key = f"pm_{brief['id']}_{data['round']}"
        with st.form(key=f"{key}_form", border=False):
            a, b = st.columns([1, 1])
            decision = a.radio("Your decision", data["decisions_allowed"], key=f"{key}_dec", horizontal=True)
            by = b.text_input("Decided by", key=f"{key}_by", placeholder="e.g. Product Manager")
            note = st.text_area("Notes", key=f"{key}_note", height=100,
                                placeholder="Required for Revise (what the teams should look at again) and Stop (why)")
            st.caption("Proceed opens launch readiness · Revise sends the idea back to both teams for a new round · "
                       "Stop closes the idea.")
            if st.form_submit_button("Record decision", type="primary"):
                if decide({"decision": decision, "by": by, "note": note}):
                    st.rerun()
    _history(wf, teams)
