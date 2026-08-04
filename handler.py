import sys
import traceback

class CLIError(Exception):
    pass

def handle_exception(exc):
    print(f"Error: {exc}")
    print(traceback.format_exc())
    sys.exit(1)

def process_input(user_input):
    if not isinstance(user_input, str):
        raise CLIError('Input must be a string')
    if len(user_input) == 0:
        raise CLIError('Input cannot be empty')
    if user_input.lower() == 'exit':
        print('Exiting...')
        sys.exit(0)
    return f'Processed input: {user_input}'

if __name__ == '__main__':
    try:
        user_input = input('Enter something: ')
        result = process_input(user_input)
        print(result)
    except CLIError as e:
        handle_exception(e)