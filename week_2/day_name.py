import calendar
date = input().split()
month, day, year = int(date[0]), int(date[1]), int(date[2])
week_day=calendar.weekday(year, month, day)
print(calendar.day_name[week_day].upper())

