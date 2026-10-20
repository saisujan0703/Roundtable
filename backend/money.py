"""
Rupee formatting
================
Roundtable reports amounts in Indian rupees with Indian digit grouping (lakh = 1,00,000; crore = 1,00,00,000):

    inr(1234567)          -> "₹12,34,567"
    inr(1234.5, paise=True) -> "₹1,234.50"
    inr_short(1234567)    -> "₹12.35 lakh"
    inr_short(98765432)   -> "₹9.88 crore"

backend.verification reads all of these back (₹, Rs, INR, Indian grouping, lakh and crore).
frontend/money.py is the same code for the Streamlit app, which does not import the backend.
"""
from __future__ import annotations

from typing import Optional

LAKH, CRORE = 1e5, 1e7


def group(n: int) -> str:
    """Indian digit grouping of a whole number: 1234567 -> "12,34,567"."""
    digits = str(abs(n))
    rest, tail = digits[:-3], digits[-3:]
    head = []
    while len(rest) > 2:
        head.insert(0, rest[-2:])
        rest = rest[:-2]
    if rest:
        head.insert(0, rest)
    return ("-" if n < 0 else "") + ",".join(head + [tail])


def inr(v: Optional[float], paise: bool = False, na: str = "n/a") -> str:
    """₹ with Indian grouping; *paise* adds two decimals."""
    if v is None:
        return na
    if not paise:
        n = round(v)
        return ("-" if n < 0 else "") + "₹" + group(abs(n))
    whole, frac = divmod(round(abs(v) * 100), 100)
    return ("-" if v < 0 else "") + f"₹{group(whole)}.{frac:02d}"


def inr_short(v: Optional[float], na: str = "n/a") -> str:
    """Compact rupees for headline figures: crore from 1 crore, lakh from 1 lakh, else the full amount."""
    if v is None:
        return na
    a = abs(v)
    sign = "-" if v < 0 else ""
    if a >= CRORE:
        return f"{sign}₹{a / CRORE:,.2f} crore"
    if a >= LAKH:
        return f"{sign}₹{a / LAKH:.2f} lakh"
    return inr(v)
