from ast import literal_eval
import os
import json


# Function to parse string to dictionary
def parse_dictionary(dictionary):
    for key_root, element_root in dictionary.items():
        try:
            dictionary[key_root] = literal_eval(element_root)
        except Exception as _:
            pass
    return dictionary


def get_settings(key=None):
    try:
        settings = parse_dictionary(json.loads(os.getenv('SETTINGS')))
    except Exception as e:
        with open('./app/settings.json') as f:
            settings = json.load(f)
    return settings[key] if key else settings
