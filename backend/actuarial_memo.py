"""
Actuarial memorandum
====================
A draft actuarial memorandum and exhibits supporting the Appointed Actuary's technical note for the new coverage,
filed under IRDAI's Use & File procedure. It is assembled from the computed work products: rate indication
(backend.pricing), loss development (backend.reserving), rating plan (backend.rating_plan), business plan
(backend.business_plan) and the actuary's benchmarks and approval (backend.actuarial). Deterministic: every number
is copied from those results, nothing is generated.

Under the IRDAI Master Circular on General Insurance Business (11 June 2024) the insurer's Product Management
Committee (PMC) approves the product and the insurer obtains a UIN before selling it. Pricing must rest on
"appropriate data and/or technical justification", with rates "not excessive or inadequate or unfairly
discriminatory" (Chapter III, 1.2-1.4). The professional standard is the Institute of Actuaries of India's APS 21
(Appointed Actuary and General Insurance, Health Insurance or Reinsurance Business, v2.00, 15 September 2023), with
APS 34 (General Actuarial Practice) for all actuarial work.

What only the insurer can supply (registration number, PMC approval, UIN, the Appointed Actuary's certificate) is
left as [TBD], and the memo says it is a draft until the indication is approved.
"""
from __future__ import annotations

from datetime import date
from typing import Any, Dict, List, Optional

MASTER_CIRCULAR = "IRDAI Master Circular on General Insurance Business, 2024"
EOM_LIMIT_PCT = 30.0   # IRDAI (Expenses of Management, including Commission, of Insurers) Regulations, 2024
STANDARDS = [
    ("IAI APS 21 §6.1", "Premium rates fair: neither excessive nor inadequate", "the indication as a whole (Sections 1-2)"),
    ("IAI APS 21 §6.2", "Claims costs and handling expenses, expense provision, future inflation, legislative change",
     "trend (Exhibit 1), expense and LAE provisions (Exhibit 4)"),
    ("IAI APS 21 §6.3", "Own experience compared with industry or reinsurer experience; data quality, large losses",
     "data (Section 3), CAT and large losses (Exhibit 1), credibility (Exhibit 3)"),
    ("IAI APS 21 §7", "Capital requirements for a new product", "business plan and capital (Exhibit 6)"),
    ("IAI APS 34", "General Actuarial Practice (data, assumptions, communication)", "this memorandum"),
    (f"{MASTER_CIRCULAR}, Ch. III 1.2-1.4", "Sound actuarial basis; rates from data or technical justification, not "
     "excessive, inadequate or unfairly discriminatory; allowance for catastrophes and large losses",
     "Exhibits 1, 3 and 5"),
    (f"{MASTER_CIRCULAR}, Ch. II C.1 and Ch. III 2-3", "PMC approval, Use & File documentation, UIN before sale",
     "header and Section 7"),
    ("IRDAI EoM Regulations, 2024", f"Expenses of management within {EOM_LIMIT_PCT:.0f}% of gross written premium",
     "Exhibit 4"),
]


def _m(x: Optional[float], cents: bool = True) -> str:
    if x is None:
        return "—"
    return f"${x:,.2f}" if cents else f"${x:,.0f}"


def _p(x: Optional[float], n: int = 1) -> str:
    return "—" if x is None else f"{x:.{n}f}%"


def eom_check(expense_ratio_pct: float, ulae_pct: float) -> str:
    """The product's expense ratio against the company-wide expenses-of-management limit."""
    over = expense_ratio_pct > EOM_LIMIT_PCT
    out = (f"Expenses of management: the expense ratio of {_p(expense_ratio_pct)} is "
           f"{'**above**' if over else 'within'} the {EOM_LIMIT_PCT:.0f}% of gross written premium that IRDAI's EoM "
           f"Regulations, 2024 allow a general insurer across its whole book; in-house claims handling (ULAE "
           f"{_p(ulae_pct)} of losses) also counts towards the limit. GST is charged on top of the premium and is not "
           "an expense here.")
    if over:
        out += " Finance must show the excess is absorbed elsewhere in the book before the PMC approves."
    return out


