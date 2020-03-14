import requests
import webbrowser

GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

params = {'address' : 'ho chi minh', 'key' : ''}

req = requests.get(GOOGLE_MAPS_API_URL, params=params)
print(req.url)


res = req.json()['results']
location = res[0]['geometry']['location']
location['lat']
location['lng']
print(location['lat'], location['lng'])


