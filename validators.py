import re

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string.')  
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty.')  
    if not re.match('^[A-Za-z0-9_ ]+$', user_input):
        raise ValueError('Input contains invalid characters.')  
    return True


def main_processing_loop():
    while True:
        try:
            user_input = input('Enter your command: ')
            validate_input(user_input)
            # Process the validated input here
            print(f'Processing: {user_input}')  
        except ValueError as ve:
            print(f'Input error: {ve}')  
        except KeyboardInterrupt:
            print('\nExiting the program.')
            break

if __name__ == '__main__':
    main_processing_loop()