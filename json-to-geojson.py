#! usr/bin/env python

# Take an input normal json file with point coords, retrieve the coords and wrap the json in the correct format.
# Output as geojson format for use in your preferred GIS system.
# Developed for Python 3.x.

# Run this script from the command line:
# eg.   python .\json-to-geojson.py <in_json.json> <out_geojson.json>

from sys import argv
from os.path import exists
import simplejson as json 

script, in_file, out_file = argv

data = json.load(open(in_file))

geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["longitude"], d["latitude"]],
            },
        "properties" : d,
     } for d in data]
}


output = open(out_file, 'w')
json.dump(geojson, output)

print(geojson)
print("Done")