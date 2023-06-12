import country_converter as coco
import json
import pycountry


with open() as f:
    data = json.load(f)

result = []

states = list(pycountry.countries)
states_names = [state.name for state in states]

for date, countries in data.items():
    for country, count in countries.items():
        converted_countries = coco.convert(names=[country], to='name_short')
        if country != states_names:
            result.append({'date': date, 'state': country, 'count': count})
with open() as f:
    json.dump(result, f, indent=4)