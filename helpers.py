import json
from typing import Any, Dict, List, Union

def load_json(file_path: str) -> Union[Dict[str, Any], List[Any]]:
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json(data: Union[Dict[str, Any], List[Any]], file_path: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def merge_dicts(dict1: Dict, dict2: Dict) -> Dict:
    return {**dict1, **dict2}


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    return [item for sublist in nested_list for item in sublist]


def extract_values(data: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
    return {key: data[key] for key in keys if key in data}
