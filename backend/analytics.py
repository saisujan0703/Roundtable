"""
Roundtable Analytics Layer
==========================
Claims-team analytics over roundtable.db (read-only). Every number the
brief shows is computed here with pandas / SQL; the LLM never computes.

Conventions (how a claims / actuarial team reads these numbers):
  - Accident year (AY)   = year of loss_date.
  - Frequency            = claims per 1,000 earned exposure-years (vehicle,
                           dwelling, location or employee), NOT share of claims.
  - Exposure scope       = the lines (and, for vehicle perils, powertrains)
                           where a risk tag actually occurs, so battery_fault
                           is measured per EV-year, not per all-policy-year.
  - Severity             = gross incurred loss (paid + case reserve) per claim
                           with a payment or reserve; ALAE shown separately.
  - Loss cost            = incurred loss per exposure-year (frequency x severity).
  - Trend frequency      = ex-catastrophe and constant-mix across lines, so CAT
                           events and book-mix shifts do not read as trends.
  - The valuation-year AY is partial and immature (IBNR, open reserves);
    it is flagged wherever it appears.
"""
from __future__ import annotations

import math
from functools import lru_cache
from typing import Any, Dict, List, Optional

import numpy as np
import pandas as pd

from backend.database import DB_PATH, get_connection

LARGE_LOSS_THRESHOLD = 100_000
MIN_CREDIBLE_CLAIMS = 30          # per AY / per state before a rate is called credible
GAP_DENIAL_REASONS = {            # denials that signal demand for coverage the policy does not give
    "mechanical_breakdown_excluded", "wear_tear_deterioration", "flood_excluded", "excluded_peril",
}


# =========================================================================
# Data access (cached per database file version)
# =========================================================================
def _db_version() -> float:
    return DB_PATH.stat().st_mtime


@lru_cache(maxsize=2)
def _load(version: float) -> Dict[str, pd.DataFrame]:
    conn = get_connection()
    try:
        claims = pd.read_sql("SELECT * FROM claims", conn, parse_dates=["loss_date", "reported_date", "close_date", "reopened_date"])
        exposures = pd.read_sql("SELECT * FROM exposures", conn)
        earned = pd.read_sql(
            "SELECT e.calendar_year, e.product_code, e.state, e.vehicle_powertrain, "
            "p.vehicle_make, p.vehicle_model, p.vehicle_year, "
            "SUM(e.earned_exposure) AS earned_exposure, SUM(e.earned_premium) AS earned_premium "
            "FROM earned_exposure e JOIN policies p USING(policy_id) "
            "GROUP BY 1,2,3,4,5,6,7", conn)
        policies = pd.read_sql(
            "SELECT policy_id, vehicle_make, vehicle_model, vehicle_year, vehicle_powertrain FROM policies", conn)
    finally:
        conn.close()
    claims["ay"] = claims["loss_date"].dt.year
    claims = claims.merge(policies, on="policy_id", how="left")
    claims["vehicle_age"] = claims["ay"] - claims["vehicle_year"]
    valuation = max(claims["reported_date"].max(), claims["close_date"].max())
    return {"claims": claims, "exposures": exposures, "earned": earned, "valuation": valuation}


def _data() -> Dict[str, Any]:
    return _load(_db_version())


def valuation_date() -> str:
    return _data()["valuation"].strftime("%Y-%m-%d")


def list_tags() -> List[str]:
    return sorted(_data()["claims"]["risk_category_tag"].dropna().unique().tolist())


def _tags(tag_value) -> List[str]:
    """A risk pattern is one tag or several pooled with '+' (proxy analysis), e.g. 'battery_fault+vehiclefire'."""
    if isinstance(tag_value, (list, tuple)):
        return [t for t in tag_value if t]
    return [t.strip() for t in str(tag_value).split("+") if t.strip()]


def _r(x, n=2):
    return None if x is None or pd.isna(x) else round(float(x), n)


def _s(x):
    """Plain string or None (pandas NaN -> None)."""
    return None if x is None or pd.isna(x) else str(x)


# =========================================================================
# Scope: where does a tag occur, and what exposure base measures it?
# =========================================================================
def get_tag_scope(tag_value: str) -> dict:
    d = _data()
    c = d["claims"]
    tc = c[c["risk_category_tag"].isin(_tags(tag_value))]
    if tc.empty:
        return {"tag_value": tag_value, "has_data": False, "products": [], "powertrain": None}
    share = tc["product_code"].value_counts(normalize=True)
    products = share[share >= 0.01].index.tolist()
    pts = tc["vehicle_powertrain"].dropna().unique().tolist()
    powertrain = pts[0] if len(pts) == 1 and tc["vehicle_powertrain"].notna().all() else None
    unit = {"PersonalAuto": "vehicle", "BusinessAuto": "vehicle", "HOPHomeowners": "dwelling",
            "CommercialProperty": "location", "WorkersComp": "employee"}
    units = sorted({unit[p] for p in products})
    label = ("EV " if powertrain == "EV" else "") + "/".join(units) + "-years"
    return {"tag_value": tag_value, "has_data": True, "products": products, "powertrain": powertrain,
            "exposure_unit": label, "description": f"{', '.join(products)}" + (f" ({powertrain} only)" if powertrain else "")}


