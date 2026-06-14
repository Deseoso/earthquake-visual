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

for f in data['features'][:5]:
    print(f['properties']['mag'], f['properties']['place'])

lons, lats, mags  = [], [], []
for f in data['features']:
    coords = f['geometry']['coordinates']

    lons.append(coords[0])
    lats.append(coords[1])
    mags.append(f['properties']['mag'])

