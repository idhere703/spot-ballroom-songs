import os, requests
from utils import make_authorization_headers

def getAccessToken():
  clientId = os.environ['SPOTIFY_CLIENT_ID']
  secretKey = os.environ['SPOTIFY_SECRET_KEY']
  url = 'https://accounts.spotify.com/api/token'
  headers = make_authorization_headers(clientId, secretKey)
  data = { 'grant_type': 'client_credentials' }
  response = requests.post(url, headers=headers, data=data, verify=True)
  content = response.json()
  return content['access_token']