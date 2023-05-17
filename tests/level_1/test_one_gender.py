from functions.level_1.one_gender import genderalize


def test_genderalize_pronounce_male():
    assert genderalize('he', 'she', 'male') == 'he'
    
def test_genderalize_pronounce_female():
    assert genderalize('he', 'she', 'female') == 'she'

def test_genderalize_gender_other():
    assert genderalize('he', 'she', 'not male') == 'she'
    
    