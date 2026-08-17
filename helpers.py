import json
from typing import Any, Dict, Union


def validate_data(data: Dict[str, Any], schema: Dict[str, type]) -> bool:
    for key, expected_type in schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False
    return True


def merge_dicts(*dicts: Dict[str, Any]) -> Dict[str, Any]:
    result = {}
    for d in dicts:
        result.update(d)
    return result


def filter_by_value(data: Dict[str, Any], filter_value: Any) -> Dict[str, Any]:
    return {k: v for k, v in data.items() if v == filter_value}


def json_to_dict(json_str: str) -> Union[Dict[str, Any], None]:
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return None


def dict_to_json(data: Dict[str, Any]) -> str:
    return json.dumps(data, indent=4)