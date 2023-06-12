import spacy
import json
import os

nlp = spacy.load('en_core_web_sm')
nlp.max_length = 3000000
folder_path =

for file_name in os.listdir(folder_path):
    if file_name.endswith('.json'):
        with open(os.path.join(folder_path,file_name), 'r') as f:
            data = json.load(f)
        text = data['Text']
        doc = nlp(text)
        ner_data = [{ent.label_: ent.text} for ent in doc.ents]
        data['Entities'] = ner_data
        with open(os.path.join(folder_path,file_name), 'w') as f:
            json.dump(data, f, indent=4)
