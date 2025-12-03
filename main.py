"""
A really fun little script for forcing a playlist to play on a certain spotify account.
The script checks every 150 seconds (2:30 min) if it's the correct time
and whether the playlist is already playing.

Have fun every one, and also I'm so sorry in advance for everyone in advance.

Author:
Aaro Kuusinen
kuusinen.aaro@gmail.com
TG: @apeoskari
"""


import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
import time
import config

correct_list = config.xmas_playlist_id


# A function to check whether the current playlist is 'correct-
def playlist_right(spotify) -> bool:
    playlist_id = ''
    try:
        cur_playback = spotify.current_playback()

        if cur_playback and cur_playback['context']:
            context_type = cur_playback['context']['type']
            context_uri = cur_playback['context']['uri']

            if context_type == 'playlist':
                playlist_id = context_uri.split(':')[-1]
                print(playlist_id)
            else:
                print('Not a playlist')
                return False
        else:
            print('No playback information available')

        if playlist_id == config.xmas_playlist_id:
            return True
        else:
            return False
    except:
        print('Something went wrong with getting the playlist')
        return False


# This tries to change the playlist back to the correct one with the shuffle mode enabled
def change_playlist(spotify) -> None:
    try:
        device = spotify.devices()['devices'][0]['id']
        print("Device:", device)
        spotify.start_playback(device_id=device, context_uri=f'spotify:playlist:{config.xmas_playlist_id}')
        spotify.shuffle(state=True, device_id=device)
        spotify.repeat(state="context", device_id=device)
    except:
        print("Couldn't change playlist :(")


# A loop to check conditions every 150 seconds.
def main() -> None:

    time_now = datetime.now()
    month = time_now.strftime("%m")
    try:
        scope = "user-modify-playback-state user-read-playback-state"
        spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID_kilta,
                                                            client_secret=config.CLIENT_SECRET_kilta,
                                                            redirect_uri=config.REDIRECT_URI,
                                                            scope=scope,
                                                            username=config.SP_USERNAME_kilta))
        print("Spotify authentication successful")
        while month == "12":

            if not playlist_right(spotify):
                change_playlist(spotify)
            if not spotify.current_playback() or not spotify.current_playback().get("is_playing", False):
                spotify.start_playback()
            month = time_now.strftime("%m")
            time.sleep(5)  # Check evey X seconds
    except Exception as e:
        print(f"Authentication failed: {e}")


if __name__ == '__main__':
    main()
