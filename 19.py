# To make things easier, months and days-of-the-month
# are counted from 0. We start on Sunday January 6, 1900
year, month, day = 1900, 0, 6
days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
sundays = 0
while year < 2001:
    if day == 0 and year > 1900:  # We don't regard 1900 as being the 20th Century
        sundays += 1
    if month == 1 and not year % 4 and year > 1900:  # No leap year in 1900
        dim = 29
    else:
        dim = days_in_month[month]
    day += 7
    if day >= dim:
        day -= dim
        month += 1
    if month == 12:
        month = 0
        year += 1
print sundays
