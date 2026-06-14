from plotly import offline

from data_fetch import get_earthquakes

eq_data = get_earthquakes()

lons = eq_data['lons']
lats = eq_data['lats']
mags = eq_data['mags']

data = {
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
}

my_layout = {
    'title': 'Earthquake Visualization'
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='earthquake_visualization.html')