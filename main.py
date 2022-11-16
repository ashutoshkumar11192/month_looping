import datetime

def last_day_of_month(any_day):
    # The day 28 exists in every month. 4 days later, it's always next month
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    # subtracting the number of the current day brings us back one month
    return next_month - datetime.timedelta(days=next_month.day)


from datetime import timedelta

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + timedelta(days=4)
    return next_month - timedelta(days=next_month.day)

def first_day_of_month(any_day):
    first_day = any_day.replace(day=1)
    return first_day

from datetime import datetime
from dateutil import rrule

# dates
start_date = datetime(2021, 10, 14)
end_date = datetime(2022, 10, 1)

start_date.date().weekday()


for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
    base_date = dt.date()
    month_end = last_day_of_month(base_date)
    month_start = first_day_of_month(base_date)
    month_days = month_end.day
    month = month_end.month

    
def monthly(any_day,outcome):
    weekDaysMapping = ("Monday", "Tuesday",
                       "Wednesday", "Thursday",
                       "Friday", "Saturday",
                       "Sunday")
    if outcome=='first_day_of_month':
        first_day = any_day.replace(day=1)
        return first_day.date()
    elif outcome=='last_day_of_month':
        next_month = any_day.replace(day=28) + timedelta(days=4)
        return (next_month - timedelta(days=next_month.day)).date()
    elif outcome=='no_of_days':
        next_month = any_day.replace(day=28) + timedelta(days=4)
        month_end = (next_month - timedelta(days=next_month.day)).date()
        return month_end.day
    elif outcome=='month':
        next_month = any_day.replace(day=28) + timedelta(days=4)
        month_end = (next_month - timedelta(days=next_month.day)).date()
        return month_end.month
    elif outcome=='year':
        next_month = any_day.replace(day=28) + timedelta(days=4)
        month_end = (next_month - timedelta(days=next_month.day)).date()
        return month_end.year
    elif outcome=='weekday':
        next_month = any_day.replace(day=28) + timedelta(days=4)
        month_end = (next_month - timedelta(days=next_month.day)).date()
        return month_end.weekday()
    elif outcome=='Day name':
        next_month = any_day.replace(day=28) + timedelta(days=4)
        month_end = (next_month - timedelta(days=next_month.day)).date()
        return weekDaysMapping[month_end.weekday()]
    else:
        return 'Please check your outcome parameter'

    

