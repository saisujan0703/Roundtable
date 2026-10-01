"""
Claims Readiness Checklist
==========================
What the Claims department must have in place before a new product launches:
policy wording reviewed, ClaimCenter configured, reserving guidance set,
vendors, routing & authority, training, and post-launch monitoring.

Each item carries guidance derived from the brief's own claims analytics
(numbers are quoted from backend.analytics output, never invented). Items are
created once per brief; after that only status / owner / note change.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

STATUSES = ("Not started", "In progress", "Done", "N/A")

STAGES = {
    "wording": "1. Policy wording review",
    "setup": "2. Operational setup",
    "monitoring": "3. Post-launch monitoring",
}


DENIAL_NAMES = {
    "mechanical_breakdown_excluded": "mechanical breakdown exclusion",
    "wear_tear_deterioration": "wear & tear / gradual deterioration exclusion",
    "flood_excluded": "flood / surface water exclusion",
    "excluded_peril": "excluded peril",
    "coverage_not_purchased": "coverage not purchased",
    "late_notice": "late notice",
}


def _money(v: Optional[float]) -> str:
    return "n/a" if v is None else f"${v:,.0f}"


def _item(item_id: str, stage: str, title: str, guidance: str, required: bool = True) -> Dict[str, Any]:
    return {"id": item_id, "stage": stage, "title": title, "guidance": guidance, "required": required,
            "status": "Not started", "owner": "", "note": "", "updated_at": None}


def build_checklist(brief_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Create the readiness checklist for a brief, tailored with its claims analytics when available.

    For a proxy-based brief, every number-backed guidance is marked as proxy data, and two items are added:
    validate the proxies, and start the product's own claims history.
    """
    items = _build_items(brief_data)
    basis = ((brief_data or {}).get("claims_analytics") or {}).get("basis") or {}
    if basis.get("basis") != "proxy":
        return items
    proxies = " + ".join(basis.get("proxy_tags") or [])
    generic = {i["id"]: i["guidance"] for i in _build_items({"title": (brief_data or {}).get("title")})}
    for i in items:
        if i["guidance"] != generic.get(i["id"]):
            i["guidance"] = f"Proxy data ({proxies}) — " + i["guidance"]
    first_setup = next(n for n, i in enumerate(items) if i["stage"] == "setup")
    items[first_setup:first_setup] = [
        _item("validate_proxy", "setup", "Validate the proxy risk patterns",
              f"This product has no claims of its own; the figures here come from {proxies}. Claims and Actuarial confirm "
              f"each proxy's cause of loss, severity drivers and handling are comparable, and record where they differ."),
        _item("own_risk_tag", "setup", "Create a dedicated risk tag for the new product",
              "Add a new risk_category_tag in ClaimCenter and set it on FNOL from launch, so the product's own history "
              "replaces the proxies once it is credible (30+ claims per accident year)."),
    ]
    return items


