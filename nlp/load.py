import json, os

DATA_DIR = os.path.join("castles_and_chambers_3", "nlp", "data")
json_files = os.listdir(DATA_DIR)

for i in json_files:
    if not i.endswith(".json"): continue
    with open(os.path.join(DATA_DIR, i)) as f:
        vars()[i.split(".")[0].upper()] = json.load(f)