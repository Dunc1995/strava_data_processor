#!/usr/bin/env python

#region #*----------Modules----------
import os
import os.path
import json
import strava_api
from pygdrive3 import service
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
#endregion

HOME = os.environ.get('HOME')

#region #*----------Main Function----------
#? Main application function.
#? This is executed by default unless this script is imported as a module.
def main():
    print("Initiating Workflow for Strava App...")
    # strava_requests = strava_api.strava_requests()
    # result = strava_requests.get_activity('3079381521')
    # splits = strava_api.fetch_activity_splits(result)

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('{}/secrets/token.pickle'.format(HOME)):
        with open('{}/secrets/token.pickle'.format(HOME), 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

    drive_service = service.build('drive', 'v3', credentials=creds)

    folder = drive_service.create_folder('Strava_Data_App')
    file = drive_service.upload_file('Testing.json', './hello_world.json', folder)
    link = drive_service.anyone_permission(file)

    folders = drive_service.list_folders_by_name('Strava_Data_App')
    files = drive_service.list_files_by_name('Testing')

    files_from_folder = drive_service.list_files_from_folder_id(folder)
#endregion

#region #!----------Application Entry Point----------
if __name__ == '__main__':
    main()
#endregion