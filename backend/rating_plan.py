"""
Rating plan
===========
Turns the indicated average premium (backend.pricing) into a rate structure the technical note needs:
base rate x territory relativity x class relativities x deductible factor (x increased-limit factor).

Relativities
  frequency   a multivariate Poisson GLM (log link, earned exposure as offset) on the experience years' non-CAT
              claims of the pattern, so correlated variables (state and vehicle age, say) are not double counted
  severity    one-way: the level's mean severity over the pattern's, non-CAT claims capped at the large-loss cap
  credibility each level's relativity is shrunk towards 1.00: selected = raw ^ Z, Z = sqrt(claims / 1,082) for
              frequency and severity separately, so a level with three claims stays near the base
Deductibles   loss elimination: factor(d) = E[(X - d)+] / E[(X - base)+] on ground-up paid losses
              (paid + deductible applied). Losses below a policy's own deductible were never reported, so the
              credits for deductibles lower than the book's are understated; that is stated.
Limits        increased-limit factors ILF(L) = E[min(X, L)] / E[min(X, basic limit)] on the same losses; limits with
              fewer than 10 losses above them are flagged as thin.
Base rate     balanced so the plan reproduces the indicated average premium on the experience exposure mix
              (off-balance factor = exposure-weighted mean of the relativity products).

For incremental pricing the relativities come from the whole pattern's claims (the newly covered claims are too few
to rate on); the risk drivers of the peril are assumed to be the same.
"""
from __future__ import annotations

import math
from functools import lru_cache
from typing import Any, Dict, List, Optional

import numpy as np
import pandas as pd

from backend import analytics
from backend.database import get_connection

FULL_CREDIBILITY_CLAIMS = 1082
VEHICLE_UNITS = {"PersonalAuto", "BusinessAuto"}
AGE_BANDS = [(-5, 2, "0-2 yrs"), (3, 5, "3-5 yrs"), (6, 9, "6-9 yrs"), (10, 200, "10+ yrs")]
LIMITS = [50_000, 100_000, 250_000, 500_000, 1_000_000, 2_500_000, 5_000_000, 10_000_000]   # INR
MIN_STATE_EXPOSURE_SHARE = 0.01   # smaller states are rated as "Other"


def _r(x, n=4):
    return None if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))) else round(float(x), n)


@lru_cache(maxsize=2)
def _exposure_frame(version: tuple) -> pd.DataFrame:
    conn = get_connection()
    try:
        return pd.read_sql(
            "SELECT e.calendar_year, e.product_code, e.state, e.vehicle_powertrain, p.vehicle_year, p.deductible, "
            "SUM(e.earned_exposure) AS earned_exposure FROM earned_exposure e JOIN policies p USING(policy_id) "
            "GROUP BY 1,2,3,4,5,6", conn)
    finally:
        conn.close()


@lru_cache(maxsize=2)
def _deductibles(version: tuple) -> pd.Series:
    conn = get_connection()
    try:
        return pd.read_sql("SELECT policy_id, deductible FROM policies", conn).set_index("policy_id")["deductible"]
    finally:
        conn.close()


def _age_band(age) -> str:
    if age is None or pd.isna(age):
        return "unknown"
    for lo, hi, label in AGE_BANDS:
        if lo <= age <= hi:
            return label
    return "unknown"


def _poisson_glm(cells: pd.DataFrame, variables: List[str], base: Dict[str, str]):
    """IRLS fit of claims ~ variables with log(exposure) offset. Returns ({(var, level): (coef, se)}, info)."""
    cols, names = [np.ones(len(cells))], [("intercept", "")]
    for v in variables:
        for level in sorted(cells[v].unique()):
            if level == base[v]:
                continue
            cols.append((cells[v] == level).astype(float).to_numpy())
            names.append((v, level))
    X = np.column_stack(cols)
    y = cells["claims"].to_numpy(dtype=float)
    offset = np.log(cells["exposure"].to_numpy(dtype=float))
    beta = np.zeros(X.shape[1])
    beta[0] = math.log(max(y.sum(), 0.5) / cells["exposure"].sum())
    ridge = np.full(X.shape[1], 1e-4)
    ridge[0] = 0.0
    converged, it = False, 0
    for it in range(1, 51):
        eta = X @ beta + offset
        mu = np.exp(eta)
        z = eta - offset + (y - mu) / np.maximum(mu, 1e-12)
        XtW = X.T * mu
        new = np.linalg.solve(XtW @ X + np.diag(ridge), XtW @ z)
        if np.max(np.abs(new - beta)) < 1e-8:
            beta, converged = new, True
            break
        beta = new
    mu = np.exp(X @ beta + offset)
    cov = np.linalg.pinv((X.T * mu) @ X + np.diag(ridge))
    se = np.sqrt(np.maximum(np.diag(cov), 0))
    with np.errstate(divide="ignore", invalid="ignore"):
        dev = 2 * np.sum(np.where(y > 0, y * np.log(y / mu), 0) - (y - mu))
    coefs = {names[i]: (float(beta[i]), float(se[i])) for i in range(len(names))}
    return coefs, {"iterations": it, "converged": converged, "deviance": _r(dev, 2), "cells": int(len(cells)),
                   "parameters": int(X.shape[1])}


