""" Class to manage connection to Spotify API.
"""

import requests
import pandas as pd
import json
import time


class Spotiapi:
    client_id = None
    secret_key = None
    access_token = None
    access_token_expiration = None
    headers = None

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

        # Base URL of all Spotify API endpoints
        self.BASE_URL = 'https://api.spotify.com/v1/'

        try:
            self.access_token = self._authorize()
            if self.access_token is None:
                raise Exception('Request for access token failed.')
        except Exception as e:
            print(e)
        else:
            # Headers contain the token for the requests
            self.headers = {}
            self.headers = {
                'Authorization': 'Bearer {token}'.format(token=self.access_token)
            }

            self.access_token_expiration = time.time() + 3500

    def _authorize(self):
        '''Creates a connection using the CLIENT_ID and CLIENT_SECRET and returns an access_token.

        Returns: 
            - access_token(str)
        '''
        try:
            AUTH_URL = 'https://accounts.spotify.com/api/token'

            auth_response = requests.post(AUTH_URL, {
                'grant_type': 'client_credentials',
                'client_id': self.client_id,
                'client_secret': self.client_secret
            })

            auth_response.raise_for_status()

        except Exception as e:
            print(e)
            return None
        else:
            return auth_response.json()['access_token']

    class Decorators():
        @staticmethod
        def refresh_token(decorated):
            '''Re-authorizes the Spotify API if the access_token has expired.
            '''
            def wrapper(api, *args, **kwargs):
                if time.time() > api.access_token_expiration:
                    api._authorize()
                return decorated(api, *args, **kwargs)
            return wrapper

    @Decorators.refresh_token
    def get_albums(self, band_name):
        """Gets data from Spotify API and transform it to the required
        format with the help of Pandas. 

        Parameters: 
            - band_name(str): Band name in the format -> Some+Band+Name

        Returns:
            - JSON in the required format.
        """

        r = requests.get(
            self.BASE_URL + f'search?q={band_name}&type=album',
            headers=self.headers,
            params={
                'include_groups': 'album',
                'limit': 50
            }
        )

        data = r.json()

        df = pd.DataFrame.from_dict(data['albums']['items'])
        df = df[['name', 'release_date', 'total_tracks', 'images']]
        df = df.rename(columns={
            'release_date': 'release',
            'total_tracks': 'tracks',
            'images': 'cover'
        })

        return json.loads(df.to_json(orient='records'))