def _scope_frames(tag_value: str):
    d = _data()
    scope = get_tag_scope(tag_value)
    c, e = d["claims"], d["earned"]
    base_c = c[c["product_code"].isin(scope["products"])]
    base_e = e[e["product_code"].isin(scope["products"])]
    if scope["powertrain"]:
        base_c = base_c[base_c["vehicle_powertrain"] == scope["powertrain"]]
        base_e = base_e[base_e["vehicle_powertrain"] == scope["powertrain"]]
    tag_c = base_c[base_c["risk_category_tag"].isin(_tags(tag_value))]
    return scope, tag_c, base_c, base_e


def _severity(df: pd.DataFrame) -> pd.Series:
    return df.loc[df["claim_amount"] > 0, "claim_amount"]


# =========================================================================
# 1-3. Frequency, severity and loss-cost trend by accident year
# =========================================================================
def get_claims_summary_stats(tag_value: str) -> dict:
    scope, tc, bc, be = _scope_frames(tag_value)
    allc = _data()["claims"]
    if tc.empty:
        return {"has_data": False, "tag_count": 0, "total_count": int(len(allc))}
    sev = _severity(tc)
    return {
        "has_data": True,
        "tag_value": tag_value,
        "scope": scope["description"],
        "exposure_unit": scope["exposure_unit"],
        "valuation_date": valuation_date(),
        "tag_count": int(len(tc)),
        "total_count": int(len(allc)),
        "scope_claim_count": int(len(bc)),
        "share_of_scope_claims_pct": _r(100 * len(tc) / max(len(bc), 1)),
        "open_count": int((tc["claim_state"] != "closed").sum()),
        "closed_count": int((tc["claim_state"] == "closed").sum()),
        "paid_loss": _r(tc["paid_loss"].sum()),
        "outstanding_reserve": _r(tc["outstanding_reserve"].sum()),
        "incurred_loss": _r(tc["claim_amount"].sum()),
        "paid_expense": _r(tc["paid_expense"].sum()),
        "recoveries": _r(tc["subrogation_amount"].sum() + tc["salvage_amount"].sum()),
        "net_incurred": _r(tc["net_incurred"].sum()),
        "avg_severity": _r(sev.mean()),
        "median_severity": _r(sev.median()),
        "frequency_per_1000": _r(1000 * len(tc) / be["earned_exposure"].sum()),
    }


def get_frequency_severity_trend(tag_value: str) -> list[dict]:
    """Per accident year: claims, exposure, frequency, severity, loss cost, vs scope baseline."""
    scope, tc, bc, be = _scope_frames(tag_value)
    if tc.empty:
        return []
    val = _data()["valuation"]
    expo = be.groupby("calendar_year")["earned_exposure"].sum()
    # Constant-mix weights: each line's share of scope exposure over all years, so a
    # shift in book mix between lines does not masquerade as a frequency trend.
    expo_py = be.groupby(["product_code", "calendar_year"])["earned_exposure"].sum()
    weights = be.groupby("product_code")["earned_exposure"].sum()
    weights = weights / weights.sum()
    ex_cat_py = tc[tc["cat_code"].isna()].groupby(["product_code", "ay"]).size()

    def mix_adjusted(ay):
        f = 0.0
        for prod, w in weights.items():
            ex = expo_py.get((prod, ay), 0.0)
            if ex > 0:
                f += w * 1000 * ex_cat_py.get((prod, ay), 0) / ex
        return f

    rows = []
    for ay in sorted(expo.index):
        t = tc[tc["ay"] == ay]
        b = bc[bc["ay"] == ay]
        ex = float(expo[ay])
        sev = _severity(t)
        t_ex_cat = t[t["cat_code"].isna()]
        rows.append({
            "year": int(ay),
            "claims": int(len(t)),
            "cat_claims": int(len(t) - len(t_ex_cat)),
            "earned_exposure": _r(ex, 1),
            "annualized_exposure": _r(ex * 365.25 / max(val.dayofyear, 1), 1) if ay == val.year else _r(ex, 1),
            "frequency_per_1000": _r(1000 * len(t) / ex, 2) if ex else None,
            "frequency_ex_cat_per_1000": _r(mix_adjusted(ay), 2) if ex else None,
            "scope_all_cause_frequency_per_1000": _r(1000 * len(b) / ex, 2) if ex else None,
            "avg_severity": _r(sev.mean()),
            "median_severity": _r(sev.median()),
            "loss_cost_per_exposure": _r(t["claim_amount"].sum() / ex) if ex else None,
            "open_pct": _r(100 * (t["claim_state"] != "closed").mean(), 1) if len(t) else None,
            "credible": bool(len(t) >= MIN_CREDIBLE_CLAIMS),
            "partial_year": bool(ay == val.year),
        })
    return rows


