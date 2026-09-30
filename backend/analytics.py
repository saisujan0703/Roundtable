"""
Roundtable Analytics Layer
==========================
Pure-SQL + pandas analytics functions that query the existing claims and
policies tables in roundtable.db.  No schema modifications — read-only.

Every function uses pandas.read_sql for querying so results come back as
DataFrames, then are converted to plain dicts for API consumption.
"""
from __future__ import annotations

import pandas as pd

from backend.database import get_connection


# =========================================================================
# 1. Year-over-year trend for any tag value
# =========================================================================
def get_claims_trend_by_tag(
    tag_value: str, group_by: str = "year"
) -> list[dict]:
    """Return per-year counts and percentages for a given risk_category_tag.

    Works for ANY tag_value — no hardcoded values.

    Returns
    -------
    list of {"year": int, "tag_matches": int, "total_claims": int, "pct": float}
    """
    conn = get_connection()
    try:
        # Pull only the two columns we need; the year is extracted in SQL
        # so pandas gets a clean integer to group on.
        query = """
            SELECT
                CAST(strftime('%Y', loss_date) AS INTEGER) AS year,
                risk_category_tag,
                COUNT(*) AS cnt
            FROM claims
            GROUP BY year, risk_category_tag
        """
        df = pd.read_sql(query, conn)
    finally:
        conn.close()

    # Total claims per year
    totals = df.groupby("year")["cnt"].sum().rename("total_claims")

    # Matches for the requested tag per year
    tag_df = df[df["risk_category_tag"] == tag_value]
    matches = tag_df.set_index("year")["cnt"].rename("tag_matches")

    # Merge and compute percentage
    result = pd.DataFrame(totals).join(matches, how="left").fillna(0)
    result["tag_matches"] = result["tag_matches"].astype(int)
    result["pct"] = result["tag_matches"] / result["total_claims"]
    result = result.reset_index()

    return result.to_dict(orient="records")


# =========================================================================
# 2. Location-based comparison for any tag value
# =========================================================================
def get_claims_trend_by_tag_and_location(
    tag_value: str, location: str
) -> dict:
    """Compare the rate of *tag_value* inside vs. outside *location*.

    Returns
    -------
    {"location": str, "location_rate": float, "other_rate": float,
     "multiplier": float, "location_total": int, "other_total": int}
    """
    conn = get_connection()
    try:
        query = """
            SELECT
                CASE WHEN location = :loc THEN 'target' ELSE 'other' END AS grp,
                COUNT(*) AS total,
                SUM(CASE WHEN risk_category_tag = :tag THEN 1 ELSE 0 END) AS hits
            FROM claims
            GROUP BY grp
        """
        df = pd.read_sql(query, conn, params={"loc": location, "tag": tag_value})
    finally:
        conn.close()

    row_target = df[df["grp"] == "target"].iloc[0] if (df["grp"] == "target").any() else None
    row_other = df[df["grp"] == "other"].iloc[0] if (df["grp"] == "other").any() else None

    loc_total = int(row_target["total"]) if row_target is not None else 0
    loc_hits = int(row_target["hits"]) if row_target is not None else 0
    other_total = int(row_other["total"]) if row_other is not None else 0
    other_hits = int(row_other["hits"]) if row_other is not None else 0

    loc_rate = loc_hits / loc_total if loc_total else 0.0
    other_rate = other_hits / other_total if other_total else 0.0
    multiplier = loc_rate / other_rate if other_rate else float("inf")

    return {
        "location": location,
        "location_rate": round(loc_rate, 4),
        "other_rate": round(other_rate, 4),
        "multiplier": round(multiplier, 2),
        "location_total": loc_total,
        "other_total": other_total,
    }


