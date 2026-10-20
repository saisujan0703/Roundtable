"""
Parametric pricing
==================
Prices a parametric cover: a fixed payout per policy when an event's index crosses a trigger, instead of
indemnity for the actual loss. Claims history cannot price that alone, so the trigger probability comes from two
sources, credibility-weighted:

  burn       the company's own catastrophe events (claims sharing a cat_code) of the product's perils: per event
             and state, an industry-loss-style index = event incurred per exposure in that state and year ($).
             An event-state "triggers" when its index is at or above the trigger. Annual trigger rate per state =
             triggering event-states / years observed. A few years hold only a handful of events, so
  hazard     the actuary enters annual trigger probabilities per state from a hazard source (NOAA SPC hail
             reports, FEMA flood zones, a wildfire or catastrophe model, a parametric vendor's index history),
             with the source cited. States without an entry use the burn rate.
  blend      p = Z x burn + (1 - Z) x hazard, Z = sqrt(events / FULL_CREDIBILITY_EVENTS)

Rate per policy in state s = payout x p_s x (1 + risk load) / (1 - expense - profit), with
risk load = RISK_MULTIPLE x the coefficient of variation of the book's annual payout (Poisson count of triggering
events), capped — a parametric book pays in lumps, so it carries a capital charge an indemnity average does not.

Basis risk (the main conduct and product risk of parametric cover), measured on history:
  hits          event-states that triggered and had losses
  misses        event-states with losses at or above the material-loss level that did NOT trigger (customers
                with a loss and no payout)
  false alarms  event-states that would have paid with losses below the material level
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional

import pandas as pd

from backend import analytics

FULL_CREDIBILITY_EVENTS = 100
RISK_MULTIPLE = 0.25
MAX_RISK_LOAD_PCT = 50.0
DEFAULTS = {"payout": 25_000.0}   # trigger: median observed event index; material loss: a quarter of it


def events(key: str) -> Dict[str, Any]:
    """Every catastrophe event in the scope, per state, with its index and losses."""
    scope, tc, bc, be = analytics._scope_frames(key)
    cat = tc[tc["cat_code"].notna()]   # the product's own perils: a hail cover is not triggered by a freeze
    expo = be.groupby(["calendar_year", "state"])["earned_exposure"].sum()
    rows = []
    for (code, state), g in cat.groupby(["cat_code", "location"]):
        year = int(g["loss_date"].min().year)
        ex = float(expo.get((year, state), 0.0))
        loss = float(g["claim_amount"].clip(lower=0).sum())
        rows.append({"event": code, "state": state, "year": year, "date": g["loss_date"].min().strftime("%Y-%m-%d"),
                     "claims": int(len(g)), "incurred": round(loss, 0),
                     "exposure": round(ex, 1),
                     "index_per_exposure": round(loss / ex, 3) if ex else None})
    valuation = analytics._data()["valuation"]
    first = bc["loss_date"].min()
    years = max((valuation - first).days / 365.25, 1.0)
    state_expo = be[be["calendar_year"] == be["calendar_year"].max() - (1 if valuation.month < 12 else 0)] \
        .groupby("state")["earned_exposure"].sum()
    return {"scope": scope, "events": rows, "years_observed": round(years, 2),
            "state_exposure": {k: float(v) for k, v in state_expo.items() if v > 0}}


def build(key: str, config: Dict[str, Any], expense_pct: float, profit_pct: float) -> Dict[str, Any]:
    """*config*: trigger_index (event loss per exposure in the state, $), payout per policy, material_loss_index
    (the index at which policyholders have a loss that matters), hazard: [{state, annual_probability, source}]."""
    if not key:
        return {"available": False, "reason": "Parametric pricing needs a risk pattern (direct or proxy) for its scope."}
    ev = events(key)
    observed = sorted(e["index_per_exposure"] for e in ev["events"] if e["index_per_exposure"])
    median = observed[len(observed) // 2] if observed else 1.0
    trig = float(config.get("trigger_index") or median)
    payout = float(config.get("payout") or DEFAULTS["payout"])
    material = float(config.get("material_loss_index") or round(median / 4, 3))
    hazard = {h["state"].upper(): h for h in config.get("hazard") or []}
    years = ev["years_observed"]
    ev_rows = []
    for e in ev["events"]:
        idx = e["index_per_exposure"]
        fires = idx is not None and idx >= trig
        material_loss = idx is not None and idx >= material
        ev_rows.append({**e, "triggers": fires,
                        "basis": "hit" if fires and material_loss else "false alarm" if fires else
                                 "miss" if material_loss else "no loss, no payout"})
    n_events = len({e["event"] for e in ev_rows})
    z = min(1.0, math.sqrt(n_events / FULL_CREDIBILITY_EVENTS))
    states = sorted(set(ev["state_exposure"]) | set(hazard))
    total_expo = sum(ev["state_exposure"].values()) or 1.0
    by_state, lam_book = [], 0.0
    for s in states:
        burn = sum(1 for e in ev_rows if e["state"] == s and e["triggers"]) / years
        h = hazard.get(s)
        hp = float(h["annual_probability"]) if h else None
        p = z * burn + (1 - z) * hp if hp is not None else burn
        share = ev["state_exposure"].get(s, 0.0) / total_expo
        lam_book += p
        by_state.append({"state": s, "exposure_share_pct": round(100 * share, 2), "burn_probability": round(burn, 4),
                         "hazard_probability": hp, "hazard_source": h.get("source") if h else None,
                         "selected_probability": round(p, 4), "expected_payout": round(payout * p, 2), "_share": share})
    # Book: expected number of triggering state-events a year; payouts are lumpy, so load on their variability
    cov = 1 / math.sqrt(lam_book) if lam_book > 0 else None
    risk_load = min(MAX_RISK_LOAD_PCT, 100 * RISK_MULTIPLE * cov) if cov else MAX_RISK_LOAD_PCT
    plr = 1 - (expense_pct + profit_pct) / 100
    for r in by_state:
        r["rate"] = round(r["expected_payout"] * (1 + risk_load / 100) / plr, 2) if plr > 0 else None
    avg_rate = sum(r["rate"] * r["_share"] for r in by_state if r["rate"] is not None)
    avg_expected = sum(r["expected_payout"] * r["_share"] for r in by_state)
    for r in by_state:
        r.pop("_share")
    count = lambda b: sum(1 for e in ev_rows if e["basis"] == b)
    material_n = count("hit") + count("miss")
    notes = [f"{n_events} catastrophe event(s) in {years:.1f} years of data: burn credibility Z = {z:.2f}. "
             + ("Enter hazard probabilities per state to carry the rest of the weight." if not hazard else
                "Hazard probabilities carry the rest of the weight where entered."),
             "Index = event incurred per exposure in the state ($) — an industry-loss-style trigger built "
             "from company claims. A physical trigger (hail size, wind speed, flood depth) needs its own hazard data.",
             "Synthetic demo data: the method is real, the figures are illustrative."]
    if not config.get("trigger_index"):
        notes.insert(0, f"Trigger defaulted to the median observed event index (${median:,.2f} per exposure); set the "
                        "trigger the product will actually use.")
    if not ev["events"]:
        notes.insert(0, "No catastrophe events of this peril in the data: the rate rests entirely on the hazard "
                        "probabilities entered.")
    if material_n:
        notes.append(f"Basis risk: of {material_n} event-state(s) with a material loss, {count('miss')} would NOT have "
                     f"paid (miss rate {100 * count('miss') / material_n:.0f}%). Lower the trigger or add tiers if that "
                     "is too high for customers.")
    return {
        "available": True, "scope": ev["scope"]["description"], "exposure_unit": ev["scope"]["exposure_unit"],
        "config": {"trigger_index": trig, "payout": payout, "material_loss_index": material,
                   "hazard": list(hazard.values())},
        "years_observed": years, "events_observed": n_events, "credibility_z": round(z, 3),
        "expected_payout_per_policy": round(avg_expected, 2), "risk_load_pct": round(risk_load, 1),
        "permissible_loss_ratio": round(plr, 4), "average_rate": round(avg_rate, 2),
        "states": by_state, "events": ev_rows,
        "basis_risk": {"hits": count("hit"), "misses": count("miss"), "false_alarms": count("false alarm"),
                       "miss_rate_pct": round(100 * count("miss") / material_n, 1) if material_n else None},
        "notes": notes,
    }


def validate_config(config: Dict[str, Any]) -> Dict[str, Any]:
    out = {}
    for k, (lo, hi) in {"trigger_index": (0.001, 1e6), "payout": (1.0, 1e7), "material_loss_index": (0.0, 1e6)}.items():
        if config.get(k) is not None:
            v = float(config[k])
            if not lo <= v <= hi:
                raise ValueError(f"{k} must be between {lo} and {hi}.")
            out[k] = v
    hazard: List[Dict[str, Any]] = []
    for h in config.get("hazard") or []:
        state = str(h.get("state", "")).strip().upper()
        if len(state) != 2:
            raise ValueError("Each hazard entry needs a two-letter state.")
        p = float(h.get("annual_probability"))
        if not 0 <= p <= 1:
            raise ValueError("Annual trigger probability must be between 0 and 1.")
        src = str(h.get("source", "")).strip()[:300]
        if not src:
            raise ValueError(f"Cite the hazard source for {state} (e.g. 'NOAA SPC hail ≥ 2in, 1995-2025').")
        hazard.append({"state": state, "annual_probability": p, "source": src})
    out["hazard"] = hazard
    return out
