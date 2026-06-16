from plotly import offline

from processing import prepare_data

def draw_map(eq_data):

    lons = eq_data['lons']
    lats = eq_data['lats']
    mags = eq_data['mags']
    places = eq_data['places']
    depths = eq_data['depths']

    hover_text = [
            f"🌍{places}<br>"
            f"📊Magnitude: {mags}<br>"
            f"📍Depth: {depths}<br>"
            for places, mags, depths in zip(places, mags, depths)
        ]

    data = {
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_text,
        'hoverinfo': 'text',
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