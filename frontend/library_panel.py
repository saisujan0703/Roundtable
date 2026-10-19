"""
Library: the risk patterns and the competitor / regulatory sources every brief draws on.
- Risk patterns: the built-in claim tags plus custom keyword patterns (backend.risk_patterns), with a preview of
  what the keywords catch before saving.
- Sources: the built-in curated set plus sources users add, typed in or picked from a web search
  (backend.evidence_sources). Nothing found online is saved until a person reviews it.
"""
from __future__ import annotations

import html
from datetime import date
from typing import Any, Callable, Dict, List, Optional

import pandas as pd
import streamlit as st

Call = Callable[..., Optional[Dict[str, Any]]]
TYPE_LABEL = {"competitor": "Competitor", "regulatory": "Regulatory"}


def _keywords(text: str) -> List[str]:
    return [k.strip() for k in text.replace("\n", ",").split(",") if k.strip()]


# ---------------------------------------------------------------------------
# Risk patterns
# ---------------------------------------------------------------------------
def _render_preview(p: Dict[str, Any]) -> None:
    if not p["claims"]:
        st.warning("No claims match these keywords. Try other words, or broaden the products.")
        return
    a, b, c = st.columns(3)
    a.metric("Matching claims", f"{p['claims']:,}")
    b.metric("Denied", f"{p['denied_pct']:.0f}%")
    c.metric("Accident years", p["years"])
    st.caption("By product: " + ", ".join(f"{k} {v:,}" for k, v in p["products"].items())
               + " · under built-in tags: " + ", ".join(f"{k} {v:,}" for k, v in p["builtin_tags"].items()))
    st.dataframe(pd.DataFrame(p["samples"]).rename(columns={
        "claim_number": "Claim", "loss_date": "Loss date", "product": "Product", "tag": "Built-in tag",
        "description": "Loss description", "denial_reason": "Denial reason"}), hide_index=True, use_container_width=True)
    st.caption("Sample matches: check they are the losses you mean before saving. Keywords match at the start of a "
               "word in the loss description, loss cause and denial reason.")


def _render_patterns(api: Call) -> None:
    data = api("GET", "risk-patterns")
    if data is None:
        return
    st.caption("A brief stands on the claims of a risk pattern. Built-in patterns are the tags ClaimCenter set on each "
               "claim; add your own to analyse a risk those tags don't cover. A custom pattern finds claims by keywords "
               "in their text and works everywhere a built-in tag does: new briefs, proxy patterns, pricing.")

    with st.expander("➕ New risk pattern", expanded=not data["patterns"]):
        with st.form("new_pattern"):
            label = st.text_input("Name", placeholder="E-bike and scooter battery fire")
            kw = st.text_area("Keywords (comma-separated)", placeholder="e-bike, scooter, lithium, battery fire",
                              height=80)
            products = st.multiselect("Only these products (optional)", data["products"])
            desc = st.text_input("Description (optional)", placeholder="What the pattern is meant to capture")
            c1, c2 = st.columns(2)
            preview = c1.form_submit_button("Preview matches")
            save = c2.form_submit_button("Save pattern", type="primary")
        if preview or save:
            body = {"keywords": _keywords(kw), "products": products}
            if preview:
                p = api("POST", "risk-patterns/preview", json=body)
                if p is not None:
                    _render_preview(p)
            else:
                saved = api("POST", "risk-patterns", json={"label": label, "description": desc, **body})
                if saved is not None:
                    st.success(f"Saved as **{saved['key']}**. Pick it when you create a brief.")
                    st.rerun()

    if data["patterns"]:
        st.markdown("##### Custom patterns")
        for p in data["patterns"]:
            used = p["used_by_briefs"]
            with st.container(border=True):
                head, act = st.columns([5, 1.2])
                head.markdown(f"**{html.escape(p['label'])}** · `{p['key']}` · {p['claims']:,} claims"
                              + (f" · used by {', '.join('#' + str(i) for i in used)}" if used else ""))
                head.caption(f"Keywords: {', '.join(p['keywords'])}"
                             + (f" · products: {', '.join(p['products'])}" if p["products"] else " · all products")
                             + (f" · {p['description']}" if p["description"] else "")
                             + f" · added by {p.get('created_by') or '—'}")
                if act.button("Delete", key=f"del_pat_{p['key']}", disabled=bool(used),
                              help="In use by a brief" if used else None, use_container_width=True):
                    if api("DELETE", f"risk-patterns/{p['key']}") is not None:
                        st.rerun()
                with st.expander("Edit"):
                    with st.form(f"edit_{p['key']}"):
                        e_label = st.text_input("Name", p["label"])
                        e_kw = st.text_area("Keywords", ", ".join(p["keywords"]), height=70)
                        e_prod = st.multiselect("Products", data["products"], default=p["products"])
                        e_desc = st.text_input("Description", p["description"])
                        if st.form_submit_button("Save changes"):
                            if api("PUT", f"risk-patterns/{p['key']}",
                                   json={"label": e_label, "keywords": _keywords(e_kw), "products": e_prod,
                                         "description": e_desc}) is not None:
                                st.rerun()
    st.markdown("##### Built-in patterns")
    st.caption(", ".join(f"`{t}`" for t in data["builtin_tags"]))


