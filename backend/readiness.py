"""
Claims Readiness Checklist
==========================
What the Claims department must have in place before a new product launches:
policy wording reviewed, ClaimCenter configured, reserving guidance set,
vendors and surveyors, routing & authority, staffing, intake, payments,
training; IRDAI claim-settlement timelines, IRDAI and reinsurance reporting,
motor third-party (MACT) and employee's compensation claims, grievances and
records; and post-launch monitoring.

Each item carries guidance derived from the brief's own claims analytics and
launch operations plan (numbers are quoted from backend.analytics /
backend.operations output, never invented). Items are created once per brief;
after that only status / owner / note change.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

from backend import compliance, operations
from backend.money import inr

STATUSES = ("Not started", "In progress", "Done", "N/A")

STAGES = {
    "wording": "1. Policy wording review",
    "setup": "2. Operational setup",
    "regulatory": "3. Regulatory, reporting & finance",
    "monitoring": "4. Post-launch monitoring",
}
# Items added after the first checklists were stored; a stored checklist missing them is rebuilt (keeping progress)
ADDED_ITEM_IDS = {"staffing_plan", "pc_cc_integration", "intake_channels", "litigation_management", "cat_response",
                  "tpa_delegation", "payments_setup", "state_compliance", "stat_reporting", "reinsurance_reporting",
                  "injury_claims_statutory", "complaints_process", "records_privacy"}


DENIAL_NAMES = {
    "mechanical_breakdown_excluded": "mechanical breakdown exclusion",
    "wear_tear_deterioration": "wear & tear / gradual deterioration exclusion",
    "flood_excluded": "flood / surface water exclusion",
    "engine_damage_excluded": "engine damage from water ingress (engine-protect add-on not bought)",
    "excluded_peril": "excluded peril",
    "coverage_not_purchased": "coverage not purchased",
    "late_notice": "late notice",
}


def _money(v: Optional[float]) -> str:
    """Rupees with Indian digit grouping: 1234567 -> "₹12,34,567"."""
    return inr(v)


def _item(item_id: str, stage: str, title: str, guidance: str, required: bool = True) -> Dict[str, Any]:
    return {"id": item_id, "stage": stage, "title": title, "guidance": guidance, "required": required,
            "status": "Not started", "owner": "", "note": "", "updated_at": None}


def build_checklist(brief_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Create the readiness checklist for a brief, tailored with its claims analytics when available.

    For a proxy-based brief, every number-backed guidance is marked as proxy data, and two items are added:
    validate the proxies, and start the product's own claims history.
    """
    try:
        plan = operations.build_plan(brief_data or {})
    except Exception as e:  # the checklist must still open if the plan can't be computed
        print(f"[NOTE] Launch operations plan unavailable: {type(e).__name__}: {e}")
        plan = {"has_data": False}
    items = _build_items(brief_data, plan)
    basis = ((brief_data or {}).get("claims_analytics") or {}).get("basis") or {}
    if basis.get("basis") != "proxy":
        return items
    proxies = " + ".join(basis.get("proxy_tags") or [])
    generic = {i["id"]: i["guidance"]
               for i in _build_items({"title": (brief_data or {}).get("title")}, {"has_data": False})}
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


def needs_upgrade(items: List[Dict[str, Any]]) -> bool:
    return not ADDED_ITEM_IDS <= {i["id"] for i in items}


