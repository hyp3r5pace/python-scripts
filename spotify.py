import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from dotenv import load_dotenv
import argparse

def listPlaylist():
    """ Function to list the playlist of a certain user"""
    # define the scope of this function on the user's spotify account data
    scope = 'playlist-read-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    results = sp.current_user_playlists()
    print("Your Spotify playlist \n")
    for i,item in enumerate(results['items']):
        print("%d %s" %(i, item['name']))


def main(args):
    # setting the environment variable by reading from key value pair from .env file
    load_dotenv()
    if args.playlist:   listPlaylist()

if __name__ == "__main__":
    main()
