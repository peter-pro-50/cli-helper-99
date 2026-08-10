from typing import List, Dict, Any


def flatten_dict(nested_dict: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """
    Flattens a nested dictionary into a single level dictionary.

    Args:
        nested_dict (Dict[str, Any]): The dictionary to flatten.
        parent_key (str, optional): The base key for the flattened keys. Defaults to ''.
        sep (str, optional): The separator to use between keys. Defaults to '.'.

    Returns:
        Dict[str, Any]: A flattened dictionary.
    """
    items = []
    for k, v in nested_dict.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def list_to_dict(lst: List[str], key: str) -> Dict[str, str]:
    """
    Converts a list of strings into a dictionary using the specified key.

    Args:
        lst (List[str]): The list to convert.
        key (str): The key to use for the dictionary.

    Returns:
        Dict[str, str]: A dictionary with the specified key and list values.
    """
    return {item: key for item in lst}


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merges two dictionaries into one. If both dictionaries have the same key, the value from dict2 takes precedence.

    Args:
        dict1 (Dict[str, Any]): The first dictionary.
        dict2 (Dict[str, Any]): The second dictionary.

    Returns:
        Dict[str, Any]: The merged dictionary.
    """
    result = dict(dict1)  # Make a copy of dict1
    result.update(dict2)  # Update with dict2
    return result
