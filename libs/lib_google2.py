from __future__ import print_function

from datetime import datetime, timedelta

import os.path
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

import time


# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/drive",
]


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

    try:
        tz = get_localzone()
    except:
        tz = "America/Los_Angeles"
        print("timezone dumb")
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


def create_google_folder(ad, name):
    creds = get_creds(ad)
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    try:
        # create drive api client
        service = build("drive", "v3", credentials=creds)
        file_metadata = {
            "name": name,
            "mimeType": "application/vnd.google-apps.folder",
        }

        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, fields="id").execute()
        print(f'Folder has created with ID: "{file.get("id")}".')

    except HttpError as error:
        print(f"An error occurred creating folder: {error}")
        file = None

    return file.get("id")


def get_creds(ad):
    creds = None

    if os.path.exists(ad + "/token2.json"):
        creds = Credentials.from_authorized_user_file(ad + "/token2.json", SCOPES)
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
    return creds


def google_files(ad, f):

    creds = get_creds(ad)
    print(creds)
    now = datetime.now()
    d = datetime.strftime(now, "%d.%m.%Y")

    try:
        service = build("drive", "v3", credentials=creds)

        file_metadata = {
            "name": "show_backup--" + d + ".zip",
            "parents": ["1-cU7omjnPTAnv9CpyKDRubRrNN2-km04"],
        }
        media = MediaFileUpload(ad + "/show2.zip", mimetype="application/zip=")
        file = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )
        return "File ID: %s" % file.get("id")
    except HttpError as error:

        return f"An error occurred: {error}"


def search_files(ad, name):
    creds = get_creds(ad)
    path = "Schedulara"
    try:
        # create drive api client
        service = build("drive", "v3", credentials=creds)
        files = []
        page_token = None
        while True:
            # pylint: disable=maybe-no-member
            response = (
                service.files()
                .list(
                    q="name='" + name + "'",
                    spaces="drive",
                    fields="nextPageToken, " "files(id, name)",
                    pageToken=page_token,
                )
                .execute()
            )
            for file in response.get("files", []):
                # Process change
                (f'Found file: {file.get("name")}, {file.get("id")}')
            files.extend(response.get("files", []))
            page_token = response.get("nextPageToken", None)
            if page_token is None:
                break

    except HttpError as error:
        print(f"An error occurred searching for folder: {error}")
        files = None
        return "FAILED TO MAKE/FIND CALENDAR"
    try:
        zzz = file.get("id")
        # print(zzz, type(zzz))
        return zzz
    except:
        create_google_folder(ad, name)
        search_files(ad, name)


def make_password(p):
    import base64
    import ast

    p2 = base64.b64encode(p.encode("utf-8"))
    p2 = str(p2)

    return p2


def r_password(p):
    import ast
    import base64

    p3 = ast.literal_eval(p)
    return str(base64.b64decode(p3).decode("utf-8"))


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
    # os.chdir("../")
    zz = os.getcwd()
    print(zz)

    # get_user_cals(ad)
    # make_user_cals(ad)
    # get_tz()
    # make_google_event(ad, x, y)
    # google_calendar_add(ad, x, y)
    # create_google_folder(ad)
    # google_files(ad)
    # search_files(ad, "bobbobob")
    pw = make_password("testtest")
    r_password(pw)
