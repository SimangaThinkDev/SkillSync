from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from to_datetime import convert_to_datetime
from datetime import datetime

def create_event(creds):

    # let's create our timezone variable
    timezone = "Africa/Johannesburg"
    summary = input("Specify the topic that will be handled during this session")
    location = input("jhb or cpt?")
    description = input("Mentor Session or Peer Session?")
    print("Please specify the booking time below: \n")
    year = int(input("Please enter the year you're booking in: "))
    month = input("Enter the month you're booking in: ")
    day = input("Enter the day you're booking in: ")
    start = {
        "year" : year,
        "month" : month,
        "day" : day,
        "hour" : int(input("Hour: ")),
        "mins" : int(input("Minutes: ")),
        "secs" : 0
        } # The generated start date in datetime format
    start = f"{start["year"]}-{start["month"]}-{start["day"]}T{start["hour"]}:{start["mins"]}:{start["secs"]}Z"
    print("When is your session going to end?: \n")
    end = {
        "year" : year,
        "month" : month,
        "day" : day,
        "hour" : int(input("Hour: ")),
        "mins" : int(input("Minutes: ")),
        "secs" : 0
        } # The generated end date in datetime format
    end = f"{end["year"]}-{end["month"]}-{end["day"]}T{end["hour"]}:{end["mins"]}:{end["secs"]}Z"
    attendees = input("the emails of attendees: ") # The mentor Booked and the students to attend

    try:
        service = build("calendar", "v3", credentials = creds)

        #Uncomment Below what you want to experiment with...

        #Let's instead create an event
        event = {
            "summary" : summary,
            "location" : location,
            "description" : description,
            "colorId" : 2,
            "start" : {
                "dateTime" : start,
                "timeZone" : timezone
            },
            "end" : {
                "dateTime" : end,
                "timeZone" : timezone
            },
            "recurrence" : [
                "RRULE:FREQ=DAILY;COUNT=1"
            ],
            "attendees" : [attendees]
        }

        event = service.events().insert(calendarId = "primary", body = event).execute()
        print(f"Session created: {event.get('htmlLink')}")
    
    except HttpError as Err:
        print("An Error Occured:", Err)

