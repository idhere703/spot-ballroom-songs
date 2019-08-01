import argparse, spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from filters import waltzFilter, salsaFilter, rumbaFilter, chaChaFilter
from utils import getTrackUri

def getTrackUrl(track):
    return track.get("external_urls").get("spotify")

def getPlaylistTracks(username, playlist_id, spotifyAPI):
    offset = 0
    songs = []
    content = { 'next': True }
    while (content['next'] is not None):
        content = spotifyAPI.user_playlist_tracks(username, playlist_id, fields=None, limit=100, offset=offset, market=None)
        songs += content['items']
        offset += 100
    return songs

def getPlaylistAudioFeatures(username, playlist_id, spotifyAPI):
    ids = []
    songs = getPlaylistTracks(username, playlist_id, spotifyAPI)

    for i in songs:
        ids.append(i['track']['id'])

    index = 0
    audio_features = []
    while index < len(ids):
        audio_features += spotifyAPI.audio_features(ids[index:index + 50])
        index += 50
    return audio_features


def getUserPlaylists(username, spotify):
    results = []
    playlists = sp.user_playlists(username)
    while playlists:
        results += playlists['items']
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
    return results

def main(username, playlistId, spotifyAPI):
    playlistAudioFeatures = getPlaylistAudioFeatures(username, playlistId, spotifyAPI)
    waltzSongs = list(map(getTrackUri, filter(waltzFilter, playlistAudioFeatures)))
    rumbaSongs = list(map(getTrackUri, filter(rumbaFilter, playlistAudioFeatures)))
    chaChaSongs = list(map(getTrackUri, filter(chaChaFilter, playlistAudioFeatures)))
    salsaSongs = list(map(getTrackUri, filter(salsaFilter, playlistAudioFeatures)))

    print('Waltz found', len(waltzSongs), waltzSongs)
    print('====================')
    print('Rumba found', len(rumbaSongs), rumbaSongs)
    print('====================')
    print('Cha Cha found', len(chaChaSongs), chaChaSongs)
    print('====================')
    print('Salsa found', len(salsaSongs), salsaSongs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='description')
    parser.add_argument('--username', help='username')
    parser.add_argument('--playlist', help='playlistId')
    args = parser.parse_args()
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    main(args.username, args.playlist, sp)