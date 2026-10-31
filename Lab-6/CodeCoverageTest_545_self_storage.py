import pytest
from self_storage import rent_due, access_allowed, payment_status


def test_rent_rejects_unknown_size():
    with pytest.raises(ValueError):
        rent_due("extra-large", 2, False, False)


def test_rent_rejects_negative_months():
    with pytest.raises(ValueError):
        rent_due("small", -1, False, False)


def test_rent_within_deposit_period():
    assert rent_due("small", 1, False, False) == 0


def test_member_gets_extra_covered_month_for_small_unit():
    assert rent_due("small", 3, False, True) == 80


def test_large_member_does_not_get_extra_covered_month():
    assert rent_due("large", 4, False, True) == 80


def test_climate_controlled_rent():
    assert rent_due("medium", 4, True, False) == 240


def test_long_non_climate_stay_discount():
    assert rent_due("small", 8, False, False) == 490


def test_long_climate_stay_discount():
    assert rent_due("small", 8, True, False) == 735


def test_owner_allowed_with_four_visitors():
    assert access_allowed(23, 4, True) is True


def test_owner_denied_with_more_than_four_visitors():
    assert access_allowed(12, 5, True) is False


def test_non_owner_allowed_during_open_hours():
    assert access_allowed(12, 2, False) is True


def test_non_owner_denied_before_opening():
    assert access_allowed(5, 1, False) is False


def test_non_owner_denied_after_closing():
    assert access_allowed(23, 1, False) is False


def test_non_owner_denied_too_many_visitors():
    assert access_allowed(12, 3, False) is False


def test_payment_current_with_autopay():
    assert payment_status(0, True, False) == "current"


def test_payment_current_without_autopay():
    assert payment_status(5, False, False) == "current"


def test_payment_grace_period():
    assert payment_status(-1, False, False) == "grace"


def test_payment_lien_status():
    assert payment_status(-11, False, False) == "lien"


def test_prior_late_payment_increases_cutoff():
    assert payment_status(10, False, True) == "grace"