# =========================================================================
# 3. Segment-based comparison for any tag value
# =========================================================================
def get_claims_trend_by_tag_and_segment(
    tag_value: str, segment_field: str, segment_value: str
) -> dict:
    """Compare the rate of *tag_value* inside vs. outside a segment.

    *segment_field* must be a real column in the claims table (e.g.
    ``product_code``).  The value is compared via ``= :seg_val``.

    Returns
    -------
    {"segment_field": str, "segment_value": str,
     "segment_rate": float, "other_rate": float, "multiplier": float,
     "segment_total": int, "other_total": int}
    """
    # Whitelist of columns allowed as segment_field to prevent SQL injection
    ALLOWED_SEGMENT_FIELDS = {
        "product_code", "claim_state", "loss_cause", "location",
    }
    if segment_field not in ALLOWED_SEGMENT_FIELDS:
        raise ValueError(
            f"segment_field must be one of {ALLOWED_SEGMENT_FIELDS}, "
            f"got {segment_field!r}"
        )

    conn = get_connection()
    try:
        # segment_field is validated above, safe to interpolate
        query = f"""
            SELECT
                CASE WHEN {segment_field} = :seg_val THEN 'target'
                     ELSE 'other' END AS grp,
                COUNT(*) AS total,
                SUM(CASE WHEN risk_category_tag = :tag THEN 1 ELSE 0 END) AS hits
            FROM claims
            GROUP BY grp
        """
        df = pd.read_sql(
            query, conn, params={"seg_val": segment_value, "tag": tag_value}
        )
    finally:
        conn.close()

    row_target = df[df["grp"] == "target"].iloc[0] if (df["grp"] == "target").any() else None
    row_other = df[df["grp"] == "other"].iloc[0] if (df["grp"] == "other").any() else None

    seg_total = int(row_target["total"]) if row_target is not None else 0
    seg_hits = int(row_target["hits"]) if row_target is not None else 0
    other_total = int(row_other["total"]) if row_other is not None else 0
    other_hits = int(row_other["hits"]) if row_other is not None else 0

    seg_rate = seg_hits / seg_total if seg_total else 0.0
    other_rate = other_hits / other_total if other_total else 0.0
    multiplier = seg_rate / other_rate if other_rate else float("inf")

    return {
        "segment_field": segment_field,
        "segment_value": segment_value,
        "segment_rate": round(seg_rate, 4),
        "other_rate": round(other_rate, 4),
        "multiplier": round(multiplier, 2),
        "segment_total": seg_total,
        "other_total": other_total,
    }


# =========================================================================
# 4. Summary statistics (overall + optional tag filter)
# =========================================================================
def get_claims_summary_stats(tag_value: str = None) -> dict:
    """Return aggregate claim statistics.

    Always returns overall stats.  If *tag_value* is provided, also
    returns the same three stats filtered to matching claims.

    Returns
    -------
    {"total_count": int, "total_amount": float, "avg_amount": float,
     "tag_count": int | None, "tag_total_amount": float | None,
     "tag_avg_amount": float | None}
    """
    conn = get_connection()
    try:
        overall = pd.read_sql(
            "SELECT COUNT(*) AS cnt, SUM(claim_amount) AS total, "
            "AVG(claim_amount) AS avg FROM claims",
            conn,
        ).iloc[0]

        result: dict = {
            "total_count": int(overall["cnt"]),
            "total_amount": round(float(overall["total"]), 2),
            "avg_amount": round(float(overall["avg"]), 2),
            "tag_count": None,
            "tag_total_amount": None,
            "tag_avg_amount": None,
        }

        if tag_value is not None:
            tag_row = pd.read_sql(
                "SELECT COUNT(*) AS cnt, SUM(claim_amount) AS total, "
                "AVG(claim_amount) AS avg FROM claims "
                "WHERE risk_category_tag = :tag",
                conn,
                params={"tag": tag_value},
            ).iloc[0]
            result["tag_count"] = int(tag_row["cnt"])
            result["tag_total_amount"] = round(float(tag_row["total"]), 2)
            result["tag_avg_amount"] = round(float(tag_row["avg"]), 2)
    finally:
        conn.close()

    return result


