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
        
def is_device_id_valid(device_id):
    devices = sp.devices()
    if devices['devices']:
        for device in devices['devices']:
            if device[['id']] == device_id:
                return True
                print('Device ID is a Match!')
    else:
        print("No active devices found.")

def play_song(song_name):
    try:
        results = sp.search(q=song_name, type='track', limit=1)
        if results['tracks']['items'][0]:
            track = results['tracks']['items'][0]
            device_id = os.getenv('SPOTIFY_DEVICE_ID')
            if is_device_id_valid(device_id):
                sp.start_playback(uris=[track['uri']], device_id=device_id)
                print(f"Playing {track['name']} by {track['artists'][0]['name']}")
            else:
                print('No Device Found.')
        else:
                print(f"No results found for '{song_name}'.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred while trying to play the song: {e}")
        
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