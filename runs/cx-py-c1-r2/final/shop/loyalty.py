from decimal import Decimal


def points_for(total: Decimal, *, first_purchase: bool = False) -> int:
    """Return the loyalty points earned for an order total."""
    if total < 0:
        raise ValueError("total must be >= 0")
    return int(total // 10) + (5 if first_purchase else 0)
