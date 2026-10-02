"""
ClaimCenter Test Scenarios panel
================================
Go-live test claims built from the brief's handling guideline: each scenario has the setup, FNOL data,
ClaimCenter steps and the result the guideline says must happen. Testers record Pass / Fail / Blocked.
Generation lives in backend/scenarios.py; claim amounts come from the brief's claims analytics.
"""
from __future__ import annotations

import csv
import io
from typing import Any, Callable, Dict, Optional

import streamlit as st

STATUS_ICON = {"Not run": "⚪", "Pass": "✅", "Fail": "❌", "Blocked": "⛔"}
EXPECTED_LABELS = (("coverage", "Coverage decision"), ("reserve", "Reserve"), ("routing", "Routing / authority"),
                   ("siu", "SIU"), ("letter", "Customer letter"))


def _md(text: Optional[str]) -> str:
    return (str(text) if text is not None else "").replace("$", "\\$")


def _csv(record: Dict[str, Any], categories: Dict[str, str]) -> str:
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["ID", "Category", "Title", "Setup", "Loss description", "Days after inception", "Reported days after loss",
                "Claimed amount", "Steps", *[label for _, label in EXPECTED_LABELS], "Status", "Tester", "Notes"])
    for s in record["scenarios"]:
        f = s["fnol"]
        w.writerow([s["id"], categories.get(s["category"], s["category"]), s["title"], s["setup"], f["loss_description"],
                    f["days_after_policy_inception"], f["reported_days_after_loss"], f.get("claimed_amount", ""),
                    " | ".join(f"{n}. {x}" for n, x in enumerate(s["steps"], 1)),
                    *[s["expected"].get(k, "") for k, _ in EXPECTED_LABELS], s["status"], s["tester"], s["note"]])
    return buf.getvalue()


def render_scenarios(brief: Dict[str, Any], data: Optional[Dict[str, Any]], generate: Callable[[], bool],
                     save: Callable[[str, Dict[str, str]], bool], letters: Optional[Dict[str, Any]] = None) -> None:
    """Render the test scenarios tab. *generate()* and *save(id, {status, tester, note})* call the backend.

    *letters* (the Customer letters data) links each scenario to the letter template it should produce.
    """
    letter_record = (letters or {}).get("letters") or {}
    letters_by_key = {l["key"]: l for l in letter_record.get("letters", [])}
    scenario_letters = (letters or {}).get("scenario_letters") or {}
    st.markdown("### ClaimCenter Test Scenarios")
    st.caption("Test claims to run through ClaimCenter before go-live, built from this brief's handling guideline: "
               "every decision-tree branch, plus SIU, large-loss and recovery cases, with the result the guideline "
               "requires. Claim amounts are real figures from the claims data.")
    if data is None:
        st.error("Could not load the test scenarios from the backend.")
        return
    bid = brief["id"]
    if not data["has_guideline"]:
        st.info("Draft the handling guideline first (Handling guideline tab) — the scenarios test what it tells adjusters to do.")
        return

    record = data.get("scenarios")
    if not record:
        if st.button("🧪 Generate test scenarios", type="primary", key=f"sc_gen_{bid}"):
            with st.spinner("Building test scenarios from the guideline..."):
                if generate():
                    st.rerun()
        return

    summary, statuses, categories = data["summary"], data["statuses"], data["categories"]
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Scenarios", summary["total"])
    c2.metric("Passed", summary["pass"])
    c3.metric("Failed", summary["fail"])
    c4.metric("Blocked", summary["blocked"])
    c5.metric("Not run", summary["not_run"])
    run = summary["total"] - summary["not_run"]
    st.progress(run / summary["total"] if summary["total"] else 0.0, text=f"{run} of {summary['total']} run")
    if summary["all_passed"]:
        st.success("All scenarios pass: ClaimCenter handles this coverage as the guideline requires.")
    elif summary["fail"]:
        st.error(f"{summary['fail']} scenario(s) failing — fix the ClaimCenter configuration or the guideline before go-live.")
    if data["stale"]:
        st.warning("The handling guideline changed after these scenarios were built. Regenerate them so they test "
                   "the current guideline.")
    if record.get("basis") == "proxy":
        st.info("Claim amounts are **proxy data** from related risk patterns; this product has no claims of its own.")

    d1, d2 = st.columns([1, 2])
    d1.download_button("⬇️ Download (.csv)", data=_csv(record, categories), key=f"sc_dl_{bid}", mime="text/csv",
                       file_name=f"claimcenter-test-scenarios-brief-{bid}.csv", use_container_width=True)
    with d2.expander("🔄 Regenerate scenarios"):
        st.caption("Rebuilds every scenario from the current guideline"
                   + (f" — the {run} recorded test result(s) will be lost." if run else "."))
        if st.button("Regenerate", key=f"sc_regen_{bid}"):
            with st.spinner("Rebuilding test scenarios..."):
                if generate():
                    st.rerun()

    st.markdown("---")
    for s in record["scenarios"]:
        icon = STATUS_ICON.get(s["status"], "⚪")
        tester = f" · 👤 {s['tester']}" if s["tester"] else ""
        with st.expander(f"{icon} {s['id']} · {categories.get(s['category'], s['category'])} — {s['title']} — "
                         f"{s['status']}{tester}"):
            f = s["fnol"]
            st.markdown(f"**Setup:** {_md(s['setup'])}")
            st.markdown(
                f"**FNOL data**\n\n"
                f"- Loss: {_md(f['loss_description'])}\n"
                f"- Loss date: {f['days_after_policy_inception']} days after policy inception\n"
                f"- Reported: {f['reported_days_after_loss']} day(s) after the loss\n"
                f"- Claimed amount: **{_md(f.get('claimed_amount'))}** ({f['amount_label']})"
            )
            st.markdown("**Steps**\n\n" + "\n".join(f"{n}. {_md(x)}" for n, x in enumerate(s["steps"], 1)))
            st.markdown("**Expected result**\n\n" + "\n".join(
                f"- **{label}:** {_md(s['expected'].get(k))}" for k, label in EXPECTED_LABELS if s["expected"].get(k)))
            if s["guideline_refs"]:
                st.caption("Tests guideline sections: " + ", ".join(s["guideline_refs"]))
            wanted = [k for k in scenario_letters.get(s["category"], [])]
            linked = [l for k in wanted for key, l in letters_by_key.items()
                      if key == k or (k == "denial_exclusion" and key.startswith("denial_exclusion"))]
            if linked:
                st.caption("Letter template to check: " + ", ".join(
                    f"{l['name']} ({'approved' if l['status'] == 'Approved' else 'draft'})" for l in linked)
                    + " — see the Customer letters tab.")

            key = f"sc_{bid}_{s['id']}"
            with st.form(key=f"{key}_form", border=False):
                a, b = st.columns([1, 2])
                status = a.selectbox("Result", statuses, index=statuses.index(s["status"]), key=f"{key}_status")
                tester_val = b.text_input("Tester", value=s["tester"], key=f"{key}_tester", placeholder="e.g. Claims QA")
                note_val = st.text_area("Notes / defect", value=s["note"], key=f"{key}_note", height=80,
                                        placeholder="What happened in ClaimCenter, defect ID...")
                if st.form_submit_button("Save result", type="primary"):
                    if save(s["id"], {"status": status, "tester": tester_val, "note": note_val}):
                        st.rerun()
            if s.get("updated_at"):
                st.caption(f"Last updated {s['updated_at'][:16].replace('T', ' ')} UTC")
