import re

def validate_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_phone(phone: str) -> bool:
    phone_regex = r'^\+?1?\d{9,15}$'
    return re.match(phone_regex, phone) is not None

def validate_url(url: str) -> bool:
    url_regex = r'^(http|https)://[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(/\S*)?$'
    return re.match(url_regex, url) is not None

def validate_password(password: str) -> bool:
    return (len(password) >= 8 and 
            any(char.isdigit() for char in password) and 
            any(char.isupper() for char in password) and 
            any(char.islower() for char in password))

# Example usage: 
# print(validate_email('test@example.com'))  # expected: True
# print(validate_phone('+1234567890'))      # expected: True
# print(validate_url('https://example.com')) # expected: True
# print(validate_password('StrongP@ss1'))    # expected: True
