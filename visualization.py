from plotly import offline


def draw_map(eq_data, map_title):

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
            'colorscale': 'YlOrRd',
            'reversescale': False,
            'colorbar': {'title': 'Magnitude'}
        }
    }

    my_layout = {
        'title': {
            'text': map_title,
            'font': {
                'size': 36,
                'color': '#1f2c56',
                'family': 'Courier New'
            },
            'x': 0.5
        },
        'geo': {
            'showland': True,
            'landcolor': "#89c47e",
            'showocean': True,
            'oceancolor': "rgb(200,220,255)",
            'showcountries': True,
            'showcoastlines': True,
        }
    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='earthquake_visualization.html')