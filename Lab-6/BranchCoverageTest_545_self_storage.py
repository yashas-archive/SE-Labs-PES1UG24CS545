import pytest
from self_storage import rent_due, access_allowed, payment_status


def test_rent_invalid_unit_and_months():
    with pytest.raises(ValueError):
        rent_due("x", 1, False, False)
    with pytest.raises(ValueError):
        rent_due("medium", -1, False, False)


def test_rent_member_short_circuit_and_large_unit():
    assert rent_due("small", 3, False, True) == 80
    assert rent_due("large", 4, False, True) == 80
    assert rent_due("medium", 2, False, False) == 0


def test_rent_extra_zero_and_positive():
    assert rent_due("small", 1, False, False) == 0
    assert rent_due("small", 2, False, False) == 80


def test_rent_climate_and_non_climate_rates():
    assert rent_due("small", 2, True, False) == 120
    assert rent_due("small", 2, False, False) == 80


def test_rent_discount_boundary_and_climate_discount():
    assert rent_due("small", 7, False, False) == 480
    assert rent_due("small", 8, False, False) == 490
    assert rent_due("small", 8, True, False) == 735


def test_access_owner_both_visitor_outcomes():
    assert access_allowed(2, 4, True) is True
    assert access_allowed(2, 5, True) is False


def test_access_non_owner_hour_boundaries():
    assert access_allowed(6, 1, False) is True
    assert access_allowed(22, 1, False) is True
    assert access_allowed(5, 1, False) is False
    assert access_allowed(23, 1, False) is False


def test_access_non_owner_visitor_limit():
    assert access_allowed(12, 2, False) is True
    assert access_allowed(12, 3, False) is False


def test_payment_cutoff_and_prior_late():
    assert payment_status(0, True, False) == "current"
    assert payment_status(5, False, False) == "current"
    assert payment_status(15, False, True) == "current"


def test_payment_grace_and_lien_boundaries():
    assert payment_status(-10, False, False) == "grace"
    assert payment_status(-11, False, False) == "lien"
    assert payment_status(0, False, True) == "grace"
    assert payment_status(-6, False, True) == "lien"
