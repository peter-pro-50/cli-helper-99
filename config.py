import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config = self.load_config(default_config_path)
        self.user_config = self.load_config(user_config_path)
        self.final_config = self.merge_configs(self.default_config, self.user_config)

    def load_config(self, path):
        if not os.path.exists(path):
            return {}
        with open(path, 'r') as config_file:
            return json.load(config_file)

    def merge_configs(self, default, user):
        config = default.copy()
        config.update(user)
        return config

    def get(self, key, default=None):
        return self.final_config.get(key, default)

# Example Usage
if __name__ == '__main__':
    loader = ConfigLoader('default_config.json', 'user_config.json')
    print(loader.get('some_setting', 'default_value'))
