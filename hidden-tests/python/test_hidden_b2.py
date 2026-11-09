"""Hidden checks for B2 (1-based pagination). Never shown to the agent."""
from shop.pagination import paginate


def test_b2_second_page_custom_size():
    assert paginate(list(range(1, 31)), page=2, page_size=5) == [6, 7, 8, 9, 10]


def test_b2_first_page_small_size():
    assert paginate(["a", "b", "c", "d"], page=1, page_size=3) == ["a", "b", "c"]


def test_b2_partial_last_page():
    assert paginate(list(range(1, 13)), page=2) == [11, 12]
