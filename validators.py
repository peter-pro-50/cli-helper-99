import re

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError("Input must be a string.")
    if len(user_input) == 0:
        raise ValueError("Input cannot be empty.")
    if not re.match("^[a-zA-Z0-9_]*$, user_input):
        raise ValueError("Input can only contain alphanumeric characters and underscores.")
    return True


def main_processing_loop():
    while True:
        try:
            user_input = input("Enter your input (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break
            validate_input(user_input)
            print(f"Valid input received: {user_input}")
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main_processing_loop()