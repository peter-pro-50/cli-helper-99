import json
from validators import validate_user_input

def process_data():
    while True:
        user_input = input('Enter data (or type exit to quit): ')
        if user_input.lower() == 'exit':
            break
        if not validate_user_input(user_input):
            print('Invalid input, please try again.')
            continue
        processed_data = json.loads(user_input)
        print(f'Processed Data: {processed_data}')

if __name__ == '__main__':
    process_data()