def _limited_mean(x: np.ndarray, limit: float) -> float:
    return float(np.minimum(x, limit).mean()) if len(x) else 0.0


def build(key: str, indicated_premium: float, experience_years: int, large_loss_cap: float,
          priced_claims: str = "whole_pattern") -> Dict[str, Any]:
    """The rating plan for risk pattern *key*, balanced to *indicated_premium* per exposure."""
    version = analytics._db_version()
    scope, tc, _, _ = analytics._scope_frames(key)
    if tc.empty:
        return {"available": False, "reason": "No claims experience to build a rating plan from."}
    if not indicated_premium:
        return {"available": False, "reason": "The indication is $0 (no incremental cost in the data). Approve a "
                                              "selected rate in Rate indication to build the rating plan around it."}
    valuation = analytics._data()["valuation"]
    full_years = sorted(y for y in tc["ay"].dropna().unique() if y < valuation.year)[-experience_years:]
    if not full_years:
        return {"available": False, "reason": "No complete accident year to rate on."}

    e = _exposure_frame(version)
    e = e[e["product_code"].isin(scope["products"]) & e["calendar_year"].isin(full_years)]
    if scope["powertrain"]:
        e = e[e["vehicle_powertrain"] == scope["powertrain"]]
    c = tc[tc["ay"].isin(full_years) & tc["cat_code"].isna()].copy()
    c["deductible"] = c["policy_id"].map(_deductibles(version))

    vehicle = set(scope["products"]) <= VEHICLE_UNITS
    e = e.assign(vehicle_age=e["calendar_year"] - e["vehicle_year"])
    states = e.groupby("state")["earned_exposure"].sum()
    keep = set(states[states / states.sum() >= MIN_STATE_EXPOSURE_SHARE].index)
    terr = lambda s: s if s in keep else "Other"
    e["territory"] = e["state"].map(terr)
    c["territory"] = c["location"].map(terr)
    variables = [("territory", "Territory (state)")]
    if vehicle:
        e["vehicle_age_band"] = e["vehicle_age"].map(_age_band)
        c["vehicle_age_band"] = c["vehicle_age"].map(_age_band)
        variables.append(("vehicle_age_band", "Vehicle age"))
        if not scope["powertrain"] and e["vehicle_powertrain"].nunique() > 1:
            e["powertrain"] = e["vehicle_powertrain"].fillna("unknown")
            c["powertrain"] = c["vehicle_powertrain"].fillna("unknown")
            variables.append(("powertrain", "Powertrain"))
    if len(scope["products"]) > 1:
        e["product"], c["product"] = e["product_code"], c["product_code"]
        variables.append(("product", "Line of business"))
    names = [v for v, _ in variables]

    expo_cells = e.groupby(names)["earned_exposure"].sum().rename("exposure")
    claim_cells = c.groupby(names).size().rename("claims")
    cells = pd.concat([expo_cells, claim_cells], axis=1).fillna(0.0).reset_index()
    cells = cells[cells["exposure"] > 0]
    base = {v: cells.groupby(v)["exposure"].sum().idxmax() for v in names}
    coefs, glm_info = _poisson_glm(cells, names, base)

    sev_x = c["claim_amount"].fillna(0).clip(lower=0, upper=large_loss_cap)
    c = c.assign(_sev=sev_x)
    sev_all = float(c.loc[c["_sev"] > 0, "_sev"].mean() or 0)
    out_vars, selected = [], {}
    for v, label in variables:
        levels = []
        ex_by = cells.groupby(v)["exposure"].sum()
        n_by = c.groupby(v).size()
        for level in sorted(ex_by.index, key=lambda L: -ex_by[L]):
            n = int(n_by.get(level, 0))
            coef, se = coefs.get((v, level), (0.0, 0.0))
            freq_raw = math.exp(coef)
            z_f = min(1.0, math.sqrt(n / FULL_CREDIBILITY_CLAIMS))
            sev_level = c.loc[(c[v] == level) & (c["_sev"] > 0), "_sev"]
            sev_raw = float(sev_level.mean() / sev_all) if len(sev_level) and sev_all else 1.0
            z_s = min(1.0, math.sqrt(len(sev_level) / FULL_CREDIBILITY_CLAIMS))
            sel = (freq_raw ** z_f) * (sev_raw ** z_s)
            selected[(v, level)] = sel
            levels.append({"level": level, "base": level == base[v], "exposure": _r(ex_by[level], 1), "claims": n,
                           "frequency_glm": _r(freq_raw), "frequency_se": _r(se) if level != base[v] else None,
                           "frequency_significant": bool(level != base[v] and se > 0 and abs(coef / se) >= 2),
                           "frequency_z": _r(z_f, 3), "severity_oneway": _r(sev_raw), "severity_z": _r(z_s, 3),
                           "selected": _r(sel)})
        out_vars.append({"name": v, "label": label, "base_level": base[v], "levels": levels})

    # Off-balance: the plan must reproduce the indicated average premium on the experience exposure mix
    cells["relativity"] = [math.prod(selected[(v, row[v])] for v in names) for _, row in cells.iterrows()]
    off_balance = float((cells["relativity"] * cells["exposure"]).sum() / cells["exposure"].sum())
    base_rate = indicated_premium / off_balance

    # Ground-up losses for deductible and limit factors: paid, non-denied claims, loss + deductible applied
    paid = tc[(tc["claim_amount"] > 0) & (tc["coverage_denied_flag"] == 0)]
    ground_up = (paid["claim_amount"] + paid["deductible_applied"].fillna(0)).to_numpy(dtype=float)
    deductibles = _deductible_table(e, ground_up)
    ilfs = _ilf_table(ground_up)

    rates = cells.assign(rate=base_rate * cells["relativity"])
    w = rates["exposure"] / rates["exposure"].sum()
    order = rates["rate"].argsort().to_numpy()
    cum = np.cumsum(w.to_numpy()[order])
    pct = lambda q: float(rates["rate"].to_numpy()[order][min(np.searchsorted(cum, q), len(order) - 1)])
    territory = next(x for x in out_vars if x["name"] == "territory")
    state_rates = [{"territory": L["level"], "relativity": L["selected"],
                    "rate_at_base_levels": _r(base_rate * L["selected"], 2)} for L in territory["levels"]]

    notes = [f"Relativities from {len(c):,} non-CAT claims of the pattern over AY {full_years[0]}-{full_years[-1]} and "
             f"{cells['exposure'].sum():,.0f} {scope['exposure_unit']}; credibility pulls thin levels towards 1.00.",
             f"States with less than {MIN_STATE_EXPOSURE_SHARE:.0%} of the exposure are rated together as 'Other'.",
             "Deductible credits are understated for deductibles below the book's: losses under a policy's own "
             "deductible were never reported." if deductibles.get("available") else
             "No deductible spread in the data to derive credits from.",
             "Synthetic demo data: the method is real, the figures are illustrative."]
    if priced_claims == "newly_covered":
        notes.insert(0, "The indication prices the newly covered claims; the relativities come from the whole "
                        "pattern's claims (too few newly covered claims to rate on), assuming the same risk drivers.")
    if not glm_info["converged"]:
        notes.append("The frequency GLM did not fully converge; treat its relativities with caution.")
    return {
        "available": True,
        "exposure_unit": scope["exposure_unit"],
        "experience_years": [int(y) for y in full_years],
        "indicated_premium": _r(indicated_premium, 2),
        "off_balance": _r(off_balance),
        "base_rate": _r(base_rate, 2),
        "base_levels": base,
        "variables": out_vars,
        "glm": glm_info,
        "deductibles": deductibles,
        "ilfs": ilfs,
        "state_rates": state_rates,
        "spread": {"p10": _r(pct(0.10), 2), "median": _r(pct(0.50), 2), "p90": _r(pct(0.90), 2),
                   "min": _r(rates["rate"].min(), 2), "max": _r(rates["rate"].max(), 2)},
        "notes": notes,
    }


