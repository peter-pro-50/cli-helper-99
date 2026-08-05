from typing import Dict, Any

class Config:
    """
    A class to manage application configuration settings.
    """

    def __init__(self, config_data: Dict[str, Any]) -> None:
        """
        Initializes the configuration with provided data.
        
        :param config_data: A dictionary containing configuration settings.
        """
        self.config_data = config_data

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieves the value for a given key from the configuration.
        
        :param key: The configuration key to retrieve.
        :param default: The default value to return if the key does not exist.
        :return: The value associated with the key or the default value.
        """
        return self.config_data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Sets a configuration value for a given key.
        
        :param key: The configuration key to set.
        :param value: The value to associate with the key.
        """
        self.config_data[key] = value

    def load_from_file(self, filepath: str) -> None:
        """
        Loads configuration data from a JSON file.
        
        :param filepath: The path to the JSON configuration file.
        """
        import json
        with open(filepath, 'r') as file:
            self.config_data = json.load(file)

    def save_to_file(self, filepath: str) -> None:
        """
        Saves the current configuration data to a JSON file.
        
        :param filepath: The path to the JSON file to save the configuration.
        """
        import json
        with open(filepath, 'w') as file:
            json.dump(self.config_data, file, indent=4)