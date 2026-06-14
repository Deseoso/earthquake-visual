import requests

def get_earthquakes():

    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

    params = {
        'format': "geojson",
        'starttime': "2026-06-13",
        'endtime': "2026-06-14"
    }

    eq_data = requests.get(url, params=params).json()

    return eq_data['features']

