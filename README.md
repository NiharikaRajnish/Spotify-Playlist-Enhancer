# Spotify-Playlist-Enhancer
A python program that assists users with rearranging the songs on their playlists to enhance the crossfade option (transition between two songs) taking into account tempo, BPI and genre. Utilizes Spotipy library for Spotify Web API.

# Local Setup
1) install or upgrade Spotipy with: pip install spotipy --upgrade
2) Obtain you Client ID and Client Secret on Spotify for Developers: https://developer.spotify.com/dashboard/applications
3) Enter credentials into spotify_client.py
4) run the File - python3 run.py
5) Enter the Url of the playlist you want to reorder (Click the 3 dots - Share - Copy Playlist Url)

# ToDo:
- load reordered songs into seperate playlist 
- BPI/genre sort options
- Rearrange more than 100 tracks
- Add Error Handling
