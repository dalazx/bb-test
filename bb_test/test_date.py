import unittest
import datetime

import date


class CalculateNextEventTestCase(unittest.TestCase):
    def test_default_weekly_schedule(self):
        # monday
        datetime_ = datetime.datetime(year=2015, month=8, day=24, hour=18)
        next_event_datetime = date.calculate_next_lottery_draw(datetime_)
        self.assertEqual(
            next_event_datetime,
            datetime.datetime(year=2015, month=8, day=26, hour=20))

        datetime_ = datetime.datetime(year=2015, month=8, day=26, hour=18)
        next_event_datetime = date.calculate_next_lottery_draw(datetime_)
        self.assertEqual(
            next_event_datetime,
            datetime.datetime(year=2015, month=8, day=26, hour=20))

        datetime_ = datetime.datetime(year=2015, month=8, day=26, hour=20)
        next_event_datetime = date.calculate_next_lottery_draw(datetime_)
        self.assertEqual(
            next_event_datetime,
            datetime.datetime(year=2015, month=8, day=29, hour=20))

        datetime_ = datetime.datetime(year=2015, month=8, day=29, hour=20)
        next_event_datetime = date.calculate_next_lottery_draw(datetime_)
        self.assertEqual(
            next_event_datetime,
            datetime.datetime(year=2015, month=9, day=2, hour=20))

    def test_multiple_events_daily(self):
        schedule = (
            date.WeeklyScheduleEntry(weekday=1, time=datetime.time(hour=16)),
            date.WeeklyScheduleEntry(weekday=1, time=datetime.time(hour=20)),
        )

        datetime_ = datetime.datetime(year=2015, month=8, day=24, hour=14)
        next_event_datetime = date.calculate_next_event(datetime_, schedule)
        self.assertEqual(
            next_event_datetime,
            datetime.datetime(year=2015, month=8, day=24, hour=16))

        datetime_ = datetime.datetime(year=2015, month=8, day=24, hour=17)
        next_event_datetime = date.calculate_next_event(datetime_, schedule)
        self.assertEqual(
            next_event_datetime,
            datetime.datetime(year=2015, month=8, day=24, hour=20))