# =========================================================================
# 4b. Loss Cause & Claim State breakdowns for a specific tag
# =========================================================================
def get_claims_loss_cause_breakdown(tag_value: str) -> list[dict]:
    """Return count and percentage breakdown of loss_cause for a given risk tag."""
    conn = get_connection()
    try:
        query = """
            SELECT loss_cause, COUNT(*) AS cnt
            FROM claims
            WHERE risk_category_tag = :tag
            GROUP BY loss_cause
            ORDER BY cnt DESC
        """
        df = pd.read_sql(query, conn, params={"tag": tag_value})
        total = df["cnt"].sum() if not df.empty else 0
        if total > 0:
            df["pct"] = df["cnt"] / total
        else:
            df["pct"] = 0.0
        return df.to_dict(orient="records")
    finally:
        conn.close()


def get_claims_state_breakdown(tag_value: str) -> list[dict]:
    """Return count and percentage breakdown of claim_state for a given risk tag."""
    conn = get_connection()
    try:
        query = """
            SELECT claim_state, COUNT(*) AS cnt
            FROM claims
            WHERE risk_category_tag = :tag
            GROUP BY claim_state
            ORDER BY cnt DESC
        """
        df = pd.read_sql(query, conn, params={"tag": tag_value})
        total = df["cnt"].sum() if not df.empty else 0
        if total > 0:
            df["pct"] = df["cnt"] / total
        else:
            df["pct"] = 0.0
        return df.to_dict(orient="records")
    finally:
        conn.close()


# =========================================================================
# 5. Proactive alert detection — generic trend scanner
# =========================================================================
def detect_notable_trends(
    min_pct_change: float = 0.02, min_year_claims: int = 2000
) -> list[dict]:
    """Scan ALL distinct risk_category_tag values and flag any whose
    percentage-point change from earliest to latest *substantial* year
    exceeds *min_pct_change*.

    Years with fewer than *min_year_claims* total claims are excluded
    to avoid edge-of-range distortion (e.g. a year with only 49 claims).

    No hardcoded tag list -- discovers patterns generically from the data.

    Returns
    -------
    list of {"tag_value": str, "first_year_pct": float,
             "last_year_pct": float, "change": float}
    """
    conn = get_connection()
    try:
        # Get all distinct tags
        tags_df = pd.read_sql(
            "SELECT DISTINCT risk_category_tag FROM claims", conn
        )
        all_tags = tags_df["risk_category_tag"].tolist()

        # Pre-fetch the full year × tag pivot in one query
        pivot_df = pd.read_sql(
            """
            SELECT
                CAST(strftime('%Y', loss_date) AS INTEGER) AS year,
                risk_category_tag,
                COUNT(*) AS cnt
            FROM claims
            GROUP BY year, risk_category_tag
            """,
            conn,
        )
        totals = pd.read_sql(
            """
            SELECT
                CAST(strftime('%Y', loss_date) AS INTEGER) AS year,
                COUNT(*) AS total
            FROM claims
            GROUP BY year
            """,
            conn,
        )
    finally:
        conn.close()

    totals = totals.set_index("year")["total"]
    # Drop years with too few claims (edge-of-range noise)
    totals = totals[totals >= min_year_claims]
    notable: list[dict] = []

    for tag in all_tags:
        tag_counts = (
            pivot_df[pivot_df["risk_category_tag"] == tag]
            .set_index("year")["cnt"]
        )
        # Compute pct per year
        years = sorted(totals.index)
        if len(years) < 2:
            continue

        pcts = {}
        for y in years:
            cnt = int(tag_counts.get(y, 0))
            tot = int(totals.get(y, 1))
            pcts[y] = cnt / tot if tot else 0.0

        first_year = years[0]
        last_year = years[-1]
        change = pcts[last_year] - pcts[first_year]

        if abs(change) >= min_pct_change:
            notable.append({
                "tag_value": tag,
                "first_year": first_year,
                "first_year_pct": round(pcts[first_year], 4),
                "last_year": last_year,
                "last_year_pct": round(pcts[last_year], 4),
                "change": round(change, 4),
            })

    # Sort by absolute change descending — biggest movers first
    notable.sort(key=lambda x: abs(x["change"]), reverse=True)
    return notable


