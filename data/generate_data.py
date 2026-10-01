"""
Synthetic Insurance Data Generator
===================================
Generates Guidewire-shaped PolicyCenter and ClaimCenter data and loads it
into roundtable.db. The data is built the way a carrier's book actually
behaves, so that claims-team metrics computed from it are meaningful:

  policies        One row per policy *period* (term). Policies renew with a
                  retention rate, so the book grows over time. Auto terms
                  are 6 months, all other lines 12 months.
  earned_exposure Earned exposure units and earned premium per policy period
                  per calendar year. This is the denominator for frequency
                  (claims per 1,000 exposure-years) and loss ratio.
  claims          Claim header (ClaimCenter Claim): dates, state, cause,
                  fault, segment, assignment, litigation, SIU, CAT code,
                  denial / no-payment reason and financial roll-ups.
  exposures       ClaimCenter Exposure rows: exposure type, coverage,
                  claimant, reserves, payments, recoveries, limits.

Claims are generated from exposure with Poisson frequencies per line and
loss cause, so claim counts follow the book and the trends below are
embedded in the rates rather than painted onto random rows:

  - EV share of the auto book grows every year, and EV claims carry a
    battery_fault tag when the high-voltage pack is damaged (collision,
    road debris, thermal event, flood) or fails on its own (denied as
    mechanical breakdown -> a coverage-gap signal).
  - Homeowners water damage frequency rises year over year, plus a winter
    freeze CAT in TX and a hurricane CAT in FL.
  - Workers' comp strain frequency rises year over year.
  - Vehicle theft is concentrated in IL and on 2015-2021 Kia/Hyundai ICE
    models, fading after the 2023 anti-theft software fix.
  - Rollovers are concentrated in TX; premises falls in commercial lines.

Typelist codes follow 04_CC_TYPELIST_CATALOG.md (LossCause, ExposureType,
CoverageType, ClaimSegment, ClaimClosedOutcomeType, FaultRating,
LitigationStatus, SIUStatus, LossType). risk_category_tag and
denial_reason / no_payment_reason are custom extensions (see
01_ENTITY_EXTENSION_GUIDE.md).

Source schemas:
  - 09_SYNTHETIC_DATA_SCHEMA.md
  - 10_SYNTHETIC_DATA_GENERATION_RULES.md
  - 08_INSURANCE_RELATIONSHIP_GRAPH.md
  - 11_POLICYCENTER_CLAIMCENTER_FIELD_INDEX.md
"""
from __future__ import annotations

import math
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Paths, dates & RNG
# ---------------------------------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = ROOT_DIR / "roundtable.db"

AS_OF = pd.Timestamp("2026-09-30")       # valuation date: nothing after this exists
BOOK_START = pd.Timestamp("2022-01-01")  # first new-business effective date
N_NEW_BUSINESS = 60_000                  # new-business policies written 2022 -> AS_OF
SEED = 20260930

# ---------------------------------------------------------------------------
# Book of business
# ---------------------------------------------------------------------------
# Population-weighted state mix (top states explicit, remainder spread)
STATE_WEIGHTS = {
    "CA": 11.5, "TX": 9.0, "FL": 6.8, "NY": 5.8, "PA": 3.9, "IL": 3.8, "OH": 3.5,
    "GA": 3.3, "NC": 3.2, "MI": 3.0, "NJ": 2.8, "VA": 2.6, "WA": 2.3, "AZ": 2.2,
    "MA": 2.1, "TN": 2.1, "IN": 2.0, "MO": 1.8, "MD": 1.8, "WI": 1.8, "CO": 1.8,
    "MN": 1.7, "SC": 1.6, "AL": 1.5, "LA": 1.4, "KY": 1.4, "OR": 1.3, "OK": 1.2,
    "CT": 1.1, "UT": 1.0, "IA": 1.0, "NV": 1.0, "AR": 0.9, "MS": 0.9, "KS": 0.9,
    "NM": 0.6, "NE": 0.6, "ID": 0.6, "WV": 0.5, "HI": 0.4, "NH": 0.4, "ME": 0.4,
    "MT": 0.3, "RI": 0.3, "DE": 0.3, "SD": 0.3, "ND": 0.2, "AK": 0.2, "VT": 0.2, "WY": 0.2,
}
STATES = np.array(list(STATE_WEIGHTS.keys()), dtype=object)
STATE_P = np.array(list(STATE_WEIGHTS.values())) / sum(STATE_WEIGHTS.values())

PRODUCT_MIX = {
    "PersonalAuto": 0.46,
    "HOPHomeowners": 0.26,
    "BusinessAuto": 0.09,
    "CommercialProperty": 0.11,
    "WorkersComp": 0.08,
}
TERM_MONTHS = {"PersonalAuto": 6, "BusinessAuto": 12, "HOPHomeowners": 12,
               "CommercialProperty": 12, "WorkersComp": 12}
RETENTION = {"PersonalAuto": 0.87, "BusinessAuto": 0.83, "HOPHomeowners": 0.88,
             "CommercialProperty": 0.84, "WorkersComp": 0.85}
CANCEL_RATE = 0.04            # share of terms cancelled mid-term
RATE_CHANGE_PER_YEAR = 0.07   # filed rate increases, applied at renewal
LOSS_TYPE = {"PersonalAuto": "AUTO", "BusinessAuto": "AUTO", "HOPHomeowners": "PR",
             "CommercialProperty": "PR", "WorkersComp": "WC"}
AUTO_LINES = ("PersonalAuto", "BusinessAuto")

# (make, model, new price) by powertrain
PA_VEHICLES = {
    "ICE": [("Toyota", "Camry", 29000), ("Toyota", "RAV4", 32000), ("Honda", "Civic", 26000),
            ("Honda", "CR-V", 32000), ("Ford", "F-150", 48000), ("Ford", "Explorer", 42000),
            ("Chevrolet", "Silverado", 45000), ("Chevrolet", "Equinox", 30000), ("Nissan", "Rogue", 30000),
            ("Jeep", "Grand Cherokee", 45000), ("Jeep", "Wrangler", 40000), ("BMW", "X5", 65000),
            ("Hyundai", "Elantra", 23000), ("Hyundai", "Tucson", 29000), ("Kia", "Sportage", 29000),
            ("Kia", "Optima", 25000), ("Subaru", "Outback", 32000)],
    "Hybrid": [("Toyota", "Prius", 30000), ("Toyota", "RAV4 Hybrid", 35000),
               ("Honda", "Accord Hybrid", 34000), ("Ford", "Maverick Hybrid", 26000)],
    "EV": [("Tesla", "Model Y", 47000), ("Tesla", "Model 3", 42000), ("Ford", "Mustang Mach-E", 48000),
           ("Chevrolet", "Bolt EV", 28000), ("Hyundai", "Ioniq 5", 45000), ("Kia", "EV6", 46000),
           ("Nissan", "Leaf", 30000), ("BMW", "i4", 55000), ("Rivian", "R1S", 78000)],
}
PA_VEHICLE_P = {
    "ICE": [0.09, 0.09, 0.07, 0.08, 0.09, 0.06, 0.07, 0.06, 0.06, 0.05, 0.04, 0.03, 0.04, 0.04, 0.04, 0.03, 0.06],
    "Hybrid": [0.30, 0.35, 0.20, 0.15],
    "EV": [0.30, 0.22, 0.10, 0.10, 0.08, 0.06, 0.06, 0.04, 0.04],
}
BA_VEHICLES = {
    "ICE": [("Ford", "Transit", 48000), ("Ford", "F-250", 55000), ("Chevrolet", "Express", 42000),
            ("Ram", "ProMaster", 44000), ("Chevrolet", "Silverado", 45000)],
    "Hybrid": [("Ford", "F-150 PowerBoost", 55000)],
    "EV": [("Ford", "E-Transit", 52000), ("Rivian", "EDV", 83000), ("Tesla", "Model Y", 47000)],
}
BA_VEHICLE_P = {"ICE": [0.30, 0.25, 0.15, 0.15, 0.15], "Hybrid": [1.0], "EV": [0.55, 0.25, 0.20]}

