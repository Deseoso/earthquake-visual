import requests


def get_earthquakes(time_data):

    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

    current_time = time_data['current_time']
    day_ago = time_data['day_ago']

    params = {
        'format': "geojson",
        'starttime': day_ago,
        'endtime': current_time
    }

    eq_data = requests.get(url, params=params).json()

    return eq_data['features']

