import re

def validate_email(email: str) -> bool:
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None


def validate_phone(phone: str) -> bool:
    regex = r'^(\+\d{1,3}[- ]?)?\d{10}$'
    return re.match(regex, phone) is not None


def validate_username(username: str) -> bool:
    return username.isalnum() and 3 <= len(username) <= 20


def validate_password(password: str) -> bool:
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return len(password) >= 8 and has_upper and has_lower and has_digit


def validate_url(url: str) -> bool:
    regex = r'^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/\S*)?$'
    return re.match(regex, url) is not None


def run_validations():
    # Example validations
    print(validate_email('test@example.com'))
    print(validate_phone('+1234567890'))
    print(validate_username('user123'))
    print(validate_password('Password1'))
    print(validate_url('https://example.com'))

if __name__ == '__main__':
    run_validations()