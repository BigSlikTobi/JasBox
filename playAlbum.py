import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

with open('devices.json') as f:
    devices_data = json.load(f)

devices = devices_data['devices']

#for device in devices:
    #print("Device name:", device['name'], device['id'])

# Select a device by id
device_id = "18f64e611c1eebf8885594a4b4e04d30eacfbbf8"  # mac
device = next((d for d in devices if d['id'] == device_id), None)

# Print the device information
if device:
    print("Device found")
    print("Device name:", device['name'])
    print("Device type:", device['type'])
    print("Device volume:", device['volume_percent'])
else:
    print("Device not found")

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


