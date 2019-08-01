import base64
import six

def make_authorization_headers(client_id, client_secret):
  auth_header = base64.b64encode(six.text_type(client_id + ':' + client_secret).encode('ascii'))
  return {'Authorization': 'Basic %s' % auth_header.decode('ascii')}

def getTrackId(track):
  return track.get('id')

def getLatestTrackIds(authtoken):
  url = 'https://api.spotify.com/v1/browse/new-releases?limit=50'
  headers = {
    'content-type': 'application/json', 
    'Accept-Charset': 'UTF-8',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + authtoken
  }
  newReleases = requests.get(url, headers=headers)
  newReleasesContent = newReleases.json()['albums']['items']
  return list(map(getTrackId, newReleasesContent))

def getAudioFeatures(trackIds, accessToken):
  url = 'https://api.spotify.com/v1/audio-features'
  headers = { 'Authorization': 'Bearer ' + accessToken }
  params = { 'ids': ','.join([str(x) for x in trackIds]) }
  print(params)
  audioFeatures = requests.get(url, headers=headers, params=params)
  return audioFeatures.json()

def getTrackUri(track):
  return track.get('uri')