def _deductible_table(e: pd.DataFrame, x: np.ndarray) -> Dict[str, Any]:
    ded_expo = e.groupby("deductible")["earned_exposure"].sum()
    ded_expo = ded_expo[ded_expo / ded_expo.sum() >= 0.01]
    if len(ded_expo) < 2 or not len(x):
        return {"available": False}
    base = float(ded_expo.idxmax())
    excess = lambda d: float(np.maximum(x - d, 0).mean())
    base_excess = excess(base)
    rows = [{"deductible": float(d), "base": float(d) == base, "exposure_share_pct": _r(100 * s / ded_expo.sum(), 1),
             "loss_elimination_pct": _r(100 * (1 - excess(d) / x.mean()), 1),
             "factor": _r(excess(d) / base_excess) if base_excess else None}
            for d, s in sorted(ded_expo.items())]
    return {"available": True, "base_deductible": base, "losses": int(len(x)), "rows": rows}


def _ilf_table(x: np.ndarray) -> Dict[str, Any]:
    if len(x) < 30:
        return {"available": False, "reason": "Too few paid losses for increased-limit factors."}
    p90 = float(np.quantile(x, 0.9))
    limits = [L for L in LIMITS if L <= 2 * x.max()] or LIMITS[:1]
    basic = max([L for L in limits if L <= p90] or [limits[0]])
    base_mean = _limited_mean(x, basic)
    rows = [{"limit": L, "basic": L == basic, "ilf": _r(_limited_mean(x, L) / base_mean) if base_mean else None,
             "losses_above": int((x > L).sum()), "thin": int((x > L).sum()) < 10} for L in limits]
    return {"available": True, "basic_limit": basic, "losses": int(len(x)), "rows": rows}
