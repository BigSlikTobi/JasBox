import spotipy
import spotipy.util as util
import json

# Read the configuration from file
with open("secrets.json", "r") as f:
    config = json.load(f)

# Read the tokens from file
with open("tokens.json", "r") as f:
    tokens = json.load(f)

# Create a new Spotify API client
sp = spotipy.Spotify(auth=tokens["access_token"])

# Get the devices
devices = sp.devices()

# Print the devices
for device in devices["devices"]:
    print(device["name"], "-", device["id"])
