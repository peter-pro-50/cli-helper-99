import json
import os

DEFAULT_CONFIG = {
    'host': 'localhost',
    'port': 8080,
    'debug': False,
}

def load_config(filename='config.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            config = json.load(file)
            return {**DEFAULT_CONFIG, **config}
    return DEFAULT_CONFIG

if __name__ == '__main__':
    config = load_config()
    print(config)