def get_severity_profile(tag_value: str) -> dict:
    scope, tc, bc, be = _scope_frames(tag_value)
    if tc.empty:
        return {"has_data": False}
    sev, base_sev = _severity(tc), _severity(bc[~bc["risk_category_tag"].isin(_tags(tag_value))])
    closed_paid = tc[(tc["claim_state"] == "closed") & (tc["paid_loss"] > 0)]["paid_loss"]
    return {
        "has_data": True,
        "claims_with_loss": int(len(sev)),
        "mean": _r(sev.mean()), "median": _r(sev.median()),
        "p90": _r(sev.quantile(0.9)), "max": _r(sev.max()),
        "baseline_mean": _r(base_sev.mean()), "baseline_median": _r(base_sev.median()),
        "severity_index_vs_baseline": _r(sev.mean() / base_sev.mean()) if len(base_sev) else None,
        "avg_paid_closed": _r(closed_paid.mean()),
        "large_losses": int((tc["claim_amount"] >= LARGE_LOSS_THRESHOLD).sum()),
        "large_loss_share_of_incurred_pct": _r(100 * tc.loc[tc["claim_amount"] >= LARGE_LOSS_THRESHOLD, "claim_amount"].sum()
                                                / max(tc["claim_amount"].sum(), 1), 1),
        "alae_ratio_pct": _r(100 * tc["paid_expense"].sum() / max(tc["claim_amount"].sum(), 1), 1),
        "total_loss_rate_pct": _r(100 * tc["total_loss_flag"].mean(), 1),
        "baseline_label": f"other causes in {scope['description']}",
    }


def get_loss_ratio_by_tag(tag_value: str) -> dict:
    """Tag loss + ALAE as points of the scope's earned premium (not a peril loss ratio)."""
    scope, tc, bc, be = _scope_frames(tag_value)
    prem = float(be["earned_premium"].sum())
    if tc.empty or prem <= 0:
        return {"has_data": False, "status": "Insufficient evidence for loss ratio framing."}
    tag_inc = float(tc["total_incurred"].sum())
    scope_inc = float(bc["total_incurred"].sum())
    by_year = []
    ep_y = be.groupby("calendar_year")["earned_premium"].sum()
    for ay, ep in ep_y.items():
        by_year.append({"year": int(ay), "loss_ratio_points": _r(100 * tc.loc[tc["ay"] == ay, "total_incurred"].sum() / ep, 2)})
    return {
        "has_data": True,
        "earned_premium": _r(prem),
        "tag_incurred_with_alae": _r(tag_inc),
        "loss_ratio_points": _r(100 * tag_inc / prem, 2),
        "scope_loss_ratio_pct": _r(100 * scope_inc / prem, 1),
        "by_year": by_year,
        "status": (f"This pattern consumed {100 * tag_inc / prem:.1f} points of loss ratio on ${prem:,.0f} earned premium "
                   f"({scope['description']}); the scope's overall loss + ALAE ratio is {100 * scope_inc / prem:.1f}%."),
    }


# =========================================================================
# 4-5. Causes of loss and types of loss (exposure / coverage level)
# =========================================================================
def get_claims_loss_cause_breakdown(tag_value: str) -> list[dict]:
    _, tc, _, _ = _scope_frames(tag_value)
    if tc.empty:
        return []
    g = tc.groupby("loss_cause").agg(cnt=("claim_id", "size"), incurred=("claim_amount", "sum"),
                                     avg=("claim_amount", "mean")).sort_values("cnt", ascending=False)
    g["pct"] = g["cnt"] / g["cnt"].sum()
    return [{"loss_cause": k, "cnt": int(r.cnt), "pct": _r(r.pct, 4), "incurred": _r(r.incurred), "avg_incurred": _r(r.avg)}
            for k, r in g.iterrows()]


def get_loss_descriptions(tag_value: str, n: int = 5) -> list[dict]:
    _, tc, _, _ = _scope_frames(tag_value)
    if tc.empty:
        return []
    g = tc.groupby("loss_description").agg(cnt=("claim_id", "size"), avg=("claim_amount", "mean"))
    g = g.sort_values("cnt", ascending=False).head(n)
    return [{"description": k, "cnt": int(r.cnt), "avg_incurred": _r(r.avg)} for k, r in g.iterrows()]


