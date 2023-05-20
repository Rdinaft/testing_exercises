from functions.level_1.two_date_parser import compose_datetime_from
import datetime
from freezegun import freeze_time


@freeze_time('14.05.2023')
def test_compose_datetime_today():
    assert compose_datetime_from('now', '15:00') == datetime.datetime(2023, 5, 14, 15, 0)

@freeze_time('14.05.2023')
def test_compose_datetime_tomorrow():
    assert compose_datetime_from('tomorrow', '15:00') == datetime.datetime(2023, 5, 15, 15, 00)