# Share of new-business vehicles by powertrain, by year written
EV_SHARE = {"PersonalAuto": {2022: 0.06, 2023: 0.09, 2024: 0.12, 2025: 0.15, 2026: 0.18},
            "BusinessAuto": {2022: 0.02, 2023: 0.03, 2024: 0.05, 2025: 0.07, 2026: 0.09}}
HYBRID_SHARE = {"PersonalAuto": 0.07, "BusinessAuto": 0.03}

# Replacement cost of the high-voltage battery pack by model (USD, parts + labour)
EV_PACK_COST = {"Model Y": 16500, "Model 3": 15500, "Mustang Mach-E": 22000, "Bolt EV": 16000,
                "Ioniq 5": 25000, "EV6": 25000, "Leaf": 9500, "i4": 22000, "R1S": 30000,
                "E-Transit": 24000, "EDV": 32000}

# ---------------------------------------------------------------------------
# Loss causes: frequency per exposure-unit-year by line
#   unit = vehicle (auto), dwelling (HO), location (CP), employee (WC)
# ---------------------------------------------------------------------------
# year_trend multiplies frequency by accident year; state_mult by policy state.
CAUSES = {
    "PersonalAuto": [
        {"cause": "vehcollision",   "freq": 0.040},
        {"cause": "rearend",        "freq": 0.030},
        {"cause": "fixedobjcoll",   "freq": 0.012},
        {"cause": "animalcollision", "freq": 0.007},
        {"cause": "otherobjcoll",   "freq": 0.004},   # road debris
        {"cause": "rollover",       "freq": 0.0025, "state_mult": {"TX": 2.1, "OK": 1.6, "WY": 1.8}},
        {"cause": "theftentire",    "freq": 0.0030, "state_mult": {"IL": 2.2, "CA": 1.3, "MO": 1.4}},
        {"cause": "theftparts",     "freq": 0.0040, "exclude_powertrain": ["EV"]},   # catalytic converters
        {"cause": "glassbreakage",  "freq": 0.028},
        {"cause": "hail",           "freq": 0.004, "state_mult": {"TX": 2.0, "CO": 2.5, "OK": 1.8, "NE": 1.8, "KS": 1.8}},
        {"cause": "vandalism",      "freq": 0.004},
        {"cause": "firedamage",     "freq": 0.0012, "exclude_powertrain": ["EV"]},
        {"cause": "waterdamage",    "freq": 0.0012},  # flood / submersion
        # EV-only high-voltage battery perils (tagged battery_fault)
        {"cause": "firedamage",     "freq": 0.0006, "only_powertrain": ["EV"], "battery": "thermal"},
        {"cause": "product",        "freq": 0.0055, "only_powertrain": ["EV"], "battery": "cell_failure",
         "age_slope": 0.30},
    ],
    "BusinessAuto": [
        {"cause": "vehcollision",   "freq": 0.060},
        {"cause": "rearend",        "freq": 0.045},
        {"cause": "fixedobjcoll",   "freq": 0.020},
        {"cause": "otherobjcoll",   "freq": 0.006},
        {"cause": "rollover",       "freq": 0.004, "state_mult": {"TX": 2.1, "OK": 1.6}},
        {"cause": "theftentire",    "freq": 0.0020, "state_mult": {"IL": 2.2}},
        {"cause": "theftparts",     "freq": 0.0060, "exclude_powertrain": ["EV"]},
        {"cause": "glassbreakage",  "freq": 0.030},
        {"cause": "loadingdamage",  "freq": 0.006},
        {"cause": "firedamage",     "freq": 0.0015, "exclude_powertrain": ["EV"]},
        {"cause": "firedamage",     "freq": 0.0008, "only_powertrain": ["EV"], "battery": "thermal"},
        {"cause": "product",        "freq": 0.0070, "only_powertrain": ["EV"], "battery": "cell_failure",
         "age_slope": 0.30},
    ],
    "HOPHomeowners": [
        {"cause": "waterdamage", "freq": 0.020,
         "year_trend": {2022: 1.00, 2023: 1.06, 2024: 1.18, 2025: 1.33, 2026: 1.48}},
        {"cause": "fire",        "freq": 0.0035},
        {"cause": "wind",        "freq": 0.010, "state_mult": {"FL": 1.8, "TX": 1.5, "LA": 1.7, "OK": 1.6}},
        {"cause": "hail",        "freq": 0.008, "state_mult": {"TX": 2.2, "CO": 2.6, "OK": 2.0, "NE": 2.0, "KS": 2.0}},
        {"cause": "burglary",    "freq": 0.006},
        {"cause": "mold",        "freq": 0.0015, "state_mult": {"FL": 1.8, "LA": 1.6}},
        {"cause": "fall",        "freq": 0.0020},   # premises liability (slip & fall)
    ],
    "CommercialProperty": [
        {"cause": "waterdamage", "freq": 0.026,
         "year_trend": {2022: 1.00, 2023: 1.05, 2024: 1.14, 2025: 1.24, 2026: 1.33}},
        {"cause": "fire",        "freq": 0.0080},
        {"cause": "wind",        "freq": 0.014, "state_mult": {"FL": 1.8, "TX": 1.5, "LA": 1.7}},
        {"cause": "hail",        "freq": 0.008, "state_mult": {"TX": 2.2, "CO": 2.6, "OK": 2.0}},
        {"cause": "burglary",    "freq": 0.012},
        {"cause": "vandalism",   "freq": 0.008},
        {"cause": "fall",        "freq": 0.030},    # premises liability (package GL)
    ],
    "WorkersComp": [
        {"cause": "strain",     "freq": 0.032,
         "year_trend": {2022: 1.00, 2023: 1.10, 2024: 1.24, 2025: 1.40, 2026: 1.55}},
        {"cause": "fall",       "freq": 0.014},
        {"cause": "struck",     "freq": 0.008},
        {"cause": "cut",        "freq": 0.010},
        {"cause": "caught_in",  "freq": 0.003},
        {"cause": "burn_scald", "freq": 0.003},
        {"cause": "motorvehicle", "freq": 0.002},
    ],
}

# Catastrophe events: extra claims for policies in force in the listed states
CAT_EVENTS = [
    {"cat_code": "CAT-2023-TX-HAIL-0412", "date": "2023-04-12", "states": ["TX"], "days": 2,
     "causes": {"PersonalAuto": ("hail", 0.050), "BusinessAuto": ("hail", 0.040),
                "HOPHomeowners": ("hail", 0.070), "CommercialProperty": ("hail", 0.060)}},
    {"cat_code": "CAT-2024-CO-HAIL-0603", "date": "2024-06-03", "states": ["CO"], "days": 2,
     "causes": {"PersonalAuto": ("hail", 0.060), "HOPHomeowners": ("hail", 0.080),
                "CommercialProperty": ("hail", 0.060)}},
    {"cat_code": "CAT-2024-FL-HURR-1009", "date": "2024-10-09", "states": ["FL"], "days": 4,
     "causes": {"HOPHomeowners": ("wind", 0.120), "CommercialProperty": ("wind", 0.100),
                "PersonalAuto": ("waterdamage", 0.020), "BusinessAuto": ("waterdamage", 0.015)}},
    {"cat_code": "CAT-2025-TX-FREEZE-0120", "date": "2025-01-20", "states": ["TX", "OK", "LA"], "days": 5,
     "causes": {"HOPHomeowners": ("waterdamage", 0.050), "CommercialProperty": ("waterdamage", 0.040)}},
    {"cat_code": "CAT-2026-IL-WIND-0315", "date": "2026-03-15", "states": ["IL", "IN", "MO"], "days": 2,
     "causes": {"HOPHomeowners": ("wind", 0.045), "CommercialProperty": ("wind", 0.035)}},
]

# ClaimCenter LossCause code -> risk_category_tag (custom extension). Perils that exist on
# both vehicles and buildings get separate tags so each is measured on its own exposure base.
CAUSE_TO_TAG = {"fall": "slipfall", "firedamage": "vehiclefire"}
AUTO_CAUSE_TO_TAG = {"waterdamage": "vehicleflood", "hail": "vehiclehail", "vandalism": "vehiclevandalism"}
WC_CAUSE_TO_TAG = {"fall": "workplace_fall"}