def _build_items(brief_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    a = (brief_data or {}).get("claims_analytics") or {}
    tag = (brief_data or {}).get("tag_value") or (brief_data or {}).get("title") or "this risk"
    has = bool(a.get("summary", {}).get("has_data"))
    s, sev, gaps = a.get("summary", {}), a.get("severity", {}), a.get("coverage_gaps", {})
    h, rd, lt = a.get("handling", {}), a.get("reserve_development", {}), a.get("loss_types", {})
    trend, fit = a.get("trend", []), a.get("frequency_trend_fit", {})

    top_denial = (gaps.get("denial_reasons") or [{}])[0].get("reason") if has else None
    top_exposures = ", ".join(f"{r['exposure_type']} / {r['coverage_type']}" for r in (lt.get("by_exposure") or [])[:3])
    groups = ", ".join(list((h.get("assigned_groups") or {}).keys())[:3])
    latest_full = next((r for r in reversed(trend) if not r.get("partial_year")), {})

    items = [
        # ---- 1. Policy wording ------------------------------------------------
        _item("covered_peril", "wording", "Define the covered peril precisely",
              (f"Customers are being denied today under the {DENIAL_NAMES.get(top_denial, top_denial)} "
               f"({gaps.get('gap_denials', 0)} claims, {gaps.get('gap_denial_rate_pct', 0)}%). The new wording must say exactly "
               f"which of these losses become covered (e.g. sudden failure vs gradual degradation) so adjusters can decide "
               f"consistently." if has and top_denial else
               f"Write a definition of the '{tag}' peril that an adjuster can apply to a real claim without interpretation.")),
        _item("proof_requirements", "wording", "Set proof-of-loss requirements",
              "Specify the evidence needed to establish a covered loss (inspection report, diagnostic data, photos, "
              "repair estimate) and who may provide it."),
        _item("limits_deductibles", "wording", "Validate limits, sub-limits and deductible against real costs",
              (f"Claims data: median incurred {_money(sev.get('median'))}, 90th percentile {_money(sev.get('p90'))}, "
               f"largest {_money(sev.get('max'))}; {sev.get('total_loss_rate_pct', 0)}% end as total losses. "
               f"A sub-limit below the P90 will leave roughly 1 in 10 customers under-indemnified." if has else
               "Compare proposed limits with typical and large-loss claim costs before filing.")),
        _item("exclusions_disputes", "wording", "Review exclusions for dispute and litigation risk",
              (f"Litigation rate on this pattern is {h.get('litigation_rate_pct')}% vs {h.get('baseline_litigation_rate_pct')}% "
               f"baseline. Have Claims Legal review every exclusion and definition for ambiguity." if has else
               "Have Claims Legal review every exclusion and definition for ambiguity.")),

        # ---- 2. Operational setup -------------------------------------------------
        _item("claimcenter_config", "setup", "Configure ClaimCenter (coverage, loss cause, FNOL questions)",
              (f"Add the new coverage type to the product model mapping, keep the '{tag}' risk tag on FNOL, and add FNOL "
               f"questions that separate covered from excluded causes. Exposures most used today: {top_exposures}. "
               f"See 01_ENTITY_EXTENSION_GUIDE.md and 04_PRODUCT_MODEL_WRITE_PATH.md." if has else
               "Add the coverage type, loss cause/risk tag and FNOL questions in ClaimCenter configuration.")),
        _item("reserving_guidance", "setup", "Issue FNOL reserving guidance",
              (f"Current FNOL reserves develop to {rd.get('incurred_to_initial_ratio')}x (baseline "
               f"{rd.get('baseline_incurred_to_initial_ratio')}x); {rd.get('claims_developed_over_25pct')}% of claims develop "
               f">25%. Set the default initial reserve near the average paid on closed claims "
               f"({_money(sev.get('avg_paid_closed'))}) and review it quarterly." if has else
               "Set a default initial reserve per exposure type and a review cadence.")),
        _item("vendor_network", "setup", "Line up vendor / repair network",
              (f"Median cycle time is {h.get('cycle_time_median_days')} days vs {h.get('baseline_cycle_time_median_days')} "
               f"baseline. Contract specialist vendors (repairers, inspectors, salvage) with capacity for ~"
               f"{latest_full.get('claims', 0)} claims a year at today's volume." if has else
               "Identify and contract the repair, inspection and salvage vendors this coverage needs.")),
        _item("routing_authority", "setup", "Set claim routing and payment authority",
              (f"Today these claims land with: {groups}. Decide the handling group, the large-loss referral threshold "
               f"(largest loss {_money(sev.get('max'))}), and adjuster payment authority levels." if has else
               "Decide the handling group, large-loss referral threshold and payment authority levels.")),
        _item("siu_triggers", "setup", "Define SIU / fraud referral triggers",
              (f"SIU referral rate {h.get('siu_referral_rate_pct')}% (baseline {h.get('baseline_siu_referral_rate_pct')}%). "
               f"Add referral rules for new coverage (e.g. loss soon after inception, late reporting — "
               f"{h.get('late_reported_pct')}% are reported after 30 days)." if has else
               "Add SIU referral rules for the new coverage."), required=False),
        _item("recovery_process", "setup", "Set subrogation and salvage process",
              (f"Subrogation recovers {h.get('subrogation_recovery_rate_pct')}% of paid on other-party-at-fault claims; "
               f"salvage {_money(h.get('salvage_recovered'))} to date. Confirm recovery rights in the wording and the "
               f"salvage route for damaged parts." if has else
               "Confirm recovery rights and the salvage route."), required=False),
        _item("training", "setup", "Train adjusters and publish handling guidelines",
              "Publish a claims handling guideline for the new coverage (coverage decision tree, documentation, "
              "reserving, authority) and train the handling group before the first policy is bound."),

        # ---- 3. Post-launch monitoring --------------------------------------------
        _item("kpi_baseline", "monitoring", "Agree launch KPIs and alert thresholds",
              (f"Baseline from claims data: frequency {s.get('frequency_per_1000')} per 1,000 {s.get('exposure_unit')} "
               f"(fitted trend {fit.get('annual_trend_pct')}%/yr), mean severity {_money(sev.get('mean'))}, "
               f"denial rate {gaps.get('denial_rate_pct')}%, median cycle time {h.get('cycle_time_median_days')} days. "
               f"Alert product & actuarial if any moves more than 20% from these." if has else
               "Agree the claims KPIs to track after launch and the thresholds that trigger a review.")),
        _item("early_claims_review", "monitoring", "Review the first claims under the new coverage",
              "File-review the first 25 claims (or first 90 days) for coverage decisions, reserve accuracy and customer "
              "complaints; report findings to Product."),
        _item("feedback_loop", "monitoring", "Schedule the feedback loop to Product & Actuarial",
              "Quarterly claims experience report against launch assumptions, with recommended wording or pricing changes."),
    ]
    return items


def summarize(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    required = [i for i in items if i["required"]]
    done = [i for i in required if i["status"] in ("Done", "N/A")]
    by_stage = {}
    for key, label in STAGES.items():
        st = [i for i in items if i["stage"] == key]
        by_stage[key] = {"label": label, "total": len(st), "complete": sum(i["status"] in ("Done", "N/A") for i in st)}
    pct = round(100 * len(done) / len(required), 0) if required else 0
    return {
        "required_total": len(required),
        "required_complete": len(done),
        "percent_complete": pct,
        "ready": bool(required) and len(done) == len(required),
        "in_progress": sum(i["status"] == "In progress" for i in items),
        "by_stage": by_stage,
    }


def update_item(items: List[Dict[str, Any]], item_id: str, status: Optional[str], owner: Optional[str],
                note: Optional[str]) -> List[Dict[str, Any]]:
    for i in items:
        if i["id"] == item_id:
            if status is not None:
                if status not in STATUSES:
                    raise ValueError(f"status must be one of {STATUSES}")
                i["status"] = status
            if owner is not None:
                i["owner"] = owner.strip()
            if note is not None:
                i["note"] = note.strip()
            i["updated_at"] = datetime.utcnow().isoformat()
            return items
    raise KeyError(item_id)
