import os
import sys

class CLIHelper:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, func):
        self.commands[name] = func

    def run(self, command_name, *args):
        if command_name in self.commands:
            return self.commands[command_name](*args)
        else:
            print(f"Command '{command_name}' not found.")

def greet(name):
    print(f"Hello, {name}!")

def farewell(name):
    print(f"Goodbye, {name}!")

if __name__ == '__main__':
    cli_helper = CLIHelper()
    cli_helper.add_command('greet', greet)
    cli_helper.add_command('farewell', farewell)

    if len(sys.argv) > 1:
        cli_helper.run(sys.argv[1], *sys.argv[2:])
    else:
        print('Please provide a command.')