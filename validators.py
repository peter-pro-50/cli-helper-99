import re

def is_valid_email(email: str) -> bool:
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(regex, email) is not None


def is_valid_phone(phone: str) -> bool:
    regex = r'^(\+?\d{1,3}[- ]?)?\(?\d{1,4}?\)?[- ]?\d{1,4}[- ]?\d{1,9}$'
    return re.match(regex, phone) is not None


def is_positive_integer(value: str) -> bool:
    return value.isdigit() and int(value) > 0


def is_valid_url(url: str) -> bool:
    regex = r'^(http|https):\/\/[\w.-]+(\/[\w.-]*)*$'
    return re.match(regex, url) is not None


def is_valid_date(date_string: str) -> bool:
    regex = r'^(\d{4})-(\d{2})-(\d{2})$'
    if not re.match(regex, date_string):
        return False
    year, month, day = map(int, date_string.split('-'))
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    return True