# =========================================================================
# 6. Segment-filtered trend detection
# =========================================================================
def detect_notable_trends_by_segment(
    segment_field: str,
    segment_value: str,
    min_pct_change: float = 0.05,
    min_year_claims: int = 100,
) -> list[dict]:
    """Same generic year-over-year scan as detect_notable_trends(), but
    first filters claims to only rows where *segment_field* == *segment_value*.

    This lets you ask: "within HOPHomeowners claims, which tags are
    trending?" — without hardcoding any tag names.

    *min_year_claims* is intentionally lower (100) than the global
    detector because a single segment has far fewer rows per year.

    Returns
    -------
    list of {"tag_value": str, "first_year": int, "first_year_pct": float,
             "last_year": int, "last_year_pct": float, "change": float}
    """
    ALLOWED_SEGMENT_FIELDS = {
        "product_code", "claim_state", "loss_cause", "location",
    }
    if segment_field not in ALLOWED_SEGMENT_FIELDS:
        raise ValueError(
            f"segment_field must be one of {ALLOWED_SEGMENT_FIELDS}, "
            f"got {segment_field!r}"
        )

    conn = get_connection()
    try:
        # Pre-fetch year x tag counts filtered to the segment
        query = f"""
            SELECT
                CAST(strftime('%Y', loss_date) AS INTEGER) AS year,
                risk_category_tag,
                COUNT(*) AS cnt
            FROM claims
            WHERE {segment_field} = :seg_val
            GROUP BY year, risk_category_tag
        """
        pivot_df = pd.read_sql(query, conn, params={"seg_val": segment_value})

        totals_query = f"""
            SELECT
                CAST(strftime('%Y', loss_date) AS INTEGER) AS year,
                COUNT(*) AS total
            FROM claims
            WHERE {segment_field} = :seg_val
            GROUP BY year
        """
        totals = pd.read_sql(
            totals_query, conn, params={"seg_val": segment_value}
        )
    finally:
        conn.close()

    if totals.empty:
        return []

    totals = totals.set_index("year")["total"]
    totals = totals[totals >= min_year_claims]
    years = sorted(totals.index)
    if len(years) < 2:
        return []

    all_tags = pivot_df["risk_category_tag"].unique().tolist()
    notable: list[dict] = []

    for tag in all_tags:
        tag_counts = (
            pivot_df[pivot_df["risk_category_tag"] == tag]
            .set_index("year")["cnt"]
        )
        pcts = {}
        for y in years:
            cnt = int(tag_counts.get(y, 0))
            tot = int(totals.get(y, 1))
            pcts[y] = cnt / tot if tot else 0.0

        first_year = years[0]
        last_year = years[-1]
        change = pcts[last_year] - pcts[first_year]

        if abs(change) >= min_pct_change:
            notable.append({
                "tag_value": tag,
                "first_year": first_year,
                "first_year_pct": round(pcts[first_year], 4),
                "last_year": last_year,
                "last_year_pct": round(pcts[last_year], 4),
                "change": round(change, 4),
            })

    notable.sort(key=lambda x: abs(x["change"]), reverse=True)
    return notable


