# core.py
import os
import json

class FileManager:
    def __init__(self, base_path):
        self.base_path = base_path

    def read_file(self, filename):
        full_path = os.path.join(self.base_path, filename)
        with open(full_path, 'r') as file:
            return file.read()

    def write_file(self, filename, data):
        full_path = os.path.join(self.base_path, filename)
        with open(full_path, 'w') as file:
            file.write(data)

class JsonFileManager(FileManager):
    def read_json(self, filename):
        content = self.read_file(filename)
        return json.loads(content)

    def write_json(self, filename, data_dict):
        json_data = json.dumps(data_dict, indent=4)
        self.write_file(filename, json_data)

if __name__ == '__main__':
    fm = JsonFileManager('./data')
    fm.write_json('sample.json', {'key': 'value'})
    json_data = fm.read_json('sample.json')
    print(json_data)