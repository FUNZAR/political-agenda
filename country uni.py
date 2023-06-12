import country_converter as coco
import json


with open() as f:
    data = json.load(f)

    for key in data.keys():
        if 'BREAK' in data[key]:
            del data[key]['BREAK']
        if 'TRANSCRIPT' in data[key]:
            del data[key]['TRANSCRIPT']
        if 'COVID-19' in data[key]:
            del data[key]['COVID-19']
        if 'COVID' in data[key]:
            del data[key]['COVID']
    with () as f:
        json.dump(data, f, indent=4)