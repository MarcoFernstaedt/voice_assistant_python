import logging
from assistant.spotify_integration import play_song, pause_song, resume_track, play_next, play_previous

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def handle_spotify_commands(command):
    try:
        if "play" in command:
            song_name = command.replace("play", "").strip()  # Get the song name
            if song_name:
                logger.info(f"Playing song: {song_name}")
                play_song(song_name)
            else:
                logger.warning("No song name provided in the play command.")
                print("Please provide a song name to play.")

        elif "pause" in command:
            logger.info("Pausing Spotify playback.")
            pause_song()

        elif 'resume' in command:
            logger.info("Resuming Spotify playback.")
            resume_track()

        elif "next" in command:
            logger.info("Skipping to the next track.")
            play_next()

        elif "previous" in command:
            logger.info("Playing the previous track.")
            play_previous()

        else:
            logger.warning(f"Spotify command not recognized: {command}")
            print("Spotify command not recognized.")

    except Exception as e:
        logger.error(f"Error handling Spotify command '{command}': {e}")
        print(f"An error occurred while processing your command: {e}")