def get_loss_type_breakdown(tag_value: str) -> dict:
    _, tc, _, _ = _scope_frames(tag_value)
    if tc.empty:
        return {"has_data": False, "by_exposure": []}
    ex = _data()["exposures"]
    ex = ex[ex["claim_id"].isin(tc["claim_id"])]
    g = ex.groupby(["exposure_type", "coverage_type"]).agg(
        exposures=("exposure_id", "size"), paid=("paid_loss", "sum"), outstanding=("outstanding_reserve", "sum"),
        incurred=("incurred_loss", "sum"), denied=("denial_reason", lambda s: s.notna().sum()),
        total_losses=("total_loss_flag", "sum")).sort_values("incurred", ascending=False)
    rows = [{"exposure_type": et, "coverage_type": cov, "exposures": int(r.exposures), "paid": _r(r.paid),
             "outstanding": _r(r.outstanding), "incurred": _r(r.incurred),
             "avg_incurred": _r(r.incurred / r.exposures), "denied": int(r.denied), "total_losses": int(r.total_losses)}
            for (et, cov), r in g.iterrows()]
    return {
        "has_data": True,
        "by_exposure": rows,
        "paid_loss": _r(tc["paid_loss"].sum()),
        "outstanding_reserve": _r(tc["outstanding_reserve"].sum()),
        "incurred_loss": _r(tc["claim_amount"].sum()),
        "paid_pct_of_incurred": _r(100 * tc["paid_loss"].sum() / max(tc["claim_amount"].sum(), 1), 1),
        "claim_segments": tc["claim_segment"].value_counts().to_dict(),
    }


# =========================================================================
# 6-7. Segments and geography (exposure-based rates)
# =========================================================================
def get_segment_breakdown(tag_value: str) -> dict:
    scope, tc, bc, be = _scope_frames(tag_value)
    if tc.empty:
        return {"has_data": False}
    total_freq = 1000 * len(tc) / be["earned_exposure"].sum()

    def rate_table(key: str, min_claims: int = 10, top: int = 8, frame_e=None):
        fe = be if frame_e is None else frame_e
        cnt = tc.groupby(key).size()
        expo = fe.groupby(key)["earned_exposure"].sum()
        out = []
        for k, n in cnt.items():
            ex = float(expo.get(k, 0))
            if ex <= 0:
                continue
            f = 1000 * n / ex
            out.append({key: k if not isinstance(k, (np.integer, np.floating)) else int(k), "claims": int(n),
                        "earned_exposure": _r(ex, 1), "frequency_per_1000": _r(f),
                        "index_vs_avg": _r(f / total_freq), "credible": bool(n >= min_claims)})
        out.sort(key=lambda r: (-r["credible"], -(r["index_vs_avg"] or 0)))
        return out[:top]

    result = {"has_data": True, "avg_frequency_per_1000": _r(total_freq),
              "by_product": rate_table("product_code", 1, 10)}
    if tc["vehicle_make"].notna().any():
        bands = dict(bins=[-1, 2, 5, 8, 50], labels=["0-2", "3-5", "6-8", "9+"])
        cnt = pd.cut(tc["vehicle_age"], **bands).value_counts()
        expo = be.groupby(pd.cut(be["calendar_year"] - be["vehicle_year"], **bands), observed=False)["earned_exposure"].sum()
        result["by_vehicle_age"] = [
            {"vehicle_age_band": str(k), "claims": int(cnt.get(k, 0)),
             "frequency_per_1000": _r(1000 * cnt.get(k, 0) / expo[k]),
             "index_vs_avg": _r(1000 * cnt.get(k, 0) / expo[k] / total_freq)}
            for k in bands["labels"] if expo.get(k, 0) > 0]
        result["by_vehicle_model"] = rate_table("vehicle_model", 8, 8)
        if not scope["powertrain"]:
            result["by_powertrain"] = rate_table("vehicle_powertrain", 1, 3)
    return result


def get_geographic_breakdown(tag_value: str, top: int = 8) -> dict:
    _, tc, _, be = _scope_frames(tag_value)
    if tc.empty:
        return {"has_data": False, "states": []}
    avg = 1000 * len(tc) / be["earned_exposure"].sum()
    cnt = tc.groupby("location").size()
    expo = be.groupby("state")["earned_exposure"].sum()
    rows = []
    for st, n in cnt.items():
        ex = float(expo.get(st, 0))
        if ex <= 0:
            continue
        f = 1000 * n / ex
        rows.append({"state": st, "claims": int(n), "frequency_per_1000": _r(f), "index_vs_avg": _r(f / avg),
                     "credible": bool(n >= MIN_CREDIBLE_CLAIMS)})
    # Rank credible states first; with a thin book fall back to states with >= 10 claims (flagged)
    credible = sorted([r for r in rows if r["claims"] >= 10], key=lambda r: (-r["credible"], -r["index_vs_avg"]))
    cats = tc[tc["cat_code"].notna()].groupby("cat_code").agg(cnt=("claim_id", "size"), incurred=("claim_amount", "sum"))
    return {
        "has_data": True, "avg_frequency_per_1000": _r(avg),
        "states": credible[:top],
        "low_credibility_states": sum(1 for r in rows if not r["credible"]),
        "cat_events": [{"cat_code": k, "claims": int(r.cnt), "incurred": _r(r.incurred)} for k, r in cats.iterrows()],
        "cat_share_of_incurred_pct": _r(100 * tc.loc[tc["cat_code"].notna(), "claim_amount"].sum() / max(tc["claim_amount"].sum(), 1), 1),
    }


