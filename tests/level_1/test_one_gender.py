from functions.level_1.one_gender import genderalize


def test_genderalize_pronounce():
    assert genderalize('he', 'she', 'male') == 'he'
    assert genderalize('he', 'she', 'male') != 'she'
    
def test_genderalize_gender():
    assert genderalize('he', 'she', 'not male') == 'she'
    assert genderalize('he', 'she', 'female') == 'she'
    