# =========================================================================
# 7. Loss Ratio Framing (Task 1)
# =========================================================================
def get_loss_ratio_by_tag(tag_value: str) -> dict:
    """Check if policies table has a premium field and return loss ratio by tag.
    
    If no reliable premium-to-tag linkage exists in schema, outputs explicit
    'Insufficient evidence' status per schema guardrail.
    """
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("PRAGMA table_info(policies)")
        p_cols = [r["name"] for r in cur.fetchall()]
        cur.execute("PRAGMA table_info(claims)")
        c_cols = [r["name"] for r in cur.fetchall()]
    finally:
        conn.close()

    if "earned_premium" not in p_cols and "premium" not in p_cols:
        return {
            "has_data": False,
            "status": "Insufficient evidence for loss ratio framing — earned premium is not present in the current data schema.",
            "tag_loss_share_of_segment_premium_pct": None,
        }

    conn = get_connection()
    try:
        # Determine relevant product line segments for this tag
        seg_query = """
            SELECT DISTINCT product_code
            FROM claims
            WHERE risk_category_tag = :tag
        """
        seg_df = pd.read_sql(seg_query, conn, params={"tag": tag_value})
        relevant_prods = [p for p in seg_df["product_code"].tolist() if p]

        # Incurred losses for tag
        incurred_df = pd.read_sql(
            "SELECT SUM(claim_amount) AS tag_incurred, COUNT(*) AS tag_claims FROM claims WHERE risk_category_tag = :tag",
            conn,
            params={"tag": tag_value}
        )
        tag_incurred = float(incurred_df["tag_incurred"].iloc[0] or 0.0)
        tag_claims = int(incurred_df["tag_claims"].iloc[0] or 0)

        # Earned premium for relevant segments
        if relevant_prods:
            placeholders = ",".join(f"'{p}'" for p in relevant_prods)
            prem_query = f"SELECT SUM(earned_premium) AS total_prem FROM policies WHERE product_code IN ({placeholders})"
            prem_df = pd.read_sql(prem_query, conn)
            earned_prem = float(prem_df["total_prem"].iloc[0] or 0.0)
        else:
            prem_df = pd.read_sql("SELECT SUM(earned_premium) AS total_prem FROM policies", conn)
            earned_prem = float(prem_df["total_prem"].iloc[0] or 0.0)
    finally:
        conn.close()

    share_pct = (tag_incurred / earned_prem * 100.0) if earned_prem > 0 else 0.0
    seg_names = ", ".join(relevant_prods) if relevant_prods else "All Product Lines"

    return {
        "has_data": True,
        "tag_value": tag_value,
        "tag_loss_share_of_segment_premium_pct": round(share_pct, 2),
        "tag_incurred": round(tag_incurred, 2),
        "earned_premium": round(earned_prem, 2),
        "tag_claims": tag_claims,
        "relevant_segments": seg_names,
        "status": (
            f"This risk pattern's incurred losses represent {share_pct:.2f}% of total earned premium "
            f"across its associated product line(s) — a directional indicator of relative exposure, "
            f"not a peril-specific actuarial loss ratio (which would require exposure-based rating data "
            f"not present in this dataset)."
        ),
    }


# =========================================================================
# 8. Litigation / Subrogation Signal (Task 2)
# =========================================================================
def get_litigation_subrogation_summary(tag_value: str) -> dict:
    """Check if claims table has litigation or subrogation tracking fields.
    
    Outputs explicit 'Insufficient evidence' if no litigation/subrogation fields exist.
    """
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("PRAGMA table_info(claims)")
        cols = [r["name"] for r in cur.fetchall()]
    finally:
        conn.close()

    lit_cols = {"litigation_status", "litigation_flag", "attorney_involved", "subrogation_amount", "recovery_amount"}
    matched_cols = lit_cols.intersection(set(cols))

    if not matched_cols or "litigation_flag" not in cols:
        return {
            "has_data": False,
            "status": "Insufficient evidence for litigation/subrogation signal — no litigation or subrogation tracking field exists in the current claims schema.",
            "litigation_pct": None,
            "subrogation_total": None,
        }

    conn = get_connection()
    try:
        query = """
            SELECT
                COUNT(*) AS total_claims,
                SUM(CASE WHEN litigation_flag = 1 THEN 1 ELSE 0 END) AS lit_claims,
                SUM(COALESCE(subrogation_amount, 0.0)) AS total_subro,
                SUM(CASE WHEN COALESCE(subrogation_amount, 0.0) > 0 THEN 1 ELSE 0 END) AS subro_claims
            FROM claims
            WHERE risk_category_tag = :tag
        """
        df = pd.read_sql(query, conn, params={"tag": tag_value})
    finally:
        conn.close()

    tot = int(df["total_claims"].iloc[0] or 0)
    lit = int(df["lit_claims"].iloc[0] or 0)
    subro = float(df["total_subro"].iloc[0] or 0.0)
    subro_cnt = int(df["subro_claims"].iloc[0] or 0)

    lit_pct = (lit / tot * 100.0) if tot > 0 else 0.0

    return {
        "has_data": True,
        "tag_value": tag_value,
        "total_claims": tot,
        "litigation_count": lit,
        "litigation_pct": round(lit_pct, 2),
        "subrogation_total": round(subro, 2),
        "subrogation_count": subro_cnt,
        "status": f"Litigation rate is {lit_pct:.1f}% ({lit:,} claims with legal counsel/dispute). Total subrogation recoveries reached ${subro:,.2f} across {subro_cnt:,} third-party recovery claims.",
    }


