import requests

from data_fetch import get_earthquakes

features = get_earthquakes()

print(len(features))
print(features[0])

for f in features[:5]:
    print(f['properties']['mag'], f['properties']['place'])



