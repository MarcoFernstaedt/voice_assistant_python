from assistant.spotify_integration import play_song, pause_song, resume_track, play_next, play_previous

def handle_spotify_commands(command):
    if "play" in command:
        song_name = command.replace("play", "").strip()  # Get the song name
        play_song(song_name)
    elif "pause" in command:
        pause_song()
    elif: 'resume' in command:
        resume_track()
    elif "next" in command:
        play_next()
    elif "previous" in command:
        play_previous()
    else:
        print("Spotify command not recognized.")
