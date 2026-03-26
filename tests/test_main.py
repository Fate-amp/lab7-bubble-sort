import pytest

from main import bubble_sort


@pytest.fixture
def sample_unsorted() -> list[int]:
    """A reusable list for basic bubble sort verification."""
    return [64, 34, 25, 12, 22, 11, 90]


def test_bubble_sort_unsorted_list(sample_unsorted: list[int]) -> None:
    result = bubble_sort(sample_unsorted.copy())
    assert result == [11, 12, 22, 25, 34, 64, 90]


def test_bubble_sort_already_sorted_list() -> None:
    result = bubble_sort([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]


def test_bubble_sort_reverse_sorted_list() -> None:
    result = bubble_sort([5, 4, 3, 2, 1])
    assert result == [1, 2, 3, 4, 5]


def test_bubble_sort_single_element() -> None:
    result = bubble_sort([42])
    assert result == [42]


def test_bubble_sort_empty_list() -> None:
    result = bubble_sort([])
    assert result == []
