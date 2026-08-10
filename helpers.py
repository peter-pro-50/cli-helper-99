from typing import List, Dict, Any


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """
    Flattens a nested list of arbitrary depth into a single list.

    Args:
        nested_list (List[List[Any]]): A list potentially containing nested lists.

    Returns:
        List[Any]: A flattened list containing all elements.
    """
    flat_list: List[Any] = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


def merge_dicts(dicts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Merges a list of dictionaries into a single dictionary.

    Args:
        dicts (List[Dict[str, Any]]): A list of dictionaries to merge.

    Returns:
        Dict[str, Any]: A dictionary containing all key-value pairs.
    """
    merged: Dict[str, Any] = {}
    for d in dicts:
        merged.update(d)
    return merged


def read_json_file(file_path: str) -> Dict[str, Any]:
    """
    Reads a JSON file and returns its content as a dictionary.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        Dict[str, Any]: The contents of the JSON file.
    """
    import json
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json_file(file_path: str, data: Dict[str, Any]) -> None:
    """
    Writes a dictionary to a JSON file.

    Args:
        file_path (str): The path where the JSON file will be saved.
        data (Dict[str, Any]): The data to write to the file.
    """
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)