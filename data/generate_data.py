"""
Synthetic Insurance Data Generator
===================================
Generates Guidewire PolicyCenter (policies) and ClaimCenter (claims) datasets
grounded in verified 10.2.1 schema definitions, then loads them into a local
SQLite database.

Source schemas:
  - 09_SYNTHETIC_DATA_SCHEMA.md
  - 10_SYNTHETIC_DATA_GENERATION_RULES.md
  - 08_INSURANCE_RELATIONSHIP_GRAPH.md
  - 11_POLICYCENTER_CLAIMCENTER_FIELD_INDEX.md
"""
from __future__ import annotations

import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd
from faker import Faker

# ---------------------------------------------------------------------------
# Paths & global RNG
# ---------------------------------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = ROOT_DIR / "roundtable.db"
RNG = np.random.default_rng(123)

# ---------------------------------------------------------------------------
# Verified typelist allowed values
# (from 09_SYNTHETIC_DATA_SCHEMA.md & source .tti/.ttx files)
# ---------------------------------------------------------------------------
US_STATES = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY",
]

# Verified Policy.ProductCode pattern codes (patterncode varchar 64)
PRODUCT_CODES = [
    "PersonalAuto",
    "CommercialProperty",
    "BusinessAuto",
    "HOPHomeowners",
    "WorkersComp",
]

# Verified PolicyPeriodStatus typelist values (PolicyPeriod.eti)
POLICY_STATUS = ["Bound", "Draft", "Quoted", "Canceled"]
POLICY_STATUS_WEIGHTS = [0.85, 0.05, 0.05, 0.05]

# Verified ClaimState typelist values (Claim.eti)
CLAIM_STATES = ["open", "closed", "draft"]
CLAIM_STATE_WEIGHTS = [0.65, 0.30, 0.05]

# Verified LossCause typelist values (LossCause.tti)
LOSS_CAUSES = [
    "vehcollision",
    "rearend",
    "rollover",
    "theftentire",
    "fire",
    "waterdamage",
    "slipfall",
    "strain",
]
LOSS_CAUSE_WEIGHTS = [0.22, 0.18, 0.08, 0.12, 0.10, 0.12, 0.10, 0.08]

# ---------------------------------------------------------------------------
# Configurable engineered-pattern list
# ---------------------------------------------------------------------------
ENGINEERED_PATTERNS = [
    {
        "type": "time_trend",
        "tag_value": "battery_fault",
        "eligible_loss_causes": ["vehcollision"],
        "yearly_targets": {2023: 0.08, 2024: 0.14, 2025: 0.22, 2026: 0.31},
    },
    {
        "type": "geographic_skew",
        "tag_value": "theftentire",
        "location": "IL",
        "multiplier": 3.0,
    },
    {
        "type": "time_trend",
        "tag_value": "waterdamage",
        "yearly_targets": {2023: 0.05, 2024: 0.05, 2025: 0.09, 2026: 0.16},
    },
    {
        "type": "segment_skew",
        "tag_value": "slipfall",
        "segment_field": "product_code",
        "segment_value": "CommercialProperty",
        "multiplier": 2.5,
    },
    {
        "type": "segment_skew",
        "tag_value": "waterdamage",
        "segment_field": "product_code",
        "segment_value": "HOPHomeowners",
        "multiplier": 2.2,
        "eligible_loss_causes": ["waterdamage", "fire"],
    },
    {
        "type": "time_trend",
        "tag_value": "strain",
        "yearly_targets": {2023: 0.03, 2024: 0.06, 2025: 0.11, 2026: 0.19},
        # Realistic: rising WorkersComp strain/repetitive-injury claims
    },
    {
        "type": "segment_skew",
        "tag_value": "fire",
        "segment_field": "product_code",
        "segment_value": "CommercialProperty",
        "multiplier": 1.8,
        # Realistic: commercial fire risk concentration
    },
    {
        "type": "geographic_skew",
        "tag_value": "rollover",
        "location": "TX",
        "multiplier": 2.1,
        # Realistic: rollover claim concentration in a specific state
    },
]

