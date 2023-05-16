from functions.level_1.three_url_builder import build_url


def test_build_url_with_querypart():
    assert build_url('cat', 'gg.com', {'seo': 'leo', 'geez': 'lol'}) == 'cat/gg.com?seo=leo&geez=lol'
    
def test_build_url_without_querypart():
    assert build_url('cat', 'gg.com') == 'cat/gg.com'
    