COLLISION_CAUSES = {"vehcollision", "rearend", "fixedobjcoll", "otherobjcoll", "rollover", "loadingdamage"}
COMP_CAUSES = {"animalcollision", "theftentire", "theftparts", "glassbreakage", "hail",
               "vandalism", "firedamage", "waterdamage", "product"}

ASSIGNED_GROUP_SIZE = {"Auto Fast Track": 8, "Auto Physical Damage": 14, "Auto Total Loss": 6,
                       "Auto Injury": 10, "Property Desk": 12, "Property Large Loss": 5,
                       "Liability": 7, "WC Medical Only": 6, "WC Lost Time": 8, "SIU": 4}

LOSS_DESCRIPTIONS = {
    "vehcollision": ["Insured vehicle collided with another vehicle at intersection",
                     "Two-vehicle collision while changing lanes", "Side-impact collision in parking lot"],
    "rearend": ["Insured vehicle rear-ended at stop light", "Insured rear-ended other vehicle in slow traffic"],
    "fixedobjcoll": ["Vehicle struck guardrail on wet road", "Vehicle struck pole while parking"],
    "animalcollision": ["Vehicle struck deer on rural highway"],
    "otherobjcoll": ["Road debris struck vehicle underbody on highway"],
    "rollover": ["Single-vehicle rollover after leaving roadway"],
    "theftentire": ["Vehicle stolen from driveway overnight", "Vehicle stolen from parking garage"],
    "theftparts": ["Catalytic converter cut from vehicle", "Wheels and tires stolen overnight"],
    "glassbreakage": ["Windshield cracked by stone chip", "Side window broken"],
    "hail": ["Hail damage to vehicle/roof during storm"],
    "vandalism": ["Vehicle keyed and windows broken", "Graffiti and forced entry damage"],
    "firedamage": ["Engine compartment fire while driving"],
    "waterdamage": ["Water damage from burst supply line", "Water damage from appliance leak",
                    "Vehicle submerged in flood water"],
    "fire": ["Kitchen fire spread to adjoining rooms", "Electrical fire in attic"],
    "wind": ["Wind damage to roof and siding"],
    "burglary": ["Forced entry, electronics and jewelry taken", "Break-in, inventory and equipment taken"],
    "mold": ["Mold growth discovered behind wall"],
    "fall": ["Visitor slipped on wet floor and was injured", "Trip and fall on uneven walkway"],
    "strain": ["Lower back strain lifting boxes", "Shoulder strain from repetitive overhead work"],
    "struck": ["Employee struck by falling object"], "cut": ["Laceration from box cutter"],
    "caught_in": ["Hand caught in machinery"], "burn_scald": ["Burn from hot equipment"],
    "motorvehicle": ["Employee injured in vehicle accident while on duty"],
    "loadingdamage": ["Cargo damaged during loading"],
}
BATTERY_DESCRIPTIONS = {
    "collision": "Collision damaged high-voltage battery enclosure; pack flagged for replacement",
    "debris": "Road debris punctured high-voltage battery enclosure",
    "thermal": "High-voltage battery thermal event; vehicle fire while parked/charging",
    "flood": "EV submerged in flood water; high-voltage battery compromised",
    "cell_failure": "High-voltage battery cell failure / capacity loss with no external cause",
}


# =========================================================================
# POLICIES: new business + renewal chains (one row per policy period)
# =========================================================================
def _pick_vehicles(rng, product, powertrain, n):
    table, probs = (PA_VEHICLES, PA_VEHICLE_P) if product == "PersonalAuto" else (BA_VEHICLES, BA_VEHICLE_P)
    idx = rng.choice(len(table[powertrain]), size=n, p=probs[powertrain])
    return [table[powertrain][i] for i in idx]


def generate_policy_df(rng: np.random.Generator) -> pd.DataFrame:
    n = N_NEW_BUSINESS
    products = rng.choice(list(PRODUCT_MIX), size=n, p=list(PRODUCT_MIX.values()))
    span_days = (AS_OF - BOOK_START).days
    inception = BOOK_START + pd.to_timedelta(rng.integers(0, span_days, size=n), unit="D")
    states = rng.choice(STATES, size=n, p=STATE_P)

    base = pd.DataFrame({"product_code": products, "inception": inception, "state": states})
    base["policy_number"] = [f"{p[:2].upper()}-{i:07d}" for i, p in enumerate(products)]
    base["account_number"] = [f"ACC-SYN-{v:07d}" for v in rng.integers(1_000_000, 10_000_000, size=n)]

    # --- Risk characteristics (fixed across renewals) ---
    units = np.ones(n)
    is_pa = products == "PersonalAuto"
    is_ba = products == "BusinessAuto"
    is_cp = products == "CommercialProperty"
    is_wc = products == "WorkersComp"
    units[is_pa] = rng.choice([1, 2, 3], size=is_pa.sum(), p=[0.55, 0.33, 0.12])
    units[is_ba] = np.clip(np.round(rng.lognormal(np.log(4), 0.8, size=is_ba.sum())), 1, 60)
    units[is_cp] = rng.choice([1, 2, 3, 4, 5], size=is_cp.sum(), p=[0.62, 0.2, 0.1, 0.05, 0.03])
    units[is_wc] = np.clip(np.round(rng.lognormal(np.log(14), 0.9, size=is_wc.sum())), 2, 400)
    base["exposure_units"] = units.astype(int)

    powertrain = np.full(n, None, dtype=object)
    make = np.full(n, None, dtype=object)
    model = np.full(n, None, dtype=object)
    new_price = np.zeros(n)
    veh_year = np.full(n, np.nan)
    for prod in AUTO_LINES:
        mask = products == prod
        idx = np.where(mask)[0]
        written_year = inception[idx].year.to_numpy()
        ev_p = np.array([EV_SHARE[prod][y] for y in written_year])
        u = rng.random(len(idx))
        pt = np.where(u < ev_p, "EV", np.where(u < ev_p + HYBRID_SHARE[prod], "Hybrid", "ICE"))
        powertrain[idx] = pt
        for p in ("ICE", "Hybrid", "EV"):
            sub = idx[pt == p]
            if len(sub) == 0:
                continue
            picks = _pick_vehicles(rng, prod, p, len(sub))
            make[sub] = [v[0] for v in picks]
            model[sub] = [v[1] for v in picks]
            new_price[sub] = [v[2] for v in picks]
            max_age = 6 if p == "EV" else 12
            ages = rng.integers(0, max_age + 1, size=len(sub))
            veh_year[sub] = inception[sub].year.to_numpy() - ages
    base["vehicle_powertrain"] = powertrain
    base["vehicle_make"] = make
    base["vehicle_model"] = model
    base["vehicle_year"] = veh_year
    base["vehicle_new_price"] = new_price
    alphabet = np.array(list("ABCDEFGHJKLMNPRSTUVWXYZ0123456789"))
    vins = ["".join(r) for r in rng.choice(alphabet, size=(n, 17))]
    base["vehicle_vin"] = np.where(np.isin(products, AUTO_LINES), vins, None)

    # Coverage structure
    auto_mask = np.isin(products, AUTO_LINES)
    old_vehicle = auto_mask & (base["vehicle_year"].fillna(2030).to_numpy() < 2014)
    base["physical_damage_cov"] = np.where(auto_mask, ~(old_vehicle & (rng.random(n) < 0.6)), False)
    deductible = np.zeros(n)
    deductible[auto_mask] = rng.choice([250, 500, 1000], size=auto_mask.sum(), p=[0.15, 0.55, 0.30])
    deductible[products == "HOPHomeowners"] = rng.choice([1000, 2500, 5000], size=(products == "HOPHomeowners").sum(), p=[0.55, 0.35, 0.10])
    deductible[is_cp] = rng.choice([2500, 5000, 10000], size=is_cp.sum(), p=[0.4, 0.45, 0.15])
    base["deductible"] = deductible
    liab = np.zeros(n)
    liab[auto_mask] = rng.choice([50_000, 100_000, 250_000, 500_000], size=auto_mask.sum(), p=[0.2, 0.4, 0.3, 0.1])
    liab[products == "HOPHomeowners"] = rng.choice([100_000, 300_000, 500_000], size=(products == "HOPHomeowners").sum(), p=[0.3, 0.5, 0.2])
    liab[is_cp] = 1_000_000
    base["liability_limit"] = liab
    prop_limit = np.zeros(n)
    prop_limit[products == "HOPHomeowners"] = np.round(rng.lognormal(np.log(380_000), 0.4, size=(products == "HOPHomeowners").sum()), -3)
    prop_limit[is_cp] = np.round(rng.lognormal(np.log(1_400_000), 0.7, size=is_cp.sum()), -3)
    base["property_limit"] = prop_limit

    # Annual premium at inception (per policy, full year)
    prem = np.zeros(n)
    state_factor = np.where(np.isin(states, ["FL", "LA", "MI", "NY", "CA"]), 1.25, 1.0)
    prem[is_pa] = 1750 * units[is_pa] * np.where(powertrain[is_pa] == "EV", 1.25, 1.0)
    prem[is_ba] = 3000 * units[is_ba]
    hop = products == "HOPHomeowners"
    prem[hop] = 1700 * (prop_limit[hop] / 380_000) ** 0.8
    prem[is_cp] = 9000 * units[is_cp] * (prop_limit[is_cp] / 1_400_000) ** 0.5
    prem[is_wc] = 1900 * units[is_wc]
    prem = prem * state_factor * rng.lognormal(0, 0.15, size=n)
    base["annual_premium_at_inception"] = prem

    # --- Renewal chains ---
    rows = []
    for i, r in enumerate(base.itertuples(index=False)):
        months = TERM_MONTHS[r.product_code]
        start = r.inception
        term = 1
        while start < AS_OF:
            end = start + pd.DateOffset(months=months)
            cancel = None
            if rng.random() < CANCEL_RATE:
                cancel = start + pd.Timedelta(days=int(rng.integers(20, (end - start).days)))
            years_since = (start - r.inception).days / 365.25
            written = r.annual_premium_at_inception * (months / 12) * (1 + RATE_CHANGE_PER_YEAR) ** years_since
            rows.append((i, term, start, end, cancel, written))
            if cancel is not None or rng.random() > RETENTION[r.product_code]:
                break
            start, term = end, term + 1

    terms = pd.DataFrame(rows, columns=["base_idx", "term_number", "period_start", "period_end",
                                        "cancel_date", "written_premium"])
    df = base.iloc[terms["base_idx"]].reset_index(drop=True).join(terms.drop(columns="base_idx"))
    df.insert(0, "policy_id", [f"PP-{i:07d}" for i in range(len(df))])
    df["policy_status"] = "Bound"   # GW keeps Bound on expired/cancelled periods; cancel_date marks cancellation
    eff_end = df[["period_end"]].assign(c=df["cancel_date"].fillna(pd.Timestamp.max), a=AS_OF).min(axis=1)
    df["earned_through"] = eff_end
    full_days = (df["period_end"] - df["period_start"]).dt.days
    earned_days = (eff_end - df["period_start"]).dt.days.clip(lower=0)
    df["earned_premium"] = (df["written_premium"] * earned_days / full_days).round(2)
    df["written_premium"] = df["written_premium"].round(2)

    # Vehicle actual cash value at term start (depreciation ~15%/yr)
    age = (df["period_start"].dt.year - df["vehicle_year"]).clip(lower=0)
    df["vehicle_acv"] = (df["vehicle_new_price"] * 0.85 ** age).round(-2)
    df.loc[~df["product_code"].isin(AUTO_LINES), "vehicle_acv"] = np.nan
    df["employee_count"] = np.where(df["product_code"] == "WorkersComp", df["exposure_units"], np.nan)

    return df.drop(columns=["inception", "annual_premium_at_inception", "vehicle_new_price"])


