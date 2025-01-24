#don't remove these imports as they are working hard in other files
from datetime import datetime
import os
import platform
import string
from pwinput import pwinput
import sys, pyrebase
import time
from key import firebase



def is_password_secure(password):

    ratings, length, upper, lower, special, numbers = 0,0,0,0,0,0

    if len(password) >= 8:
        length = True
    
    for char in password:
        if str(char) in string.digits:
            numbers = True
        elif char in string.ascii_uppercase:
            upper = True
        elif char in string.ascii_lowercase:
            lower = True
        elif char in string.punctuation:
            special = True
    
    if numbers is True and length is True and upper is True and lower is True and special is True:
        return True
    else:
        return False
    

def clear():
    if "windows" in platform.system().lower():
        os.system("cls")
    else:
        os.system("clear")




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


def is_valid_booking_time(start_time):
    """Check if the event falls on Monday to Friday between 07:00 and 17:00."""
    
    # Check if the day is between Monday (0) and Friday (4)
    if start_time.weekday() < 6:  # Weekdays (Monday to Friday)
        # Check if the time is between 07:00 and 17:00 (5 PM)
        if start_time.hour >= 7 and start_time.hour < 17:
            return True
        else:
            print(f"Event time {start_time.time()} is outside of the allowed 07:00-17:00 range.")
            return False
    else:
        print(f"Event day {start_time.strftime('%A')} is outside of Monday to Friday.")
        return False
    
def is_conflicting(booking, existing_events):
    b_end, b_start = booking
    # Check if the day is between Monday (0) and Friday (4)
    for event in existing_events:
        e_start, e_end = event
        if b_start < e_end and b_end > e_start:
            print("Your event conflits with other events, try booking again")
            return False
    else:
        return True