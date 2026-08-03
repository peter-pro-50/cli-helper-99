import json
from collections import ChainMap

class ConfigLoader:
    def __init__(self, defaults=None):
        self.defaults = defaults or {}

    def load(self, file_path):
        try:
            with open(file_path, 'r') as f:
                user_config = json.load(f)
                combined_config = ChainMap(user_config, self.defaults)
                return dict(combined_config)
        except FileNotFoundError:
            return self.defaults
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON in configuration file.')

# Example usage
if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080}
    config_loader = ConfigLoader(defaults)
    config = config_loader.load('config.json')
    print(config)