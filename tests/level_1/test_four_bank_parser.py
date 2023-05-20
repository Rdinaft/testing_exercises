from functions.level_1.four_bank_parser import (
    BankCard,
    SmsMessage,
    Expense,
    parse_ineco_expense,
)
from decimal import Decimal
import datetime


def test_parse_ineco_expense():
    text = "300 bucks, 1111155516661222 16.05.23 15:00 Gym authcode 23d9"
    author = "Bank"
    sent_at = "2023-05-16 15:00"
    last_digits = "1222"
    owner = "Billy"
    amount = Decimal("300")
    spent_in = "Gym"
    spent_at = datetime.datetime(2023, 5, 16, 15, 0)
    card = BankCard(last_digits, owner)
    assert parse_ineco_expense(
        SmsMessage(text, author, sent_at), [BankCard(last_digits, owner)]
    ) == Expense(amount, card, spent_in, spent_at)
