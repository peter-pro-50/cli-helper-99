import os
import json
import shutil
from typing import Any, Dict

def read_json(file_path: str) -> Dict[str, Any]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def copy_file(src: str, dst: str) -> None:
    if not os.path.isfile(src):
        raise FileNotFoundError(f"{src} does not exist")
    shutil.copy2(src, dst)


def ensure_directory_exists(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def flatten_nested_dict(nested_dict: Dict) -> Dict[str, Any]:
    flat_dict = {}
    def flatten(x: Dict, parent_key: str = ''):
        for k, v in x.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            if isinstance(v, dict):
                flatten(v, new_key)
            else:
                flat_dict[new_key] = v
    flatten(nested_dict)
    return flat_dict
