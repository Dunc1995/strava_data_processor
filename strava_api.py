import requests
import http
import json
import os
import urllib

#? Payload to obtain latest access token
STRAVA_APP_CREDS = {
    'client_id': 'a',
    'client_secret': 'b',
    'refresh_token': 'c',
    'grant_type': 'refresh_token'
}

class strava_requests():
    def __init__(self):
        try:
            self.connection = http.client.HTTPSConnection('www.strava.com:443')
            print(json.dumps(STRAVA_APP_CREDS, indent=4))
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
        

    def __get_authorization_header(self, token):
        '''creates the header dict for making Strava API calls'''
        return { "Authorization": "Bearer {}".format(token) }

    def get_athlete(self):
        result = None      
        self.connection.request(method="GET", url=self.athlete_query, headers=self.__authorization_header)
        r = self.connection.getresponse()
        result = json.loads(r.read())
        return result
    
    def athlete_query(self):
        return "/api/v3/athlete"
