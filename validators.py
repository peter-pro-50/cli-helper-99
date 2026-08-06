from typing import Any, Dict, Union

def validate_integer(value: Any) -> Union[int, None]:
    """
    Validates if the provided value is an integer.

    Args:
        value (Any): The value to validate.

    Returns:
        Union[int, None]: Returns the integer if valid, otherwise None.
    """
    if isinstance(value, int):
        return value
    return None


def validate_string(value: Any) -> Union[str, None]:
    """
    Validates if the provided value is a string.

    Args:
        value (Any): The value to validate.

    Returns:
        Union[str, None]: Returns the string if valid, otherwise None.
    """
    if isinstance(value, str):
        return value
    return None


def validate_dict(value: Any) -> Union[Dict[str, Any], None]:
    """
    Validates if the provided value is a dictionary.

    Args:
        value (Any): The value to validate.

    Returns:
        Union[Dict[str, Any], None]: Returns the dictionary if valid, otherwise None.
    """
    if isinstance(value, dict):
        return value
    return None


def validate_float(value: Any) -> Union[float, None]:
    """
    Validates if the provided value is a float.

    Args:
        value (Any): The value to validate.

    Returns:
        Union[float, None]: Returns the float if valid, otherwise None.
    """
    if isinstance(value, float):
        return value
    return None