def _table(headers: List[str], rows: List[List[Any]]) -> str:
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    out += ["| " + " | ".join("—" if v is None else str(v) for v in r) + " |" for r in rows]
    return "\n".join(out)


def build(title: str, indication: Dict[str, Any], development: Dict[str, Any], plan: Dict[str, Any],
          business: Dict[str, Any], state: Dict[str, Any], status: Dict[str, Any],
          launch_states: Optional[List[str]] = None, extras: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """*extras*: {"provenance": cited sources of the company settings, "rating_tests": backend.rating_tests summary,
    "monitoring": backend.monitoring result, "parametric": backend.parametric result or None}."""
    if not indication.get("available"):
        return {"available": False, "reason": indication.get("reason", "No indication to document.")}
    extras = extras or {}
    prov = extras.get("provenance") or {}
    a, unit = indication["assumptions"], indication["exposure_unit"]
    cred = indication["credibility"]
    ap = status.get("approval") if status.get("approved") else None
    selected = ap["selected_premium"] if ap else None
    draft = not status.get("approved")
    tbd = []

    def TBD(what: str) -> str:
        tbd.append(what)
        return f"[TBD: {what}]"

    md = [f"# Actuarial Memorandum — {title}",
          f"**Status:** {'DRAFT — the indication is not approved' + (' (approval stale)' if status.get('stale') else '') if draft else 'Indication approved by ' + ap['name'] + ' on ' + ap['approved_at'][:10]}  ",
          f"**Insurer:** {TBD('insurer name and IRDAI registration number')}  ",
          f"**Filing route:** Use & File ({MASTER_CIRCULAR})  ",
          f"**PMC approval:** {TBD('Product Management Committee approval date')}  ",
          f"**UIN:** {TBD('UIN allotted by IRDAI after PMC approval')}  ",
          f"**Proposed launch date:** {indication['effective_date']}  ",
          f"**Launch states:** {', '.join(launch_states) if launch_states else TBD('launch states')}  ",
          f"**Prepared:** {date.today().isoformat()} from Roundtable (synthetic demo data — illustrative figures)",
          "",
          "## 1. Purpose",
          f"This memorandum supports the proposed rates for a new coverage, *{title}*. It documents the data, "
          f"methods and assumptions behind the indicated average premium of **{_m(indication['indicated_premium'])} "
          f"per {unit[:-1] if unit.endswith('s') else unit}**"
          + (f" and the selected rate of **{_m(selected)}**" if selected else "") + ", and the rating plan that "
          "distributes it, and supports the Appointed Actuary's technical note for the PMC. Motor third-party "
          "liability premium is set by the Central Government under the Motor Vehicles Act, 1988 and is not "
          "priced here.",
          "",
          "## 2. Summary of the indication",
          _table(["Step", "Per exposure"], [[s["step"], _m(s["value"])] for s in indication["steps"]]),
          "",
          f"Range on the frequency trend's 95% interval: {_m(indication['range']['low'])} – "
          f"{_m(indication['range']['high'])}. Today's average premium in the same scope: "
          f"{_m(indication.get('average_current_premium'))} (the indication is "
          f"{_p(indication.get('share_of_current_premium_pct'))} of it).",
          ""]
    if ap and ap.get("deviation_pct") is None:
        md += [f"**Selected rate with a $0 indication** (no incremental cost in the data). Basis: {ap['note']}", ""]
    elif ap and abs(ap["deviation_pct"]) > 0.05:
        md += [f"**Selected vs indicated:** {ap['deviation_pct']:+.1f}%. Reason: {ap['note'] or '—'}", ""]

    md += ["## 3. Data",
           f"Company claims and earned exposure from PolicyCenter / ClaimCenter extracts, valued "
           f"{indication['valuation_date']}. Accident years {', '.join(str(r['year']) for r in indication['experience'])} "
           f"are used ({a['experience_years']} complete years; the current partial year is excluded as immature).",
           ("The priced claims are those the new coverage would newly pay: claims denied today for a coverage reason "
            "and not excluded by the new wording, costed from paid claims with the same loss description."
            if indication["priced_claims"] == "newly_covered" else
            "All claims of the risk pattern are priced (no covered-claims set was available)."),
           "",
           "Limitations (APS 21 §6.3.1, data quality): the data is a synthetic demonstration extract; there is no payment "
           "transaction history, so development triangles are reconstructed from report and close dates; "
           "losses below a policy's deductible are unobserved.", ""]
    if indication["basis"] == "proxy":
        md += ["**Proxy experience:** the product has no claims of its own; the experience is the pooled claims of "
               "related risk patterns. The Appointed Actuary must confirm the perils are comparable.", ""]

    md += ["## Exhibit 1 — Experience, development and trend",
           _table(["AY", "Exposure", "Claims", "Loss cost", "Non-CAT capped share", "Development", "Trend",
                   "Trended loss cost"],
                  [[r["year"], f"{r['earned_exposure']:,.0f}", r["claims"], _m(r["loss_cost_per_exposure"]),
                    f"{r.get('basic_share', 1):.3f}", f"{r['development_factor']:.4f}", f"{r['trend_factor']:.4f}",
                    _m(r["trended_loss_cost"])] for r in indication["experience"]]),
           "",
           f"- Frequency trend {a['frequency_trend_pct']:+.1f}%/yr"
           + (f" (fitted {a['fitted_frequency_trend_pct']:+.1f}%/yr ex-CAT, constant mix, "
              f"{'significant' if a['fitted_trend_significant'] else 'not significant'})"
              if a.get("fitted_frequency_trend_pct") is not None else "")
           + f"; severity trend {a['severity_trend_pct']:+.1f}%/yr; trended from each accident year's midpoint to the "
             f"average accident date {indication['average_accident_date']}.",
           ]
    cl = indication["cat_large"]
    if cl["applied"]:
        md.append(f"- Catastrophe losses removed and replaced by a {cl['cat_load_pct']:.1f}% provision; non-CAT losses "
                  f"capped at {_m(cl['cap'], False)} per claim with an excess factor of {cl['excess_factor']:.3f} "
                  f"(from the {cl['excess_source']}'s long-run losses).")
    elif cl["cat_driven"]:
        md.append(f"- Catastrophes are {cl['cat_share_pct']:.0f}% of losses; priced with CAT losses in. "
                  + TBD("catastrophe-model load"))
    md += ["", "## Exhibit 2 — Loss development"]
    if development.get("has_data"):
        inc = development["incurred"]
        md += [f"Factors from the {'pattern' if development['factor_basis'] == 'pattern' else 'whole scope'} "
               f"({development['factor_basis_claims']:,} claims). Method used in the indication: "
               f"{indication['development']['label']} on {indication['development']['measure']}s"
               + ("" if indication["development"]["applied"] else " (switched off)") + ".",
               "",
               _table(["Age (months)", "Incurred age-to-age", "AYs"],
                      [[f"{f['from_age']}-{f['to_age']}", f"{f['factor']:.4f}", f["years_used"]] for f in inc["factors"]]),
               "",
               _table(["AY", "Age", "Reported incurred", "CDF", "Chain-ladder ultimate", "BF ultimate"],
                      [[r["year"], r["age_months"], _m(r["latest"], False), f"{r['cdf']:.4f}",
                        _m(r["chain_ladder_ultimate"], False), _m(r["bf_ultimate"], False)] for r in inc["rows"]]),
               "", f"Tail factor {inc['tail']:.3f}. " + " ".join(development.get("notes") or [])]
    else:
        md.append("No development triangle could be built; a heuristic development factor was used.")

    md += ["", "## Exhibit 3 — Credibility (APS 21 §6.3: own and industry experience)",
           f"Classical full-credibility standard of {cred['full_credibility_claims']:,} claims; {cred['claims']:,} "
           f"claims in the experience give Z = {cred['z']:.3f}."]
    bench = [b for b in state.get("benchmarks") or [] if b.get("include", True)]
    if bench:
        md += ["", _table(["Source", "Type", "Value", "As of", "Unit", "Reference"],
                          [[b["source"], b["kind"].replace("_", " "), _m(b["value"]), b["as_of"], b.get("unit") or "—",
                            b.get("url") or "—"] for b in bench]),
               "", f"Complement: mean trended benchmark loss cost {_m(cred['complement'])}"
                   + ("" if cred["applied"] else " (not applied by the actuary's selection)") + "."]
    else:
        md += ["", "No external benchmark was entered, so the experience is used at full weight. "
               + TBD("credibility complement (IIB industry statistics, a competitor's published rate or a "
                     "reinsurer quote)")]

    saved = state.get("assumptions") or {}

    def source(key: str, missing: str) -> str:
        """The brief's own selection, else the cited company setting, else a [TBD] for the Appointed Actuary."""
        if key in saved:
            return "selected for this product by the actuary"
        return prov.get(key) or TBD(missing)

    md += ["", "## Exhibit 4 — Expense, LAE and profit provisions (APS 21 §6.2)",
           _table(["Provision", "Value", "Source"],
                  [["ALAE", _p(indication["alae_pct"]), "company claims data (paid expense / incurred)"],
                   ["ULAE", _p(a["ulae_pct"]), source("ulae_pct", "ULAE study")],
                   ["Expense ratio (commission, levies, general, other acquisition; excl. GST)",
                    _p(a["expense_ratio_pct"]),
                    source("expense_ratio_pct", "company expense exhibit by component")],
                   ["Profit & contingencies", _p(a["profit_pct"]),
                    source("profit_pct", "profit provision support (return on capital)")],
                   ["Unreported demand load", _p(a["unreported_load_pct"]) if indication["priced_claims"] == "newly_covered"
                    else "n/a", prov.get("unreported_load_pct") or "actuarial judgement"],
                   ["Adverse selection load", _p(a["adverse_selection_pct"]),
                    prov.get("adverse_selection_pct") or "actuarial judgement"]]),
           "", eom_check(a["expense_ratio_pct"], a["ulae_pct"]), ""]

    md.append("## Exhibit 5 — Rating plan (not unfairly discriminatory, Master Circular Ch. III 1.4)")
    if plan.get("available"):
        md += [f"Base rate **{_m(plan['base_rate'])}** at base levels "
               + ", ".join(f"{k.replace('_', ' ')} = {v}" for k, v in plan["base_levels"].items())
               + f"; off-balance factor {plan['off_balance']:.4f} reproduces the indicated average premium.", ""]
        for v in plan["variables"]:
            md += [f"**{v['label']}**", "",
                   _table(["Level", "Exposure", "Claims", "GLM frequency", "Severity (one-way)", "Selected"],
                          [[L["level"] + (" (base)" if L["base"] else ""), f"{L['exposure']:,.0f}", L["claims"],
                            f"{L['frequency_glm']:.3f}", f"{L['severity_oneway']:.3f}", f"{L['selected']:.3f}"]
                           for L in v["levels"]]), ""]
        if plan["deductibles"].get("available"):
            d = plan["deductibles"]
            md += ["**Deductible factors** (loss elimination)", "",
                   _table(["Deductible", "Loss eliminated", "Factor"],
                          [[_m(r["deductible"], False) + (" (base)" if r["base"] else ""), _p(r["loss_elimination_pct"]),
                            f"{r['factor']:.3f}"] for r in d["rows"]]), ""]
        if plan["ilfs"].get("available"):
            md += ["**Increased-limit factors**", "",
                   _table(["Limit", "ILF", "Losses above"],
                          [[_m(r["limit"], False) + (" (basic)" if r["basic"] else ""), f"{r['ilf']:.3f}",
                            f"{r['losses_above']}" + (" (thin)" if r["thin"] else "")] for r in plan["ilfs"]["rows"]]), ""]
        md += ["**Rates by territory at base levels**", "",
               _table(["Territory", "Relativity", "Rate"],
                      [[s["territory"], f"{s['relativity']:.3f}", _m(s["rate_at_base_levels"])] for s in plan["state_rates"]]),
               "", " ".join(plan["notes"]), ""]
    else:
        md += [plan.get("reason", "No rating plan."), ""]

    if business.get("available"):
        t = business["totals"]
        md += ["## Exhibit 6 — Business plan (supporting the profit provision)",
               f"At {_m(business['rate'])} per exposure and {business['inputs']['take_up_pct']:.1f}% take-up of "
               f"{business['eligible_exposure']:,.0f} eligible {business['exposure_unit']}: "
               f"{business['inputs']['years']}-year premium {_m(t['written_premium'], False)}, combined ratio "
               f"{_p(t['combined_ratio_pct'])}, after-tax result {_m(t['after_tax_result'], False)}"
               + (f"; break-even take-up {business['breakeven_take_up_pct']:.1f}%." if business.get("breakeven_take_up_pct")
                  else "."), "",
               _table(["Scenario", "Combined ratio", "After-tax result", "Return on capital"],
                      [[s["scenario"], _p(s["combined_ratio_pct"]), _m(s["after_tax_result"], False),
                        _p(s["return_on_peak_capital_pct"])] for s in business["scenarios"]]), ""]

    pm = extras.get("parametric")
    if pm and pm.get("available"):
        br = pm["basis_risk"]
        md += ["## Exhibit 7 — Parametric option",
               f"Payout {_m(pm['config']['payout'], False)} per policy when the event index reaches "
               f"{_m(pm['config']['trigger_index'])} per exposure. {pm['events_observed']} company catastrophe event(s) "
               f"in {pm['years_observed']:.1f} years (burn credibility Z = {pm['credibility_z']:.2f}); risk load "
               f"{pm['risk_load_pct']:.1f}%. Average rate {_m(pm['average_rate'])}.", "",
               _table(["State", "Burn probability", "Hazard probability", "Hazard source", "Selected", "Rate"],
                      [[s["state"], f"{s['burn_probability']:.4f}",
                        "—" if s["hazard_probability"] is None else f"{s['hazard_probability']:.4f}",
                        s["hazard_source"] or "—", f"{s['selected_probability']:.4f}", _m(s["rate"])]
                       for s in pm["states"] if s["selected_probability"] > 0]), "",
               f"Basis risk on history: {br['hits']} hit(s), {br['misses']} miss(es), {br['false_alarms']} false "
               f"alarm(s)" + (f"; miss rate {br['miss_rate_pct']:.0f}%." if br["miss_rate_pct"] is not None else "."),
               ""]

    rt = extras.get("rating_tests") or {}
    md += ["## Exhibit 8 — Implementation and monitoring",
           "**PolicyCenter rating tests:** "
           + (f"{rt['pass']} of {rt['total']} cases pass ({rt['fail']} fail, {rt['blocked']} blocked, "
              f"{rt['not_run']} not run)" + (" — STALE, the rating plan changed since generation" if rt["stale"] else "")
              + "." if rt.get("generated") else TBD("PolicyCenter rating test results")), ""]
    mon = extras.get("monitoring") or {}
    if mon.get("available"):
        md += [f"**Actual vs expected ({mon['mode']}, {mon['period']['start']} to {mon['period']['end']}, "
               f"{mon['claims_reported']} claims, Z = {mon['credibility_z']:.2f}):** overall {mon['overall'].upper()}.", "",
               _table(["KPI", "Actual", "Expected", "A/E", "Credibility-weighted A/E", "Status"],
                      [[k["kpi"], k["actual"], k["expected"], k["a_to_e"], k["credibility_weighted_a_to_e"],
                        k["status"]] for k in mon["kpis"]]), "",
               "**Monitoring plan**", "",
               _table(["KPI", "Cadence", "Threshold", "Owner"],
                      [[p["kpi"], p["cadence"], p["threshold"], p["owner"]] for p in mon["plan"]]), ""]

    md += ["## 6. Standards and regulations",
           _table(["Reference", "Requirement", "Where addressed"], [list(x) for x in STANDARDS]), "",
           "## 7. Certification and approval",
           "- " + TBD("Appointed Actuary's certificate that the premium rates are fair and sound (APS 21 §6.1), "
                      "countersigned by the CEO"),
           "- " + TBD("PMC sign-off by the Chief Underwriting Officer, the Appointed Actuary and the other members "
                      "(quorum of three plus the Appointed Actuary)"),
           "- " + TBD("Appointed Actuary's Certificate of Practice from the Institute of Actuaries of India"), "",
           "## 8. Notes and limitations", *[f"- {n}" for n in indication["notes"]]]
    return {"available": True, "markdown": "\n".join(md), "draft": draft, "tbd": tbd,
            "filename": f"actuarial_memo_{indication['effective_date']}.md"}
