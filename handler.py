import sys
import json

def validate_input(user_input):
    if not user_input:
        raise ValueError('Input cannot be empty')
    if not user_input.isalnum():
        raise ValueError('Input must be alphanumeric')

    return user_input

def main_loop():
    print('Enter your input:')
    while True:
        user_input = input('> ')
        try:
            validated_input = validate_input(user_input)
            print(f'Valid input received: {validated_input}')
            break
        except ValueError as e:
            print(f'Error: {e}. Please try again.')

if __name__ == '__main__':
    main_loop()