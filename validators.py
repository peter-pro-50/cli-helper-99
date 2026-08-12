import re

def is_email_valid(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

def is_phone_number_valid(phone_number):
    regex = r'^\+?[1-9]\d{1,14}$'
    return re.match(regex, phone_number) is not None

def is_url_valid(url):
    regex = r'^(https?://)?(www\.)?([\w-]+\.)+[\w-]+(/\S*)?$'
    return re.match(regex, url) is not None

def is_integer(value):
    return isinstance(value, int)

def is_positive_integer(value):
    return is_integer(value) and value > 0

def is_float(value):
    return isinstance(value, float)

def is_non_empty_string(value):
    return isinstance(value, str) and len(value) > 0

def validate_user_input(user_input):
    if not is_non_empty_string(user_input):
        raise ValueError('Input should be a non-empty string')
    return True