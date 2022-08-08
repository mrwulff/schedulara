from __future__ import print_function

from datetime import datetime, timedelta

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pickle
import time


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def make_user_cals(ad):
    service = get_calendar_service(ad)
    print("Getting list of calendars")
    calendars_result = service.calendarList().list().execute()

    calendars = calendars_result.get("items", [])

    if not calendars:
        print("No calendars found.")
    for calendar in calendars:
        summary = calendar["summary"]
        id = calendar["id"]
        primary = "Primary" if calendar.get("primary") else ""
        print("%s\t%s\t%s" % (summary, id, primary))
    tz = time.strftime("%z")
    calendar = {"summary": "Schedulara", "timeZone": get_tz()}

    created_calendar = service.calendars().insert(body=calendar).execute()

    return created_calendar["id"]


def get_tz():
    from tzlocal import get_localzone

    tz = get_localzone()
    # print(type(tz))
    return str(tz)


def make_google_event(ad, y, id):
    # creates one hour event tomorrow 10 AM IST
    service = get_calendar_service(ad)

    d = datetime.now().date()

    event_result = (
        service.events()
        .insert(
            calendarId=id,
            body={
                "summary": y["show"] + " " + y["time"],
                "description": y["venue"]
                + " \n"
                + y["location"]
                + " \n"
                + y["client"]
                + " \n"
                + y["type"]
                + " \n"
                + y["pos"]
                + " \n"
                + y["status"]
                + " \n"
                + y["notes"],
                "start": {
                    "dateTime": y["date"] + " " + y["time"],
                    "timeZone": get_tz(),
                },
                "end": {"dateTime": y["date"] + " " + y["time"], "timeZone": get_tz()},
            },
        )
        .execute()
    )

    print("created event")
    print("id: ", event_result["id"])
    print("summary: ", event_result["summary"])
    print("starts at: ", event_result["start"]["dateTime"])
    print("ends at: ", event_result["end"]["dateTime"])


def get_calendar_service(ad):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(ad + "/token2.json"):
        with open(ad + "/token2.json", "rb") as token:
            creds = Credentials.from_authorized_user_file(ad + "/token2.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials_g.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(ad + "/token2.json", "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)
    # print("successfully found service")
    return service


def google_calendar_add(ad, x, y):
    # creates one hour event tomorrow 10 AM IST
    service = get_calendar_service(ad)

    d = datetime.now().date()
    tomorrow = datetime(d.year, d.month, d.day, 10) + timedelta(days=1)
    start_time = datetime.strptime(x["date"] + " " + x["time"], "%m/%d/%Y %H:%M")
    start = start_time.isoformat()
    end = start
    # print(x["venue"], "what")
    event_result = (
        service.events()
        .insert(
            calendarId=y,
            body={
                "summary": x["show"],
                "description": (x["venue"])
                + x["location"]
                + "\n"
                + x["pos"]
                + "\n"
                + x["type"]
                + "\n"
                + x["client"]
                + "\n"
                + x["job"]
                + "\n"
                + x["notes"]
                + "\n",
                "start": {"dateTime": start, "timeZone": get_tz()},
                "end": {"dateTime": end, "timeZone": get_tz()},
            },
        )
        .execute()
    )

    # print("created event")
    # print("id: ", event_result["id"])
    print("summary: ", event_result["summary"])
    # print("starts at: ", event_result["start"]["dateTime"])
    # print("ends at: ", event_result["end"]["dateTime"])
    return event_result["id"]


if __name__ == "__main__":
    ad = "C:/Users/kw/AppData/Roaming/demo3/"
    x = {
        "date": "08/07/2022",
        "time": "14:30",
        "job": "26575",
        "show": "(GGA) UNITED STEEL WORKERS",
        "venue": "MGM GRAND GARDEN ARENA",
        "location": "MEET AT THE LOADING DOCK",
        "client": "MGM RESORTS",
        "type": "IN",
        "pos": "ME",
        "details": "\xa0",
        "status": "Confirmed",
        "notes": "CORPORATE: BLACK POLO/BLACK PANTS; SHOW CREW WORKS THRU OUT; HARD HAT, SAFETY VEST, GLOVES, & FULL ANKLE PROTECTIVE TOE BOOTS REQ'D ON IN/OUT; BRING PARKING STUB TO SUP AT SIGN IN",
        "timekeep": "\xa0",
        "plus": "\xa0",
        "canceled": False,
        "confirmid": "",
        "lunches": "",
        "endtime": "",
        "is_new": False,
        "confirable": "False",
        "old": False,
    }
    y = "nmspahldtcqmsuh0hp3utfsm7s@group.calendar.google.com"
    # create(ad)
    #
    # make_new_calendar("C:/Users/kw/AppData/Roaming/demo3/")
    # make_google_event(ad)
    os.chdir("../")

    # get_user_cals(ad)
    # make_user_cals(ad)
    # get_tz()
    # make_google_event(ad, x, y)
    google_calendar_add(ad, x, y)


"""body={
                "summary": x["show"],
                "description": +"\n"  # +str(x["venue"])
                + x["location"]
                + "\n"
                + x["pos"]
                + "\n"
                + x["type"]
                + "\n"
                + x["client"]
                + x["job"]
                + "\n"
                + x["notes"]
                + "\n",
                "start": {"dateTime": start, "timeZone": get_tz()},
                "end": {"dateTime": end, "timeZone": get_tz()},
            },
            """