# =========================================================================
# 9. Claim Cycle Time & Reserve Development (Task 3)
# =========================================================================
def get_cycle_time_and_reserve_development(tag_value: str) -> dict:
    """Check if claims table has claim close dates and initial reserve amounts.
    
    Outputs explicit 'Insufficient evidence' if either required pair is missing.
    """
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("PRAGMA table_info(claims)")
        cols = set(r["name"] for r in cur.fetchall())
    finally:
        conn.close()

    missing_fields = []
    if "close_date" not in cols and "claim_close_date" not in cols:
        missing_fields.append("claim close date (close_date)")
    if "initial_reserve" not in cols and "reserve_initial" not in cols:
        missing_fields.append("initial reserve amount (initial_reserve)")

    if missing_fields:
        missing_str = " and ".join(missing_fields)
        return {
            "has_data": False,
            "status": f"Insufficient evidence for claim cycle time and reserve development — {missing_str} are not present in the current data schema.",
            "avg_days_to_close": None,
            "adverse_development_pct": None,
        }

    conn = get_connection()
    try:
        cycle_query = """
            SELECT
                AVG(JULIANDAY(close_date) - JULIANDAY(loss_date)) AS avg_days,
                COUNT(*) AS closed_count
            FROM claims
            WHERE risk_category_tag = :tag
              AND close_date IS NOT NULL
              AND claim_state = 'closed'
        """
        cycle_df = pd.read_sql(cycle_query, conn, params={"tag": tag_value})

        res_query = """
            SELECT
                AVG((claim_amount - initial_reserve) * 1.0 / NULLIF(initial_reserve, 0)) * 100.0 AS avg_dev_pct,
                COUNT(*) AS res_count
            FROM claims
            WHERE risk_category_tag = :tag
              AND initial_reserve IS NOT NULL
              AND initial_reserve > 0
        """
        res_df = pd.read_sql(res_query, conn, params={"tag": tag_value})
    finally:
        conn.close()

    avg_days = float(cycle_df["avg_days"].iloc[0] or 0.0)
    closed_cnt = int(cycle_df["closed_count"].iloc[0] or 0)
    dev_pct = float(res_df["avg_dev_pct"].iloc[0] or 0.0)

    if dev_pct > 0:
        direction = "UPWARD"
        direction_label = f"reserves were adjusted upward by {abs(dev_pct):.2f}% on average, indicating initial under-reserving (adverse development)"
    elif dev_pct < 0:
        direction = "DOWNWARD"
        direction_label = f"reserves were adjusted downward by {abs(dev_pct):.2f}% on average, indicating initial over-reserving (favorable development)"
    else:
        direction = "NEUTRAL"
        direction_label = "reserves were settled exactly at initial reserve estimates on average"

    return {
        "has_data": True,
        "tag_value": tag_value,
        "avg_days_to_close": round(avg_days, 1),
        "closed_claims_count": closed_cnt,
        "adverse_development_pct": round(dev_pct, 2),
        "development_direction": direction,
        "development_direction_label": direction_label,
        "status": f"Average claim cycle time to closure is {avg_days:.1f} days ({closed_cnt:,} closed claims). Reserve development: {direction_label}.",
    }


