import json

def load_json(filepath):
    """Loads a JSON file and returns its content."""
    with open(filepath, 'r') as file:
        return json.load(file)

def save_json(filepath, data):
    """Saves data to a JSON file."""
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def update_json(filepath, updates):
    """Updates a JSON file with given data."""
    data = load_json(filepath)
    data.update(updates)
    save_json(filepath, data)

if __name__ == '__main__':
    # Example usage
    sample_data = {'name': 'cli-helper-99', 'version': 1.0}
    save_json('data.json', sample_data)
    print(load_json('data.json'))
    update_json('data.json', {'version': 2.0})
    print(load_json('data.json'))
