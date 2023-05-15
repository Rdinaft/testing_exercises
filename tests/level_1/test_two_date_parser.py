from functions.level_1.two_date_parser import compose_datetime_from
import datetime
from freezegun import freeze_time


def test_compose_datetime_from():
    now = '14.05.2023'
    timedelta = datetime.date.today() - datetime.date(2023, 5, 14)
    assert compose_datetime_from(now, '15:00') == datetime.datetime(2023, 5, 14, 15, 0) + timedelta
    with freeze_time(now):
        assert compose_datetime_from('tomorrow', '15:00') == datetime.datetime(2023, 5, 15, 15, 00)
    assert isinstance(compose_datetime_from('tomorrow', '15:00'), datetime.datetime)
