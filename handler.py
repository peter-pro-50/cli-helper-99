import json

class DataHandler:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        return [self._transform(item) for item in self.data]

    def _transform(self, item):
        if isinstance(item, dict):
            return {k: self._clean_value(v) for k, v in item.items()}
        return self._clean_value(item)

    def _clean_value(self, value):
        if isinstance(value, str):
            return value.strip().lower()
        if isinstance(value, list):
            return [self._clean_value(v) for v in value]
        return value

    def to_json(self):
        return json.dumps(self.process_data(), indent=2)

# Example usage
if __name__ == '__main__':
    data = [{' Name ': ' Alice ', ' Age ': 30, ' Hobbies ': [' Reading ', ' Traveling ']}, {' Name ': ' Bob ', ' Age ': 25}]
    handler = DataHandler(data)
    print(handler.to_json())