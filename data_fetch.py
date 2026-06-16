import requests
from datetime import datetime, timedelta


def get_time():
    current_time = datetime.utcnow()
    day_ago = current_time - timedelta(hours=24)

    return {
        'current_time': current_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'day_ago': day_ago.strftime("%Y-%m-%dT%H:%M:%S")
    }

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

