import json

def process_json(document):
    d = json.dumps(document)
    d["rate"] = float(d["rate"])
    return d
