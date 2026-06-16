def prepare_data(features):
    lons, lats, mags, places, depths = [], [], [], [], []
    for f in features:

        mag = float(f['properties']['mag'])
        if mag < 0 or mag is None:
            continue

        coords = f['geometry']['coordinates']

        places.append(f['properties']['place'])
        lons.append(coords[0])
        lats.append(coords[1])
        depths.append(coords[2])
        mags.append(mag)

    return {
        'lons': lons,
        'lats': lats,
        'mags': mags,
        'places': places,
        'depths': depths,
    }