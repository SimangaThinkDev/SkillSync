import datetime

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
    

# if __name__ == "__main__":
#     is_conflicting()