import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta
import time

# Read the secrets
with open("secrets.json", "r") as f:
    config = json.load(f)

# Set up the client credentials
client_id = config["client_id"]
client_secret = config["client_secret"]
redirect_uri = config["redirect_uri"]

# Set up the authentication flow
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="user-library-read user-read-playback-state"))
# Define a function to check the token expiration time and refresh the token if necessary
def check_token_expiration():
    tokens = sp.auth_manager.get_cached_token()
    expire_time = datetime.fromisoformat(tokens["expires_at"])
    time_left = expire_time - datetime.now()
    if time_left < timedelta(seconds=300):
        sp.auth_manager.refresh_access_token(tokens["refresh_token"])
        tokens = sp.auth_manager.get_cached_token()
        with open('tokens.json', 'w') as f:
            json.dump(tokens, f)
        print("Token refreshed at:", datetime.now())

# Retrieve the access token and refresh token
access_token = sp.auth_manager.get_access_token(as_dict=False)
refresh_token = sp.auth_manager.get_cached_token()["refresh_token"]

# Save tokens to JSON file
tokens = {'access_token': access_token, 'refresh_token': refresh_token}

with open('tokens.json', 'w') as f:
    json.dump(tokens, f)

# Test the authentication by getting the current user's saved tracks
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

# Check Token in console
print("Access token:", access_token)
print("Refresh token:", refresh_token)

# Continuously check token expiration and refresh if necessary
while True:
    check_token_expiration()
    time.sleep(3000)