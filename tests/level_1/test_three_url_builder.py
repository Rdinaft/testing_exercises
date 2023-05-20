from functions.level_1.three_url_builder import build_url


def test_build_url_with_querypart():
    assert build_url('cat', 'gg.com', {'seo': 'leo', 'geez': 'lol'}) == 'cat/gg.com?seo=leo&geez=lol'
    assert build_url('cat', 'gg.com', {'書類': '書類', ' ▲\n▲ ▲': ' ▲\n▲ ▲'}) == 'cat/gg.com?書類=書類& ▲\n▲ ▲= ▲\n▲ ▲'
    
def test_build_url_without_querypart():
    assert build_url('cat', 'gg.com') == 'cat/gg.com'
    assert build_url(' ▲\n▲ ▲', '書類.(A,.ÿ)') == ' ▲\n▲ ▲/書類.(A,.ÿ)'
    