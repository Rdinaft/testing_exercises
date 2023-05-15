from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize('he', 'she', 'male') == 'he'
    assert not genderalize('he', 'she', 'not male') == 'he'
    assert isinstance(genderalize('he', 'she', 'male'), str)
    