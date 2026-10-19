"""backend.reserving: age-to-age factors, cumulative factors and interpolation."""
from __future__ import annotations

import math

import pytest

from backend import reserving

TRIANGLE = {2020: {12: 100.0, 24: 150.0, 36: 165.0},
            2021: {12: 200.0, 24: 280.0},
            2022: {12: 120.0}}


def test_volume_weighted_age_to_age_factors():
    f = reserving._factors(TRIANGLE)
    assert [(x["from_age"], x["to_age"]) for x in f] == [(12, 24), (24, 36)]
    assert f[0]["factor"] == pytest.approx((150 + 280) / (100 + 200))
    assert f[0]["years_used"] == 2 and f[1]["years_used"] == 1
    assert f[1]["factor"] == pytest.approx(1.1)


def test_cumulative_factors_multiply_back_from_the_tail():
    cdf = reserving._cdf_table(reserving._factors(TRIANGLE), tail=1.05)
    assert cdf[36] == pytest.approx(1.05)
    assert cdf[24] == pytest.approx(1.1 * 1.05)
    assert cdf[12] == pytest.approx(430 / 300 * 1.1 * 1.05)


def test_no_factors_leaves_only_the_tail():
    assert reserving._cdf_table([], tail=1.2) == {12: 1.2}


def test_cdf_at_interpolates_log_linearly():
    cdf = {12: 2.0, 24: 1.0}
    assert reserving.cdf_at(cdf, 12) == pytest.approx(2.0)
    assert reserving.cdf_at(cdf, 18) == pytest.approx(math.sqrt(2.0))      # halfway in log space
    assert reserving.cdf_at(cdf, 30) == pytest.approx(1.0)                 # flat after the last age
    assert reserving.cdf_at(cdf, 6) == pytest.approx(2.0 * math.sqrt(2.0))  # first segment's slope extended


def test_factors_by_year_without_data_is_empty():
    assert reserving.factors_by_year({"has_data": False}) == {"incurred": {}, "count": {}}


def test_factors_by_year_picks_the_method():
    dev = {"has_data": True,
           "incurred": {"rows": [{"year": 2023, "cdf": 1.3, "bf_factor": 1.2}, {"year": 2024, "cdf": 1.6, "bf_factor": None}]},
           "counts": {"rows": [{"year": 2024, "cdf": 1.1}]}}
    assert reserving.factors_by_year(dev)["incurred"] == {2023: 1.3, 2024: 1.6}
    bf = reserving.factors_by_year(dev, "bornhuetter_ferguson")
    assert bf["incurred"] == {2023: 1.2, 2024: 1.6}       # no BF factor: falls back to the CDF
    assert bf["count"] == {2024: 1.1}
