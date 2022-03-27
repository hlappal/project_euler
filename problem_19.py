import numpy as np

STARTING_YEAR = 1900
STARTING_MONTH = 1
STARTING_DAY = 1
STARTING_WKD = 1

MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def is_leap_year(year):
    leap_year = False
    if year % 100 == 0:  # is century
        if year % 400 == 0:  # is leap year
            leap_year = True
    else:  # is not century
        if year % 4 == 0:  # is leap year
            leap_year = True
    return leap_year

def next_day(year, month, day, wkd):
    months = MONTHS.copy()
    if is_leap_year(year):
        months[1] = 29
    if day < months[month-1]:
        day += 1
    else:  # end of month
        if month < 12:
            month += 1
        else:  # end of year
            year += 1
            month = 1
        day = 1
    if wkd < 7:
        wkd += 1
    else:
        wkd = 1
    return year, month, day, wkd

def main():
    year = STARTING_YEAR
    month = STARTING_MONTH
    day = STARTING_DAY
    wkd = STARTING_WKD

    sunday_count = 0

    while year < 1901:
        year, month, day, wkd = next_day(year, month, day, wkd)
    print("Starting from", year, " ", MONTH_NAMES[month-1], " ", day, ", which is a", DAY_NAMES[wkd-1])
    while year < 2001:
        year, month, day, wkd = next_day(year, month, day, wkd)
        if day == 1 and wkd == 7:
            print("Sunday fell on", day, " ", MONTH_NAMES[month-1], " ", year)
            sunday_count += 1
    print("Ended at", year, " ", MONTH_NAMES[month-1], " ", day, ", which is a", DAY_NAMES[wkd-1])
    print(sunday_count, "Sundays fell on the 1st of a month")

main()
