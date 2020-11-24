import random
import requests
import string
import urllib
import spotipy
import operator
import pprint
import sys

from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
cid ="Enter Client ID"
secret = "Enter Client Secret"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, 
client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

    def get_tracks(self,playlisturl):
        link = playlisturl[34:]
        a = link.split("?")
        songs =[]
        ids=[]
        content = sp.user_playlist_tracks(a[1],a[0],fields=None,limit =100,offset = 0,market=None)
        songs += content["items"]
        for i in songs:
            ids.append(i['track']['id'])
        return ids

    def get_names(self,playlisturl):
        link = playlisturl[34:]
        a = link.split("?")
        songs =[]
        ids=[]
        content = sp.user_playlist_tracks(a[1],a[0],fields=None,limit =100,offset = 0,market=None)
        songs += content["items"]
        for i in songs:
            ids.append(i['track']['name'])

        return ids

    def get_analysis(self, track_ids):
        audio_features = []
        audio_features += sp.audio_features(track_ids)
        features_list = []
        for features in audio_features:
            features_list.append(features['tempo'])

        return features_list

    def sort(self, names, analysis):
        keys_list = names
        values_list = analysis
        zip_iterator = zip(keys_list, values_list)
        x = dict(zip_iterator)
        sorted_d = sorted(x.items(), key= operator.itemgetter(1))
        return sorted_d






