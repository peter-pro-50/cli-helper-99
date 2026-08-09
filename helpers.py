import sys

class InputError(Exception):
    pass

def validate_input(user_input):
    if not user_input:
        raise InputError('Input cannot be empty')
    if not user_input.isalpha():
        raise InputError('Input must contain only alphabetic characters')

def main_loop():
    while True:
        user_input = input('Enter a command: ')
        try:
            validate_input(user_input)
            print(f'You entered: {user_input}')
        except InputError as e:
            print(f'Error: {e}')
        except KeyboardInterrupt:
            print('\nExiting program.')
            sys.exit(0)

if __name__ == '__main__':
    main_loop()