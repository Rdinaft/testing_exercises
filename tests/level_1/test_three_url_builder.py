from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url('goat', 'gm', {'cool': 'cat'}) == 'goat/gm?cool=cat'
    assert not build_url('goat', 'gm', {'cool': 'cat'}) == 'goat/gm&cool=cat'
    assert build_url('cat', 'gg.com', {'seo': 'leo', 'geez': 'lol'}) == 'cat/gg.com?seo=leo&geez=lol'
    assert isinstance(build_url('goat', 'gm', {'cool': 'cat'}), str)