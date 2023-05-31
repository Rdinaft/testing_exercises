from functions.level_1.two_date_parser import compose_datetime_from
import datetime
import pytest
from freezegun import freeze_time


@freeze_time("14.05.2023")
@pytest.mark.parametrize(
    "date_str, time_str, expected_result",
    [
        ("now", "15:00", datetime.datetime(2023, 5, 14, 15, 0)),
        ("tomorrow", "15:00", datetime.datetime(2023, 5, 15, 15, 00)),
    ],
    ids=["today", "tomorrow"],
)
def test__compose_datetime_from(date_str, time_str, expected_result):
    assert compose_datetime_from(date_str, time_str) == expected_result
