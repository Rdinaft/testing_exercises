from functions.level_1_5.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__with_none_result():
    text = 'we will make armenia great again!'
    good_words = {'sauce', 'like'}
    bad_words = {'woof', 'bad'}
    assert check_tweet_sentiment(text, good_words, bad_words) == None
    
    good_words = {'great', 'we'}
    bad_words = {'again!', 'make'}
    assert check_tweet_sentiment(text, good_words, bad_words) == None
    assert check_tweet_sentiment(text, {}, {}) == None

    text = 'we will make make armenia great again'
    assert check_tweet_sentiment(text, good_words, bad_words) == None

def test__check_tweet_sentiment__good_words():
    text = 'we will make armenia, great again!'
    good_words = {'great', 'we'}
    bad_words = {'bad', 'make', 'make', 'bad', ','}
    assert check_tweet_sentiment(text, good_words, bad_words) == 'GOOD'
    
    bad_words = {'bad', 'make', 'again'}
    assert check_tweet_sentiment(text, good_words, bad_words) == 'GOOD'

def test__check_tweet_sentiment__bad_words():
    text = 'we will make armenia great again!'
    good_words = {'meow', 'we'}
    bad_words = {'again!', 'make'}
    assert check_tweet_sentiment(text, good_words, bad_words) == 'BAD'
    assert check_tweet_sentiment('damn', {}, {'damn'}) == 'BAD'