def build_earned_exposure(policies: pd.DataFrame) -> pd.DataFrame:
    """Earned exposure-years and earned premium per policy period per calendar year."""
    out = []
    start = policies["period_start"]
    end = policies["earned_through"]
    full_days = (policies["period_end"] - policies["period_start"]).dt.days
    for year in range(BOOK_START.year, AS_OF.year + 1):
        y0, y1 = pd.Timestamp(f"{year}-01-01"), pd.Timestamp(f"{year + 1}-01-01")
        lo = start.where(start > y0, y0)
        hi = end.where(end < y1, y1)
        days = (hi - lo).dt.days.clip(lower=0)
        m = days > 0
        if not m.any():
            continue
        p = policies[m]
        out.append(pd.DataFrame({
            "policy_id": p["policy_id"],
            "calendar_year": year,
            "product_code": p["product_code"],
            "state": p["state"],
            "vehicle_powertrain": p["vehicle_powertrain"],
            "earned_exposure": (days[m] / 365.25 * p["exposure_units"]).round(4),
            "earned_premium": (p["written_premium"] * days[m] / full_days[m]).round(2),
        }))
    return pd.concat(out, ignore_index=True)


# =========================================================================
# CLAIM OCCURRENCES: Poisson frequency on earned exposure
# =========================================================================
def _uniform_dates(rng, starts, ends):
    span = np.maximum((ends - starts).dt.days.to_numpy(), 1)
    return starts.to_numpy() + (rng.random(len(span)) * span).astype(int) * np.timedelta64(1, "D")


def generate_occurrences(rng: np.random.Generator, policies: pd.DataFrame) -> pd.DataFrame:
    earned_years = ((policies["earned_through"] - policies["period_start"]).dt.days.clip(lower=0) / 365.25).to_numpy()
    units = policies["exposure_units"].to_numpy()
    occ = []
    for product, specs in CAUSES.items():
        pmask = (policies["product_code"] == product).to_numpy()
        for spec in specs:
            mask = pmask.copy()
            pt = policies["vehicle_powertrain"].to_numpy()
            if "only_powertrain" in spec:
                mask &= np.isin(pt, spec["only_powertrain"])
            if "exclude_powertrain" in spec:
                mask &= ~np.isin(pt, spec["exclude_powertrain"])
            idx = np.where(mask)[0]
            if len(idx) == 0:
                continue
            sub = policies.iloc[idx]
            lam = spec["freq"] * earned_years[idx] * units[idx]
            if "state_mult" in spec:
                lam = lam * sub["state"].map(spec["state_mult"]).fillna(1.0).to_numpy()
            if spec.get("age_slope"):
                veh_age = (sub["period_start"].dt.year - sub["vehicle_year"]).clip(lower=0).to_numpy()
                lam = lam * (1 + spec["age_slope"] * veh_age)
            # Kia/Hyundai 2015-2021 ICE theft wave (strongest 2022-2023)
            kia_mult_max = 1.0
            if spec["cause"] == "theftentire":
                kia = (sub["vehicle_make"].isin(["Kia", "Hyundai"]) & (sub["vehicle_powertrain"] == "ICE")
                       & sub["vehicle_year"].between(2015, 2021)).to_numpy()
                kia_mult_max = 6.0
                lam = lam * np.where(kia, kia_mult_max, 1.0)
            trend = spec.get("year_trend")
            tmax = max(trend.values()) if trend else 1.0
            n = rng.poisson(lam * tmax)
            rep = np.repeat(idx, n)
            if len(rep) == 0:
                continue
            rp = policies.iloc[rep]
            loss_date = pd.Series(_uniform_dates(rng, rp["period_start"], rp["earned_through"]))
            years = loss_date.dt.year.to_numpy()
            keep = np.ones(len(rep), dtype=bool)
            if trend:
                keep &= rng.random(len(rep)) < np.array([trend.get(y, tmax) for y in years]) / tmax
            if spec["cause"] == "theftentire":
                kia_r = (rp["vehicle_make"].isin(["Kia", "Hyundai"]) & (rp["vehicle_powertrain"] == "ICE")
                         & rp["vehicle_year"].between(2015, 2021)).to_numpy()
                decay = {2022: 1.0, 2023: 0.9, 2024: 0.45, 2025: 0.28, 2026: 0.22}
                keep &= ~kia_r | (rng.random(len(rep)) < np.array([decay.get(y, 0.2) for y in years]))
            occ.append(pd.DataFrame({
                "policy_row": rep[keep], "loss_date": loss_date.to_numpy()[keep],
                "loss_cause": spec["cause"], "battery_mode": spec.get("battery"), "cat_code": None,
            }))

    # Catastrophe events
    for ev in CAT_EVENTS:
        d0 = pd.Timestamp(ev["date"])
        for product, (cause, freq) in ev["causes"].items():
            m = ((policies["product_code"] == product) & policies["state"].isin(ev["states"])
                 & (policies["period_start"] <= d0) & (policies["earned_through"] > d0)).to_numpy()
            idx = np.where(m)[0]
            n = rng.poisson(freq * units[idx])
            rep = np.repeat(idx, n)
            if len(rep) == 0:
                continue
            ld = d0.to_datetime64() + rng.integers(0, ev["days"], size=len(rep)) * np.timedelta64(1, "D")
            pt = policies["vehicle_powertrain"].to_numpy()[rep]
            battery = np.where((pt == "EV") & (cause == "waterdamage") & (rng.random(len(rep)) < 0.7), "flood", None)
            occ.append(pd.DataFrame({"policy_row": rep, "loss_date": ld, "loss_cause": cause,
                                     "battery_mode": battery, "cat_code": ev["cat_code"]}))

    occ = pd.concat(occ, ignore_index=True)
    occ["loss_date"] = pd.to_datetime(occ["loss_date"])
    return occ.sort_values("loss_date").reset_index(drop=True)


