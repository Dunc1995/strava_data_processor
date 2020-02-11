#!/usr/bin/env python

#region #*----------Modules----------
import os
import json
import strava_api
from pygdrive3 import service
#endregion

#region #*----------Main Function----------
#? Main application function.
#? This is executed by default unless this script is imported as a module.
def main():
    print("Initiating Workflow for Strava App...")
    # strava_requests = strava_api.strava_requests()
    # result = strava_requests.get_activity('3079381521')
    # splits = strava_api.fetch_activity_splits(result)

    drive_service = service.DriveService(os.environ.get('GOOGLE_DRIVE_SECRET') )
    drive_service.auth()

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