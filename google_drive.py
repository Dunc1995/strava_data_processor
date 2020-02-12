from googleapiclient.discovery import build, MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

HOME = os.environ.get('HOME')

class client():
    def __init__(self):
        creds = None

        if os.path.exists('{}/secrets/token.pickle'.format(HOME)):
            with open('{}/secrets/token.pickle'.format(HOME), 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())

        self.__service = build('drive', 'v3', credentials=creds)

    def upload_file(self):
        file_metadata = {
            'name': 'activity_3079381521.json',
            'parents': ['19fS1Z3K8E61OOqLkDpSh6siPpZ1PRgCk']
            }
        media = MediaFileUpload('./activity_3079381521.json',
                                mimetype='application/json')
        file = self.__service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print('File ID: %s' % file.get('id'))

    def list_folders(self):
        page_token = None
        while True:
            response = self.__service.files().list(q="name='Strava', mimeType='application/vnd.google-apps.folder'",
                                                spaces='drive',
                                                fields='nextPageToken, files(id, name)',
                                                pageToken=page_token).execute()
            for file in response.get('files', []):
                # Process change
                print('Found file: %s (%s)' % (file.get('name'), file.get('id')))
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break