import re

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_positive_integer(value: str) -> bool:
    return value.isdigit() and int(value) > 0


def validate_choice(value: str, choices: list) -> bool:
    return value in choices


def validate_inputs(email: str, age: str, choice: str, choices: list) -> dict:
    errors = []
    if not validate_email(email):
        errors.append('Invalid email format.')
    if not validate_positive_integer(age):
        errors.append('Age must be a positive integer.')
    if not validate_choice(choice, choices):
        errors.append('Choice must be one of the predefined options.')
    return {'is_valid': not errors, 'errors': errors}


if __name__ == '__main__':
    # Sample input loop for demonstration
    choices = ['option1', 'option2', 'option3']
    while True:
        email = input('Enter your email: ')
        age = input('Enter your age: ')
        choice = input('Choose an option (option1/option2/option3): ')
        validation_result = validate_inputs(email, age, choice, choices)
        if validation_result['is_valid']:
            print('Inputs are valid!')
            break
        else:
            print('Errors:', validation_result['errors'])