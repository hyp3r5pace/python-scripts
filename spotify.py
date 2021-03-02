import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from dotenv import load_dotenv
import argparse
from termcolor import colored 

def listPlaylist():
    """ Function to list the playlist of a certain user"""
    # define the scope of this function on the user's spotify account data
    scope = 'playlist-read-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    results = sp.current_user_playlists()
    print("Your Spotify playlist \n")
    for i,item in enumerate(results['items']):
        print("%d %s" %(i, item['name']))

def expandPlaylist(playlist):
    """Function to list the songs in the playlist passed as argument"""
    scope = 'playlist-read-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    playlists = sp.current_user_playlists()
    for pl in playlists['items']:
        if pl['name'].casefold() == playlist.casefold():
            pl_id = pl['id']
            results = sp.playlist(pl_id, fields="tracks,next")
            tracks = results['tracks']
            print('The tracks in the playlist {}:\n'.format(playlist))
            for i,item in enumerate(tracks['items']):
                song = item['track']
                print("%d %s  --  %s" %(i, song['name'], colored(song['artists'][0]['name'], 'green')))
            return
    raise Exception('playlist not found!\n')

def listArtist():
    """Function to list the artists followed by the user"""
    scope = 'user-follow-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    followList = sp.current_user_followed_artists()
    artists = followList['artists']['items']
    print("Artists followed by you:\n")
    for i,item in enumerate(artists):
        print("%d %s" %(i, item['name']))

def main(args):
    # setting the environment variable by reading from key value pair from .env file
    load_dotenv()
    if args.playlist            :listPlaylist()
    if args.name                :expandPlaylist(args.name)
    if args.artistFollowed      :listArtist()

if __name__ == "__main__":
    main()
