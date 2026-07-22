import json
import os

class ConfigLoader:
    def __init__(self, default_config_path='default_config.json'):
        self.default_config_path = default_config_path
        self.config = self.load_config()

    def load_config(self):
        try:
            with open(self.default_config_path, 'r') as file:
                config = json.load(file)
        except FileNotFoundError:
            config = {}
        config.update(self.load_env_variables())
        return config

    def load_env_variables(self):
        return {key: os.getenv(key) for key in self.get_env_keys()}

    def get_env_keys(self):
        return [key for key in self.config.keys() if key.startswith('APP_')]

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage
if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.get('APP_NAME', 'Default App'))