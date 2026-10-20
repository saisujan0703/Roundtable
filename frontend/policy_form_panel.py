"""
Policy Wording panel
====================
Upload the product's policy form (PDF, DOCX, TXT) so the handling guideline and letters quote the real clauses,
and screen each exclusion against the claims the brief stands on: "would this exclusion have caught these
claims?". Parsing and the screen live in backend/policy_form.py.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, Optional

import pandas as pd
import streamlit as st

from money import inr


def _md(text: Optional[str]) -> str:
    return (str(text) if text is not None else "").replace("$", "\\$")


def _money(v: Optional[float]) -> str:
    return inr(v)


def render_policy_form(brief: Dict[str, Any], data: Optional[Dict[str, Any]],
                       upload: Callable[[str, bytes], bool], remove: Callable[[], bool]) -> None:
    """Render the tab. *upload(filename, bytes)* and *remove()* call the backend and return True on success."""
    st.markdown("### Policy Wording")
    st.caption("Upload the coverage's policy form or endorsement. The handling guideline and denial letters then "
               "quote its clauses instead of [TBD] placeholders (Legal still confirms each one), and each exclusion "
               "is screened against today's claims to show which of them it would catch.")
    if data is None:
        st.error("Could not load the policy wording from the backend.")
        return
    bid, form, screen = brief["id"], data.get("form"), data.get("screen")

    with st.expander("⬆️ Upload policy form" if not form else f"🔁 Replace {form['filename']}", expanded=not form):
        f = st.file_uploader("Policy form (PDF with a text layer, DOCX, TXT or MD; max 5 MB)",
                             type=["pdf", "docx", "txt", "md"], key=f"pf_file_{bid}")
        if f is not None and st.button("Upload and parse", type="primary", key=f"pf_upload_{bid}"):
            with st.spinner("Reading the policy form..."):
                if upload(f.name, f.getvalue()):
                    st.rerun()
        if form:
            st.caption("Uploading a new form, or removing this one, flags a drafted handling guideline for redrafting.")
    if not form:
        st.info("No policy form uploaded yet: the guideline and letters keep [TBD] placeholders for the wording.")
        return

    counts, kinds = form["counts"], data["kinds"]
    cols = st.columns(5)
    for col, k in zip(cols, ("insuring_agreement", "definition", "exclusion", "condition", "limit")):
        col.metric(kinds[k], counts.get(k, 0))
    st.caption(f"**{_md(form['filename'])}** · {form['characters']:,} characters · uploaded "
               f"{form['uploaded_at'][:16].replace('T', ' ')} UTC · clause types are detected from headings, so "
               "check them below.")

    st.markdown("#### Exclusion screen against today's claims")
    if not screen:
        st.info("This brief has no claims history to screen the exclusions against.")
    elif not screen["exclusions"]:
        st.warning("No exclusions were detected in the form. Check that it has an 'Exclusions' heading.")
    else:
        st.caption(f"{screen['claims_screened']:,} claims screened. Each exclusion is matched to claim descriptions "
                   "and denial reasons by shared concepts (wear and tear, mechanical breakdown, flood...); exceptions "
                   "in the exclusion ('unless...') are ignored. A keyword screen to focus the wording review — not a "
                   "coverage decision.")
        st.dataframe(pd.DataFrame([{
            "Clause": r["clause_id"], "Exclusion": r["text"][:90], "Concepts": ", ".join(r["concepts"]) or "—",
            "Claims caught": r["matched_claims"], "% of claims": r["matched_share_pct"],
            "Incurred": _money(r["matched_incurred"]), "Denied today for same reason": r["denied_today_same_reason"],
        } for r in screen["exclusions"]]), hide_index=True, width="stretch")
        for r in screen["exclusions"]:
            if not r["matched_claims"]:
                continue
            with st.expander(f"{r['clause_id']} would catch {r['matched_claims']} claims ({r['matched_share_pct']}%)"):
                st.markdown(f"> {_md(r['text'])}")
                st.markdown("\n".join(f"- **{d['claims']}** claims — “{_md(d['description'])}” ({_money(d['incurred'])}"
                                      f"; shared: {', '.join(d['concepts'])})" for d in r["descriptions"]))
                if r["denied_today_same_reason"]:
                    st.caption(f"{r['denied_today_same_reason']} of these claims are already denied today for the "
                               "same reason: if the new coverage is meant to pay them, this exclusion conflicts "
                               "with its purpose.")
        if screen["not_matched_by_any_exclusion"]:
            st.caption("Not caught by any exclusion (these stay covered if they meet the insuring agreement): "
                       + "; ".join(f"“{_md(d['description'])}” ({d['claims']})"
                                   for d in screen["not_matched_by_any_exclusion"]))

    st.markdown("#### Clauses")
    kind = st.selectbox("Show", ["All", *kinds.values()], key=f"pf_kind_{bid}")
    for c in form["clauses"]:
        if kind != "All" and kinds[c["kind"]] != kind:
            continue
        with st.expander(f"{c['id']} · {kinds[c['kind']]} — {_md(c['heading'])}"):
            st.markdown(_md(c["text"]))

    if st.button("🗑️ Remove policy form", key=f"pf_remove_{bid}"):
        if remove():
            st.rerun()
