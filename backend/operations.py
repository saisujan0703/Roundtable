"""
Launch Operations Plan
======================
The operational, regulatory and financial setup Claims owns before a new coverage launches, computed from
the same claims data as the brief:

- state footprint            where the product's exposure and claims sit (input to the compliance matrix)
- staffing                   adjusters needed, from claim volume, cycle time and today's caseloads (Little's law)
- large losses & reinsurance how many claims a year would cross each candidate reporting threshold; CAT share
- statutory reporting        the NAIC Annual Statement line each exposure type would report to (suggested)
- Medicare Section 111       whether bodily-injury / WC / no-fault payments make MMSEA reporting apply
- litigation                 states where these claims are litigated most (panel counsel)

Every figure is computed here from roundtable.db. Treaty terms, caseload standards and statutory
classifications are business decisions, so they appear as [TBD] or as "suggested — confirm".
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional

import pandas as pd

from backend import analytics

LARGE_LOSS_THRESHOLDS = (500_000, 1_000_000, 2_500_000, 5_000_000, 10_000_000)   # Rs 5 lakh to Rs 1 crore
MIN_STATE_CLAIMS = 10  # per state before a litigation rate is shown

# NAIC Annual Statement lines (Statutory Page 14 / U&I exhibit) by product and exposure type.
_AUTO_PD = {"VehicleDamage", "TowOnly", "LossOfUseDamage"}
_AUTO_LIAB = {"BodilyInjuryDamage", "PropertyDamage", "MedPay"}
_BI_EXPOSURES = {"BodilyInjuryDamage", "MedPay", "LostWages", "WCInjuryDamage"}


def _statement_line(product: str, exposure: str) -> Dict[str, Optional[str]]:
    if product == "PersonalAuto":
        if exposure in _AUTO_PD:
            return {"line": "21.1 Private passenger auto physical damage", "note": None}
        if exposure in _AUTO_LIAB:
            return {"line": "19.2 Other private passenger auto liability",
                    "note": "19.1 (no-fault) if paid as PIP in a no-fault state" if exposure == "MedPay" else None}
    if product == "BusinessAuto":
        if exposure in _AUTO_PD:
            return {"line": "21.2 Commercial auto physical damage", "note": None}
        if exposure in _AUTO_LIAB:
            return {"line": "19.4 Other commercial auto liability",
                    "note": "19.3 (no-fault) if paid as PIP in a no-fault state" if exposure == "MedPay" else None}
    if product == "HOPHomeowners":
        return {"line": "4 Homeowners multiple peril", "note": None}
    if product == "CommercialProperty":
        return {"line": "1 Fire / 2.1 Allied lines", "note": "5.1 Commercial multiple peril if sold in a package"}
    if product == "WorkersComp":
        return {"line": "16 Workers' compensation", "note": None}
    return {"line": None, "note": "[TBD — Statutory Reporting]"}


def _r(x, n=1):
    return None if x is None or pd.isna(x) else round(float(x), n)


# ---------------------------------------------------------------------------
# Which claims the plan stands on (same basis as the brief)
# ---------------------------------------------------------------------------
def resolve_basis(brief: Dict[str, Any]) -> Dict[str, Any]:
    """direct / proxy -> a risk-pattern key; line_baseline -> product lines; none -> nothing to compute."""
    brief = brief or {}
    a = brief.get("claims_analytics") or {}
    b = a.get("basis") or {}
    kind = b.get("basis") or brief.get("analysis_basis")
    known = set(analytics.list_tags())
    tag = brief.get("tag_value")
    if kind == "proxy":
        tags = [t for t in (b.get("proxy_tags") or brief.get("proxy_tags") or []) if t in known]
        if tags:
            return {"basis": "proxy", "key": "+".join(tags), "proxy_tags": tags}
    if kind in (None, "direct") and tag in known:
        return {"basis": "direct", "key": tag}
    lines = b.get("product_lines") or (a.get("line_baseline") or {}).get("products")
    if not lines and brief.get("title"):
        from backend.llm import infer_product_lines
        lines = infer_product_lines(brief["title"])
    if lines:
        return {"basis": "line_baseline", "product_lines": list(lines)}
    return {"basis": "none"}


def _frames(basis: Dict[str, Any]):
    """(claims for this product, claims of its whole scope, earned exposure of the scope) or None."""
    d = analytics._data()
    if basis["basis"] in ("direct", "proxy"):
        _, tc, bc, be = analytics._scope_frames(basis["key"])
        return None if tc.empty else (tc, bc, be)
    if basis["basis"] == "line_baseline":
        c, e = d["claims"], d["earned"]
        lc = c[c["product_code"].isin(basis["product_lines"])]
        return None if lc.empty else (lc, lc, e[e["product_code"].isin(basis["product_lines"])])
    return None


# ---------------------------------------------------------------------------
# Sections
# ---------------------------------------------------------------------------
def state_footprint(tc: pd.DataFrame, be: pd.DataFrame) -> List[Dict[str, Any]]:
    """Every state where the scope earns exposure, with its share of exposure and of this product's claims."""
    expo = be.groupby("state")["earned_exposure"].sum()
    expo = expo[expo > 0]
    total = float(expo.sum()) or 1.0
    claims = tc.groupby("location").size()
    rows = [{"state": st, "exposure_share_pct": _r(100 * ex / total), "claims": int(claims.get(st, 0)),
             "claims_share_pct": _r(100 * claims.get(st, 0) / max(len(tc), 1))} for st, ex in expo.items()]
    return sorted(rows, key=lambda r: -r["exposure_share_pct"])