# ---------------------------------------------------------------------------
# Realistic vehicle make/model tuples (PersonalVehicle schema)
# ---------------------------------------------------------------------------
VEHICLE_MAKES = {
    "Honda":      ["Accord", "Civic", "CR-V", "Pilot"],
    "Toyota":     ["Camry", "Corolla", "RAV4", "Highlander"],
    "Ford":       ["F-150", "Escape", "Explorer", "Mustang"],
    "Chevrolet":  ["Malibu", "Impala", "Silverado", "Equinox"],
    "Nissan":     ["Altima", "Sentra", "Rogue", "Frontier"],
    "Jeep":       ["Cherokee", "Wrangler", "Grand Cherokee", "Compass"],
    "BMW":        ["3 Series", "5 Series", "X5", "X3"],
    "Tesla":      ["Model 3", "Model Y", "Model S", "Model X"],
}


# =========================================================================
# Helper: vectorized VIN generation (17-char ISO 3779 format)
# =========================================================================
def generate_vins(count: int, rng: np.random.Generator) -> np.ndarray:
    """Generate *count* synthetic 17-character VINs (I, O, Q excluded)."""
    alphabet = "ABCDEFGHJKLMNPRSTUVWXYZ0123456789"
    choices = np.array(list(alphabet), dtype="U1")
    # Build a (count, 17) matrix of random chars, then join each row
    char_matrix = rng.choice(choices, size=(count, 17))
    vin_array = np.array(
        ["".join(row) for row in char_matrix], dtype="U17"
    )
    return vin_array


