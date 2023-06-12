import json
import os

folder_path =
for file_name in os.listdir(folder_path):
    if file_name.endswith('.json'):
        with open(os.path.join(folder_path, file_name), 'r') as f:
            data = json.load(f)

        person_list = []
        norp_list = []
        org_list = []
        gpe_list = []

        for entity in data["Entities"]:
            if "PERSON" in entity:
                person_list.append(entity["PERSON"])
            if "NORP" in entity:
                norp_list.append(entity["NORP"])
            if "ORG" in entity:
                org_list.append(entity["ORG"])
            if "GPE" in entity:
                gpe_list.append(entity["GPE"])

        data['Entities'] = [
            {
                'PERSON': person_list,
                'NORP': norp_list,
                'ORG': org_list,
                "GPE": gpe_list
            }
        ]

        with open(os.path.join(folder_path, file_name), 'w') as f:
            json.dump(data, f, indent=4)