def staffing(tc: pd.DataFrame, bc: pd.DataFrame, valuation: pd.Timestamp, volume_factor: float = 1.0,
             caseload: Optional[float] = None) -> Dict[str, Any]:
    """Adjusters needed = average open inventory / caseload per adjuster.

    Open inventory follows Little's law: claims reported per year x average days open / 365. The annual volume
    is the last 12 months of reported claims, scaled by *volume_factor* (expected uptake of the new coverage vs
    today's pattern). The caseload default is today's median open claims (whole book) per adjuster
    who handles this scope.
    """
    recent = tc[tc["reported_date"] > valuation - pd.Timedelta(days=365)]
    annual = len(recent)
    closed = tc[tc["claim_state"] == "closed"]
    cycle = (closed["close_date"] - closed["reported_date"]).dt.days
    if annual == 0 or cycle.empty:
        return {"has_data": False}
    mean_cycle = float(cycle.mean())
    # Adjusters handle several products: their caseload is their whole open inventory, not just this scope's
    allc = analytics._data()["claims"]
    adjusters = bc["adjuster_id"].dropna().unique()
    open_all = allc[(allc["claim_state"] != "closed") & allc["adjuster_id"].isin(adjusters)]
    per_adj = open_all.groupby("adjuster_id").size()
    observed = float(per_adj.median()) if len(per_adj) else None
    load = caseload or observed
    projected = annual * volume_factor
    inventory = projected * mean_cycle / 365
    groups = tc["assigned_group"].value_counts(normalize=True).head(4)
    return {
        "has_data": True,
        "claims_last_12_months": int(annual),
        "volume_factor": volume_factor,
        "projected_annual_claims": _r(projected, 0),
        "projected_monthly_claims": _r(projected / 12, 0),
        "mean_cycle_days": _r(mean_cycle),
        "median_cycle_days": _r(cycle.median()),
        "projected_open_inventory": _r(inventory, 0),
        "observed_caseload_median": _r(observed),
        "observed_adjusters_in_scope": int(len(per_adj)),
        "caseload_used": _r(load),
        "caseload_is_observed": caseload is None,
        "adjusters_needed_fte": _r(inventory / load, 1) if load else None,
        "adjusters_needed": math.ceil(inventory / load) if load else None,
        "handling_groups": [{"group": g, "share_pct": _r(100 * s)} for g, s in groups.items()],
    }


def large_losses(tc: pd.DataFrame, valuation: pd.Timestamp, cat: Dict[str, Any]) -> Dict[str, Any]:
    """Claims per year above each candidate large-loss / reinsurance reporting threshold."""
    span_years = max((valuation - tc["loss_date"].min()).days / 365.25, 1.0)
    amt = tc["claim_amount"].fillna(0)
    rows = []
    for t in LARGE_LOSS_THRESHOLDS:
        over = amt[amt >= t]
        rows.append({"threshold": t, "claims": int(len(over)), "per_year": _r(len(over) / span_years),
                     "share_of_incurred_pct": _r(100 * over.sum() / max(amt.sum(), 1))})
    return {
        "has_data": True,
        "years_of_data": _r(span_years),
        "largest": _r(amt.max(), 0),
        "p99": _r(amt[amt > 0].quantile(0.99), 0) if (amt > 0).any() else None,
        "thresholds": rows,
        "cat_claims": cat["claims"],
        "cat_share_of_incurred_pct": cat["share_pct"],
        "cat_events": cat["events"],
    }


