from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
from decimal import Decimal
import datetime


def test_parse_ineco_expense():
    assert parse_ineco_expense(SmsMessage(text='300 bucks, 1111155516661222 16.05.23 15:00 Gym authcode 23d9', author='Bank', sent_at='2023-05-16 15:00'), [BankCard(last_digits='1222', owner='Billy')]) == Expense(amount=Decimal('300'), card=BankCard(last_digits='1222', owner='Billy'), spent_in='Gym', spent_at=datetime.datetime(2023, 5, 16, 15, 0))
    assert parse_ineco_expense(SmsMessage(text='Payed 300 bucks, 001222 15.05.23 10:00 Gym authcode 2333d9', author='Gym', sent_at='2023-05-16 10:00'), [BankCard(last_digits='1222', owner='Van')]) == Expense(amount=Decimal('300'), card=BankCard(last_digits='1222', owner='Van'), spent_in='Gym', spent_at=datetime.datetime(2023, 5, 15, 10, 0))
