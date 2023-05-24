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

def test__get_median_value__even_amount_of_numbers():
    assert get_median_value([1, 3, 5, 9, 7, 5]) == 6
    assert get_median_value([-1, 0, 2, -5, 5, 7]) == 6
    assert get_median_value([-5, -3, -2, -3, -1, -7]) == -4
    assert get_median_value([0, 0, 0, 1, 1, 2]) == 1

def test__get_median_value__odd_amount_of_numbers():
    assert get_median_value([1, 3, 5, 5, 7]) == 5
    assert get_median_value([7, 3, 1]) == 1
    assert get_median_value([-1, 0, 1, 3, -5, 5, 7]) == -5
    assert get_median_value([-5, -3, -2, -1, -7]) == -1

def test__get_median_value__none_result():
    assert get_median_value([]) == None
    assert get_median_value({}) == None
    assert get_median_value(()) == None
