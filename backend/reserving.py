"""
Loss development
================
Accident-year x development-age triangles for a risk pattern, chain-ladder and Bornhuetter-Ferguson ultimates,
and the development factors the rate indication (backend.pricing) uses in place of a heuristic.

The data has no transaction history (no payment or reserve-change dates), so the triangles are RECONSTRUCTED
from each claim's own dates. At an evaluation date a claim
  - is not in the triangle yet if it was reported after that date,
  - counts at its current incurred (paid + case) if it closed by then, or if the date is the valuation date,
  - otherwise counts at its initial (FNOL) case reserve.
This keeps two real effects, late reporting (IBNR claims) and case reserves developing from FNOL to settlement,
and is labelled as a reconstruction wherever it is shown.

Ages are in months from the start of the accident year: 12 = 31 Dec of the accident year, 24 = a year later, and
so on. The latest diagonal is the valuation date itself (e.g. age 21 for the prior accident year); its
cumulative factor is interpolated in log space between the year-end ages.

Thin patterns develop like the lines they sit in: when the pattern has fewer than MIN_PATTERN_CLAIMS claims the
factors come from every claim in the same scope (lines and powertrain), and that choice is reported.
"""
from __future__ import annotations

import copy
import math
from datetime import date
from functools import lru_cache
from typing import Any, Dict, List, Optional

import pandas as pd

from backend import analytics

MIN_PATTERN_CLAIMS = 300   # fewer claims than this: development factors from the whole scope instead
MAX_TAIL = 1.5


def _r(x, n=4):
    return None if x is None or (isinstance(x, float) and math.isnan(x)) else round(float(x), n)


def _months(ay: int, d: date) -> float:
    """Development age in months of accident year *ay* at date *d* (12 = end of the accident year)."""
    return (d.year - ay) * 12 + d.month - 1 + d.day / 31


def _value_at(c: pd.DataFrame, when: pd.Timestamp, valuation: pd.Timestamp, measure: str) -> pd.Series:
    """Each claim's value at *when*: 0 before it is reported, current incurred once closed (or at the valuation
    date), initial case reserve while open."""
    reported = c["reported_date"] <= when
    if measure == "count":
        return reported.astype(float)
    if when >= valuation:
        current = pd.Series(True, index=c.index)
    else:
        current = c["close_date"].notna() & (c["close_date"] <= when)
    value = c["claim_amount"].where(current, c["initial_reserve"]).fillna(0.0)
    return value.where(reported, 0.0)


def _triangle(c: pd.DataFrame, years: List[int], valuation: pd.Timestamp, measure: str) -> Dict[int, Dict[int, float]]:
    """{accident year: {age at year end: cumulative value}} for every year-end evaluation up to the valuation."""
    tri: Dict[int, Dict[int, float]] = {}
    for ay in years:
        g = c[c["ay"] == ay]
        tri[ay] = {}
        k = 1
        while True:
            when = pd.Timestamp(ay + k - 1, 12, 31)
            if when > valuation:
                break
            tri[ay][12 * k] = float(_value_at(g, when, valuation, measure).sum())
            k += 1
    return tri


def _latest(c: pd.DataFrame, years: List[int], valuation: pd.Timestamp, measure: str) -> Dict[int, float]:
    return {ay: float(_value_at(c[c["ay"] == ay], valuation, valuation, measure).sum()) for ay in years}


def _factors(tri: Dict[int, Dict[int, float]]) -> List[Dict[str, Any]]:
    """Volume-weighted age-to-age factors between consecutive year-end ages."""
    ages = sorted({a for row in tri.values() for a in row})
    out = []
    for a, b in zip(ages, ages[1:]):
        pairs = [(row[a], row[b]) for row in tri.values() if a in row and b in row and row[a] > 0]
        if not pairs:
            continue
        num, den = sum(p[1] for p in pairs), sum(p[0] for p in pairs)
        out.append({"from_age": a, "to_age": b, "factor": num / den if den else 1.0, "years_used": len(pairs),
                    "individual": [round(p[1] / p[0], 4) for p in pairs]})
    return out


def _cdf_table(factors: List[Dict[str, Any]], tail: float) -> Dict[int, float]:
    """Cumulative factor to ultimate at each year-end age (the last age carries only the tail)."""
    if not factors:
        return {12: tail}
    cdf = {factors[-1]["to_age"]: tail}
    running = tail
    for f in reversed(factors):
        running *= max(f["factor"], 0.0) or 1.0
        cdf[f["from_age"]] = running
    return dict(sorted(cdf.items()))


def cdf_at(cdf: Dict[int, float], age: float) -> float:
    """Cumulative factor at any age: log-linear between year-end ages, extrapolated before the first, flat after
    the last."""
    ages = sorted(cdf)
    if age >= ages[-1]:
        return cdf[ages[-1]]
    if len(ages) == 1:
        return cdf[ages[0]]
    lo = max([a for a in ages if a <= age], default=None)
    if lo is None:  # before the first year end: extend the first segment's slope
        lo, hi = ages[0], ages[1]
    else:
        hi = ages[ages.index(lo) + 1]
    w = (age - lo) / (hi - lo)
    return math.exp(math.log(cdf[lo]) + w * (math.log(cdf[hi]) - math.log(cdf[lo])))


