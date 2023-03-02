import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import config as cnf
import random
import secrets
import parseResponse as pr



playlistLeo = "spotify:playlist:5Y5kiYaST9xJvOBi67kfbC"
allPlaylists = ["spotify:playlist:5Y5kiYaST9xJvOBi67kfbC", "spotify:playlist:37i9dQZEVXcF4seGHughlX", "spotify:playlist:37i9dQZF1E37VfQF5r5tQI", "spotify:playlist:37i9dQZF1E38mtL7U2XKKf", "spotify:playlist:37i9dQZF1E35vp7Lzvxe8f", "spotify:playlist:37i9dQZF1E37tEEOsCxRn8", "spotify:playlist:37i9dQZF1E36eJNC5Kb29O", "spotify:playlist:37i9dQZF1E38iu0h4bBHTE"]




sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cnf.spotify_client_id,client_secret=cnf.spotify_client_secret,redirect_uri="http://127.0.0.1:9090",scope="user-library-read playlist-read-private user-modify-playback-state user-read-playback-state"))


def getAvailableDevice():
    devices = sp.devices()["devices"]
    if len(devices) > 0:
        return devices[0]["id"]
    else:
        return None

device_id = getAvailableDevice()

def playPlaylist(playlist):
    
    if device_id is not None:
        sp.volume(100, device_id=device_id)
        sp.start_playback(context_uri=playlist, device_id=device_id)
    else:
        print("No active devices found.")

def stopMusic():
    sp.pause_playback()

def resumeMusic():
    sp.start_playback()

def changeVolume(volume):
    
    currentPlayback = sp.current_playback()
    currentVolume = currentPlayback["device"]["volume_percent"]
    if device_id is not None:
        sp.volume(volume, device_id=device_id)
    else:
        print("No active devices found.")
