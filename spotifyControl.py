

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="ADD YOUR CLIENT ID",
    client_secret="ADD YOUR SECRET KEY"
))

def play_song_in_browser(song_name):
    results = sp.search(q=song_name, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_url = track['external_urls']['spotify']
        webbrowser.open(track_url)
        return f"Opening {track['name']} by {track['artists'][0]['name']} on Spotify..."
    else:
        return f"Sorry, I couldn't find {song_name} on Spotify."
