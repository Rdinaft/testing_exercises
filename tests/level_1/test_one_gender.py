import pytest
from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    "verb_male, verb_female, gender, expected_result",
    [
        ("he", "she", "male", "he"),
        ("he", "she", "female", "she"),
        ("he", "she", "not male", "she"),
    ],
    ids=["pronounce_male", "pronounce_female", "gender_other"],
)
def test__genderalize__(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) is expected_result