# =========================================================================
# CLAIM BUILDER: exposures, lifecycle, reserves, payments, recoveries
# =========================================================================
def _ln(rng, median, sigma):
    return float(rng.lognormal(math.log(median), sigma))


def _inflation(year, rate):
    return (1 + rate) ** (year - BOOK_START.year)


class ClaimBuilder:
    def __init__(self, rng):
        self.rng = rng
        self.claims = []
        self.exposures = []

    # ---- exposure definitions ------------------------------------------------
    def _exposure(self, etype, coverage, claimant, gross_loss, deductible=0.0, limit=None,
                  cycle_median=30, reserve_bias=1.0, total_loss=False, denial=None, subro=0.0, salvage=0.0):
        return {"exposure_type": etype, "coverage_type": coverage, "claimant_type": claimant,
                "gross_loss": gross_loss, "deductible": deductible, "limit": limit,
                "cycle_median": cycle_median, "reserve_bias": reserve_bias, "total_loss": total_loss,
                "denial": denial, "subro_pct": subro, "salvage": salvage}

    def _auto_exposures(self, p, cause, battery_mode, year):
        rng = self.rng
        ba = p["product_code"] == "BusinessAuto"
        cov_coll, cov_comp = ("BACollisionCov", "BAComprehensiveCov") if ba else ("PACollisionCov", "PAComprehensiveCov")
        cov_liab = "BAOwnedLiabilityCov" if ba else "PALiabilityCov"
        cov_med = "BAOwnedMedPayCov" if ba else "PAMedPayCov"
        acv = float(p["vehicle_acv"] or 20000)
        ev = p["vehicle_powertrain"] == "EV"
        ded = float(p["deductible"])
        infl = _inflation(year, 0.06)
        exps, fault, tag = [], "0", None

        if cause in COLLISION_CAUSES:
            if cause == "rearend":
                fault = rng.choice(["thirdparty", "1"], p=[0.6, 0.4])
            elif cause == "vehcollision":
                fault = rng.choice(["1", "thirdparty", "0"], p=[0.5, 0.35, 0.15])
            else:
                fault = "1"
        else:
            fault = "nofault"

        # --- Own vehicle damage ---
        coverage = cov_coll if cause in COLLISION_CAUSES else cov_comp
        repair = {
            "vehcollision": _ln(rng, 4800, 0.75), "rearend": _ln(rng, 3600, 0.7),
            "fixedobjcoll": _ln(rng, 4200, 0.75), "otherobjcoll": _ln(rng, 2400, 0.7),
            "rollover": _ln(rng, 16000, 0.5), "loadingdamage": _ln(rng, 2500, 0.8),
            "animalcollision": _ln(rng, 4500, 0.6), "theftentire": acv,
            "theftparts": _ln(rng, 2300, 0.35) * (1.6 if p["vehicle_powertrain"] == "Hybrid" else 1.0),
            "glassbreakage": _ln(rng, 420, 0.35) + (650 if (p["vehicle_year"] or 0) >= 2020 else 0),  # ADAS recalibration
            "hail": _ln(rng, 3900, 0.5), "vandalism": _ln(rng, 1800, 0.7),
            "firedamage": acv, "waterdamage": acv * rng.uniform(0.6, 1.2), "product": 0.0,
        }[cause] * (infl if cause not in ("theftentire", "firedamage") else 1.0)
        if ev and cause in COLLISION_CAUSES:
            repair *= 1.35   # EV repair premium: ADAS sensors, structural parts, certified shops

        pack_cost = EV_PACK_COST.get(p["vehicle_model"], 18000) * _inflation(year, 0.03)
        pack_damaged = False
        if ev:
            if cause in COLLISION_CAUSES:
                pack_damaged = rng.random() < (0.35 if cause == "otherobjcoll" else 0.14 if cause != "rollover" else 0.4)
                battery_mode = battery_mode or ("debris" if cause == "otherobjcoll" else "collision") if pack_damaged else battery_mode
            if battery_mode in ("thermal", "flood"):
                pack_damaged = True
        if pack_damaged:
            repair += pack_cost * rng.uniform(0.9, 1.25)
            tag = "battery_fault"
        if battery_mode == "cell_failure":
            tag = "battery_fault"

        cycle = {"glassbreakage": 6, "theftentire": 45, "theftparts": 14}.get(cause, 25)
        reserve_bias = 1.0
        if tag == "battery_fault":
            cycle = 75                 # pack sourcing and certified-shop backlog
            reserve_bias = 0.55        # FNOL estimate prices a conventional repair
        total_loss = cause in ("theftentire", "firedamage") or repair > 0.75 * acv
        loss = acv if total_loss else repair
        salvage = 0.0
        if total_loss:
            cycle = max(cycle, 40)
            salvage = acv * (rng.uniform(0.04, 0.10) if pack_damaged else rng.uniform(0.12, 0.25))
        if cause == "theftentire" and rng.random() < 0.45:   # recovered vehicle
            loss = _ln(rng, 3500, 0.6)
            total_loss, salvage = False, 0.0

        denial = None
        if not p["physical_damage_cov"]:
            denial = "coverage_not_purchased"
        elif battery_mode == "cell_failure":
            loss = pack_cost * rng.uniform(0.95, 1.3)
            denial = "mechanical_breakdown_excluded" if rng.random() < 0.9 else None
            cycle, reserve_bias = 35, 1.0
        elif battery_mode == "thermal" and rng.random() < 0.12:
            denial = "mechanical_breakdown_excluded"   # carrier argues internal defect, not fire
        elif cause == "waterdamage" and rng.random() < 0.05:
            denial = "wear_tear_deterioration"
        subro = rng.uniform(0.6, 0.95) if fault == "thirdparty" else 0.0
        exps.append(self._exposure("VehicleDamage", coverage, "insured", loss, ded, acv, cycle,
                                   reserve_bias, total_loss, denial, subro, salvage))

        # --- Third-party & injury exposures ---
        if fault == "1" and cause in ("vehcollision", "rearend", "fixedobjcoll", "loadingdamage"):
            if cause != "fixedobjcoll" or rng.random() < 0.3:
                exps.append(self._exposure("PropertyDamage", cov_liab, "third_party",
                                           _ln(rng, 4200, 0.7) * infl, 0, p["liability_limit"], 30))
            bi_p = {"vehcollision": 0.18, "rearend": 0.24, "loadingdamage": 0.02}.get(cause, 0.05)
            if rng.random() < bi_p * (1.3 if ba else 1.0):
                exps.append(self._exposure("BodilyInjuryDamage", cov_liab, "third_party",
                                           _ln(rng, 15000, 1.05) * _inflation(year, 0.08), 0,
                                           p["liability_limit"], 180, 0.7))
        if cause in ("rollover", "vehcollision", "fixedobjcoll") and rng.random() < (0.35 if cause == "rollover" else 0.08):
            exps.append(self._exposure("MedPay", cov_med, "insured", _ln(rng, 3200, 0.8), 0, 10000, 60))
        if cause == "rollover" and fault == "1" and rng.random() < 0.3:
            exps.append(self._exposure("BodilyInjuryDamage", cov_liab, "third_party",
                                       _ln(rng, 28000, 1.1) * _inflation(year, 0.08), 0,
                                       p["liability_limit"], 220, 0.7))
        if tag == "battery_fault" and battery_mode != "cell_failure":
            # EV quarantine storage & high-voltage-safe towing
            exps.append(self._exposure("TowOnly", "PATowingLaborCov" if not ba else "BATowingLaborCov",
                                       "insured", _ln(rng, 1400, 0.5), 0, None, 20))
        return exps, fault, tag, battery_mode

    def _property_exposures(self, p, cause, cat_code, year):
        rng = self.rng
        hop = p["product_code"] == "HOPHomeowners"
        limit = float(p["property_limit"] or 400000)
        ded = float(p["deductible"])
        infl = _inflation(year, 0.07)
        exps, denial = [], None
        dwell, content, ale, liab_cov = (("Dwelling", "HOPCovA"), ("Content", "HOPCovC"),
                                         ("LivingExpenses", "HOPCovD"), "HOPCovE") if hop else \
                                        (("PropertyDamage", "CPBldgCov"), ("Content", "CPBPPCov"),
                                         ("LossOfUseDamage", "CPBldgBusIncomeCov"), "GLCGLCov")
        scale = 1.0 if hop else 2.4
        if cause == "fall":
            exps.append(self._exposure("BodilyInjuryDamage", liab_cov, "third_party",
                                       _ln(rng, 16000 if hop else 24000, 1.1) * _inflation(year, 0.08),
                                       0, p["liability_limit"], 200, 0.7))
            return exps
        if cause == "waterdamage":
            if cat_code and "HURR" in cat_code:
                denial = "flood_excluded" if rng.random() < 0.35 else None
            elif rng.random() < 0.13:
                denial = "wear_tear_deterioration"   # long-term seepage / gradual leak
            elif rng.random() < 0.03:
                denial = "late_notice"
            main = _ln(rng, 9500, 0.9) * scale
            cycle = 60
        elif cause == "fire":
            main, cycle = _ln(rng, 38000, 1.25) * scale, 150
        elif cause in ("wind", "hail"):
            main, cycle = _ln(rng, 11500, 0.75) * scale, 55
            if cat_code and "HURR" in cat_code:
                main *= 2.2
        elif cause == "burglary":
            main, cycle = 0.0, 40
        elif cause == "mold":
            main, cycle = _ln(rng, 7000, 0.8) * scale, 60
            denial = "excluded_peril" if rng.random() < 0.55 else None
        elif cause == "vandalism":
            main, cycle = _ln(rng, 4500, 0.8) * scale, 35
        else:
            main, cycle = _ln(rng, 6000, 0.8) * scale, 45
        main *= infl
        if main > 0:
            exps.append(self._exposure(dwell[0], dwell[1], "insured", main, ded, limit, cycle,
                                       0.85 if cause == "fire" else 1.0, main > 0.5 * limit, denial))
        content_p = {"fire": 0.75, "burglary": 1.0, "waterdamage": 0.35, "wind": 0.15, "hail": 0.05,
                     "vandalism": 0.3, "mold": 0.2}.get(cause, 0.2)
        if rng.random() < content_p:
            exps.append(self._exposure(content[0], content[1], "insured",
                                       _ln(rng, 4200 if hop else 15000, 0.9) * infl * (3 if cause == "fire" else 1),
                                       0 if main > 0 else ded, limit * 0.5, cycle, 1.0, False, denial))
        ale_p = {"fire": 0.6, "waterdamage": 0.12, "wind": 0.08}.get(cause, 0.0)
        if rng.random() < ale_p:
            exps.append(self._exposure(ale[0], ale[1], "insured",
                                       _ln(rng, 6000 if hop else 25000, 0.8) * infl, 0, limit * 0.2,
                                       cycle + 30, 0.8, False, denial))
        return exps

    def _wc_exposures(self, p, cause, year):
        rng = self.rng
        infl = _inflation(year, 0.06)
        med_median = {"strain": 2400, "fall": 3200, "struck": 2600, "cut": 1100, "caught_in": 6500,
                      "burn_scald": 2200, "motorvehicle": 7000}[cause]
        lost_time_p = {"strain": 0.30, "fall": 0.36, "struck": 0.25, "cut": 0.10, "caught_in": 0.55,
                       "burn_scald": 0.25, "motorvehicle": 0.5}[cause]
        denial = None
        if rng.random() < 0.07:
            denial = rng.choice(["wc_2B_preexisting_condition", "wc_1A_coming_and_going",
                                 "wc_2D_no_medical_evidence"], p=[0.5, 0.2, 0.3])
        lost_time = rng.random() < lost_time_p
        exps = [self._exposure("WCInjuryDamage", "WCWorkersCompCov", "insured",
                               _ln(rng, med_median, 1.0) * infl * (2.5 if lost_time else 1.0), 0, None,
                               220 if lost_time else 45, 0.8 if lost_time else 1.0, False, denial)]
        if lost_time:
            exps.append(self._exposure("LostWages", "WCWorkersCompCov", "insured",
                                       _ln(rng, 16000, 1.05) * infl, 0, None, 300, 0.7, False, denial))
        return exps

    # ---- lifecycle & financials ---------------------------------------------
    def build(self, claim_idx, occ, p):
        rng = self.rng
        product, cause, cat_code = p["product_code"], occ.loss_cause, occ.cat_code
        loss_date = occ.loss_date
        year = loss_date.year
        tag, fault, battery_mode = None, None, occ.battery_mode
        if product in AUTO_LINES:
            exps, fault, tag, battery_mode = self._auto_exposures(p, cause, battery_mode, year)
        elif product == "WorkersComp":
            exps = self._wc_exposures(p, cause, year)
        else:
            exps = self._property_exposures(p, cause, cat_code, year)
        line_map = AUTO_CAUSE_TO_TAG if product in AUTO_LINES else WC_CAUSE_TO_TAG if product == "WorkersComp" else {}
        tag = tag or line_map.get(cause) or CAUSE_TO_TAG.get(cause, cause)

        # Reporting lag
        is_injury = any(e["exposure_type"] in ("BodilyInjuryDamage", "LostWages") for e in exps)
        lag_median = {"AUTO": 1.0, "PR": 3.0, "WC": 4.0}[LOSS_TYPE[product]]
        if is_injury and product != "WorkersComp":
            lag_median = 12.0
        if battery_mode == "cell_failure":
            lag_median = 9.0
        if cat_code:
            lag_median = 6.0
        lag = int(rng.lognormal(math.log(lag_median), 1.1)) if lag_median > 0 else 0
        if cause == "mold" or (cause == "waterdamage" and product != "PersonalAuto" and rng.random() < 0.04):
            lag += int(rng.integers(30, 180))   # gradual losses discovered late
        reported = loss_date + pd.Timedelta(days=lag)
        if reported > AS_OF:
            return None   # incurred but not reported (IBNR) at valuation date

        # SIU referral
        new_policy = int(p["term_number"]) == 1 and (loss_date - p["period_start"]).days < 60
        siu_p = {"theftentire": 0.12, "fire": 0.08, "firedamage": 0.10, "burglary": 0.06}.get(cause, 0.02)
        siu_p += (0.10 if lag > 30 else 0) + (0.08 if new_policy else 0)
        siu = rng.random() < siu_p
        fraud = siu and rng.random() < 0.22

        # Litigation (claim level)
        lit_p = 0.0
        for e in exps:
            if e["exposure_type"] == "BodilyInjuryDamage":
                lit_p = max(lit_p, 0.33)
            elif e["exposure_type"] == "LostWages":
                lit_p = max(lit_p, 0.18)
            elif e["denial"]:
                lit_p = max(lit_p, 0.12)
        lit_p = max(lit_p, 0.015)
        litigated = rng.random() < lit_p

        claim_id = f"CLM-{claim_idx:07d}"
        claim_close = []
        totals = dict(initial_reserve=0.0, paid_loss=0.0, paid_expense=0.0, outstanding=0.0,
                      subro=0.0, salvage=0.0, deductible=0.0)
        any_paid, denial_reasons, exp_rows = False, [], []
        for k, e in enumerate(exps):
            gross = max(e["gross_loss"], 0.0)
            denial = e["denial"] or ("fraud_misrepresentation" if fraud else None)
            limit = e["limit"]
            limit_exhausted = False
            if denial:
                ultimate, ded_applied = 0.0, 0.0
            else:
                ded_applied = min(e["deductible"], gross)
                ultimate = gross - ded_applied
                if litigated and e["claimant_type"] == "third_party":
                    ultimate *= 1.6
                if limit and ultimate > limit:
                    ultimate, limit_exhausted = float(limit), True
            expense = _ln(rng, 180, 0.6) + (0.05 * ultimate)
            if litigated and (e["claimant_type"] == "third_party" or denial or e["exposure_type"] == "LostWages"):
                expense += _ln(rng, 18000, 0.8)
            if siu:
                expense += _ln(rng, 1500, 0.5)

            cycle = e["cycle_median"] * (1.0 if not litigated else 2.8) * (1.3 if siu else 1.0)
            if denial:
                cycle = min(cycle, 45) * (3 if litigated else 1)
            days_open = int(rng.lognormal(math.log(max(cycle, 3)), 0.6))
            close = reported + pd.Timedelta(days=days_open)
            is_closed = close <= AS_OF

            initial = (gross if not denial else gross * 0.5) * e["reserve_bias"] * rng.lognormal(0, 0.3)
            initial = max(round(initial, 2), 250.0) if gross > 0 else 0.0
            if is_closed:
                paid_loss, outstanding, paid_exp = ultimate, 0.0, expense
                if denial:
                    outcome = "fraud" if denial == "fraud_misrepresentation" else "completed"
                else:
                    outcome = "paymentscomplete" if ultimate > 0 else "completed"
            else:
                age = (AS_OF - reported).days
                progress = min(age / max(days_open, 1), 0.95)
                current_estimate = ultimate * rng.lognormal(math.log(max(e["reserve_bias"], 0.5) ** 0.5), 0.2)
                paid_loss = 0.0 if denial else round(ultimate * progress * rng.uniform(0.3, 0.9), 2)
                outstanding = max(current_estimate - paid_loss, 0.0)
                paid_exp = expense * progress
                outcome = None
            # Recoveries
            subro = 0.0
            if e["subro_pct"] and paid_loss > 0 and is_closed and rng.random() < 0.8:
                subro = round((paid_loss + ded_applied) * e["subro_pct"], 2)
            salvage = round(e["salvage"], 2) if is_closed and e["total_loss"] and not denial else 0.0

            if denial:
                denial_reasons.append(denial)
            if ultimate > 0:
                any_paid = True
            claim_close.append(close if is_closed else None)
            totals["initial_reserve"] += initial
            totals["paid_loss"] += paid_loss
            totals["paid_expense"] += paid_exp
            totals["outstanding"] += outstanding
            totals["subro"] += subro
            totals["salvage"] += salvage
            totals["deductible"] += ded_applied
            exp_rows.append({
                "exposure_id": f"{claim_id}-E{k + 1}", "claim_id": claim_id,
                "exposure_type": e["exposure_type"], "coverage_type": e["coverage_type"],
                "claimant_type": e["claimant_type"],
                "exposure_state": "closed" if is_closed else "open",
                "closed_outcome": outcome, "close_date": close.normalize() if is_closed else None,
                "initial_reserve": round(initial, 2), "paid_loss": round(paid_loss, 2),
                "paid_expense": round(paid_exp, 2), "outstanding_reserve": round(outstanding, 2),
                "incurred_loss": round(paid_loss + outstanding, 2),
                "subrogation_recovery": subro, "salvage_recovery": salvage,
                "deductible_applied": round(ded_applied, 2), "coverage_limit": limit,
                "limit_exhausted": int(limit_exhausted), "total_loss_flag": int(e["total_loss"] and not denial),
                "denial_reason": denial,
            })

        all_closed = all(c is not None for c in claim_close)
        close_date = max(claim_close) if all_closed else None
        state = "closed" if all_closed else "open"
        if (AS_OF - reported).days <= 2 and rng.random() < 0.4:
            state, close_date = "draft", None
        # Reopens (supplemental payments / new treatment)
        reopened_date = None
        if state == "closed":
            reopen_p = 0.06 if product == "WorkersComp" else 0.05 if is_injury else 0.025
            if rng.random() < reopen_p:
                reopened_date = close_date + pd.Timedelta(days=int(rng.integers(20, 240)))
                if reopened_date > AS_OF:
                    reopened_date = None
                else:
                    extra = totals["paid_loss"] * rng.uniform(0.08, 0.3)
                    if rng.random() < 0.5:
                        state, close_date = "open", None
                        totals["outstanding"] += extra
                    else:
                        totals["paid_loss"] += extra
                        close_date = reopened_date + pd.Timedelta(days=int(rng.integers(15, 90)))
                        if close_date > AS_OF:
                            state, close_date = "open", None
                            totals["paid_loss"] -= extra
                            totals["outstanding"] += extra

        denial_reason = denial_reasons[0] if denial_reasons and not any_paid else None
        if state == "closed":
            if fraud:
                closed_outcome = "fraud"
            elif any_paid:
                closed_outcome = "paymentscomplete"
            else:
                closed_outcome = "completed"
        else:
            closed_outcome = None
        no_payment_reason = None
        if state == "closed" and not any_paid:
            if denial_reason:
                no_payment_reason = "coverage_denied" if denial_reason != "fraud_misrepresentation" else "fraud"
            elif totals["deductible"] > 0:
                no_payment_reason = "below_deductible"
            else:
                no_payment_reason = "withdrawn"

        incurred_loss = totals["paid_loss"] + totals["outstanding"]
        segment_prefix = {"AUTO": "auto", "PR": "prop", "WC": "wc"}[LOSS_TYPE[product]]
        if product == "WorkersComp":
            segment = "wc_lost_time" if any(e["exposure_type"] == "LostWages" for e in exps) else "wc_med_only"
        elif cause == "glassbreakage":
            segment = "auto_glass"
        elif is_injury or cause == "fall":
            segment = "injury_low" if incurred_loss < 15000 else "injury_mid" if incurred_loss < 75000 else "injury_high"
        else:
            segment = f"{segment_prefix}_" + ("low" if incurred_loss < 5000 else "mid" if incurred_loss < 25000 else "high")

        if siu:
            group = "SIU"
        elif product == "WorkersComp":
            group = "WC Lost Time" if segment == "wc_lost_time" else "WC Medical Only"
        elif product in AUTO_LINES:
            group = ("Auto Injury" if is_injury else
                     "Auto Total Loss" if any(e["total_loss"] for e in exps) else
                     "Auto Fast Track" if incurred_loss < 2500 else "Auto Physical Damage")
        else:
            group = "Liability" if cause == "fall" else "Property Large Loss" if incurred_loss > 50000 else "Property Desk"
        adjuster = f"ADJ-{''.join(w[0] for w in group.split())}-{int(rng.integers(1, ASSIGNED_GROUP_SIZE[group] + 1)):02d}"

        if litigated:
            lit_status = "complete" if state == "closed" else rng.choice(["rep", "suit_filed", "litigated"], p=[0.4, 0.35, 0.25])
        else:
            lit_status = "not_litigated"
        siu_status = ("Investigation_Closed" if state == "closed" else "Under_Investigation") if siu else "No_Referral"

        desc = BATTERY_DESCRIPTIONS[battery_mode] if (tag == "battery_fault" and battery_mode) else \
            str(rng.choice(LOSS_DESCRIPTIONS.get(cause, ["Loss reported"])))
        if tag == "battery_fault" and not battery_mode:
            desc = BATTERY_DESCRIPTIONS["collision"]
        location = p["state"] if rng.random() < 0.96 or product != "PersonalAuto" else str(rng.choice(STATES, p=STATE_P))

        total_incurred = incurred_loss + totals["paid_expense"]
        recoveries = totals["subro"] + totals["salvage"]
        self.claims.append({
            "claim_id": claim_id,
            "claim_number": f"{LOSS_TYPE[product]}-{year}-{claim_idx:07d}",
            "policy_id": p["policy_id"], "policy_number": p["policy_number"],
            "product_code": product, "loss_type": LOSS_TYPE[product],
            "loss_date": loss_date.normalize(), "reported_date": reported.normalize(),
            "report_lag_days": lag, "close_date": close_date.normalize() if close_date is not None else None,
            "reopened_date": reopened_date.normalize() if reopened_date is not None else None,
            "claim_state": state, "closed_outcome": closed_outcome,
            "loss_cause": cause, "risk_category_tag": tag, "loss_description": desc,
            "location": location, "cat_code": cat_code, "fault_rating": fault,
            "claim_segment": segment, "assigned_group": group, "adjuster_id": adjuster,
            "exposure_count": len(exps),
            "total_loss_flag": int(any(r["total_loss_flag"] for r in exp_rows)),
            "coverage_denied_flag": int(denial_reason is not None and denial_reason != "fraud_misrepresentation"),
            "denial_reason": denial_reason, "no_payment_reason": no_payment_reason,
            "litigation_flag": int(litigated), "litigation_status": lit_status,
            "siu_status": siu_status,
            "initial_reserve": round(totals["initial_reserve"], 2),
            "paid_loss": round(totals["paid_loss"], 2),
            "paid_expense": round(totals["paid_expense"], 2),
            "outstanding_reserve": round(totals["outstanding"], 2),
            "claim_amount": round(incurred_loss, 2),       # gross incurred loss (paid + case reserve)
            "total_incurred": round(total_incurred, 2),    # incl. allocated expense (ALAE)
            "subrogation_amount": round(totals["subro"], 2),
            "salvage_amount": round(totals["salvage"], 2),
            "net_incurred": round(total_incurred - recoveries, 2),
            "deductible_applied": round(totals["deductible"], 2),
        })
        self.exposures.extend(exp_rows)
        return claim_id


