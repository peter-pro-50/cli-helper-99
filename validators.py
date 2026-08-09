import re

def is_valid_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def is_valid_phone(phone: str) -> bool:
    phone_regex = r'^(\+\d{1,3}[- ]?)?\d{10}$'
    return re.match(phone_regex, phone) is not None

def validate_user_info(email: str, phone: str) -> dict:
    validations = {
        'email': is_valid_email(email),
        'phone': is_valid_phone(phone),
    }
    return validations

if __name__ == '__main__':
    user_email = 'test@example.com'
    user_phone = '+1234567890'
    print(validate_user_info(user_email, user_phone))