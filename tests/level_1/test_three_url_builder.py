from functions.level_1.three_url_builder import build_url
import pytest


@pytest.mark.parametrize(
    "host_name, relative_url, get_params, expected_results",
    [
        ("cat", "gg.com", {"seo": "leo", "geez": "lol"}, "cat/gg.com?seo=leo&geez=lol"),
        (
            "cat",
            "gg.com",
            {"書類": "書類", " ▲\n▲ ▲": " ▲\n▲ ▲"},
            "cat/gg.com?書類=書類& ▲\n▲ ▲= ▲\n▲ ▲",
        ),
        ("cat", "gg.com", "", "cat/gg.com"),
        (" ▲\n▲ ▲", "書類.(A,.ÿ)", "", " ▲\n▲ ▲/書類.(A,.ÿ)"),
    ],
    ids=[
        "with_letter_querypart",
        "with_symbol_querypart",
        "without_querypart",
        "without_querypart_with_sybmols",
    ],
)
def test__build_url__(host_name, relative_url, get_params, expected_results):
    assert build_url(host_name, relative_url, get_params) == expected_results
