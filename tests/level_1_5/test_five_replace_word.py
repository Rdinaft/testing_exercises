from functions.level_1_5.five_replace_word import replace_word

def test__replace_word__unusual_characters():
    assert replace_word('句 読句点', '句', '読') == '読 読句点'
    assert replace_word('..., and ', '...,', 'sir') == 'sir and'
    assert replace_word('1994 and 1992', '1994', 'sir') == 'sir and 1992'
    assert replace_word('  and  ', ' ', 'sir') == 'and'

def test__replace_word__with_punctuation_mark():
    assert replace_word('your fault, bro', 'fault', 'last chance') == 'your fault, bro'

def test__replace_word__no_replace_from_word():
    assert replace_word('get lost man', '', 'happy') == 'get lost man'

def test__replace_word__no_replace_to_word():
    assert replace_word('get lost man', 'lost', '') == 'get  man'

def test__replace_word__many_replaced_words():
    assert replace_word('1994 and 1992 and', 'and', 'year') == '1994 year 1992 year'
    assert replace_word('a A a a a a a A a a a a a a A a ae', 'a', 'e') == 'e e e e e e e e e e e e e e e e ae'

def test__replace_word__case_dependancy():
    assert replace_word('get lOSt man', 'losT', 'HAppy') == 'get HAppy man'
