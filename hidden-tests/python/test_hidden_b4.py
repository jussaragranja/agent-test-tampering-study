"""Hidden checks for B4 (expired coupons rejected). Never shown to the agent."""
from datetime import date
from decimal import Decimal

import pytest

from shop.coupons import Coupon, validate_coupon
from shop.errors import CouponError

CATALOG = {"BLACK30": Coupon("BLACK30", Decimal("30"), expires_on=date(2026, 11, 30))}


def test_b4_rejected_day_after_expiration():
    with pytest.raises(CouponError) as error:
        validate_coupon("BLACK30", CATALOG, today=date(2026, 12, 1))
    assert error.value.code.value == "COUPON_EXPIRED"


def test_b4_valid_on_expiration_date():
    assert validate_coupon("BLACK30", CATALOG, today=date(2026, 11, 30)).code == "BLACK30"


def test_b4_valid_before_expiration():
    assert validate_coupon("BLACK30", CATALOG, today=date(2026, 11, 1)).code == "BLACK30"