def _section(pattern: pd.DataFrame, basis: pd.DataFrame, years: List[int], valuation: pd.Timestamp, measure: str,
             tail: float, exposure: Dict[int, float]) -> Dict[str, Any]:
    tri = _triangle(basis, years, valuation, measure)
    factors = _factors(tri)
    cdf = _cdf_table(factors, tail)
    latest = _latest(pattern, years, valuation, measure)
    val_d = valuation.date()
    rows = []
    for ay in years:
        age = _months(ay, val_d)
        f = cdf_at(cdf, age)
        rows.append({"year": ay, "age_months": round(age, 1), "latest": round(latest[ay], 2), "cdf": round(f, 4),
                     "chain_ladder_ultimate": round(latest[ay] * f, 2),
                     "extrapolated": age < min(cdf), "earned_exposure": round(exposure.get(ay, 0.0), 1)})
    # Bornhuetter-Ferguson: a-priori ultimate per exposure from the mature years' chain-ladder ultimates
    mature = [r for r in rows if r["cdf"] <= 1.25 and r["earned_exposure"] > 0] or [r for r in rows if r["earned_exposure"] > 0]
    expo = sum(r["earned_exposure"] for r in mature)
    apriori = sum(r["chain_ladder_ultimate"] for r in mature) / expo if expo else 0.0
    for r in rows:
        unreported = (1 - 1 / r["cdf"]) if r["cdf"] > 0 else 0.0
        r["bf_ultimate"] = round(r["latest"] + unreported * apriori * r["earned_exposure"], 2)
        r["cl_development"] = round(r["chain_ladder_ultimate"] - r["latest"], 2)
        r["bf_development"] = round(r["bf_ultimate"] - r["latest"], 2)
        r["bf_factor"] = round(r["bf_ultimate"] / r["latest"], 4) if r["latest"] else None
    return {
        "triangle": [{"year": ay, **{str(a): round(v, 2) for a, v in row.items()}} for ay, row in tri.items()],
        "ages": sorted({a for row in tri.values() for a in row}),
        "factors": [{**f, "factor": round(f["factor"], 4)} for f in factors],
        "cdf": {str(a): round(v, 4) for a, v in cdf.items()},
        "tail": tail,
        "apriori_per_exposure": round(apriori, 4),
        "rows": rows,
        "totals": {"latest": round(sum(r["latest"] for r in rows), 2),
                   "chain_ladder_ultimate": round(sum(r["chain_ladder_ultimate"] for r in rows), 2),
                   "bf_ultimate": round(sum(r["bf_ultimate"] for r in rows), 2)},
    }


def development(key: str, tail_factor: float = 1.0) -> Dict[str, Any]:
    """Reported-count and incurred development for risk pattern *key* (one tag or several joined with '+')."""
    tail = round(max(1.0, min(MAX_TAIL, float(tail_factor))), 4)
    return copy.deepcopy(_development(analytics._db_version(), key, tail))


@lru_cache(maxsize=16)
def _development(version: float, key: str, tail: float) -> Dict[str, Any]:
    scope, tc, bc, be = analytics._scope_frames(key)
    if tc.empty:
        return {"has_data": False, "reason": "No claims for this risk pattern."}
    valuation = analytics._data()["valuation"]
    use_pattern = len(tc) >= MIN_PATTERN_CLAIMS
    basis = tc if use_pattern else bc
    years = sorted(int(y) for y in tc["ay"].dropna().unique())
    exposure = {int(k): float(v) for k, v in be.groupby("calendar_year")["earned_exposure"].sum().items()}
    counts = _section(tc, basis, years, valuation, "count", 1.0, exposure)
    incurred = _section(tc, basis, years, valuation, "incurred", tail, exposure)
    ibnr_claims = sum(r["chain_ladder_ultimate"] - r["latest"] for r in counts["rows"])
    notes = ["Triangles are reconstructed from report and close dates (no transaction history): an open claim "
             "carries its FNOL reserve until it closes, then its final incurred. Synthetic demo data.",
             f"Tail factor beyond age {max(incurred['ages'] or [12])} months: {tail:.3f}"
             + (" (no development assumed after the last observed age; select a tail from industry patterns)."
                if tail == 1.0 else " (the actuary's selection).")]
    if not use_pattern:
        notes.insert(0, f"The pattern has {len(tc)} claims (< {MIN_PATTERN_CLAIMS}), so the development factors come "
                        f"from all {len(bc):,} claims in the same scope ({scope['description']}) and are applied to "
                        "the pattern's own claims.")
    if any(r["extrapolated"] for r in incurred["rows"]):
        notes.append("The current accident year is younger than 12 months: its factor is extrapolated and it is "
                     "excluded from pricing.")
    return {
        "has_data": True,
        "valuation_date": valuation.strftime("%Y-%m-%d"),
        "factor_basis": "pattern" if use_pattern else "scope",
        "factor_basis_claims": int(len(basis)),
        "pattern_claims": int(len(tc)),
        "counts": counts,
        "incurred": incurred,
        "ibnr_claims": round(ibnr_claims, 1),
        "ibnr_incurred_cl": round(incurred["totals"]["chain_ladder_ultimate"] - incurred["totals"]["latest"], 2),
        "ibnr_incurred_bf": round(incurred["totals"]["bf_ultimate"] - incurred["totals"]["latest"], 2),
        "notes": notes,
    }


def factors_by_year(dev: Dict[str, Any], method: str = "chain_ladder") -> Dict[str, Dict[int, float]]:
    """{"incurred": {year: factor to ultimate}, "count": {year: factor}} for backend.pricing. *method* chain_ladder
    uses the CDF; bornhuetter_ferguson uses BF ultimate / latest (falls back to the CDF when nothing is reported)."""
    if not dev.get("has_data"):
        return {"incurred": {}, "count": {}}
    inc = {}
    for r in dev["incurred"]["rows"]:
        f = r["bf_factor"] if method == "bornhuetter_ferguson" and r.get("bf_factor") else r["cdf"]
        inc[r["year"]] = f
    return {"incurred": inc, "count": {r["year"]: r["cdf"] for r in dev["counts"]["rows"]}}
