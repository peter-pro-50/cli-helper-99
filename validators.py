import re

def validate_integer(value):
    if not isinstance(value, int):
        raise ValueError(f'Expected integer but got {type(value).__name__}')
    return True


def validate_non_empty_string(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('Expected non-empty string')
    return True


def validate_email(value):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, value):
        raise ValueError('Invalid email format')
    return True


def validate_positive_float(value):
    if not isinstance(value, float) or value <= 0:
        raise ValueError('Expected positive float')
    return True


def validate_list_of_strings(value):
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError('Expected a list of strings')
    return True