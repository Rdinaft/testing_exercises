import pytest
from functions.level_1_5.three_first import first, NOT_SET


def test__first__with_parameters():
    assert first([1, 2, 3], 2) == 1
    assert first([1, 2, 3], None) == 1
    assert first([1, 2, 3]) == 1

def test__first__with_not_set_default():
    assert first([1, 2, 3], NOT_SET) == 1

def test__first__without_items_and_with_default():
    assert first([], 2) == 2
    assert first([], 'Something') == 'Something'
    assert first([], None) == None

def test__first__without_items_and_not_set_default():
    with pytest.raises(AttributeError):
        first([], NOT_SET)

def test__first__without_items_and_default():
    with pytest.raises(AttributeError):
        first([])
