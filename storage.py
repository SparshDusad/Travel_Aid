import json, os

def save_itinerary(name, data):
    path = "data/itineraries.json"
    if not os.path.exists("data"):
        os.mkdir("data")
    try:
        with open(path, 'r') as f:
            all_data = json.load(f)
    except:
        all_data = {}

    all_data[name] = data
    with open(path, 'w') as f:
        json.dump(all_data, f, indent=2)

def load_itinerary(name):
    with open("data/itineraries.json", 'r') as f:
        return json.load(f).get(name, "")
