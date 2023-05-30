from functions.level_1.four_bank_parser import (
    BankCard,
    SmsMessage,
    Expense,
    parse_ineco_expense,
)
from decimal import Decimal
import datetime
import pytest


@pytest.mark.parametrize(
    "sms_message, bank_card, expense",
    [
        (
            SmsMessage(
                "300 bucks, 1111155516661222 16.05.23 15:00 Gym authcode 23d9",
                "Bank",
                "2023-05-16 15:00",
            ),
            [BankCard("1222", "Billy")],
            Expense(
                Decimal("300"),
                BankCard("1222", "Billy"),
                "Gym",
                datetime.datetime(2023, 5, 16, 15, 0),
            ),
        )
    ],
    ids=["is_valid"],
)
def test__parse_ineco_expense_(sms_message, bank_card, expense):
    assert parse_ineco_expense(sms_message, bank_card) == expense