# =========================================================================
# 10. Benchmark / Urgency Framing (Task 4)
# =========================================================================
def get_relative_growth_benchmark(tag_value: str) -> dict:
    """Compute this tag's year-over-year growth rate vs the AVERAGE year-over-year
    growth rate across tracked pattern tags, returning the ratio.
    """
    TRACKED_TAGS = [
        "battery_fault", "theftentire", "waterdamage", "slipfall",
        "strain", "fire", "rollover", "vehcollision"
    ]
    
    conn = get_connection()
    try:
        query = """
            SELECT
                CAST(strftime('%Y', loss_date) AS INTEGER) AS year,
                risk_category_tag,
                COUNT(*) AS cnt
            FROM claims
            GROUP BY year, risk_category_tag
        """
        df = pd.read_sql(query, conn)
        totals = pd.read_sql(
            """
            SELECT
                CAST(strftime('%Y', loss_date) AS INTEGER) AS year,
                COUNT(*) AS total
            FROM claims
            GROUP BY year
            """,
            conn
        ).set_index("year")["total"]
    finally:
        conn.close()

    years = sorted(totals.index)
    if len(years) < 2:
        return {
            "has_data": False,
            "status": "Insufficient historical years to calculate relative growth benchmark.",
            "tag_growth_rate": 0.0,
            "benchmark_avg_growth_rate": 0.0,
            "multiplier": 1.0,
            "narrative": "Insufficient historical years to calculate relative growth benchmark."
        }

    first_year = years[0]
    last_year = years[-1]
    
    tag_growths = {}
    for t in TRACKED_TAGS:
        t_counts = df[df["risk_category_tag"] == t].set_index("year")["cnt"]
        p_first = (int(t_counts.get(first_year, 0)) / totals.get(first_year, 1))
        p_last = (int(t_counts.get(last_year, 0)) / totals.get(last_year, 1))
        if p_first > 0:
            growth = (p_last - p_first) / p_first
        else:
            growth = 0.0
        tag_growths[t] = growth

    target_growth = tag_growths.get(tag_value)
    if target_growth is None:
        t_counts = df[df["risk_category_tag"] == tag_value].set_index("year")["cnt"]
        p_first = (int(t_counts.get(first_year, 0)) / totals.get(first_year, 1))
        p_last = (int(t_counts.get(last_year, 0)) / totals.get(last_year, 1))
        target_growth = (p_last - p_first) / p_first if p_first > 0 else 0.0

    avg_tracked_growth = sum(tag_growths.values()) / len(tag_growths) if tag_growths else 0.0
    
    if avg_tracked_growth > 0:
        multiplier = round(target_growth / avg_tracked_growth, 2)
    elif avg_tracked_growth < 0 and target_growth > 0:
        multiplier = round(abs(target_growth / avg_tracked_growth), 2)
    else:
        multiplier = 1.0

    if target_growth > avg_tracked_growth and multiplier > 1.0:
        narrative = f"This risk pattern is growing {multiplier:.1f}x faster than the average tracked pattern baseline ({target_growth:+.1%} vs {avg_tracked_growth:+.1%} benchmark average across {first_year}–{last_year})."
    elif target_growth < avg_tracked_growth:
        narrative = f"This risk pattern growth ({target_growth:+.1%}) is pacing below or in line with the tracked benchmark average ({avg_tracked_growth:+.1%} across {first_year}–{last_year})."
    else:
        narrative = f"This risk pattern is growing at {target_growth:+.1%}, matching the portfolio benchmark average across {first_year}–{last_year}."

    return {
        "has_data": True,
        "tag_value": tag_value,
        "tag_growth_rate": round(target_growth, 4),
        "benchmark_avg_growth_rate": round(avg_tracked_growth, 4),
        "multiplier": multiplier,
        "narrative": narrative,
        "start_year": first_year,
        "end_year": last_year,
    }


# =========================================================================
# 11. Representative Example Claims (Task 5)
# =========================================================================
def get_sample_claims_for_tag(tag_value: str, n: int = 3) -> list[dict]:
    """Return n diverse real claim records for this tag across different years
    with synthetic IDs, loss dates, amounts, causes, and states.
    """
    conn = get_connection()
    try:
        query = """
            SELECT
                claim_id,
                strftime('%Y-%m-%d', loss_date) AS loss_date,
                CAST(strftime('%Y', loss_date) AS INTEGER) AS year,
                claim_amount,
                loss_cause,
                claim_state,
                location
            FROM claims
            WHERE risk_category_tag = :tag
            ORDER BY year ASC, claim_amount DESC
        """
        df = pd.read_sql(query, conn, params={"tag": tag_value})
    finally:
        conn.close()

    if df.empty:
        return []

    # Pick a diverse mix across different years
    years = sorted(df["year"].unique())
    selected_rows = []

    for y in years:
        if len(selected_rows) >= n:
            break
        year_subset = df[df["year"] == y]
        idx = len(year_subset) // 2
        selected_rows.append(year_subset.iloc[idx].to_dict())

    if len(selected_rows) < n:
        used_ids = set(r["claim_id"] for r in selected_rows)
        remaining = df[~df["claim_id"].isin(used_ids)]
        if not remaining.empty:
            for _, r in remaining.head(n - len(selected_rows)).iterrows():
                selected_rows.append(r.to_dict())

    results = []
    for r in selected_rows[:n]:
        results.append({
            "claim_id": str(r["claim_id"]),
            "claim_date": str(r["loss_date"]),
            "year": int(r["year"]),
            "incurred_amount": round(float(r["claim_amount"]), 2),
            "loss_cause": str(r["loss_cause"]),
            "claim_state": str(r["claim_state"]),
            "location": str(r["location"]),
        })

    return results


