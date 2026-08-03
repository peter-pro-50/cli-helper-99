import os
import json


def load_json(file_path):
    """Load JSON file and return its contents."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    """Save data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def format_size(size_bytes):
    """Convert bytes to a human-readable size."""
    if size_bytes == 0:
        return '0 Bytes'
    size_units = ['Bytes', 'KB', 'MB', 'GB', 'TB']
    idx = int(log(size_bytes, 1024))
    pwr = 1024 ** idx
    size = round(size_bytes / pwr, 2)
    return f'{size} {size_units[idx]}'


def is_valid_email(email):
    """Check if the given string is a valid email address."""
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None
