from plotly import offline

from processing import prepare_data

def draw_map(eq_data):

    lons = eq_data['lons']
    lats = eq_data['lats']
    mags = eq_data['mags']

    data = {
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'marker': {
            'size': [mag*5 for mag in mags],
            'color': mags,
            'colorscale': 'Reds',
            'reversescale': False,
            'colorbar': {'title': 'Magnitude'}
        }
    }

    my_layout = {
        'title': 'Earthquake Visualization'
    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='earthquake_visualization.html')