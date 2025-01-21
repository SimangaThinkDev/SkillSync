import datetime

def is_conflicting(existing, booking):
    
    # Check if the day is between Monday (0) and Friday (4)
    if booking.start >= existing.end and booking.end <= existing.start:
        return True
    else:
        return False
    

# if __name__ == "__main__":
#     is_conflicting()