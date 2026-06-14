import requests


url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

params = {
    'format': "geojson",
    'starttime': "2026-06-13",
    'endtime': "2026-06-14"
}

data = requests.get(url, params=params).json()

print(len(data['features']))
print(data['features'][0])