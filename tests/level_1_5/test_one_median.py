import pytest
from functions.level_1_5.one_median import get_median_value


def test__get_median_value__four_two_one_numbers():
    with pytest.raises(IndexError):
        get_median_value([1, -3, 5, 7])
    with pytest.raises(IndexError):
        assert get_median_value([1]) == 1
    with pytest.raises(IndexError):
        assert get_median_value([-1, 3]) == 3

def test__get_median_value__even_positive_numbers():
    assert get_median_value([1, 3, 5, 5, 7]) == 5

def test__get_median_value__odd_positive_numbers():
    assert get_median_value([1, 3, 5, 9, 7, 5]) == 6
    assert get_median_value([7, 3, 1]) == 1

def test__get_median_value__odd_mixed_numbers():
    assert get_median_value([-1, 0, 1, 3, -5, 5, 7]) == -5

def test__get_median_value__even_mixed_numbers():
    assert get_median_value([-1, 0, 2, -5, 5, 7]) == 6

def test__get_median_value__odd_negative_numbers():
    assert get_median_value([-5, -3, -2, -1, -7]) == -1

def test__get_median_value__even_negative_numbers():
    assert get_median_value([-5, -3, -2, -3, -1, -7]) == -4

def test__get_median_value__none_result():
    assert get_median_value([]) == None
    assert get_median_value({}) == None
    assert get_median_value(()) == None

def test__get_median_value__float_result():
    assert get_median_value([0, 0, 0, 1, 1, 2]) == 1
