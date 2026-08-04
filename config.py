import json
import os

class ConfigLoader:
    def __init__(self, default_config=None):
        self.default_config = default_config if default_config else {}
        self.user_config = {}

    def load_config(self, config_path):
        if os.path.exists(config_path):
            with open(config_path, 'r') as config_file:
                self.user_config = json.load(config_file)
        else:
            print(f'Config file {config_path} not found. Using defaults.')

    def get_config(self):
        return {**self.default_config, **self.user_config}

# Example default config
default_settings = {
    'logging_level': 'INFO',
    'max_connections': 10,
    'timeout': 30
}

# Usage
config_loader = ConfigLoader(default_settings)
config_loader.load_config('config.json')
final_config = config_loader.get_config()
print(final_config)