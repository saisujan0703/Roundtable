"""
External rate data: industry files and competitor products
==========================================================
Two ways external data reaches the credibility complement (backend.actuarial benchmarks):

industry CSV  an industry or reinsurer file (Insurance Information Bureau of India statistics, a GIC Re or other
              reinsurer's rating sheet, a vendor study) exported to CSV and uploaded. Columns (header row,
              case-insensitive): source, kind (loss_cost | premium), value, as_of (YYYY-MM-DD), and optionally state,
              unit, url, permissible_loss_ratio_pct, note. When the file carries a state column, only rows for the
              brief's launch states (or all, if none are set) are kept. Every row is validated like a hand-entered
              benchmark; invalid rows are reported, not guessed.
product leads competitors' products for the same kind of cover. India has no public database of filed rates like
              the US SERFF: under Use & File the insurer's Product Management Committee approves a product and IRDAI
              allots a UIN, and the Appointed Actuary's technical note stays private. What is public is each
              insurer's policy wording, prospectus and customer information sheet (on its website before launch or
              within seven days of the UIN, IRDAI Master Circular on General Insurance Business, 2024, Ch. III 2.3)
              and the quarterly Form NL-27 public disclosure listing products launched with their UINs. Leads are for
              the actuary to read; no number is taken from them automatically, because a published rate needs its
              rating base, effective date and exposure unit checked before it is comparable.
"""
from __future__ import annotations

import csv
import io
import os
from typing import Any, Dict, List, Optional

from backend import actuarial

MAX_ROWS = 200

# Where Indian product and industry data is published (no per-state register: IRDAI regulates nationally)
REGISTERS = [
    {"label": "IRDAI", "url": "https://irdai.gov.in",
     "note": "regulations and master circulars; products are filed under Use & File, without public rates"},
    {"label": "Insurance Information Bureau of India", "url": "https://iib.gov.in",
     "note": "industry claims and premium statistics, the nearest thing to a rating bureau"},
    {"label": "GIC Re", "url": "https://www.gicre.in/en/",
     "note": "national reinsurer; a reinsurer quote can serve as a benchmark"},
    {"label": "General Insurance Council", "url": "https://www.gicouncil.in",
     "note": "industry premium figures by insurer and line"},
]
WEB_QUERY_HINT = "India IRDAI UIN policy wording prospectus premium"


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
                "value": row["value"].replace("₹", "").replace("Rs.", "").replace("Rs", "").replace("$", "")
                                     .replace(",", "").strip(),
                "as_of": row["as_of"],
                "permissible_loss_ratio_pct": row.get("permissible_loss_ratio_pct") or None,
                "unit": row.get("unit", ""), "url": row.get("url", ""), "note": row.get("note", "")}, by)
            added += 1
        except ValueError as e:
            errors.append(f"Row {i}: {e}")
    return {"added": added, "skipped_other_states": skipped, "errors": errors}


def filing_leads(title: str, scope_description: str) -> Dict[str, Any]:
    """Where to read competitors' products, and (with TAVILY_API_KEY) web results for comparable Indian products."""
    out = {"registers": REGISTERS,
           "how_to": "Search each competitor's website for the product's policy wording and prospectus (they carry "
                     "the IRDAI UIN), and its quarterly Form NL-27 public disclosure for products launched. Technical "
                     "notes and filed rates are not public."}
    key = os.environ.get("TAVILY_API_KEY", "").strip()
    if not key or key == "your_tavily_api_key_here":
        return {**out, "web": [], "web_status": "Web search is off (set TAVILY_API_KEY)."}
    try:
        from tavily import TavilyClient
        res = TavilyClient(api_key=key).search(
            query=f"{title} insurance {WEB_QUERY_HINT} {scope_description}",
            search_depth="advanced", max_results=8)
    except Exception as e:  # network, quota, package missing
        return {**out, "web": [], "web_status": f"Web search failed: {e}"}
    web = [{"title": r.get("title", "")[:200], "url": r.get("url", ""), "snippet": (r.get("content") or "")[:400]}
           for r in res.get("results", [])]
    return {**out, "web": web, "web_status": f"{len(web)} result(s)."}
