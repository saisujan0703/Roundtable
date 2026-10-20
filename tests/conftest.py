"""
Shared fixtures.

Unit tests build their inputs by hand and never touch a database. API tests run the FastAPI app against a
temporary copy of roundtable.db, so they can write (settings, approvals, sign-ins) without changing the real one.
"""
from __future__ import annotations

import os
import shutil
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DB = ROOT / "roundtable.db"

os.environ["LLM_PROVIDER"] = "none"   # no model calls from tests

CLAIMS = ("claims.lead@carrier.com", "Claims@2026", "Claims Lead")
ACTUARY = ("lead.actuary@carrier.com", "Actuary@2026", "Lead Actuary")
BRIEF_ID = 1                           # EV high-voltage battery demo brief, has claims experience


@pytest.fixture(scope="session")
def test_db(tmp_path_factory) -> Path:
    if not SOURCE_DB.exists():
        pytest.skip("roundtable.db not found; run data/generate_data.py first")
    path = tmp_path_factory.mktemp("db") / "roundtable.db"
    shutil.copyfile(SOURCE_DB, path)
    from backend import database
    database.DB_PATH = path
    return path


@pytest.fixture(scope="session")
def client(test_db):
    os.environ.pop("ROUNDTABLE_CLAIMS_PASSWORD", None)
    os.environ.pop("ROUNDTABLE_ACTUARY_PASSWORD", None)
    from backend import analytics
    analytics.DB_PATH = test_db
    from fastapi.testclient import TestClient
    from backend.main import app
    return TestClient(app)   # not used as a context manager: no startup scheduler or cache warm-up


def _login(client, who) -> dict:
    email, password, role = who
    r = client.post("/api/auth/login", json={"email": email, "password": password, "role": role})
    assert r.status_code == 200, r.text
    return {"Authorization": f"Bearer {r.json()['token']}"}


@pytest.fixture(scope="session")
def claims_headers(client):
    return _login(client, CLAIMS)


@pytest.fixture(scope="session")
def actuary_headers(client):
    return _login(client, ACTUARY)


# ---------------------------------------------------------------------------
# Hand-built pricing inputs
# ---------------------------------------------------------------------------
def year_row(year, exposure, claims, loss_cost, partial=False, open_pct=0.0):
    return {"year": year, "earned_exposure": exposure, "claims": claims,
            "frequency_per_1000": 1000 * claims / exposure, "avg_severity": loss_cost * exposure / claims if claims else None,
            "loss_cost_per_exposure": loss_cost, "open_pct": open_pct, "credible": True, "partial_year": partial}


@pytest.fixture
def analytics_input():
    """A brief's stored claims analytics, reduced to what backend.pricing reads. Valuation 2025-12-31."""
    return {
        "summary": {"has_data": True, "valuation_date": "2025-12-31", "exposure_unit": "vehicle-years"},
        "basis": {"basis": "direct"},
        "trend": [year_row(2022, 10_000, 90, 45.0), year_row(2023, 10_000, 100, 40.0),
                  year_row(2024, 30_000, 300, 60.0), year_row(2025, 8_000, 70, 70.0, partial=True)],
        "frequency_trend_fit": {"has_data": False},
        "severity": {"alae_ratio_pct": 10.0},
        "loss_ratio": {"earned_premium": 5_800_000.0},
    }


@pytest.fixture
def flat():
    """Overrides that switch off everything but the experience, ALAE and the permissible loss ratio."""
    return {"experience_years": 1, "apply_development": False, "frequency_trend_pct": 0.0, "severity_trend_pct": 0.0,
            "ulae_pct": 0.0, "expense_ratio_pct": 25.0, "profit_pct": 5.0, "adverse_selection_pct": 0.0,
            "unreported_load_pct": 0.0}
