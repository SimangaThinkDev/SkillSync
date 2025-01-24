# Main Code will go here
import datetime
import os.path
from create_events import create_event
from get_events import get_events
from tools import *

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"] #Avoid using read only because we want to affect the calendar

def initiate_calendar():
    creds = None

    if os.path.exists("secrets/token.json"):
        creds = Credentials.from_authorized_user_file("secrets/token.json")

    #If we don't have credentials or if the creds are invalid
    if not creds or not creds.valid:
        
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
          flow = InstalledAppFlow.from_client_secrets_file("secrets/credentials.json", SCOPES)
          creds = flow.run_local_server(port = 0)

        with open("secrets/token.json", "w") as token:
            token.write(creds.to_json())
    try:
        service = build("calendar", "v3", credentials=creds)
    except HttpError as e:
        print("An Error Occurred:", e)
    return creds

if __name__ == "__main__":
    clear()
    queries = ["Create Booking", "Get Bookings"]
    [print(query) for query in queries]
    query = int(input("What would you like to do: ")) - 1
    print("WELCOME TO THE BOOKINGS CONSOLE")

    if queries[query] == "Create Booking":
        clear()
        existing = get_events(initiate_calendar())
        create_event(initiate_calendar(), existing)
    elif queries[query] == "Get Bookings":
        clear()
        get_events(creds = initiate_calendar())