# =========================================================================
# 8. Coverage-gap evidence (denials, no-payment closures, limits)
# =========================================================================
def get_coverage_gap_signals(tag_value: str) -> dict:
    scope, tc, bc, _ = _scope_frames(tag_value)
    if tc.empty:
        return {"has_data": False}
    closed = tc[tc["claim_state"] == "closed"]
    base_closed = bc[(bc["claim_state"] == "closed") & (~bc["risk_category_tag"].isin(_tags(tag_value)))]
    denied = tc[tc["coverage_denied_flag"] == 1]
    gap = denied[denied["denial_reason"].isin(GAP_DENIAL_REASONS)]
    ex = _data()["exposures"]
    tex = ex[ex["claim_id"].isin(tc["claim_id"])]
    reasons = denied.groupby("denial_reason").agg(cnt=("claim_id", "size"), est=("initial_reserve", "sum"))
    return {
        "has_data": True,
        "claims": int(len(tc)),
        "denied_claims": int(len(denied)),
        "denial_rate_pct": _r(100 * len(denied) / len(tc), 1),
        "baseline_denial_rate_pct": _r(100 * base_closed["coverage_denied_flag"].mean(), 1) if len(base_closed) else None,
        "gap_denials": int(len(gap)),
        "gap_denial_rate_pct": _r(100 * len(gap) / len(tc), 1),
        "gap_denial_estimated_loss": _r(gap["initial_reserve"].sum()),
        "denial_reasons": [{"reason": k, "claims": int(r.cnt), "estimated_loss_at_fnol": _r(r.est)} for k, r in
                           reasons.sort_values("cnt", ascending=False).iterrows()],
        "closed_without_payment_pct": _r(100 * closed["no_payment_reason"].notna().mean(), 1) if len(closed) else None,
        "baseline_closed_without_payment_pct": _r(100 * base_closed["no_payment_reason"].notna().mean(), 1) if len(base_closed) else None,
        "no_payment_reasons": closed["no_payment_reason"].value_counts().to_dict(),
        "limit_exhausted_exposures": int(tex["limit_exhausted"].sum()),
        "total_losses": int(tc["total_loss_flag"].sum()),
    }


# =========================================================================
# 9-10. Claim handling, reserve development, recurring & emerging signals
# =========================================================================
def get_claim_handling_metrics(tag_value: str) -> dict:
    scope, tc, bc, _ = _scope_frames(tag_value)
    if tc.empty:
        return {"has_data": False}
    val = _data()["valuation"]
    base = bc[~bc["risk_category_tag"].isin(_tags(tag_value))]
    closed = tc[tc["claim_state"] == "closed"]
    cycle = (closed["close_date"] - closed["reported_date"]).dt.days
    base_closed = base[base["claim_state"] == "closed"]
    base_cycle = (base_closed["close_date"] - base_closed["reported_date"]).dt.days
    open_ = tc[tc["claim_state"] != "closed"]
    age = (val - open_["reported_date"]).dt.days
    buckets = pd.cut(age, [-1, 30, 90, 180, 365, 10_000], labels=["0-30", "31-90", "91-180", "181-365", "365+"])
    subro_elig = tc[(tc["fault_rating"] == "thirdparty") & (tc["claim_state"] == "closed") & (tc["paid_loss"] > 0)]
    repeat = tc.groupby("policy_number").size()
    return {
        "has_data": True,
        "report_lag_median_days": _r(tc["report_lag_days"].median(), 1),
        "report_lag_p90_days": _r(tc["report_lag_days"].quantile(0.9), 1),
        "late_reported_pct": _r(100 * (tc["report_lag_days"] > 30).mean(), 1),
        "baseline_report_lag_median_days": _r(base["report_lag_days"].median(), 1),
        "cycle_time_median_days": _r(cycle.median(), 1),
        "cycle_time_p90_days": _r(cycle.quantile(0.9), 1),
        "baseline_cycle_time_median_days": _r(base_cycle.median(), 1),
        "open_claims": int(len(open_)),
        "open_aging": {str(k): int(v) for k, v in buckets.value_counts().sort_index().items()},
        "open_outstanding_reserve": _r(open_["outstanding_reserve"].sum()),
        "reopen_rate_pct": _r(100 * tc["reopened_date"].notna().mean(), 1),
        "baseline_reopen_rate_pct": _r(100 * base["reopened_date"].notna().mean(), 1),
        "litigation_rate_pct": _r(100 * tc["litigation_flag"].mean(), 1),
        "baseline_litigation_rate_pct": _r(100 * base["litigation_flag"].mean(), 1),
        "litigation_status": tc.loc[tc["litigation_flag"] == 1, "litigation_status"].value_counts().to_dict(),
        "siu_referral_rate_pct": _r(100 * (tc["siu_status"] != "No_Referral").mean(), 1),
        "baseline_siu_referral_rate_pct": _r(100 * (base["siu_status"] != "No_Referral").mean(), 1),
        "fraud_closures": int((tc["closed_outcome"] == "fraud").sum()),
        "subrogation_recovered": _r(tc["subrogation_amount"].sum()),
        "subrogation_recovery_rate_pct": _r(100 * subro_elig["subrogation_amount"].sum() / max(subro_elig["paid_loss"].sum(), 1), 1),
        "salvage_recovered": _r(tc["salvage_amount"].sum()),
        "repeat_claim_policies": int((repeat >= 2).sum()),
        "assigned_groups": tc["assigned_group"].value_counts().to_dict(),
    }


