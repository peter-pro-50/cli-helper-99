import re

def validate_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


def validate_phone(phone: str) -> bool:
    phone_regex = r'^(\+\d{1,3})?\d{10}$'
    return re.match(phone_regex, phone) is not None


def validate_url(url: str) -> bool:
    url_regex = r'^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/\S*)?$'
    return re.match(url_regex, url) is not None


def validate_integer(value: str) -> bool:
    return value.isdigit()


def validate_boolean(value: str) -> bool:
    return value.lower() in ['true', 'false']
