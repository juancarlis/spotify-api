import requests


class Spotiapi:
    def __init__(self, client_id, client_secret):
        self.CLIENT_ID = client_id
        self.CLIENT_SECRET = client_secret

        # Base URL of all Spotify API endpoints
        self.BASE_URL = 'https://api.spotify.com/v1/'

        # Contains the access token for the requests
        self.headers = {}

        # Store data in memory
        self.data = {}

    def authorize(self):
        AUTH_URL = 'https://accounts.spotify.com/api/token'

        # Clean headers
        self.headers = {}

        # POST
        auth_response = requests.post(AUTH_URL, {
            'grant_type': 'client_credentials',
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET
        })

        # Convert the response to JSON
        auth_response_data = auth_response.json()

        # Save the access token
        access_token = auth_response_data['access_token']

        # Get headers
        self.headers = {
            'Authorization': 'Bearer {token}'.format(token=access_token)
        }

    def _is_valid(foo):
        def inner(self):
            pass

    def get_albums(self, band_name):
        r = requests.get(
            self.BASE_URL + f'search?q={band_name}&type=album',
            headers=self.headers,
            params={
                'include_groups': 'album',
                'limit': 50
            }
        )

        print(r.status_code)

        # self.data = {r.status_code, r.json()}

#        df = pd.DataFrame.from_dict(data['albums']['items'])
#        df = df[['name', 'release_date', 'total_tracks', 'images']]
#        df = df.rename(columns={
#            'release_date': 'release',
#            'total_tracks': 'tracks',
#            'images': 'cover'
#        })
