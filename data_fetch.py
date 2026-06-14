import requests

def get_earthquakes():

    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

    params = {
        'format': "geojson",
        'starttime': "2026-06-13",
        'endtime': "2026-06-14"
    }

    eq_data = requests.get(url, params=params).json()

    lons, lats, mags  = [], [], []
    for f in eq_data['features']:
        coords = f['geometry']['coordinates']

        lons.append(coords[0])
        lats.append(coords[1])
        mags.append(f['properties']['mag'])

    return {
        'features': eq_data['features'],
        'lons': lons,
        'lats': lats,
        'mags': mags
    }
