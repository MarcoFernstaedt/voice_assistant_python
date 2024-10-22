import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import logging
from .tts import speak

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Spotify authentication
def authenticate_spotify():
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv('SPOTIPY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
            redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
            scope='user-modify-playback-state user-read-playback-state'
        ))
        logger.info("Successfully authenticated with Spotify.")
        # speak("Successfully authenticated with Spotify.")
        return sp
    except Exception as e:
        logger.error(f"Error authenticating Spotify: {e}")
        speak(f"Error authenticating Spotify: {e}")
        return None

# Initialize Spotify object
sp = authenticate_spotify()

def list_devices():
    """List available devices to play on."""
    try:
        devices = sp.devices()
        if devices['devices']:
            for device in devices['devices']:
                logger.info(f"Device: {device['name']}, ID: {device['id']}")
                speak(f"Device: {device['name']}, ID: {device['id']}")
        else:
            logger.warning("No active devices found.")
            speak("No active devices found.")
    except Exception as e:
        logger.error(f"Error fetching devices: {e}")
        speak("Error fetching devices: {e}")

def is_device_id_valid(device_id):
    """Check if the given device ID is valid and active."""
    try:
        devices = sp.devices()
        if devices['devices']:
            for device in devices['devices']:
                if device['id'] == device_id:
                    logger.info('Device ID is a match!')
                    speak('Device ID is a match!')
                    return True
        logger.warning("No matching device found.")
        speak("No matching device found.")
        return False
    except Exception as e:
        logger.error(f"Error checking device ID: {e}")
        speak(f"Error checking device ID: {e}")
        return False

def play_song(song_name):
    """Search for and play a song by name."""
    try:
        results = sp.search(q=song_name, type='track', limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            device_id = os.getenv('SPOTIFY_DEVICE_ID')
            if is_device_id_valid(device_id):
                sp.start_playback(uris=[track['uri']], device_id=device_id)
                logger.info(f"Playing {track['name']} by {track['artists'][0]['name']}")
                speak(f"Playing {track['name']} by {track['artists'][0]['name']}")
            else:
                logger.warning('No valid device found to play on.')
                speak('No valid device found to play on.')
        else:
            logger.warning(f"No results found for '{song_name}'.")
            speak(f"No results found for '{song_name}'.")
    except spotipy.exceptions.SpotifyException as se:
        logger.error(f"Spotify API error: {se}")
        speak(f"Spotify API error: {se}")
    except Exception as e:
        logger.error(f"An error occurred while trying to play the song: {e}")
        speak(f"An error occurred while trying to play the song: {e}")

def pause_song():
    """Pause playback on the active device."""
    try:
        sp.pause_playback()
        logger.info('Paused playback.')
        speak('Paused playback.')
    except spotipy.exceptions.SpotifyException as se:
        logger.error(f"Spotify API error: {se}")
        speak(f"Spotify API error: {se}")
    except Exception as e:
        logger.error(f"An error occurred while trying to pause the song: {e}")
        speak(f"An error occurred while trying to pause the song: {e}")

def resume_track():
    """Resume playback on the active device."""
    try:
        sp.start_playback()
        logger.info("Resumed playback.")
        speak("Resumed playback.")
    except spotipy.exceptions.SpotifyException as se:
        logger.error(f"Spotify API error: {se}")
        speak(f"Spotify API error: {se}")
    except Exception as e:
        logger.error(f"An error occurred while trying to resume playback: {e}")
        speak(f"An error occurred while trying to resume playback: {e}")

def play_next():
    """Skip to the next track."""
    try:
        sp.next_track()
        logger.info("Skipped to the next track.")
        speak("Skipped to the next track.")
    except spotipy.exceptions.SpotifyException as se:
        logger.error(f"Spotify API error: {se}")
        speak(f"Spotify API error: {se}")
    except Exception as e:
        logger.error(f"An error occurred while trying to skip to the next track: {e}")
        speak(f"An error occurred while trying to skip to the next track: {e}")

def play_previous():
    """Play the previous track."""
    try:
        sp.previous_track()
        logger.info("Playing the previous track.")
        speak("Playing the previous track.")
    except spotipy.exceptions.SpotifyException as se:
        logger.error(f"Spotify API error: {se}")
        speak(f"Spotify API error: {se}")
    except Exception as e:
        logger.error(f"An error occurred while trying to play the previous track: {e}")
        speak(f"An error occurred while trying to play the previous track: {e}")
