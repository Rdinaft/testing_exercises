from functions.level_1.five_title import change_copy_item


def test_change_copy_item_copy_count():
    assert change_copy_item('Copy of document (3)') == 'Copy of document (4)'

def test_change_copy_item_count():
    assert change_copy_item('document (3)') == 'Copy of document (3)'

def test_change_copy_item():
    assert change_copy_item('document') == 'Copy of document'

def test_change_copy_item_copy():
    assert change_copy_item('Copy of document') == 'Copy of document (2)'