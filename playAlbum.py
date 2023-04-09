import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Get the device ID from selected_device.json
with open('selected_device.json') as f:
    selected_device_data = json.load(f)

device_id = selected_device_data['device_id']

# Set up Spotify authentication
with open('secrets.json', 'r') as f:
    secrets = json.load(f)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=secrets['client_id'],
                                               client_secret=secrets['client_secret'],
                                               redirect_uri=secrets['redirect_uri'],
                                               scope='user-read-playback-state,user-modify-playback-state'))

# Play the first song of an album
album_uri = 'spotify:album:0S0KGZnfBGSIssfF54WSJh'  # Change this to the URI of the album you want to play
sp.start_playback(device_id=device_id, context_uri=album_uri, offset={"position": 0})