def get_litigation_subrogation_summary(tag_value: str) -> dict:
    h = get_claim_handling_metrics(tag_value)
    if not h.get("has_data"):
        return {"has_data": False, "status": "Insufficient evidence for litigation/subrogation signal."}
    h["status"] = (f"Litigation rate {h['litigation_rate_pct']}% (baseline {h['baseline_litigation_rate_pct']}%); "
                   f"subrogation recovered ${h['subrogation_recovered']:,.0f} "
                   f"({h['subrogation_recovery_rate_pct']}% of paid on other-party-at-fault claims); "
                   f"salvage ${h['salvage_recovered']:,.0f}.")
    return h


def get_reserve_development(tag_value: str) -> dict:
    """Initial (FNOL) case reserve vs current incurred. >1.0 = adverse development."""
    _, tc, bc, _ = _scope_frames(tag_value)
    if tc.empty:
        return {"has_data": False}

    def dev(df):
        df = df[(df["initial_reserve"] > 0) & (df["coverage_denied_flag"] == 0) & (df["no_payment_reason"].isna())]
        if df.empty:
            return None, None, None
        ratio = df["claim_amount"].sum() / df["initial_reserve"].sum()
        per = df["claim_amount"] / df["initial_reserve"]
        return ratio, per.median(), (per > 1.25).mean()

    base = bc[~bc["risk_category_tag"].isin(_tags(tag_value))]
    r, med, adverse = dev(tc)
    br, bmed, badverse = dev(base)
    by_ay = []
    for ay, g in tc.groupby("ay"):
        rr, _, _ = dev(g)
        by_ay.append({"year": int(ay), "incurred_to_initial_ratio": _r(rr)})
    direction = "adverse" if (r or 1) > 1.05 else "favorable" if (r or 1) < 0.95 else "neutral"
    return {
        "has_data": r is not None,
        "incurred_to_initial_ratio": _r(r), "median_claim_ratio": _r(med),
        "claims_developed_over_25pct": _r(100 * (adverse or 0), 1),
        "baseline_incurred_to_initial_ratio": _r(br), "baseline_claims_developed_over_25pct": _r(100 * (badverse or 0), 1),
        "direction": direction, "by_year": by_ay,
    }


def get_cycle_time_and_reserve_development(tag_value: str) -> dict:
    h, rd = get_claim_handling_metrics(tag_value), get_reserve_development(tag_value)
    if not h.get("has_data") or not rd.get("has_data"):
        return {"has_data": False, "status": "Insufficient evidence for claim cycle time and reserve development."}
    return {**rd, "cycle_time_median_days": h["cycle_time_median_days"],
            "status": (f"Median {h['cycle_time_median_days']:.0f} days report-to-close (baseline {h['baseline_cycle_time_median_days']:.0f}); "
                       f"incurred is {rd['incurred_to_initial_ratio']:.2f}x the FNOL reserve "
                       f"(baseline {rd['baseline_incurred_to_initial_ratio']:.2f}x) -> {rd['direction']} development.")}


def _credible_trend_rows(tag_value: str) -> list[dict]:
    return [r for r in get_frequency_severity_trend(tag_value) if r["claims"] >= 10]


def fit_frequency_trend(tag_value: str, min_claims: int = 20) -> dict:
    """Exponential frequency trend fitted across accident years (ex-CAT, constant mix).

    Weighted least squares on log(frequency) with weights = claim counts (the inverse
    variance of a Poisson log-rate). The partial valuation year is excluded from the
    fit because it is immature. Significance: |z| >= 2.
    """
    rows = [r for r in get_frequency_severity_trend(tag_value)
            if r["claims"] >= min_claims and not r["partial_year"] and r["frequency_ex_cat_per_1000"]]
    if len(rows) < 2:
        return {"has_data": False, "narrative": "Insufficient credible accident years to fit a frequency trend."}
    x = np.array([r["year"] for r in rows], dtype=float)
    y = np.log([r["frequency_ex_cat_per_1000"] for r in rows])
    w = np.array([r["claims"] - r["cat_claims"] for r in rows], dtype=float)
    xm = np.sum(w * x) / w.sum()
    ym = np.sum(w * y) / w.sum()
    sxx = np.sum(w * (x - xm) ** 2)
    b = np.sum(w * (x - xm) * (y - ym)) / sxx
    se = math.sqrt(1 / sxx)
    annual = math.exp(b) - 1
    z = b / se
    significant = abs(z) >= 2
    return {
        "has_data": True, "years": [int(v) for v in x], "annual_trend_pct": _r(100 * annual, 1),
        "ci95_low_pct": _r(100 * (math.exp(b - 2 * se) - 1), 1), "ci95_high_pct": _r(100 * (math.exp(b + 2 * se) - 1), 1),
        "z": _r(z), "significant": bool(significant),
        "direction": ("rising" if b > 0 else "falling") if significant else "no significant trend",
        "narrative": (f"Fitted ex-CAT frequency trend {100 * annual:+.1f}% per year over AY {int(x[0])}-{int(x[-1])} "
                      f"(95% range {100 * (math.exp(b - 2 * se) - 1):+.1f}% to {100 * (math.exp(b + 2 * se) - 1):+.1f}%; "
                      + ("statistically significant)." if significant else "not statistically significant)."))
    }


