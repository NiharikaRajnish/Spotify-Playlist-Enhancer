import os
from spotify_client import SpotifyClient
import operator


def run():
    spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
    playlisturl = input("Please enter the playlist link: ")
    tracks =[]
    tracks = spotify_client.get_tracks(playlisturl)
    names= []
    names = spotify_client.get_names(playlisturl)
    analysis = spotify_client.get_analysis(tracks)
    sorted_d = spotify_client.sort(names,analysis)
    i = 0
    print("Here is the suggested order of your playlist: ")
    while i < len(sorted_d):
        print(sorted_d[i][0])
        i=i+1

if __name__ == '__main__':
    run()