def _cat(tc: pd.DataFrame) -> Dict[str, Any]:
    c = tc[tc["cat_code"].notna()]
    ev = c.groupby("cat_code").agg(claims=("claim_id", "size"), incurred=("claim_amount", "sum"))
    return {"claims": int(len(c)),
            "share_pct": _r(100 * c["claim_amount"].sum() / max(tc["claim_amount"].sum(), 1)),
            "events": [{"cat_code": k, "claims": int(r.claims), "incurred": _r(r.incurred, 0)}
                       for k, r in ev.sort_values("claims", ascending=False).head(5).iterrows()]}


def statutory_reporting(tc: pd.DataFrame) -> Dict[str, Any]:
    exp = analytics._data()["exposures"]
    e = exp[exp["claim_id"].isin(tc["claim_id"])].merge(tc[["claim_id", "product_code"]], on="claim_id")
    if e.empty:
        return {"has_data": False, "rows": []}
    g = e.groupby(["product_code", "exposure_type", "coverage_type"]).agg(
        exposures=("exposure_id", "size"), incurred=("incurred_loss", "sum")).reset_index()
    total = max(int(g["exposures"].sum()), 1)
    rows = []
    for r in g.sort_values("exposures", ascending=False).itertuples():
        m = _statement_line(r.product_code, r.exposure_type)
        rows.append({"product": r.product_code, "exposure_type": r.exposure_type, "coverage_type": r.coverage_type,
                     "share_pct": _r(100 * r.exposures / total), "statement_line": m["line"] or "[TBD]",
                     "note": m["note"]})
    return {"has_data": True, "rows": rows[:12], "lines": sorted({r["statement_line"] for r in rows})}


def medicare(tc: pd.DataFrame) -> Dict[str, Any]:
    exp = analytics._data()["exposures"]
    e = exp[exp["claim_id"].isin(tc["claim_id"])]
    bi_claims = e.loc[e["exposure_type"].isin(_BI_EXPOSURES), "claim_id"].nunique()
    return {"applies": bool(bi_claims), "bi_claims": int(bi_claims),
            "bi_share_pct": _r(100 * bi_claims / max(len(tc), 1)),
            "exposure_types": sorted(set(e["exposure_type"]) & _BI_EXPOSURES)}


def litigation(tc: pd.DataFrame, bc: pd.DataFrame) -> Dict[str, Any]:
    rate = float(tc["litigation_flag"].mean())
    by_state = tc.groupby("location").agg(claims=("claim_id", "size"), litigated=("litigation_flag", "sum"))
    by_state = by_state[by_state["claims"] >= MIN_STATE_CLAIMS]
    by_state["rate"] = 100 * by_state["litigated"] / by_state["claims"]
    top = by_state[by_state["litigated"] > 0].sort_values(["rate", "claims"], ascending=False).head(6)
    base = bc[~bc["claim_id"].isin(tc["claim_id"])]
    return {"rate_pct": _r(100 * rate), "baseline_rate_pct": _r(100 * base["litigation_flag"].mean()) if len(base) else None,
            "litigated_claims": int(tc["litigation_flag"].sum()),
            "states": [{"state": s, "claims": int(r.claims), "litigated": int(r.litigated), "rate_pct": _r(r.rate)}
                       for s, r in top.iterrows()]}


# ---------------------------------------------------------------------------
# Everything, in one call
# ---------------------------------------------------------------------------
def build_plan(brief: Dict[str, Any], volume_factor: float = 1.0, caseload: Optional[float] = None) -> Dict[str, Any]:
    basis = resolve_basis(brief)
    frames = _frames(basis)
    if frames is None:
        return {"has_data": False, "basis": basis}
    tc, bc, be = frames
    valuation = analytics._data()["valuation"]
    cat = _cat(tc)
    return {
        "has_data": True,
        "basis": basis,
        "valuation_date": analytics.valuation_date(),
        "claims_analyzed": int(len(tc)),
        "products": sorted(tc["product_code"].dropna().unique().tolist()),
        "states": state_footprint(tc, be),
        "staffing": staffing(tc, bc, valuation, volume_factor, caseload),
        "large_losses": large_losses(tc, valuation, cat),
        "statutory_reporting": statutory_reporting(tc),
        "medicare": medicare(tc),
        "litigation": litigation(tc, bc),
    }
