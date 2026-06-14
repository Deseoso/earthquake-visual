from data_fetch import get_earthquakes

features = get_earthquakes()

def prepare_data():
    lons, lats, mags = [], [], []
    for f in features:
        coords = f['geometry']['coordinates']

        lons.append(coords[0])
        lats.append(coords[1])
        mags.append(f['properties']['mag'])

    return {
        'lons': lons,
        'lats': lats,
        'mags': mags
    }