def generate_claims(rng, policies, occ):
    builder = ClaimBuilder(rng)
    pol_records = policies.to_dict("records")
    idx = 0
    for o in occ.itertuples(index=False):
        if builder.build(idx, o, pol_records[o.policy_row]) is not None:
            idx += 1
    claims = pd.DataFrame(builder.claims)
    exposures = pd.DataFrame(builder.exposures)
    return claims, exposures


# =========================================================================
# Integrity checks (10_SYNTHETIC_DATA_GENERATION_RULES.md §4 + financial rules)
# =========================================================================
def validate_integrity(policies: pd.DataFrame, claims: pd.DataFrame, exposures: pd.DataFrame) -> None:
    lookup = policies.set_index("policy_id")
    ps = lookup.loc[claims["policy_id"], "period_start"].to_numpy()
    pe = lookup.loc[claims["policy_id"], "earned_through"].to_numpy()
    ld = claims["loss_date"].to_numpy()
    checks = {
        "loss_date outside policy period": ((ld < ps) | (ld > pe)).sum(),
        "reported_date before loss_date": (claims["reported_date"] < claims["loss_date"]).sum(),
        "dates after valuation date": ((claims["reported_date"] > AS_OF) | (claims["close_date"] > AS_OF)).sum(),
        "closed claim without close_date": ((claims["claim_state"] == "closed") & claims["close_date"].isna()).sum(),
        "closed claim with open reserve": ((claims["claim_state"] == "closed") & (claims["outstanding_reserve"] > 0.01)).sum(),
        "negative financials": (claims[["paid_loss", "paid_expense", "outstanding_reserve"]] < 0).any(axis=1).sum(),
        "incurred != paid + reserve": ((claims["claim_amount"] - claims["paid_loss"] - claims["outstanding_reserve"]).abs() > 0.05).sum(),
        "EV battery tag on non-EV": (claims["risk_category_tag"].eq("battery_fault")
                                     & lookup.loc[claims["policy_id"], "vehicle_powertrain"].ne("EV").to_numpy()).sum(),
        "orphan exposures": (~exposures["claim_id"].isin(claims["claim_id"])).sum(),
    }
    bad = {k: int(v) for k, v in checks.items() if v}
    if bad:
        raise ValueError(f"INTEGRITY VIOLATIONS: {bad}")
    print("[OK]  All integrity checks passed:", ", ".join(checks))


