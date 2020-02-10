#!/usr/bin/env python

#region #*----------Modules----------
import argparse
import os
import json
import strava_api
#endregion

#region #*----------Main Function----------
#? Main application function.
#? This is executed by default unless this script is imported as a module.
def main(args):
    print("Initiating Workflow for Strava App...")
    strava_requests = strava_api.strava_requests()
    athlete = strava_requests.get_athlete()
    print(json.dumps(athlete, indent=4))
#endregion

#region #!----------Application Entry Point----------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='template')
    parser.add_argument('--example', '-e', help='This is an example argument')
    args = parser.parse_args()
    main(args)
#endregion