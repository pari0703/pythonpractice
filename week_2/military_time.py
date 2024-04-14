def timeConversion(s):
    # Extracting hours, minutes, and seconds
    hours, minutes, seconds = map(int, s[:-2].split(':'))
    # Checking if it's PM and not 12:00:00 PM
    if s[-2:] == 'PM' and hours != 12:
        hours += 12
    # Checking if it's AM and 12:00:00 AM
    elif s[-2:] == 'AM' and hours == 12:
        hours = 0
    # Formatting the time in 24-hour format
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)

if __name__ == '__main__':
    s = input().strip()
    result = timeConversion(s)
    print(result)
