from assistant.spotify_integration import play_song
# , pause_song, play_next, play_previous

def handle_spotify_commands(command):
    if 'play' in command:
        song_name = command.replace('play', '').strip()
        play_song(song_name)
    else:
        print('Spotify command not found')