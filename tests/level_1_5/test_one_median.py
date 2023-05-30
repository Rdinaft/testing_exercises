import pytest
from functions.level_1_5.one_median import get_median_value


def test__get_median_value__four_numbers():
    with pytest.raises(IndexError):
        get_median_value([1, -3, 5, 7])


def test__get_median_value__one_number():
    with pytest.raises(IndexError):
        assert get_median_value([1]) == 1


def test__get_median_value__two_numbers():
    with pytest.raises(IndexError):
        assert get_median_value([-1, 3]) == 3


@pytest.mark.parametrize(
    "items, expected_result",
    [
        ([1, 3, 5, 9, 7, 5], 6),
        ([-1, 0, 2, -5, 5, 7], 6),
        ([-5, -3, -2, -3, -1, -7], -4),
        ([0, 0, 0, 1, 1, 2], 1),
        ([1, 3, 5, 5, 7], 5),
        ([7, 3, 1], 1),
        ([-1, 0, 1, 3, -5, 5, 7], -5),
        ([-5, -3, -2, -1, -7], -1),
        ([], None),
        ({}, None),
        ((), None),
    ],
    ids=[
        "even_positive",
        "even_mixed",
        "even_negative",
        "even",
        "odd_positive",
        "odd_amount_three",
        "odd_mixed",
        "odd_negative",
        "empty_list_none",
        "empty_dictionary_none",
        "empty_tuple_none",
    ],
)
def test__get_median_value__(items, expected_result):
    assert get_median_value(items) == expected_result