def detect_notable_trends(min_annual_trend: float = 0.03) -> list[dict]:
    """Every tag with a statistically significant fitted frequency trend of at least
    min_annual_trend per year (ex-CAT, constant mix, scope-specific exposure base)."""
    return [dict(t) for t in _notable_trends(_db_version(), min_annual_trend)]


@lru_cache(maxsize=8)
def _notable_trends(version: float, min_annual_trend: float) -> tuple:
    notable = []
    for tag in list_tags():
        f = fit_frequency_trend(tag)
        if f["has_data"] and f["significant"] and abs(f["annual_trend_pct"]) >= 100 * min_annual_trend:
            notable.append({"tag_value": tag, "annual_trend_pct": f["annual_trend_pct"], "z": f["z"],
                            "years": f"{f['years'][0]}-{f['years'][-1]}",
                            "direction": "UP" if f["annual_trend_pct"] > 0 else "DOWN"})
    notable.sort(key=lambda t: -abs(t["annual_trend_pct"]))
    return tuple(notable)


@lru_cache(maxsize=2)
def _all_fitted_trends(version: float) -> tuple:
    out = []
    for tag in list_tags():
        f = fit_frequency_trend(tag)
        if f["has_data"]:
            out.append((tag, f["annual_trend_pct"]))
    return tuple(out)


def get_relative_growth_benchmark(tag_value: str) -> dict:
    """This tag's fitted annual frequency trend vs the average across all other tags."""
    tags = _tags(tag_value)
    trends = dict(_all_fitted_trends(_db_version()))
    if len(tags) > 1:   # pooled proxy pattern: fit it as one pattern, compare with tags outside the pool
        fit = fit_frequency_trend(tag_value)
        trends = {k: v for k, v in trends.items() if k not in tags}
        if fit["has_data"]:
            trends[tag_value] = fit["annual_trend_pct"]
    if tag_value not in trends or len(trends) < 2:
        return {"has_data": False, "narrative": "Insufficient credible accident years to benchmark frequency growth."}
    others = [v for k, v in trends.items() if k != tag_value]
    avg = sum(others) / len(others)
    own = trends[tag_value]
    rank = sorted(trends.values(), reverse=True).index(own) + 1
    return {"has_data": True, "tag_growth_pct": own, "benchmark_avg_growth_pct": _r(avg, 1), "rank": rank,
            "tags_compared": len(trends),
            "narrative": (f"Fitted frequency trend {own:+.1f}%/yr vs {avg:+.1f}%/yr average across {len(trends) - 1} other "
                          f"risk patterns (ranked #{rank} of {len(trends)} for growth).")}


def get_emerging_signals(tag_value: str) -> dict:
    rows = _credible_trend_rows(tag_value)
    if len(rows) < 2:
        return {"has_data": False}
    yoy = []
    for a, b in zip(rows, rows[1:]):
        yoy.append({"from": a["year"], "to": b["year"],
                    "frequency_change_pct": _r(100 * (b["frequency_ex_cat_per_1000"] / a["frequency_ex_cat_per_1000"] - 1), 1)
                    if a["frequency_ex_cat_per_1000"] else None,
                    "severity_change_pct": _r(100 * (b["avg_severity"] / a["avg_severity"] - 1), 1) if a["avg_severity"] and b["avg_severity"] else None,
                    "to_partial_year": b["partial_year"]})
    d = _data()
    _, tc, _, _ = _scope_frames(tag_value)
    val = d["valuation"]
    last12 = tc[tc["loss_date"] > val - pd.DateOffset(months=12)]
    prior12 = tc[(tc["loss_date"] <= val - pd.DateOffset(months=12)) & (tc["loss_date"] > val - pd.DateOffset(months=24))]
    return {"has_data": True, "yoy": yoy,
            "last_12m_claims": int(len(last12)), "prior_12m_claims": int(len(prior12)),
            "last_12m_vs_prior_pct": _r(100 * (len(last12) / len(prior12) - 1), 1) if len(prior12) else None}


