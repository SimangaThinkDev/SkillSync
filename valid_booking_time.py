import datetime

def is_valid_booking_time(start_time):
    """Check if the event falls on Monday to Friday between 07:00 and 17:00."""
    
    # Check if the day is between Monday (0) and Friday (4)
    if start_time.weekday() < 5:  # Weekdays (Monday to Friday)
        # Check if the time is between 07:00 and 17:00 (5 PM)
        if start_time.hour >= 7 and start_time.hour < 17:
            return True
        else:
            print(f"Event time {start_time.time()} is outside of the allowed 07:00-17:00 range.")
            return False
    else:
        print(f"Event day {start_time.strftime('%A')} is outside of Monday to Friday.")
        return False
    
if __name__ == "__main__":
    is_valid_booking_time()