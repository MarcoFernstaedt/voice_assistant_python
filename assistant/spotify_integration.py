import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

# Authentication with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIPY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    scope='user-modify-playback-state user-read-playback-state'
))

def list_devices():
    devices = sp.devices()
    if devices['devices']:
        for device in devices['devices']:
            print(f"Device: {device['name']}, ID: {device['id']}")
    else:
        print("No active devices found.")

def play_song(song_name):
    results = sp.search(q=song_name, type='track', limit=1)
    if results['tracks']['items'][0]:
        track = results['tracks']['items'][0]
        sp.start_playback(uris=[track['uri']], device_id=os.getenv('SPOTIFY_DEVICE_ID'))
        print(f"Playing {track['name']} by {track['artists'][0]['name']}")
        
def pause_song():
    sp.pause_playback()
    print('Paused')

def resume_track():
    sp.start_playback()
    print("Resuming playback.")

def play_next():
    sp.next_track()
    print("Skipped to the next track.")

def play_previous():
    sp.previous_track()
    print("Playing previous track.")