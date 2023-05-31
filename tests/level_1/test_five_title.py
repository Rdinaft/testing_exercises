from functions.level_1.five_title import change_copy_item
import pytest


@pytest.mark.parametrize(
    "title, expected_result",
    [
        ("Copy of document (3)", "Copy of document (4)"),
        ("Copy of 書類 (3)", "Copy of 書類 (4)"),
        (
            "Copy of 書類. document, document, document document document document document document document document document (2)",
            "Copy of 書類. document, document, document document document document document document document document document (2)",
        ),
        ("Copy of ÿ ▲  ee 書類 (3)", "Copy of ÿ ▲  ee 書類 (4)"),
        ("document (3)", "Copy of document (3)"),
        ("書類 (3)", "Copy of 書類 (3)"),
        (
            "document. 書類, document, document document document document document document document document document (2)",
            "document. 書類, document, document document document document document document document document document (2)",
        ),
        ("ÿ ▲  ee 書類 (3)", "Copy of ÿ ▲  ee 書類 (3)"),
        ("document", "Copy of document"),
        ("書類", "Copy of 書類"),
        ("書類 (書類)", "Copy of 書類 (書類)"),
        (
            "document. 書類, document, document document document document document document document document document",
            "document. 書類, document, document document document document document document document document document",
        ),
        ("ÿ ▲  ee 書類", "Copy of ÿ ▲  ee 書類"),
        (" ▲\n▲ ▲", "Copy of  ▲\n▲ ▲"),
        ("Copy of document", "Copy of document (2)"),
        ("Copy of 書類", "Copy of 書類 (2)"),
        (
            "Copy of 書類. document, document, document document document document document document document document document",
            "Copy of 書類. document, document, document document document document document document document document document",
        ),
        ("Copy of ÿ ▲  ee 書類 (A,.ÿ)", "Copy of ÿ ▲  ee 書類 (A,.ÿ) (2)"),
    ],
)
def test__change_copy_item(title, expected_result):
    assert change_copy_item(title) == expected_result
