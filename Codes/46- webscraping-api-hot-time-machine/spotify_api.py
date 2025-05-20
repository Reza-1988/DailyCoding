import spotipy
from spotipy.oauth2 import SpotifyOAuth

from Codes.local_settings import SPOTIFY_DATA
from billboard_scraper import hot_year, song_names


# Step 7 - Log in to the Spotify Developer Dashboard and create an app to get API credentials
# You'll receive a Client ID, Client Secret, and set a Redirect URI
# These credentials are needed to authenticate with Spotify's Web API


# STEP 8 - Use Spotify library to create a Spotipy client instance with OAuth authentication
# This uses the SpotifyOAuth flow to log in and authorize access to the user's Spotify account
# The credentials and configuration (client ID, secret, redirect URI, and scopes) are provided from SPOTIFY_DATA
# After authentication, this object (sp) allows you to interact with Spotify's Web API (e.g. search, create playlists, etc.)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_DATA['client_id'],
                                               client_secret=SPOTIFY_DATA['client_secret'],
                                               redirect_uri=SPOTIFY_DATA['redirect_uri'],
                                               scope="playlist-modify-private")) # **make sure this matches your intent**
# After you successfully log in through the Spotify login page (opened in your browser),
# you'll be redirected to the URL you set as the redirect URI.
# Copy the full URL from your browser's address bar and paste it into the terminal when prompted.
# If authentication is successful, a `.cache` file will be created in your project directory.
# This file stores your access token so you don't have to log in again every time you run the script.


# STEP 9 - Search for each song on Spotify using the Spotipy library and collect their URIs
# For each song title scraped from Billboard, we use Spotipy (a Python wrapper for the Spotify Web API)
# to search for a matching track on Spotify.
# The search query includes both the track name and the year (from the date) to improve accuracy.
# If a track is found, we extract its Spotify URI and add it to the song_uris list.
# If no result is found (IndexError), we print a message and skip that song.
song_uris = []
year = hot_year.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track") # Use Spotipy's search function to query Spotify for the track
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"] # Try to get the URI of the first search result
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")  # If no results are found, skip the song and log it


# STEP 10 - Get the current user's Spotify ID
# This ID is needed to create a playlist under the user's account
# sp.current_user() returns a dictionary with the user's profile info, including their unique ID
user_id = sp.current_user()["id"]
print(user_id)


# STEP 11 - Create a new private playlist in the user's Spotify account
# We use the user's Spotify ID and give the playlist a name based on the selected Billboard date
# Setting public=False makes the playlist private (only visible to the user)
# The returned 'playlist' object is a dictionary with metadata, including the playlist ID, name, URL, etc.
playlist = sp.user_playlist_create(user=user_id, name=f"{hot_year} Billboard 100", public=False)
print(playlist)

# STEP 12 - Add all found song URIs to the newly created Spotify playlist
# We pass the playlist ID (from the playlist object) and the list of track URIs we collected earlier
# This step uploads the songs to the playlist so the user can listen to them on Spotify
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)