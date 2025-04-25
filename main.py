def is_leap_year(year):
    # Check if a year is a leap year
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_anchor_day(century):
    # Get the anchor day for the given century
    anchor_days = {
        17: 5,  # 1700s -> Friday
        18: 3,  # 1800s -> Wednesday
        19: 2,  # 1900s -> Tuesday
        20: 0,  # 2000s -> Sunday
        21: 5,  # 2100s -> Friday
    }
    # Default calculation if century not in table
    return anchor_days.get(century, (5 * (century % 4) + 2) % 7)

def get_doomsday(year):
    # Calculate the doomsday (weekday) for a specific year
    century = year // 100             # Extract century
    anchor = get_anchor_day(century)  # Get the anchor day for the century
    y = year % 100                    # Last two digits of the year
    # Doomsday formula: (y // 12) + (y % 12) + ((y % 12) // 4) + anchor
    doomsday = (y // 12 + (y % 12) + (y % 12) // 4 + anchor) % 7
    return doomsday

def get_month_doomsday(month, leap):
    # Get the "doomsday" date for each month
    doomsday_dates = {
        1: 4 if leap else 3,   # Jan 4 (or 3)
        2: 29 if leap else 28, # Feb 29 (or 28)
        3: 14,
        4: 4,
        5: 9,
        6: 6,
        7: 11,
        8: 8,
        9: 5,
        10: 10,
        11: 7,
        12: 12
    }
    return doomsday_dates[month]

def day_of_week_name(index):
    # Convert weekday index (0=Sunday, ..., 6=Saturday) to name
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days[index]

def get_weekday(day, month, year):
    # Main function to get weekday for any date
    leap = is_leap_year(year)                       # Check if it's a leap year
    doomsday = get_doomsday(year)                   # Get year's doomsday
    month_doomsday = get_month_doomsday(month, leap) # Get month's reference doomsday
    diff = (day - month_doomsday) % 7               # Difference from reference date
    weekday = (doomsday + diff) % 7                 # Final day of the week index
    return day_of_week_name(weekday)                # Convert to day name
