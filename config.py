import json
import os

class ConfigLoader:
    def __init__(self, default_config, custom_config_path=None):
        self.default_config = default_config
        self.custom_config_path = custom_config_path
        self.config = self.load_config()

    def load_config(self):
        config = self.default_config.copy()
        if self.custom_config_path and os.path.exists(self.custom_config_path):
            with open(self.custom_config_path, 'r') as file:
                try:
                    custom_config = json.load(file)
                    config.update(custom_config)
                except json.JSONDecodeError:
                    print('Invalid JSON in custom configuration file.')
        return config

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage
if __name__ == '__main__':
    default_config = {
        'host': 'localhost',
        'port': 8080,
        'debug': True
    }
    loader = ConfigLoader(default_config, 'custom_config.json')
    print(loader.get('host'))
    print(loader.get('port'))
    print(loader.get('debug'))
    