# =========================================================================
# Main entry-point
# =========================================================================
def main() -> None:
    rng = np.random.default_rng(SEED)
    print("=" * 72)
    print("  Roundtable -- Synthetic Insurance Data Generator")
    print(f"  Guidewire PolicyCenter + ClaimCenter (schema v10.2.1), valued {AS_OF.date()}")
    print("=" * 72)

    print(f"\n[1/5] Writing {N_NEW_BUSINESS:,} new-business policies with renewals ...")
    policies = generate_policy_df(rng)
    print(f"      {len(policies):,} policy periods")
    print("[2/5] Computing earned exposure by calendar year ...")
    earned = build_earned_exposure(policies)
    print("[3/5] Simulating loss occurrences from exposure ...")
    occ = generate_occurrences(rng, policies)
    print(f"      {len(occ):,} occurrences")
    print("[4/5] Building claims, exposures and financials ...")
    claims, exposures = generate_claims(rng, policies, occ)
    print(f"      {len(claims):,} reported claims ({len(occ) - len(claims):,} IBNR), {len(exposures):,} exposures")
    validate_integrity(policies, claims, exposures)

    print(f"[5/5] Writing to SQLite -> {DB_PATH}")
    date_cols = {"policies": ["period_start", "period_end", "cancel_date", "earned_through"],
                 "claims": ["loss_date", "reported_date", "close_date", "reopened_date"],
                 "exposures": ["close_date"]}
    frames = {"policies": policies, "earned_exposure": earned, "claims": claims, "exposures": exposures}
    with sqlite3.connect(str(DB_PATH)) as conn:
        for name, df in frames.items():
            df = df.copy()
            for col in date_cols.get(name, []):
                df[col] = pd.to_datetime(df[col]).dt.strftime("%Y-%m-%d")
            df.to_sql(name, conn, if_exists="replace", index=False, chunksize=5000)
        conn.executescript("""
            CREATE INDEX IF NOT EXISTS ix_claims_tag ON claims(risk_category_tag);
            CREATE INDEX IF NOT EXISTS ix_claims_policy ON claims(policy_id);
            CREATE INDEX IF NOT EXISTS ix_exposures_claim ON exposures(claim_id);
            CREATE INDEX IF NOT EXISTS ix_earned_year ON earned_exposure(calendar_year, product_code);
        """)

    # ── Verification summary ────────────────────────────────────────────
    print("\n" + "=" * 72)
    print("  VERIFICATION -- recomputed from generated data")
    print("=" * 72)
    claims["ay"] = pd.to_datetime(claims["loss_date"]).dt.year
    lr = claims.groupby("product_code")["total_incurred"].sum() / earned.groupby("product_code")["earned_premium"].sum()
    print("\n  Loss + ALAE ratio by line:", {k: f"{v:.0%}" for k, v in lr.items()})
    ev_years = earned[earned["vehicle_powertrain"] == "EV"].groupby("calendar_year")["earned_exposure"].sum()
    bf = claims[claims["risk_category_tag"] == "battery_fault"].groupby("ay").size()
    print("  battery_fault claims / 1,000 EV vehicle-years by AY:",
          {int(y): f"{bf.get(y, 0)} claims, {1000 * bf.get(y, 0) / ev_years[y]:.1f}" for y in ev_years.index})
    print("  Median gross incurred by tag:",
          claims[claims["claim_amount"] > 0].groupby("risk_category_tag")["claim_amount"].median().round(0).to_dict())
    print(f"\n  POLICY PERIODS: {len(policies):,}   CLAIMS: {len(claims):,}   EXPOSURES: {len(exposures):,}")
    print("=" * 72)


if __name__ == "__main__":
    main()