# ---------------------------------------------------------------------------
# Sources
# ---------------------------------------------------------------------------
def _source_form(key: str, initial: Dict[str, Any], submit: str) -> Optional[Dict[str, Any]]:
    with st.form(key):
        kind = st.radio("Type", list(TYPE_LABEL), format_func=TYPE_LABEL.get, horizontal=True,
                        index=list(TYPE_LABEL).index(initial.get("source_type", "competitor")))
        c1, c2 = st.columns(2)
        name = c1.text_input("Carrier or regulator", initial.get("name", ""),
                             placeholder="Allstate / California Department of Insurance")
        title = c2.text_input("Product, page or regulation title", initial.get("title", ""))
        url = st.text_input("Web address", initial.get("url", ""), placeholder="https://...")
        summary = st.text_area("Summary: what the source says, in your words", initial.get("summary", ""), height=130,
                               help="The brief quotes and cites this text, so keep it to what the page actually says.")
        collected = st.date_input("Date collected", date.fromisoformat(initial.get("date_collected") or date.today().isoformat()))
        if st.form_submit_button(submit, type="primary"):
            return {"source_type": kind, "name": name, "title": title, "url": url, "summary": summary,
                    "date_collected": collected.isoformat(), "origin": initial.get("origin", "manual")}
    return None


def _render_sources(api: Call) -> None:
    data = api("GET", "sources")
    if data is None:
        return
    added, builtin = data["added"], data["builtin"]
    st.caption("Every competitor and regulatory statement in a brief must cite one of these sources. Add as many as you "
               "need: from then on every brief can retrieve and cite them. Web search only suggests pages; you read "
               "each one and save it with a summary of what it says.")
    m1, m2, m3 = st.columns(3)
    m1.metric("Competitor sources", sum(s["source_type"] == "competitor" for s in added + builtin))
    m2.metric("Regulatory sources", sum(s["source_type"] == "regulatory" for s in added + builtin))
    m3.metric("Added by your team", len(added))

    with st.expander("🔎 Find sources online"):
        with st.form("source_search"):
            c1, c2 = st.columns([3, 1])
            q = c1.text_input("Search for", placeholder="EV battery replacement coverage endorsement")
            kind = c2.selectbox("Type", list(TYPE_LABEL), format_func=TYPE_LABEL.get)
            go = st.form_submit_button("Search")
        if go:
            with st.spinner("Searching the web..."):
                res = api("POST", "sources/search", json={"query": q, "source_type": kind}, timeout=60)
            if res is not None:
                st.session_state.lib_search = {**res, "source_type": kind}
        res = st.session_state.get("lib_search")
        if res:
            if res.get("message"):
                st.info(res["message"])
            for i, r in enumerate(res["results"]):
                with st.container(border=True):
                    st.markdown(f"**{html.escape(r['title'] or r['site'])}**  \n"
                                f"[{html.escape(r['site'])}]({r['url']})"
                                + (f" · published {r['published']}" if r.get("published") else ""))
                    st.caption(r["snippet"][:600])
                    with st.expander("Review and add"):
                        got = _source_form(f"web_add_{i}", {"source_type": res["source_type"], "title": r["title"],
                                                            "url": r["url"], "summary": r["snippet"][:1500],
                                                            "origin": "web"}, "Add source")
                        if got and api("POST", "sources", json=got) is not None:
                            st.success("Added.")
                            st.rerun()

    with st.expander("➕ Add a source by hand"):
        got = _source_form("manual_add", {}, "Add source")
        if got and api("POST", "sources", json=got) is not None:
            st.rerun()

    if added:
        st.markdown("##### Added by your team")
        for s in added:
            with st.container(border=True):
                head, act = st.columns([5, 1.2])
                head.markdown(f"**{html.escape(s['name'])}** — {html.escape(s['title'])} · "
                              f"{TYPE_LABEL[s['source_type']]} · [source]({s['url']})")
                head.caption(f"{s['summary'][:400]}{'…' if len(s['summary']) > 400 else ''}  \n"
                             f"Collected {s['date_collected']} · {'from web search' if s['origin'] == 'web' else 'entered by hand'}"
                             f" · added by {s.get('added_by') or '—'}")
                if act.button("Delete", key=f"del_src_{s['id']}", use_container_width=True):
                    if api("DELETE", f"sources/{s['id']}") is not None:
                        st.rerun()
                with st.expander("Edit"):
                    got = _source_form(f"edit_src_{s['id']}", s, "Save changes")
                    if got and api("PUT", f"sources/{s['id']}", json=got) is not None:
                        st.rerun()

    st.markdown("##### Built-in")
    st.dataframe(pd.DataFrame([{"Type": TYPE_LABEL[b["source_type"]], "Name": b["name"], "Title": b["title"],
                                "Collected": b["date_collected"], "Link": b["url"]} for b in builtin]),
                 hide_index=True, use_container_width=True,
                 column_config={"Link": st.column_config.LinkColumn(display_text="open")})


def render_library(api: Call) -> None:
    st.markdown("## Library")
    tab_p, tab_s = st.tabs(["Risk patterns", "Competitor & regulatory sources"])
    with tab_p:
        _render_patterns(api)
    with tab_s:
        _render_sources(api)
