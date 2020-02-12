#!/usr/bin/env python

#region #*----------Modules----------
import os
import os.path
import json
import strava
import google_drive
#endregion

#region #*----------Main Function----------
#? Main application function.
#? This is executed by default unless this script is imported as a module.
def main():
    print("Initiating Workflow for Strava App...")
    # strava_client = strava.client()
    google_drive_client = google_drive.client()
    # result = strava_client.get_activity('3079381521')
    # splits = strava.fetch_activity_splits(result)

    # with open("activity_3079381521.json", "w") as f:
    #     f.write(json.dumps(splits, indent=4))
    #     f.close()
    google_drive_client.list_folders()
#endregion

#region #!----------Application Entry Point----------
if __name__ == '__main__':
    main()
#endregion