# =========================================================================
# POLICIES generator  (10,000 rows)
# =========================================================================
def generate_policy_df(count: int = 10_000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    fake = Faker("en_US")
    fake.seed_instance(seed)
    n = int(count)

    # --- Vectorized categorical columns ---
    product_code = rng.choice(
        np.array(PRODUCT_CODES, dtype=object),
        size=n,
        p=np.array([0.43, 0.20, 0.15, 0.10, 0.12]),
        #           PA    CP    BA    HOP   WC  (bumped WC from .10 to .12)
    )
    policy_status = rng.choice(
        np.array(POLICY_STATUS, dtype=object),
        size=n,
        p=np.array(POLICY_STATUS_WEIGHTS),
    )
    state = rng.choice(np.array(US_STATES, dtype=object), size=n)

    # --- Period start: random date covering 2023-2026 range ---
    #     ~1400 days back from today (Sept 2026) reaches early 2023
    start_offsets = rng.integers(0, 1400, size=n)
    base = pd.Timestamp.now().normalize()
    period_start = base - pd.to_timedelta(start_offsets, unit="D")

    # --- Period end: vectorized (6 months for PersonalAuto, 1 year otherwise)
    #     per verified temporal rule in 10_SYNTHETIC_DATA_GENERATION_RULES.md §4.3
    is_pa = product_code == "PersonalAuto"
    period_end = np.where(
        is_pa,
        period_start + pd.DateOffset(months=6),
        period_start + pd.DateOffset(years=1),
    )
    # np.where produces object array; convert back to datetime
    period_end = pd.to_datetime(period_end)

    # --- Account number: ACC-SYN-{7 digits} ---
    acct_nums = rng.integers(1_000_000, 10_000_000, size=n)
    account_number = np.array(
        [f"ACC-SYN-{v:07d}" for v in acct_nums], dtype=object
    )

    # --- Policy ID (primary key) ---
    policy_id = np.array([f"POL-{i:06d}" for i in range(n)], dtype=object)

    # --- Vehicle info (linked make/model tuples) ---
    make_names = list(VEHICLE_MAKES.keys())
    make_idx = rng.integers(0, len(make_names), size=n)
    vehicle_make = np.array([make_names[i] for i in make_idx], dtype=object)
    vehicle_model = np.array(
        [
            VEHICLE_MAKES[make_names[i]][
                rng.integers(0, len(VEHICLE_MAKES[make_names[i]]))
            ]
            for i in make_idx
        ],
        dtype=object,
    )
    vehicle_year = rng.integers(2017, 2027, size=n)  # endpoint-exclusive → 2017..2026
    vehicle_vin = generate_vins(n, rng)

    # --- Earned Premium (Formula: Base by product line + vehicle age/make factor + lognormal variance) ---
    PREMIUM_BASE = {
        "PersonalAuto": 1450.0,
        "CommercialProperty": 6200.0,
        "BusinessAuto": 3400.0,
        "HOPHomeowners": 1750.0,
        "WorkersComp": 4800.0,
    }
    base_prem = np.array([PREMIUM_BASE.get(pc, 1600.0) for pc in product_code])
    is_auto = np.isin(product_code, ["PersonalAuto", "BusinessAuto"])
    age_factor = 1.0 + np.clip((vehicle_year - 2020) * 0.02, -0.12, 0.15)
    make_factor = np.where(np.isin(vehicle_make, ["BMW", "Mercedes-Benz", "Audi", "Tesla", "Porsche"]), 1.25, 1.0)
    auto_adjust = np.where(is_auto, age_factor * make_factor, 1.0)
    prem_variance = rng.lognormal(mean=0.0, sigma=0.18, size=n)
    earned_premium = np.round(np.clip(base_prem * auto_adjust * prem_variance, 450.0, 45000.0), 2)

    policy_df = pd.DataFrame({
        "policy_id":      policy_id,
        "account_number": account_number,
        "product_code":   product_code,
        "policy_status":  policy_status,
        "state":          state,
        "period_start":   period_start,
        "period_end":     period_end,
        "vehicle_vin":    vehicle_vin,
        "vehicle_year":   vehicle_year,
        "vehicle_make":   vehicle_make,
        "vehicle_model":  vehicle_model,
        "earned_premium": earned_premium,
    })
    policy_df = policy_df.sort_values("period_start").reset_index(drop=True)
    return policy_df


# =========================================================================
# CLAIMS generator  (30,000 rows)
# =========================================================================
def generate_claim_df(
    policies_df: pd.DataFrame, count: int = 30_000, seed: int = 99
) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    n = int(count)

    # --- Pick random policies (with replacement) ---
    policy_index = rng.integers(0, len(policies_df), size=n)
    sel = policies_df.iloc[policy_index].reset_index(drop=True)

    # --- loss_date: STRICTLY within [period_start, period_end] ---
    p_start = sel["period_start"].values.astype("datetime64[ns]")
    p_end   = sel["period_end"].values.astype("datetime64[ns]")
    delta_days = ((p_end - p_start) / np.timedelta64(1, "D")).astype(np.int64)
    # Guard: ensure at least 1-day span
    delta_days = np.maximum(delta_days, 1)
    loss_offsets = rng.integers(0, delta_days)  # 0 … (delta-1) inclusive
    loss_date = p_start + (loss_offsets * np.timedelta64(1, "D"))

    # --- reported_date: loss_date + random(0..14) days ---
    reported_offsets = rng.integers(0, 15, size=n)
    reported_date = loss_date + (reported_offsets * np.timedelta64(1, "D"))

    # --- Claim state ---
    claim_state = rng.choice(
        np.array(CLAIM_STATES, dtype=object),
        size=n,
        p=np.array(CLAIM_STATE_WEIGHTS),
    )

    # --- Loss cause: Mapped realistically by Policy Product Line ---
    PRODUCT_LOSS_CAUSES = {
        "PersonalAuto": (
            ["vehcollision", "rearend", "theftentire", "rollover", "fire"],
            [0.38, 0.30, 0.16, 0.10, 0.06]
        ),
        "BusinessAuto": (
            ["vehcollision", "rearend", "theftentire", "rollover", "fire"],
            [0.38, 0.30, 0.16, 0.10, 0.06]
        ),
        "CommercialProperty": (
            ["waterdamage", "fire", "slipfall", "theftentire"],
            [0.35, 0.25, 0.25, 0.15]
        ),
        "HOPHomeowners": (
            ["waterdamage", "fire", "theftentire", "slipfall"],
            [0.45, 0.30, 0.15, 0.10]
        ),
        "WorkersComp": (
            ["strain", "slipfall"],
            [0.65, 0.35]
        ),
    }

    loss_cause = np.empty(n, dtype=object)
    for prod, (causes, weights) in PRODUCT_LOSS_CAUSES.items():
        mask = sel["product_code"].values == prod
        count_prod = int(mask.sum())
        if count_prod > 0:
            loss_cause[mask] = rng.choice(
                np.array(causes, dtype=object),
                size=count_prod,
                p=np.array(weights)
            )

    # --- Claim amount (log-normal, realistic range) ---
    claim_amount = np.round(
        np.clip(
            rng.lognormal(mean=4.9, sigma=0.85, size=n),
            a_min=250.0,
            a_max=400_000.0,
        ),
        2,
    )

    # --- Location (state code) ---
    location = rng.choice(np.array(US_STATES, dtype=object), size=n)

    # --- Close Date: Realistic cycle duration for closed claims only ---
    # Fast-closing perils: 15-75 days; Complex perils: 45-210 days
    is_complex_cause = np.isin(loss_cause, ["fire", "slipfall", "strain", "rollover"])
    base_cycle_days = np.where(
        is_complex_cause,
        rng.integers(45, 210, size=n),
        rng.integers(15, 75, size=n),
    )
    # Staggered close date calculation
    calc_close_date = reported_date + (base_cycle_days * np.timedelta64(1, "D"))
    close_date = np.where(claim_state == "closed", calc_close_date.astype(str), None)

    # --- Initial Reserve: Realistic estimation with adverse/favorable variance ---
    # High severity/complex claims tend to exhibit adverse development (initial < final)
    res_factor = np.where(
        claim_amount > 15000.0,
        rng.uniform(0.72, 1.05, size=n),  # Higher probability of upward development
        rng.uniform(0.85, 1.25, size=n),
    )
    initial_reserve = np.round(np.clip(claim_amount * res_factor, 150.0, 450000.0), 2)

    # --- Litigation Flag: ~8-14% baseline, elevated for liability & high severity ---
    lit_prob = np.where(
        claim_amount > 20000.0,
        0.32,
        np.where(np.isin(loss_cause, ["slipfall", "strain", "rollover"]), 0.18, 0.05)
    )
    litigation_flag = (rng.random(size=n) < lit_prob).astype(int)

    # --- Subrogation Amount: Only for third-party fault perils (vehcollision, rearend) ---
    is_subro_eligible = np.isin(loss_cause, ["vehcollision", "rearend"])
    has_subro = is_subro_eligible & (rng.random(size=n) < 0.28)
    subro_ratio = rng.uniform(0.35, 0.75, size=n)
    subrogation_amount = np.where(has_subro, np.round(claim_amount * subro_ratio, 2), 0.0)

    # --- Claim ID: CLM-SYN-{3}-{2}-{6} ---
    claim_id = np.array(
        [
            f"CLM-SYN-{i // 10_000_000:03d}-"
            f"{(i % 10_000_000) // 100_000:02d}-"
            f"{i % 100_000:06d}"
            for i in range(n)
        ],
        dtype=object,
    )

    claims_df = pd.DataFrame({
        "claim_id":           claim_id,
        "policy_id":          sel["policy_id"].values,
        "product_code":       sel["product_code"].values,
        "loss_date":          loss_date,
        "reported_date":      reported_date,
        "close_date":         close_date,
        "claim_state":        claim_state,
        "loss_cause":         loss_cause,
        "claim_amount":       claim_amount,
        "initial_reserve":    initial_reserve,
        "litigation_flag":     litigation_flag,
        "subrogation_amount": subrogation_amount,
        "location":           location,
    })

    # CUSTOM EXTENSION FIELD — not a native Guidewire field, modeled on
    # the .etx extension pattern documented in our Entity Extension Guide
    claims_df["risk_category_tag"] = claims_df["loss_cause"].copy()

    return claims_df


# =========================================================================
# GENERIC pattern-injection function
# =========================================================================
def apply_engineered_pattern(
    claims_df: pd.DataFrame, pattern: dict
) -> pd.DataFrame:
    """Apply ONE engineered pattern to the claims DataFrame.

    This function is fully generic — it reads pattern configuration from the
    *pattern* dict and contains NO references to any specific tag value,
    product name, or domain concept.  All domain knowledge is externalised
    in the ENGINEERED_PATTERNS config list.
    """
    df = claims_df.copy()
    pattern_type = pattern.get("type")

    if pattern_type == "time_trend":
        # Overwrite risk_category_tag on enough rows so the TOTAL rate
        # for the tag_value reaches the yearly target.  Accounts for
        # rows that already carry the tag from base assignment.
        yearly_targets = pattern.get("yearly_targets", {})
        eligible = pattern.get("eligible_loss_causes")

        for year, target_rate in yearly_targets.items():
            year_mask = df["loss_date"].dt.year == int(year)
            if eligible:
                year_mask = year_mask & df["loss_cause"].isin(eligible)
            pool = df.index[year_mask].to_numpy()
            if pool.size == 0:
                continue
            # How many should carry the tag in total?
            desired = max(1, int(np.round(pool.size * target_rate)))
            # How many already do?
            already = int(
                (df.loc[pool, "risk_category_tag"] == pattern["tag_value"]).sum()
            )
            needed = desired - already
            if needed <= 0:
                continue
            # Only flip rows that don't yet have the tag
            flippable = pool[
                df.loc[pool, "risk_category_tag"] != pattern["tag_value"]
            ]
            if flippable.size == 0:
                continue
            flip_count = min(needed, flippable.size)
            selected = RNG.choice(flippable, size=flip_count, replace=False)
            df.loc[selected, "risk_category_tag"] = pattern["tag_value"]

    elif pattern_type == "geographic_skew":
        # Boost occurrence of tag_value in a specific location by multiplier.
        target_location = pattern.get("location")
        if target_location is None:
            return df
        loc_mask = df["location"] == target_location
        loc_idx = df.index[loc_mask].to_numpy()
        if loc_idx.size == 0:
            return df
        baseline_rate = (
            df["risk_category_tag"] == pattern["tag_value"]
        ).mean()
        boosted_rate = min(
            1.0, baseline_rate * float(pattern.get("multiplier", 1.0))
        )
        sel_count = max(1, int(np.floor(loc_idx.size * boosted_rate)))
        sel_count = min(sel_count, loc_idx.size)
        selected = RNG.choice(loc_idx, size=sel_count, replace=False)
        df.loc[selected, "risk_category_tag"] = pattern["tag_value"]

    elif pattern_type == "segment_skew":
        # Boost occurrence of tag_value in a specific segment by multiplier.
        # Optional: restrict candidates to specific loss_cause values via
        # "eligible_loss_causes" in the config.
        seg_field = pattern.get("segment_field")
        seg_value = pattern.get("segment_value")
        if not seg_field or seg_value is None:
            return df
        seg_mask = df[seg_field] == seg_value
        eligible = pattern.get("eligible_loss_causes")
        if eligible:
            seg_mask = seg_mask & df["loss_cause"].isin(eligible)
        seg_idx = df.index[seg_mask].to_numpy()
        if seg_idx.size == 0:
            return df
        baseline_rate = (
            df["risk_category_tag"] == pattern["tag_value"]
        ).mean()
        boosted_rate = min(
            1.0, baseline_rate * float(pattern.get("multiplier", 1.0))
        )
        sel_count = max(1, int(np.floor(seg_idx.size * boosted_rate)))
        sel_count = min(sel_count, seg_idx.size)
        selected = RNG.choice(seg_idx, size=sel_count, replace=False)
        df.loc[selected, "risk_category_tag"] = pattern["tag_value"]

    elif pattern_type == "value_bias":
        # Generic rate-based tag assignment on rows where a given field is
        # non-null (extensibility hook for future patterns).
        factor_field = pattern.get("field")
        if factor_field is None:
            return df
        candidates = df.index[df[factor_field].notna()].to_numpy()
        if candidates.size == 0:
            return df
        sel_count = max(
            1, int(np.floor(candidates.size * float(pattern.get("rate", 0.1))))
        )
        selected = RNG.choice(candidates, size=sel_count, replace=False)
        df.loc[selected, "risk_category_tag"] = pattern["tag_value"]

    return df


# =========================================================================
# Verification helpers
# =========================================================================
def _summarize_pattern(claims_df: pd.DataFrame, pattern: dict) -> dict:
    """Re-derive actual metrics from the generated data for one pattern."""
    ptype = pattern.get("type")
    tag   = pattern.get("tag_value")
    info: dict = {"type": ptype, "tag_value": tag}

    if ptype == "time_trend":
        eligible = pattern.get("eligible_loss_causes")
        yearly = {}
        for year, target in pattern.get("yearly_targets", {}).items():
            ym = claims_df["loss_date"].dt.year == int(year)
            if eligible:
                ym = ym & claims_df["loss_cause"].isin(eligible)
            total = int(ym.sum())
            hits  = int((ym & (claims_df["risk_category_tag"] == tag)).sum())
            actual = hits / total if total else 0.0
            yearly[int(year)] = {
                "target": target, "actual": round(actual, 4),
                "hits": hits, "total": total,
            }
        info["yearly"] = yearly

    elif ptype == "geographic_skew":
        loc = pattern.get("location")
        in_loc  = claims_df["location"] == loc
        out_loc = ~in_loc
        in_total  = int(in_loc.sum())
        out_total = int(out_loc.sum())
        in_hits   = int((in_loc & (claims_df["risk_category_tag"] == tag)).sum())
        out_hits  = int((out_loc & (claims_df["risk_category_tag"] == tag)).sum())
        in_rate   = in_hits / in_total if in_total else 0.0
        out_rate  = out_hits / out_total if out_total else 0.0
        actual_mult = in_rate / out_rate if out_rate else float("inf")
        info["location"] = loc
        info["in_rate"]  = round(in_rate, 4)
        info["out_rate"] = round(out_rate, 4)
        info["actual_multiplier"] = round(actual_mult, 2)

    elif ptype == "segment_skew":
        sf = pattern.get("segment_field")
        sv = pattern.get("segment_value")
        in_seg  = claims_df[sf] == sv
        out_seg = ~in_seg
        in_total  = int(in_seg.sum())
        out_total = int(out_seg.sum())
        in_hits   = int((in_seg & (claims_df["risk_category_tag"] == tag)).sum())
        out_hits  = int((out_seg & (claims_df["risk_category_tag"] == tag)).sum())
        in_rate   = in_hits / in_total if in_total else 0.0
        out_rate  = out_hits / out_total if out_total else 0.0
        actual_mult = in_rate / out_rate if out_rate else float("inf")
        info["segment"] = f"{sf}={sv}"
        info["in_rate"]  = round(in_rate, 4)
        info["out_rate"] = round(out_rate, 4)
        info["actual_multiplier"] = round(actual_mult, 2)

    return info


def validate_integrity(
    policies_df: pd.DataFrame, claims_df: pd.DataFrame
) -> None:
    """Enforce verified temporal integrity rules from §4 of
    10_SYNTHETIC_DATA_GENERATION_RULES.md:
      - loss_date >= period_start AND loss_date <= period_end
      - reported_date >= loss_date
    """
    lookup = policies_df.set_index("policy_id")
    p_start = lookup.loc[claims_df["policy_id"], "period_start"].values
    p_end   = lookup.loc[claims_df["policy_id"], "period_end"].values

    bad_loss = (
        (claims_df["loss_date"].values < p_start)
        | (claims_df["loss_date"].values > p_end)
    )
    if bad_loss.any():
        raise ValueError(
            f"INTEGRITY VIOLATION: {int(bad_loss.sum())} claims have "
            f"loss_date outside their policy period."
        )

    bad_reported = claims_df["reported_date"].values < claims_df["loss_date"].values
    if bad_reported.any():
        raise ValueError(
            f"INTEGRITY VIOLATION: {int(bad_reported.sum())} claims have "
            f"reported_date before loss_date."
        )

    print("[OK]  All temporal integrity checks passed.")


# =========================================================================
# Main entry-point
# =========================================================================
def main() -> None:
    print("=" * 72)
    print("  Roundtable -- Synthetic Insurance Data Generator")
    print("  Guidewire PolicyCenter + ClaimCenter  (schema v10.2.1)")
    print("=" * 72)

    # ── Generate ──────────────────────────────────────────────────────────
    print("\n[1/4] Generating 10,000 policies ...")
    policies_df = generate_policy_df(count=10_000, seed=42)

    print("[2/4] Generating 30,000 claims ...")
    claims_df = generate_claim_df(policies_df, count=30_000, seed=99)

    # ── Apply engineered patterns ─────────────────────────────────────────
    print("[3/4] Applying engineered patterns ...")
    for pat in ENGINEERED_PATTERNS:
        claims_df = apply_engineered_pattern(claims_df, pat)

    # ── Validate ──────────────────────────────────────────────────────────
    validate_integrity(policies_df, claims_df)

    # ── Load into SQLite ──────────────────────────────────────────────────
    print(f"[4/4] Writing to SQLite -> {DB_PATH}")
    with sqlite3.connect(str(DB_PATH)) as conn:
        policies_df.to_sql(
            "policies", conn,
            if_exists="replace", index=False,
            method="multi", chunksize=1000,
        )
        claims_df.to_sql(
            "claims", conn,
            if_exists="replace", index=False,
            method="multi", chunksize=1000,
        )

    # ── Verification block ────────────────────────────────────────────────
    print("\n" + "=" * 72)
    print("  VERIFICATION — actual values recalculated from generated data")
    print("=" * 72)

    for i, pat in enumerate(ENGINEERED_PATTERNS, 1):
        result = _summarize_pattern(claims_df, pat)
        print(f"\n-- Pattern {i}: {result['type']} "
              f"(tag_value={result['tag_value']!r}) --")
        if result["type"] == "time_trend":
            for yr, info in result["yearly"].items():
                print(f"   {yr}:  target={info['target']:.2%}  "
                      f"actual={info['actual']:.2%}  "
                      f"({info['hits']}/{info['total']})")
        elif result["type"] == "geographic_skew":
            print(f"   location={result['location']}  "
                  f"in_rate={result['in_rate']:.4f}  "
                  f"out_rate={result['out_rate']:.4f}  "
                  f"actual_multiplier={result['actual_multiplier']}  "
                  f"(target x{pat['multiplier']})")
        elif result["type"] == "segment_skew":
            print(f"   segment={result['segment']}  "
                  f"in_rate={result['in_rate']:.4f}  "
                  f"out_rate={result['out_rate']:.4f}  "
                  f"actual_multiplier={result['actual_multiplier']}  "
                  f"(target x{pat['multiplier']})")

    print(f"\n  POLICIES rows: {len(policies_df):,}")
    print(f"  CLAIMS   rows: {len(claims_df):,}")
    print("=" * 72)


if __name__ == "__main__":
    main()
