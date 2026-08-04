def main_loop():
    while True:
        user_input = input('Enter a command: ')
        if validate_input(user_input):
            process_command(user_input)
        else:
            print('Invalid input. Please try again.')


def validate_input(user_input):
    valid_commands = ['start', 'stop', 'status', 'exit']
    return user_input in valid_commands


def process_command(command):
    if command == 'start':
        print('Starting...')
    elif command == 'stop':
        print('Stopping...')
    elif command == 'status':
        print('Current status...')
    elif command == 'exit':
        print('Exiting...')
        exit(0)


if __name__ == '__main__':
    main_loop()