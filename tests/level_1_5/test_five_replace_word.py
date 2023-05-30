from functions.level_1_5.five_replace_word import replace_word
import pytest


@pytest.mark.parametrize(
    "text, replace_from, replace_to, expected_results",
    [
        ("句 読句点", "句", "読", "読 読句点"),
        ("..., and ", "...,", "sir", "sir and"),
        ("1994 and 1992", "1994", "sir", "sir and 1992"),
        ("  and  ", " ", "sir", "and"),
        ("your fault, bro", "fault", "last chance", "your fault, bro"),
        ("get lost man", "", "happy", "get lost man"),
        ("get lost man", "lost", "", "get  man"),
        (
            "a A a a a a a A a a a a a a A a ae",
            "a",
            "e",
            "e e e e e e e e e e e e e e e e ae",
        ),
        ("get lOSt man", "losT", "HAppy", "get HAppy man"),
    ],
    ids=[
        "text_with_hieroglyphs",
        "text_with_dots",
        "text_with_numbers",
        "text_with_invisible_sights",
        "text_with_punctuation_mark",
        "without_replace_from_word",
        "without_replace_to_word",
        "text_with_many_replaced_words",
        "case_dependancy",
    ],
)
def test__replace_word__case_dependancy(
    text, replace_from, replace_to, expected_results
):
    assert replace_word(text, replace_from, replace_to) == expected_results
