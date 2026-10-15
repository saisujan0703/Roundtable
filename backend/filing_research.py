"""
External rate data: bureau files and competitor filings
=======================================================
Two ways external data reaches the credibility complement (backend.actuarial benchmarks):

bureau CSV   a bureau or vendor loss-cost file (ISO/Verisk, AAIS, NCCI, a reinsurer's rating sheet) exported to CSV
             and uploaded. Columns (header row, case-insensitive): source, kind (loss_cost | premium), value,
             as_of (YYYY-MM-DD), and optionally state, unit, url, permissible_loss_ratio_pct, note. When the file
             carries a state column, only rows for the brief's launch states (or all, if none are set) are kept.
             Every row is validated like a hand-entered benchmark; invalid rows are reported, not guessed.
filing leads competitors' filings for the same kind of cover: links to SERFF Filing Access for each launch state
             and, with TAVILY_API_KEY set, web results for published rate filings. Leads are for the actuary to
             read; no number is taken from them automatically, because a filed rate needs its rating base,
             effective date and exposure unit checked before it is comparable.
"""
from __future__ import annotations

import csv
import io
import os
from typing import Any, Dict, List, Optional

from backend import actuarial

SERFF_URL = "https://filingaccess.serff.com/sfa/home/{state}"
MAX_ROWS = 200


def import_csv(state: Dict[str, Any], text: str, by: str, launch_states: Optional[List[str]] = None) -> Dict[str, Any]:
    reader = csv.DictReader(io.StringIO(text.lstrip("﻿")))
    if not reader.fieldnames:
        raise ValueError("The file has no header row.")
    fields = {f.strip().lower(): f for f in reader.fieldnames}
    missing = [c for c in ("source", "kind", "value", "as_of") if c not in fields]
    if missing:
        raise ValueError(f"Missing column(s): {', '.join(missing)}.")
    keep = {s.upper() for s in launch_states or []}
    added, skipped, errors = 0, 0, []
    for i, raw in enumerate(reader, start=2):
        if i - 1 > MAX_ROWS:
            errors.append(f"Stopped after {MAX_ROWS} rows.")
            break
        row = {k: (raw.get(orig) or "").strip() for k, orig in fields.items()}
        st = row.get("state", "").upper()
        if keep and st and st not in keep:
            skipped += 1
            continue
        try:
            actuarial.add_benchmark(state, {
                "kind": row["kind"].lower(), "source": row["source"] + (f" ({st})" if st else ""),
                "value": row["value"].replace("$", "").replace(",", ""), "as_of": row["as_of"],
                "permissible_loss_ratio_pct": row.get("permissible_loss_ratio_pct") or None,
                "unit": row.get("unit", ""), "url": row.get("url", ""), "note": row.get("note", "")}, by)
            added += 1
        except ValueError as e:
            errors.append(f"Row {i}: {e}")
    return {"added": added, "skipped_other_states": skipped, "errors": errors}


def filing_leads(title: str, scope_description: str, states: List[str]) -> Dict[str, Any]:
    serff = [{"state": s, "url": SERFF_URL.format(state=s)} for s in sorted(set(states))[:20]]
    key = os.environ.get("TAVILY_API_KEY", "").strip()
    if not key or key == "your_tavily_api_key_here":
        return {"serff": serff, "web": [], "web_status": "Web search is off (set TAVILY_API_KEY)."}
    try:
        from tavily import TavilyClient
        res = TavilyClient(api_key=key).search(
            query=f"{title} insurance rate filing actuarial memorandum loss cost {scope_description}",
            search_depth="advanced", max_results=8)
    except Exception as e:  # network, quota, package missing
        return {"serff": serff, "web": [], "web_status": f"Web search failed: {e}"}
    web = [{"title": r.get("title", "")[:200], "url": r.get("url", ""), "snippet": (r.get("content") or "")[:400]}
           for r in res.get("results", [])]
    return {"serff": serff, "web": web, "web_status": f"{len(web)} result(s)."}
