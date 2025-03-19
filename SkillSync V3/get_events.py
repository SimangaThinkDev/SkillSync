from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.exceptions import TransportError
import datetime
# from calendar_1 import initiate_calendar

def get_events(creds):
        
    try:    
        service = build("calendar", "v3", credentials=creds)
        # This is for getting events 
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

        event_result = service.events().list(calendarId = "primary",
                                            timeMin = now,
                                            maxResults = 20,
                                            singleEvents = True,
                                            orderBy = "startTime"
                                            ).execute()
        events = event_result.get("items", [])

        if not events:
            print("No Upcoming Events Found!")
            return
        
        sessions = []

        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            end = event["end"].get("dateTime", event["end"].get("date"))
            sessions.append((start, end))

        # print("This is events: \n",events)

    except HttpError as Err:
        print("An Error Occured:", Err)
    return sessions

def print_events(creds):

    try:    
        service = build("calendar", "v3", credentials=creds)
        # This is for getting events 
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

        event_result = service.events().list(calendarId = "primary",
                                            timeMin = now,
                                            maxResults = 20,
                                            singleEvents = True,
                                            orderBy = "startTime"
                                            ).execute()
        events = event_result.get("items", [])

        if not events:
            print("No Upcoming Events Found!")
            return
        
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])

        print("This is events: \n",events)

    except HttpError as Err:
        print("An Error Occured:", Err)
    except TransportError:
        print("Bad Network, Can't get events!")

# if __name__ == "__main__":
#     print_events(initiate_calendar())