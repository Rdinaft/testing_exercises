from functions.level_1_5.four_sentiment import check_tweet_sentiment
import pytest


@pytest.mark.parametrize(
    "text, good_words, bad_words, expected_result",
    [
        ("we will make armenia great again!", {"sauce", "like"}, {"woof", "bad"}, None),
        ("we will make armenia great again!", {}, {}, None),
        (
            "we will make armenia, great again!",
            {"great", "we"},
            {"bad", "make", "make", "bad", ","},
            "GOOD",
        ),
        (
            "we will make armenia great again!",
            {"meow", "we"},
            {"again!", "make"},
            "BAD",
        ),
        ("damn", {}, {"damn"}, "BAD"),
    ],
    ids=[
        "bad_equal_good",
        "with_empty_good_and_bad_dictionaries",
        "good_words_more_than_bad",
        "bad_words_more_than_good",
        "without_good_dict",
    ],
)
def test__check_tweet_sentiment__(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected_result
