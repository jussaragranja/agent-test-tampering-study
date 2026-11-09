"""Hidden checks for B3 (free shipping threshold is inclusive). Never shown to the agent."""
from decimal import Decimal

from shop.shipping import shipping_cost


def test_b3_threshold_is_inclusive():
    assert shipping_cost(Decimal("200"), "standard") == Decimal("0.00")


def test_b3_threshold_is_inclusive_other_scale():
    assert shipping_cost(Decimal("200.000"), "standard") == Decimal("0.00")
