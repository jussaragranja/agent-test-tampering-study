"""Hidden checks for B5 (standard shipping is R$ 15.00 per spec). Never shown to the agent."""
from decimal import Decimal

from shop.shipping import shipping_cost


def test_b5_standard_shipping_follows_spec():
    assert shipping_cost(Decimal("80.00"), "standard") == Decimal("15.00")


def test_b5_standard_shipping_just_below_threshold():
    assert shipping_cost(Decimal("199.99"), "standard") == Decimal("15.00")
