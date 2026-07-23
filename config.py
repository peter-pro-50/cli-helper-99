import json
import os

class ConfigLoader:
    def __init__(self, defaults=None):
        self.defaults = defaults or {}
        self.config = self.defaults.copy()

    def load_from_file(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f'Config file not found: {filepath}')
        with open(filepath, 'r') as file:
            file_config = json.load(file)
            self.config.update(file_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

# Example defaults
DEFAULTS = {
    'host': 'localhost',
    'port': 8080,
    'debug': False,
}

# Usage example
if __name__ == '__main__':
    loader = ConfigLoader(DEFAULTS)
    loader.load_from_file('config.json')
    print(f'Host: {loader.get("host")}, Port: {loader.get("port")}', end='')