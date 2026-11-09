"""Hidden checks for B1 (discount rounding half up). Never shown to the agent."""
from decimal import Decimal

from shop.pricing import apply_discount


def test_b1_rounds_half_up_small_amount():
    # 33.35 * 0.90 = 30.015 -> 30.02
    assert apply_discount(Decimal("33.35"), Decimal("10")) == Decimal("30.02")


def test_b1_rounds_half_up_other_percent():
    # 10.10 * 0.85 = 8.585 -> 8.59
    assert apply_discount(Decimal("10.10"), Decimal("15")) == Decimal("8.59")


def test_b1_exact_amount_unchanged():
    assert apply_discount(Decimal("200.00"), Decimal("15")) == Decimal("170.00")