def carry_over(new_items: List[Dict[str, Any]], old_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Keep status, owner, note and timestamp of items in both lists (guidance comes from the new list)."""
    old = {i["id"]: i for i in old_items}
    for i in new_items:
        if i["id"] in old:
            i.update({k: old[i["id"]][k] for k in ("status", "owner", "note", "updated_at")})
    return new_items


def _build_items(brief_data: Dict[str, Any], plan: Dict[str, Any]) -> List[Dict[str, Any]]:
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
        _item("proof_requirements", "wording", "Set proof-of-loss and survey requirements",
              "Specify the evidence needed to establish a covered loss (survey report, diagnostic data, photos, repair "
              "estimate) and who may provide it. Losses of ₹50,000 or more on motor, or ₹1 lakh or more on other lines, "
              "must be surveyed by an IRDAI-licensed surveyor and loss assessor. Ask only for documents directly related "
              "to the claim: under the IRDAI Master Circular 2024 no claim may be rejected for want of documents."),
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
               f"See docs/01_ENTITY_EXTENSION_GUIDE.md and docs/04_PRODUCT_MODEL_WRITE_PATH.md." if has else
               "Add the coverage type, loss cause/risk tag and FNOL questions in ClaimCenter configuration.")),
        _item("reserving_guidance", "setup", "Issue FNOL reserving guidance",
              (f"Current FNOL reserves develop to {rd.get('incurred_to_initial_ratio')}x (baseline "
               f"{rd.get('baseline_incurred_to_initial_ratio')}x); {rd.get('claims_developed_over_25pct')}% of claims develop "
               f">25%. Set the default initial reserve near the average paid on closed claims "
               f"({_money(sev.get('avg_paid_closed'))}) and review it quarterly." if has else
               "Set a default initial reserve per exposure type and a review cadence.")),
        _item("vendor_network", "setup", "Line up vendor / repair network",
              (f"Median cycle time is {h.get('cycle_time_median_days')} days vs {h.get('baseline_cycle_time_median_days')} "
               f"baseline. Contract network garages for cashless repair, licensed surveyors and loss assessors, and "
               f"salvage buyers with capacity for ~{latest_full.get('claims', 0)} claims a year at today's volume. The "
               f"surveyor must be allocated within 24 hours of intimation and report within 15 days." if has else
               "Identify and contract the network garages, licensed surveyors and salvage buyers this coverage needs; "
               "the surveyor must be allocated within 24 hours of intimation and report within 15 days.")),
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
        *_operations_items(h, plan),
        _item("training", "setup", "Train adjusters and publish handling guidelines",
              "Publish a claims handling guideline for the new coverage (coverage decision tree, documentation, "
              "reserving, authority) and train the handling group before the first policy is bound."),

        # ---- 3. Regulatory, reporting & finance -------------------------------------
        *_regulatory_items(plan),

        # ---- 4. Post-launch monitoring --------------------------------------------
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


def _operations_items(h: Dict[str, Any], plan: Dict[str, Any]) -> List[Dict[str, Any]]:
    has = bool(plan.get("has_data"))
    sf, lit, ll = plan.get("staffing") or {}, plan.get("litigation") or {}, plan.get("large_losses") or {}
    groups = ", ".join(g["group"] for g in sf.get("handling_groups") or [])
    lit_states = ", ".join(f"{s['state']} ({s['rate_pct']}%)" for s in (lit.get("states") or [])[:4])
    cat_events = ", ".join(e["cat_code"] for e in (ll.get("cat_events") or [])[:3])
    has_cat = has and (ll.get("cat_claims") or 0) > 0
    late = h.get("late_reported_pct")
    return [
        _item("staffing_plan", "setup", "Plan adjuster staffing and capacity",
              (f"{sf['claims_last_12_months']} of these claims were reported in the last 12 months and stay open "
               f"{sf['mean_cycle_days']} days on average, so about {sf['projected_open_inventory']:.0f} are open at any "
               f"time. At today's median caseload of {sf['caseload_used']} open claims per adjuster that is "
               f"{sf['adjusters_needed_fte']} FTE (handled today by {groups}). Set the expected uptake in the Launch "
               f"operations tab and confirm hiring and training lead time." if has and sf.get("has_data") else
               "Estimate monthly claim volume and average days open, divide the open inventory by the target caseload "
               "per adjuster, and confirm hiring and training lead time.")),
        _item("pc_cc_integration", "setup", "Test PolicyCenter → ClaimCenter policy verification",
              "Confirm the new coverage, its limits and deductible come through on the verified policy in ClaimCenter "
              "(policy search and retrieval), including mid-term endorsements that add or remove it, and that no "
              "payment can be made under it on an unverified policy. The policy-verification test scenarios check this."),
        _item("intake_channels", "setup", "Prepare FNOL intake (call center, digital, agents)",
              "Turn the handling guideline's FNOL questions (section 3) into the call-center script, the digital FNOL "
              "form and agent instructions, and brief the intake team on routing."
              + (f" {late}% of these claims today are reported more than 30 days after the loss; the script must "
                 f"record the reason for any delay." if late is not None else "")
              + " Late intimation alone is never a reason to reject or close a claim (IRDAI Master Circular 2024)."),
        _item("litigation_management", "setup", "Set up litigation management and panel counsel",
              (f"Litigation rate {lit['rate_pct']}%"
               + (f" vs {lit['baseline_rate_pct']}% baseline" if lit.get("baseline_rate_pct") is not None else "")
               + f" ({lit['litigated_claims']} litigated claims)."
               + (f" Highest-litigation states: {lit_states}." if lit_states else "")
               + " Appoint panel advocates there for consumer commission, MACT and civil court matters, and set "
               "litigation guidelines and budget approval."
               if has else "Appoint panel advocates for the launch states (consumer commissions, MACT, civil courts) "
                           "and set litigation guidelines.")),
        _item("cat_response", "setup", "Prepare a catastrophe response plan",
              (f"{ll['cat_claims']} of these claims ({ll['cat_share_of_incurred_pct']}% of incurred) came from "
               f"catastrophe events ({cat_events}). Define surge staffing, standby surveyor and garage capacity in "
               f"flood- and cyclone-prone states, and CAT coding for this coverage." if has_cat else
               "No catastrophe-coded claims in this pattern's history. Confirm with Product whether the covered peril "
               "can produce CAT events; if so, define surge staffing and CAT coding."), required=has_cat),
        _item("tpa_delegation", "setup", "Decide on TPA / delegated authority",
              "If any claims will be handled by a third-party administrator or under delegated authority, contract it, "
              "set its authority limits, reporting and audit rights, and give it the guideline, letters and IRDAI "
              "claim timelines.",
              required=False),
        _item("payments_setup", "setup", "Set up claim payments",
              "Configure payment methods (NEFT / RTGS to a verified bank account, cashless settlement with network "
              "garages), payee rules (financier under a hypothecation endorsement, nominee, legal heirs), KYC of "
              "payees, and TDS on surveyor and vendor fees [TBD — Finance: applicable sections]. A claim settled late "
              "carries interest at bank rate plus 2% from intimation, paid without being asked; the payment deadline "
              "comes from the compliance matrix."),
    ]


def _regulatory_items(plan: Dict[str, Any]) -> List[Dict[str, Any]]:
    has = bool(plan.get("has_data"))
    states = plan.get("states") or []
    ll, sr = plan.get("large_losses") or {}, plan.get("statutory_reporting") or {}
    inj = plan.get("injury_claims") or {}
    products = sorted({r["product"] for r in sr.get("rows") or []})
    rules = [compliance.rule_for(s["state"], products) for s in states]
    sources = "; ".join(sorted({r["source"] for r in rules}))
    no_rule = sum(r["placeholder"] for r in rules)
    top = ", ".join(f"{s['state']} {s['exposure_share_pct']}%" for s in states[:3])
    thr = {t["threshold"]: t for t in ll.get("thresholds") or []}
    t10l, t25l = thr.get(1_000_000), thr.get(2_500_000)
    injury = []
    if inj.get("mact_claims"):
        injury.append(
            f"{inj['mact_claims']} of these claims ({inj['mact_share_pct']}%) carry motor third-party injury. These are "
            f"decided by the Motor Accident Claims Tribunal (MACT): name a designated officer to receive the police "
            f"accident reports and make a settlement offer before the Tribunal (Central Motor Vehicles Rules, rule "
            f"150A), and deposit any award within 30 days of it.")
    if inj.get("ec_claims"):
        injury.append(
            f"{inj['ec_claims']} claims ({inj['ec_share_pct']}%) are employee's compensation. Under the Employee's "
            f"Compensation Act, 1923, s.4A, compensation is due from the date of the accident, the admitted amount is "
            f"paid provisionally when liability is disputed, and payment more than one month late brings 12% interest "
            f"and up to 50% penalty: set ClaimCenter diaries for both.")
    return [
        _item("state_compliance", "regulatory", "Confirm IRDAI claim-settlement timelines for every launch state",
              (f"Exposure spans {len(states)} states (largest: {top}). Claim settlement is regulated nationally, so "
               f"every state carries the same rule: {sources}"
               + (f"; {no_rule} have no rule loaded" if no_rule else "") + ". In the Launch operations tab, choose the "
               f"launch states and have Compliance confirm the surveyor-allocation, decision and payment deadlines "
               f"and the rejection / grievance notice. ClaimCenter diaries and the letters' "
               f"{{{{state_required_notice}}}} use these." if has and states else
               "List the launch states and have Compliance confirm the IRDAI surveyor-allocation (24 hours), "
               "survey-report (15 days) and decision (7 days) timelines, the payment deadline and the rejection / "
               "grievance notice; set them as ClaimCenter diaries.")),
        _item("stat_reporting", "regulatory", "Map the coverage to IRDAI reporting lines",
              (f"Suggested IRDAI line(s) of business from the exposures used today: {'; '.join(sr['lines'])}. Finance "
               f"confirms the segment for the IRDAI returns and public disclosures, adds the coverage to the claims "
               f"data reported to the Insurance Information Bureau of India [TBD — Statutory Reporting], and adds it "
               f"to claims MI reports." if has and sr.get("has_data") else
               "Finance assigns the IRDAI line of business for the returns and public disclosures, sets up Insurance "
               "Information Bureau of India reporting, and adds the coverage to claims MI reports.")),
        _item("reinsurance_reporting", "regulatory", "Set large-loss and reinsurance notification rules",
              (f"Claims of ₹10 lakh or more: {t10l['per_year']} a year; ₹25 lakh or more: {t25l['per_year']} a year; "
               f"largest {_money(ll.get('largest'))}. Agree with Reinsurance the notice threshold [TBD — treaty terms], "
               f"whether this coverage sits inside the existing treaties and its obligatory cession to GIC Re, then add "
               f"a ClaimCenter large-loss notification at that threshold." if has and t10l and t25l else
               "Agree with Reinsurance the large-loss notice threshold, whether the coverage sits inside existing "
               "treaties and its obligatory cession to GIC Re; add a ClaimCenter large-loss notification.")),
        _item("injury_claims_statutory", "regulatory", "Motor third-party (MACT) and employee's compensation claims",
              (" ".join(injury) if has and inj.get("applies") else
               "No motor third-party injury or employee's compensation exposures in this pattern's claims. Mark N/A "
               "unless the coverage can pay third-party or employee injury claims."),
              required=bool(has and inj.get("applies"))),
        _item("complaints_process", "regulatory", "Set the grievance redressal and Ombudsman process",
              "Route grievances about this coverage to the Grievance Redressal Officer under its own coverage code: "
              "acknowledge immediately and resolve within 14 days, with reasons citing the policy terms (IRDAI Master "
              "Circular 2024). Confirm the grievance system mirrors to IRDAI's Bima Bharosa portal, that every "
              "rejection and resolution letter names the Insurance Ombudsman with jurisdiction, and that Ombudsman "
              "awards are complied with within 30 days (₹5,000 a day penalty after that). Track grievance volume in "
              "the launch KPIs."),
        _item("records_privacy", "regulatory", "Confirm records retention and data privacy",
              "Classify any new data captured at FNOL (e.g. vehicle diagnostics, telematics, photos, medical records) "
              "under the Digital Personal Data Protection Act, 2023, record the consent and purpose, set its retention "
              "period [TBD — Records Management], and confirm surveyor and vendor access."),
    ]


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
