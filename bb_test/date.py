import datetime
import collections


WeeklyScheduleEntry = collections.namedtuple(
    'WeeklyScheduleEntry', ('weekday', 'time'))

DEFAULT_WEEKLY_SCHEDULE = (
    WeeklyScheduleEntry(weekday=3, time=datetime.time(hour=20)),
    WeeklyScheduleEntry(weekday=6, time=datetime.time(hour=20)),
)


def calculate_next_event(datetime_, weekly_schedule):
    """Calculate the datetime of the next following event based on
    the supplied datetime and weekly schedule
    """

    weekday = datetime_.isoweekday()

    next_event_datetime = None
    for entry in weekly_schedule:
        weekdaydelta = entry.weekday - weekday
        if weekdaydelta == 0 and datetime_.time() >= entry.time:
            # same weekday, but the event's already been started today
            # next event is in a week
            weekdaydelta = 7
        elif weekdaydelta < 0:
            # the event's taken place this week
            # next event is in less than a week
            weekdaydelta = 7 + weekdaydelta
        # otherwise the event is still ahead this week

        timedelta = datetime.timedelta(days=weekdaydelta)
        entry_datetime = datetime_ + timedelta
        # TODO: is there something like
        # entry_datetime.replace(time=entry.time) there instead of specifying
        # all the time attrs explicitly?
        entry_datetime = entry_datetime.replace(
            hour=entry.time.hour, minute=entry.time.minute,
            second=entry.time.second, microsecond=entry.time.microsecond)

        if next_event_datetime is None or next_event_datetime > entry_datetime:
            # the newly calculated entry datetime is closer to the datetime
            # passed than the previous one
            next_event_datetime = entry_datetime

    return next_event_datetime


def calculate_next_lottery_draw(
        datetime_=None, weekly_schedule=DEFAULT_WEEKLY_SCHEDULE):
    """Calculate the datetime of the next lottery draw based on the supplied
    datetime and the default lottery draw weekly schedule

    If the datetime_ is omitted, the current datetime is used
    """
    datetime_ = datetime_ or datetime.datetime.now()
    return calculate_next_event(datetime_, weekly_schedule)