# =========================================================================
# CLI verification
# =========================================================================
if __name__ == "__main__":
    import json

    print("=" * 72)
    print("  Roundtable Analytics Layer -- Verification")
    print("=" * 72)

    # --- 1. battery_fault trend ---
    print("\n[1] get_claims_trend_by_tag('battery_fault'):")
    trend = get_claims_trend_by_tag("battery_fault")
    for row in trend:
        print(f"    {row['year']}: {row['tag_matches']:,} / {row['total_claims']:,}"
              f"  = {row['pct']:.2%}")

    # --- 2. theftentire in IL ---
    print("\n[2] get_claims_trend_by_tag_and_location('theftentire', 'IL'):")
    loc_result = get_claims_trend_by_tag_and_location("theftentire", "IL")
    print(f"    {json.dumps(loc_result, indent=6)}")

    # --- 3. slipfall in CommercialProperty ---
    print("\n[3] get_claims_trend_by_tag_and_segment('slipfall', 'product_code', 'CommercialProperty'):")
    seg_result = get_claims_trend_by_tag_and_segment(
        "slipfall", "product_code", "CommercialProperty"
    )
    print(f"    {json.dumps(seg_result, indent=6)}")

    # --- 4. Summary stats ---
    print("\n[4] get_claims_summary_stats('battery_fault'):")
    stats = get_claims_summary_stats("battery_fault")
    print(f"    {json.dumps(stats, indent=6)}")

    # --- 5. Proactive detection (the key test) ---
    print("\n[5] detect_notable_trends() -- discovering ALL patterns generically:")
    trends = detect_notable_trends()
    if not trends:
        print("    No notable trends detected.")
    else:
        for t in trends:
            direction = "UP" if t["change"] > 0 else "DOWN"
            print(f"    {direction:>4}  {t['tag_value']:<20s}  "
                  f"{t['first_year']}={t['first_year_pct']:.2%} -> "
                  f"{t['last_year']}={t['last_year_pct']:.2%}  "
                  f"(change={t['change']:+.2%})")

    # --- 6. Segment-filtered trend detection (HOPHomeowners) ---
    print("\n[6] detect_notable_trends_by_segment('product_code', 'HOPHomeowners'):")
    hop_trends = detect_notable_trends_by_segment(
        "product_code", "HOPHomeowners", min_pct_change=0.02
    )
    if not hop_trends:
        print("    No notable segment-specific trends detected.")
    else:
        for t in hop_trends:
            direction = "UP" if t["change"] > 0 else "DOWN"
            print(f"    {direction:>4}  {t['tag_value']:<20s}  "
                  f"{t['first_year']}={t['first_year_pct']:.2%} -> "
                  f"{t['last_year']}={t['last_year_pct']:.2%}  "
                  f"(change={t['change']:+.2%})")

    # --- 6b. Cross-segment proof: waterdamage rate in HOP vs others ---
    print("\n[6b] get_claims_trend_by_tag_and_segment('waterdamage', 'product_code', 'HOPHomeowners'):")
    hop_seg = get_claims_trend_by_tag_and_segment(
        "waterdamage", "product_code", "HOPHomeowners"
    )
    print(f"    {json.dumps(hop_seg, indent=6)}")

    print("\n" + "=" * 72)
