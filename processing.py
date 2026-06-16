from data_fetch import get_earthquakes


def prepare_data(features):
    lons, lats, mags, hover_text = [], [], [], []
    for f in features:

        mag = float(f['properties']['mag'])
        if mag < 0 or mag is None:
            continue

        coords = f['geometry']['coordinates']

        hover_text.append(f['properties']['place'])
        lons.append(coords[0])
        lats.append(coords[1])
        mags.append(mag)

    return {
        'lons': lons,
        'lats': lats,
        'mags': mags,
        'hover_text': hover_text,
    }