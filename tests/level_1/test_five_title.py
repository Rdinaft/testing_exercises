from functions.level_1.five_title import change_copy_item


def test_change_copy_item_copy_count():
    assert change_copy_item('Copy of document (3)') == 'Copy of document (4)'
    assert change_copy_item('Copy of 書類 (3)') == 'Copy of 書類 (4)'
    assert change_copy_item('Copy of 書類. document, document, document document document document document document document document document (2)') == 'Copy of 書類. document, document, document document document document document document document document document (2)'
    assert change_copy_item('Copy of ÿ ▲  ee 書類 (3)') == 'Copy of ÿ ▲  ee 書類 (4)'

def test_change_copy_item_count():
    assert change_copy_item('document (3)') == 'Copy of document (3)'
    assert change_copy_item('書類 (3)') == 'Copy of 書類 (3)'
    assert change_copy_item('document. 書類, document, document document document document document document document document document (2)') == 'document. 書類, document, document document document document document document document document document (2)'
    assert change_copy_item('ÿ ▲  ee 書類 (3)') == 'Copy of ÿ ▲  ee 書類 (3)'

def test_change_copy_item():
    assert change_copy_item('document') == 'Copy of document'
    assert change_copy_item('書類') == 'Copy of 書類'
    assert change_copy_item('書類 (書類)') == 'Copy of 書類 (書類)'
    assert change_copy_item('document. 書類, document, document document document document document document document document document') == 'document. 書類, document, document document document document document document document document document'
    assert change_copy_item('ÿ ▲  ee 書類') == 'Copy of ÿ ▲  ee 書類'
    assert change_copy_item(' ▲\n▲ ▲') == 'Copy of  ▲\n▲ ▲'

def test_change_copy_item_copy():
    assert change_copy_item('Copy of document') == 'Copy of document (2)'
    assert change_copy_item('Copy of 書類') == 'Copy of 書類 (2)'
    assert change_copy_item('Copy of 書類. document, document, document document document document document document document document document') == 'Copy of 書類. document, document, document document document document document document document document document'
    assert change_copy_item('Copy of ÿ ▲  ee 書類 (A,.ÿ)') == 'Copy of ÿ ▲  ee 書類 (A,.ÿ) (2)'
