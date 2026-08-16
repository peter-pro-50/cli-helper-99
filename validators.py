import re

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string.')
    if not user_input:
        raise ValueError('Input cannot be empty.')
    if len(user_input) < 3:
        raise ValueError('Input must be at least 3 characters long.')
    if not re.match('^[a-zA-Z0-9_]*$', user_input):
        raise ValueError('Input can only contain alphanumeric characters and underscores.')
    return True

if __name__ == '__main__':
    while True:
        user_input = input('Enter your input: ')
        try:
            validate_input(user_input)
            print('Valid input:', user_input)
            break
        except ValueError as ve:
            print('Error:', ve)