import pytest
from functions.level_1_5.one_median import get_median_value


def test__get_median_value__IndexError():
    with pytest.raises(IndexError):
        get_median_value([1, -3, 5, 7])
        get_median_value([1])
        get_median_value([-1, 3])

def test__get_median_value__even_positive_numbers():
    assert get_median_value([1, 3, 5, 5, 7]) == 5

def test__get_median_value__odd_positive_numbers():
    assert get_median_value([1, 3, 5, 9, 7, 5]) == 6

def test__get_median_value__three_numbers():
    assert get_median_value([7, 3, 1]) == 1  #must be -3

def test__get_median_value__odd_mixed_numbers():
    assert get_median_value([-1, 0, 1, 3, -5, 5, 7]) == -5  #must be 1

def test__get_median_value__even_mixed_numbers():
    assert get_median_value([-1, 0, 2, -5, 5, 7]) == 6  #must be 1

def test__get_median_value__odd_negative_numbers():
    assert get_median_value([-5, -3, -2, -1, -7]) == -1  #must be -3

def test__get_median_value__even_negative_numbers():
    assert get_median_value([-5, -3, -2, -3, -1, -7]) == -4  #must be -3

def test__get_median_value__None_result():
    assert get_median_value([]) == None
    assert get_median_value({}) == None
    assert get_median_value(()) == None

def test__get_median_value__float_result():
    assert get_median_value([0, 0, 0, 1, 1, 2]) == 1  #must be 0.5
