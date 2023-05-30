import pytest
from functions.level_1_5.three_first import first, NOT_SET
import pytest


@pytest.mark.parametrize(
    "items, default, expected_result",
    [
        ([1, 2, 3], 2, 1),
        ([1, 2, 3], None, 1),
        ([1, 2, 3], "", 1),
        ([1, 2, 3], NOT_SET, 1),
        ([], 2, 2),
        ([], "Something", "Something"),
        ([], None, None),
    ],
    ids=[
        "with_all_params",
        "with_none_default",
        "without_defualt",
        "with_not_set_default",
        "without_items_with_int_default",
        "without_items_with_str_default",
        "without_items_with_none_default",
    ],
)
def test__first__(items, default, expected_result):
    assert first(items, default) == expected_result


def test__first__without_items_and_not_set_default():
    with pytest.raises(AttributeError):
        first([], NOT_SET)


def test__first__without_items_and_default():
    with pytest.raises(AttributeError):
        first([])