def get_sample_claims_for_tag(tag_value: str, n: int = 3) -> list[dict]:
    """Representative claims: a typical closed claim, the largest loss, and an open or denied claim."""
    _, tc, _, _ = _scope_frames(tag_value)
    if tc.empty:
        return []
    picks = []
    closed_paid = tc[(tc["claim_state"] == "closed") & (tc["paid_loss"] > 0)].sort_values("claim_amount")
    if len(closed_paid):
        picks.append(("Typical closed claim", closed_paid.iloc[len(closed_paid) // 2]))
    picks.append(("Largest loss", tc.sort_values("claim_amount").iloc[-1]))
    denied = tc[tc["coverage_denied_flag"] == 1]
    open_ = tc[tc["claim_state"] == "open"].sort_values("claim_amount")
    if len(denied):
        picks.append(("Coverage denied", denied.iloc[len(denied) // 2]))
    elif len(open_):
        picks.append(("Open claim", open_.iloc[len(open_) // 2]))
    out, seen = [], set()
    for label, r in picks:
        if r["claim_id"] in seen:
            continue
        seen.add(r["claim_id"])
        out.append({
            "label": label, "claim_id": r["claim_number"], "claim_date": r["loss_date"].strftime("%Y-%m-%d"),
            "year": int(r["ay"]), "location": r["location"], "loss_cause": r["loss_cause"],
            "description": r["loss_description"], "vehicle": (f"{int(r['vehicle_year'])} {r['vehicle_make']} {r['vehicle_model']}"
                                                              if pd.notna(r["vehicle_make"]) else None),
            "claim_state": r["claim_state"], "incurred_amount": _r(r["claim_amount"]), "paid_loss": _r(r["paid_loss"]),
            "outstanding_reserve": _r(r["outstanding_reserve"]), "initial_reserve": _r(r["initial_reserve"]),
            "denial_reason": _s(r["denial_reason"]), "litigation_status": _s(r["litigation_status"]),
        })
    return out[:n]


# =========================================================================
# Line-of-business baseline (no direct or proxy risk pattern to measure)
# =========================================================================
def get_line_baseline(product_codes: List[str]) -> dict:
    """Whole-line claims experience: the starting point for a product with no comparable risk pattern."""
    d = _data()
    c, e = d["claims"], d["earned"]
    lc, le = c[c["product_code"].isin(product_codes)], e[e["product_code"].isin(product_codes)]
    expo, prem = float(le["earned_exposure"].sum()), float(le["earned_premium"].sum())
    if lc.empty or expo <= 0:
        return {"has_data": False, "products": product_codes}
    sev = _severity(lc)
    closed = lc[lc["claim_state"] == "closed"]
    causes = lc.groupby("risk_category_tag").agg(claims=("claim_id", "size"), incurred=("claim_amount", "sum"))
    causes = causes.sort_values("claims", ascending=False).head(8)
    return {
        "has_data": True,
        "products": product_codes,
        "valuation_date": valuation_date(),
        "claims": int(len(lc)),
        "earned_exposure": _r(expo),
        "frequency_per_1000": _r(1000 * len(lc) / expo),
        "avg_severity": _r(sev.mean()),
        "median_severity": _r(sev.median()),
        "p90_severity": _r(sev.quantile(0.9)),
        "loss_ratio_pct": _r(100 * lc["total_incurred"].sum() / prem, 1) if prem > 0 else None,
        "denial_rate_pct": _r(100 * closed["coverage_denied_flag"].mean(), 1) if len(closed) else None,
        "litigation_rate_pct": _r(100 * lc["litigation_flag"].mean(), 1),
        "top_patterns": [{"tag_value": k, "claims": int(r.claims), "share_pct": _r(100 * r.claims / len(lc), 1),
                          "avg_incurred": _r(r.incurred / r.claims)} for k, r in causes.iterrows()],
    }


# =========================================================================
# Everything the brief needs, in one call
# =========================================================================
def build_claims_analytics(tag_value: str) -> dict:
    return {
        "valuation_date": valuation_date(),
        "scope": get_tag_scope(tag_value),
        "summary": get_claims_summary_stats(tag_value),
        "trend": get_frequency_severity_trend(tag_value),
        "frequency_trend_fit": fit_frequency_trend(tag_value),
        "severity": get_severity_profile(tag_value),
        "loss_ratio": get_loss_ratio_by_tag(tag_value),
        "loss_causes": get_claims_loss_cause_breakdown(tag_value),
        "loss_descriptions": get_loss_descriptions(tag_value),
        "loss_types": get_loss_type_breakdown(tag_value),
        "segments": get_segment_breakdown(tag_value),
        "geography": get_geographic_breakdown(tag_value),
        "coverage_gaps": get_coverage_gap_signals(tag_value),
        "handling": get_claim_handling_metrics(tag_value),
        "reserve_development": get_reserve_development(tag_value),
        "emerging": get_emerging_signals(tag_value),
        "benchmark": get_relative_growth_benchmark(tag_value),
        "notable_portfolio_trends": detect_notable_trends(),
        "sample_claims": get_sample_claims_for_tag(tag_value),
    }


# =========================================================================
# CLI verification
# =========================================================================
if __name__ == "__main__":
    import json
    import sys

    tag = sys.argv[1] if len(sys.argv) > 1 else "battery_fault"
    print(json.dumps(build_claims_analytics(tag), indent=2, default=str))
