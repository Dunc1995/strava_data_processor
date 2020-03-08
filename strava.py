import requests
import http
import json
import os
import urllib

#? Payload to obtain latest access token
STRAVA_APP_CREDS = {
    'client_id': os.environ.get('STRAVA_CLIENT_ID'),
    'client_secret': os.environ.get('STRAVA_CLIENT_SECRET'),
    'refresh_token': os.environ.get('STRAVA_REFRESH_TOKEN') ,
    'grant_type': 'refresh_token'
}

class client():
    def __init__(self):
        try:
            self.connection = http.client.HTTPSConnection('www.strava.com:443')
            refresh_query = "https://www.strava.com/oauth/token?{}".format(urllib.parse.urlencode(STRAVA_APP_CREDS))
            print(refresh_query)
            self.connection.request(method="POST", url=refresh_query)
            r = self.connection.getresponse()

            if (r.status == 200):
                result = json.loads(r.read())
                token = result['access_token']
                self.__authorization_header = self.__get_authorization_header(token)
            else:
                print("Status Code {} when trying to obtain access token!".format(r.status))
                raise Exception(str(r.read()))
        except Exception as e:
            print('Strava API failed to initialize! {}'.format(str(e)))

    def get_athlete(self):
        '''Returns a dict containing Athlete data.'''
        return self.__get_query(self.__athlete_query())
    
    def get_activity(self, activity_id):
        '''Returns a dict containing activity data from a given id.'''
        return self.__get_query(self.__activity_query(activity_id))

    def __get_query(self, query):
        print(query)
        result = None      
        self.connection.request(method="GET", url=query, headers=self.__authorization_header)
        r = self.connection.getresponse()
        result = json.loads(r.read())
        return result

    def __get_authorization_header(self, token):
        '''creates the header dict for making Strava API calls'''
        return { "Authorization": "Bearer {}".format(token) }

    def __athlete_query(self):
        return "/api/v3/athlete"

    def __activity_query(self, activity_id):
        return '/api/v3/activities/{}'.format(activity_id)

def fetch_activity_splits(activity_json):
    '''takes the raw json from the Strava activities query and returns only the splits array plus some metadata.'''
    
    splits={ 
    "name": activity_json["name"], 
    "start_date": activity_json["start_date"], 
    "start_date_local": activity_json["start_date_local"], 
    "timezone": activity_json["timezone"], 
    "utc_offset": activity_json["utc_offset"], 
    "splits_metric": activity_json["splits_metric"] }

    return splits