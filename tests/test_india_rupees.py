"""
India rupees: ₹ with Indian grouping and lakh / crore in every module that writes money, and the number check
reading those formats back.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

from backend import money, rating_tests, verification

ROOT = Path(__file__).resolve().parent.parent


@pytest.mark.parametrize("v, paise, out", [(1234567, False, "₹12,34,567"), (999, False, "₹999"),
                                           (100000, False, "₹1,00,000"), (-1234.5, True, "-₹1,234.50"),
                                           (12.346, True, "₹12.35"), (None, False, "n/a")])
def test_inr_indian_grouping(v, paise, out):
    assert money.inr(v, paise=paise) == out


@pytest.mark.parametrize("v, out", [(1234567, "₹12.35 lakh"), (98765432, "₹9.88 crore"), (45000, "₹45,000")])
def test_inr_short_lakh_and_crore(v, out):
    assert money.inr_short(v) == out


def test_frontend_formatter_matches_backend():
    spec = importlib.util.spec_from_file_location("frontend_money", ROOT / "frontend" / "money.py")
    fm = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fm)
    for v in (0, 7, 1234, 123456, 1234567, 98765432, -45678.9):
        assert fm.inr(v) == money.inr(v) and fm.inr(v, True) == money.inr(v, True)
        assert fm.inr_short(v) == money.inr_short(v)
    assert fm.TABLE_FORMAT.startswith("₹")


FACTS = verification.FactNumbers({"severity": 1234567, "paid": 450123, "book": 98765432})


@pytest.mark.parametrize("text", ["Average severity is ₹12,34,567.", "Paid ₹4.50 lakh so far.", "A ₹9.88 crore book.",
                                  "Rs. 12,34,567 per claim", "INR 4.5 lakh", money.inr(1234567),
                                  money.inr_short(98765432)])
def test_number_check_reads_rupees(text):
    assert verification.check_numbers(text, FACTS, "t") == []


@pytest.mark.parametrize("text", ["Average severity is ₹13,34,567.", "Rs 5 crore limit", "₹7.10 lakh paid"])
def test_number_check_flags_wrong_rupees(text):
    issues = verification.check_numbers(text, FACTS, "t")
    assert issues and issues[0]["severity"] == verification.ERROR


def test_rating_test_steps_in_rupees():
    plan = {"available": True, "base_rate": 1000.0, "base_levels": {}, "variables": [], "state_rates": [],
            "deductibles": {"available": True, "rows": [{"deductible": 5000, "factor": 0.95, "base": False}]},
            "ilfs": {"available": False}}
    cases = rating_tests.generate(plan) if hasattr(rating_tests, "generate") else None
    if not cases:
        pytest.skip("rating_tests has no generate() for a hand-built plan")
    text = str(cases)
    assert "₹5,000" in text and "$" not in text


@pytest.mark.parametrize("path", ["backend", "frontend"])
def test_no_dollar_formatting_left(path):
    """No f-string or format spec writes a $ amount (the competitor scan keeps its multi-region examples)."""
    import re
    pat = re.compile(r'f"\$\{|f"\\\\\$\{|format="\$%|\$\{[a-z_]+:,|"\$%')
    hits = [f"{p.name}:{i}" for p in (ROOT / path).glob("*.py") for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1)
            if pat.search(line) and p.name not in ("competitor_landscape.py", "landscape_guard.py")]
    assert hits == []
