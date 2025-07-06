

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="0a2bef201251435fb7e7c7e44d47fb2d",
    client_secret="efcfa287d1dc44d88bbbd3615e6a1a0e"
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
