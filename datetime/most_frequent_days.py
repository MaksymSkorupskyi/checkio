"""The Most Frequent Weekdays
What’s your favourite day of the week? Check if it's the most common day of the week in a year.

You are given a year as an integer (e. g. 2001).
You should return the most frequent day(s) of the week in that particular year.
The result has to be a list of days sorted by the order of days in a week (e. g. ['Monday', 'Tuesday']).
Week starts with Monday.

Input: Year as an int.
Output: The list of most common days sorted by the order of days in a week (from Monday to Sunday).

Example:
most_frequent_days(1084) == ['Tuesday', 'Wednesday']
most_frequent_days(1167) == ['Sunday']

Preconditions: Year is between 1 and 9999. Week starts with Monday.
"""
from calendar import isleap, weekday, day_name
from datetime import date
from typing import List

WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


# v1 - datetime.date
def most_frequent_days(year: int) -> List[str]:
    """ The list of most common days sorted by the order of days in a week (from Monday to Sunday) """
    year_first_day = date(year, 1, 1)
    year_last_day = date(year, 12, 31)
    year_days = (year_last_day - year_first_day).days
    first_weekday = year_first_day.weekday()
    # non-leap year - the first day of the week is the most common day
    if not year_days % 7:
        return [WEEKDAYS[first_weekday]]
    # leap year - the first day of the week and the next day are the most common days
    if first_weekday == 6:
        return ['Monday', 'Sunday']  # special case for sunday as week starts from monday
    return [WEEKDAYS[first_weekday], WEEKDAYS[first_weekday + 1]]


# v2 - isleap and weekday
def most_frequent_days(year: int) -> List[str]:
    """ The list of most common days sorted by the order of days in a week (from Monday to Sunday) """
    first_weekday = weekday(year, 1, 1)
    # non-leap year - the first day of the week is the most common day
    if not isleap(year):
        return [WEEKDAYS[first_weekday]]
    # leap year - the first day of the week and the next day are the most common days
    if first_weekday == 6:
        return ['Monday', 'Sunday']  # special case for sunday as week starts from monday
    return [WEEKDAYS[first_weekday], WEEKDAYS[first_weekday + 1]]


# v3 - calendar: isleap, weekday, day_name
def most_frequent_days(year: int) -> List[str]:
    """ The list of most common days sorted by the order of days in a week (from Monday to Sunday) """
    first_weekday = weekday(year, 1, 1)
    # non-leap year - the first day of the week is the most common day
    if not isleap(year):
        return [day_name[first_weekday]]
    # leap year - the first day of the week and the next day are the most common days
    if first_weekday == 6:
        return ['Monday', 'Sunday']  # special case for sunday as week starts from monday
    return [day_name[first_weekday], day_name[first_weekday + 1]]


if __name__ == '__main__':
    print("Example:")
    print(most_frequent_days(1084))
    print(most_frequent_days(1167))
    print(most_frequent_days(1216))
    print(most_frequent_days(1492))
    print(most_frequent_days(1770))
    print(most_frequent_days(1785))
    print(most_frequent_days(328))
    print(most_frequent_days(2016))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
    assert most_frequent_days(1167) == ['Sunday']
    assert most_frequent_days(1216) == ['Friday', 'Saturday']
    assert most_frequent_days(1492) == ['Friday', 'Saturday']
    assert most_frequent_days(1770) == ['Monday']
    assert most_frequent_days(1785) == ['Saturday']
    assert most_frequent_days(212) == ['Wednesday', 'Thursday']
    assert most_frequent_days(1) == ['Monday']
    assert most_frequent_days(2135) == ['Saturday']
    assert most_frequent_days(3043) == ['Sunday']
    assert most_frequent_days(2001) == ['Monday']
    assert most_frequent_days(3150) == ['Sunday']
    assert most_frequent_days(3230) == ['Tuesday']
    assert most_frequent_days(328) == ['Monday', 'Sunday']
    assert most_frequent_days(2016) == ['Friday', 'Saturday']
    print("Coding complete? Click 'Check' to earn cool rewards!")
