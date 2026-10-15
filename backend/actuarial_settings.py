"""
Company actuarial settings
==========================
Company-level assumptions that replace the placeholder defaults in backend.pricing and backend.business_plan,
each with the source the Lead Actuary cites (expense study, ULAE study, capital plan, ...). Stored once in the
actuarial_settings table; every brief starts from them and can still override per product.

Expense ratio = commission + premium tax + other acquisition + general expense (the components a filing exhibits).
Profit & contingencies is DERIVED from the target return on equity (ASOP No. 30 style return-on-capital model):
    after-tax return = (underwriting profit + investment yield x (surplus + loss reserves)) x (1 - tax)
    => underwriting profit (% of premium) = ROE x S / (1 - tax) - yield x (S + R)
with S = 1 / premium-to-surplus and R = loss reserves per unit of premium.
"""
from __future__ import annotations

import json
from datetime import datetime
from typing import Any, Dict, Optional

from backend.database import get_connection

FIELDS = {  # key: (label, default, low, high)
    "commission_pct": ("Commission %", 12.0, 0.0, 40.0),
    "premium_tax_pct": ("Premium tax & fees %", 2.5, 0.0, 10.0),
    "other_acquisition_pct": ("Other acquisition %", 4.5, 0.0, 30.0),
    "general_expense_pct": ("General expense %", 6.0, 0.0, 30.0),
    "ulae_pct": ("ULAE % of loss & ALAE", 5.0, 0.0, 20.0),
    "target_roe_pct": ("Target after-tax return on equity %", 10.0, 0.0, 30.0),
    "premium_to_surplus": ("Premium-to-surplus ratio", 2.0, 0.5, 6.0),
    "loss_reserves_to_premium": ("Loss reserves per $ of premium", 0.6, 0.0, 5.0),
    "investment_yield_pct": ("Investment yield %", 3.0, 0.0, 15.0),
    "tax_rate_pct": ("Tax rate %", 21.0, 0.0, 50.0),
    "severity_trend_pct": ("Default severity trend %/yr", 5.0, -10.0, 25.0),
    "unreported_load_pct": ("Default unreported-demand load %", 25.0, 0.0, 200.0),
    "adverse_selection_pct": ("Default adverse-selection load %", 10.0, -20.0, 100.0),
}


def init_table() -> None:
    with get_connection() as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS actuarial_settings (id INTEGER PRIMARY KEY CHECK (id = 1), "
                     "settings_json TEXT NOT NULL, updated_by TEXT, updated_at TEXT)")
        conn.commit()


def load() -> Dict[str, Any]:
    """{"values": {key: value}, "sources": {key: text}, "updated_by", "updated_at"} — values only for keys set."""
    try:
        with get_connection() as conn:
            row = conn.execute("SELECT settings_json, updated_by, updated_at FROM actuarial_settings WHERE id = 1").fetchone()
    except Exception:
        row = None
    data = json.loads(row["settings_json"]) if row else {"values": {}, "sources": {}}
    data.setdefault("values", {})
    data.setdefault("sources", {})
    data["updated_by"], data["updated_at"] = (row["updated_by"], row["updated_at"]) if row else (None, None)
    return data


def save(values: Dict[str, Any], sources: Dict[str, str], by: str) -> Dict[str, Any]:
    clean_v, clean_s = {}, {}
    for k, v in values.items():
        if k not in FIELDS or v is None:
            continue
        _, _, lo, hi = FIELDS[k]
        v = float(v)
        if not lo <= v <= hi:
            raise ValueError(f"{FIELDS[k][0]} must be between {lo} and {hi}.")
        src = (sources.get(k) or "").strip()[:300]
        if not src:
            raise ValueError(f"Cite the source for {FIELDS[k][0]} (e.g. '2025 expense study, Exhibit 3').")
        clean_v[k], clean_s[k] = v, src
    with get_connection() as conn:
        conn.execute("INSERT INTO actuarial_settings (id, settings_json, updated_by, updated_at) VALUES (1, ?, ?, ?) "
                     "ON CONFLICT(id) DO UPDATE SET settings_json = excluded.settings_json, "
                     "updated_by = excluded.updated_by, updated_at = excluded.updated_at",
                     (json.dumps({"values": clean_v, "sources": clean_s}), by[:120], datetime.utcnow().isoformat()))
        conn.commit()
    return load()


def value(settings: Dict[str, Any], key: str) -> float:
    return float(settings["values"].get(key, FIELDS[key][1]))


def expense_ratio_pct(settings: Dict[str, Any]) -> float:
    return sum(value(settings, k) for k in ("commission_pct", "premium_tax_pct", "other_acquisition_pct",
                                            "general_expense_pct"))


def profit_pct(settings: Dict[str, Any]) -> float:
    """Underwriting profit provision needed for the target ROE (see module docstring)."""
    s = 1 / value(settings, "premium_to_surplus")
    r = value(settings, "loss_reserves_to_premium")
    roe, y, t = (value(settings, k) / 100 for k in ("target_roe_pct", "investment_yield_pct", "tax_rate_pct"))
    return round(100 * (roe * s / (1 - t) - y * (s + r)), 2)


def pricing_defaults(settings: Dict[str, Any]) -> Dict[str, Any]:
    """The pricing assumptions the company settings imply (only for what is set, so placeholders stay visible)."""
    v = settings["values"]
    out: Dict[str, Any] = {}
    if any(k in v for k in ("commission_pct", "premium_tax_pct", "other_acquisition_pct", "general_expense_pct")):
        out["expense_ratio_pct"] = round(expense_ratio_pct(settings), 2)
    if any(k in v for k in ("target_roe_pct", "premium_to_surplus", "loss_reserves_to_premium",
                            "investment_yield_pct", "tax_rate_pct")):
        out["profit_pct"] = profit_pct(settings)
    for k in ("ulae_pct", "severity_trend_pct", "unreported_load_pct", "adverse_selection_pct"):
        if k in v:
            out[k] = v[k]
    return out


def business_plan_defaults(settings: Dict[str, Any]) -> Dict[str, Any]:
    v = settings["values"]
    return {k: v[k] for k in ("premium_to_surplus", "investment_yield_pct", "tax_rate_pct") if k in v}


def provenance(settings: Dict[str, Any]) -> Dict[str, str]:
    """Where each pricing assumption's default comes from: a cited company setting or a placeholder."""
    src = settings["sources"]
    v = settings["values"]

    def cite(keys):
        got = [f"{FIELDS[k][0]}: {src[k]}" for k in keys if k in v]
        return "; ".join(got) if got else None

    return {k: s for k, s in {
        "expense_ratio_pct": cite(["commission_pct", "premium_tax_pct", "other_acquisition_pct", "general_expense_pct"]),
        "profit_pct": (f"derived from target ROE ({cite(['target_roe_pct', 'premium_to_surplus', 'loss_reserves_to_premium', 'investment_yield_pct', 'tax_rate_pct'])})"
                       if cite(["target_roe_pct", "premium_to_surplus", "loss_reserves_to_premium",
                                "investment_yield_pct", "tax_rate_pct"]) else None),
        "ulae_pct": cite(["ulae_pct"]), "severity_trend_pct": cite(["severity_trend_pct"]),
        "unreported_load_pct": cite(["unreported_load_pct"]), "adverse_selection_pct": cite(["adverse_selection_pct"]),
    }.items() if s}
