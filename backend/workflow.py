"""
Idea Workflow (PM -> Claims + Actuarial -> PM decision)
======================================================
A product idea entered by the PM goes to the Claims and Actuarial workspaces at the same time. Each team
reviews it and gives a recommendation; once both have responded, the PM decides:

  Proceed  launch readiness (guideline, letters, test scenarios, launch operations, launch gate) unlocks
  Revise   the idea goes back to both teams with the PM's notes for a new review round
  Stop     the idea is closed

A team that recommends against the idea does not block it: the PM sees both recommendations and decides.
Every round (reviews and decision) is kept in the history.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

TEAMS = {"claims": "Claims", "actuarial": "Actuarial"}
RECOMMENDATIONS = ("Support", "Support with conditions", "Do not support")
DECISIONS = ("Proceed", "Revise", "Stop")

# Lifecycle states, in order
IN_REVIEW, READY, PROCEED, STOPPED = "In review", "Ready for decision", "Proceed", "Stopped"


def new() -> Dict[str, Any]:
    return {"round": 1, "reviews": {}, "decision": None, "revise_notes": None, "history": []}


def status(wf: Optional[Dict[str, Any]]) -> str:
    wf = wf or new()
    d = wf.get("decision")
    if d and d["decision"] == "Proceed":
        return PROCEED
    if d and d["decision"] == "Stop":
        return STOPPED
    return READY if all(t in wf["reviews"] for t in TEAMS) else IN_REVIEW


def awaiting(wf: Optional[Dict[str, Any]]) -> List[str]:
    """Teams whose recommendation is still missing in the current round."""
    wf = wf or new()
    return [t for t in TEAMS if t not in wf["reviews"]] if status(wf) == IN_REVIEW else []


def summary(wf: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    wf = wf or new()
    return {"status": status(wf), "round": wf["round"], "awaiting": awaiting(wf),
            "recommendations": {t: (wf["reviews"].get(t) or {}).get("recommendation") for t in TEAMS},
            "decision": (wf.get("decision") or {}).get("decision")}


def review(wf: Optional[Dict[str, Any]], team: str, recommendation: str, reviewer: str, rationale: str,
           claims_status: Optional[str] = None) -> Dict[str, Any]:
    """Record (or change) a team's recommendation for the current round, until the PM has decided."""
    wf = wf or new()
    if team not in TEAMS:
        raise KeyError(team)
    if recommendation not in RECOMMENDATIONS:
        raise ValueError(f"recommendation must be one of {RECOMMENDATIONS}")
    if status(wf) in (PROCEED, STOPPED):
        raise PermissionError(f"The PM has already decided ({status(wf)}); recommendations are closed.")
    reviewer, rationale = reviewer.strip()[:120], rationale.strip()[:4000]
    if not reviewer:
        raise ValueError("Enter the reviewer's name.")
    if not rationale:
        raise ValueError("Give the reasons for the recommendation; the PM decides on them.")
    if team == "claims" and recommendation != "Do not support" and claims_status != "Approved":
        raise PermissionError("Approve the Claims finding before supporting the idea.")
    wf["reviews"][team] = {"recommendation": recommendation, "reviewer": reviewer, "rationale": rationale,
                           "at": datetime.utcnow().isoformat()}
    return wf


def decide(wf: Optional[Dict[str, Any]], decision: str, by: str, note: str) -> Dict[str, Any]:
    """The PM's decision on the current round. Needs both teams' recommendations."""
    wf = wf or new()
    if decision not in DECISIONS:
        raise ValueError(f"decision must be one of {DECISIONS}")
    if status(wf) != READY:
        raise PermissionError(
            "Waiting for " + " and ".join(TEAMS[t] for t in awaiting(wf)) + " to recommend."
            if status(wf) == IN_REVIEW else f"This idea is already decided ({status(wf)}).")
    by, note = by.strip()[:120], note.strip()[:4000]
    if not by:
        raise ValueError("Enter the name of the person deciding.")
    if decision != "Proceed" and not note:
        raise ValueError("Explain the decision: what to revise, or why the idea stops.")
    record = {"decision": decision, "by": by, "note": note, "at": datetime.utcnow().isoformat(), "round": wf["round"]}
    wf["history"].append({"round": wf["round"], "reviews": wf["reviews"], "decision": record,
                          "revise_notes": wf.get("revise_notes")})
    if decision == "Revise":
        # Back to both teams for a new round, with the PM's notes
        wf.update(round=wf["round"] + 1, reviews={}, decision=None, revise_notes=note)
    else:
        wf["decision"] = record
    return wf


def is_proceeding(wf: Optional[Dict[str, Any]]) -> bool:
    return status(wf) == PROCEED
