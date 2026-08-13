import os
import json

def load_json(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} not found")
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

class JSONHelper:
    @staticmethod
    def read(file_path):
        return load_json(file_path)

    @staticmethod
    def write(data, file_path):
        save_json(data, file_path)

    @staticmethod
    def merge(dict1, dict2):
        return merge_dicts(dict1, dict2)

    @staticmethod
    def flatten(nested_list):
        return flatten_list(nested_list)