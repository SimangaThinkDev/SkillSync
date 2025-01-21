from datetime import datetime

def convert_to_datetime(date= '2025-01-22T10:00:00Z') -> datetime: 
    """
    This function will take in the date string as input and return it as a
    datetime object so we can work on it...
    """

    days, time = date.split("T")

    if "Z" in time:
        time = time[:-1]
        # print(time)

    year, mon, day = [int(section) for section in days.split("-")]
    hr, min, sec = [int(section) for section in time.split(":")]
    
    return datetime(year, mon, day, hr, min, sec)

# convert_to_datetime()