from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def create_event(creds):

    # let's create our timezone variable
    timezone = "Africa/Johannesburg"
    summary = None
    location = ["cpt", "jhb"]
    description = ["Mentor Sessions", "Peer Sessions"]
    start = None # The generated start date in datetime format
    end = None # The generated end date in datetime format
    attendees = None # The mentor Booked and the students to attend

    try:
        service = build("calendar", "v3", credentials = creds)

        #Uncomment Below what you want to experiment with...


        #Let's instead create an event
        event = {
            "summary" : "Christmas Braai",
            "location" : "2903/11 miller road",
            "description" : "!Everyone is coming together to enjoy this amazing day:)",
            "colorId" : 3,
            "start" : {
                "dateTime" : "2024-12-25T14:00:00+02:00",
                "timeZone" : timezone
            },
            "end" : {
                "dateTime" : "2024-12-25T22:00:00+02:00",
                "timeZone" : timezone
            },
            "recurrence" : [
                "RRULE:FREQ=DAILY;COUNT=1"
            ],
            "attendees" : [{"email" : "worldwidephytonix@gmail.com"},
            {"email": "siphakwe@gmail.com"}]
        }

        event = service.events().insert(calendarId = "primary", body = event).execute()
        print(f"Session created: {event.get('htmlLink')}")
    
    except HttpError as Err:
        print("An Error Occured:", Err)