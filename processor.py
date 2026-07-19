import re

class DataProcessor:
    def __init__(self):
        self.regex_pattern = re.compile(r'^[a-zA-Z0-9_]{3,20}$')

    def validate_input(self, user_input):
        if self.regex_pattern.match(user_input):
            return True
        raise ValueError('Input must be alphanumeric and 3-20 characters long')

    def process_data(self, inputs):
        validated_inputs = []
        for user_input in inputs:
            try:
                self.validate_input(user_input)
                validated_inputs.append(user_input)
            except ValueError as e:
                print(f'Error: {e}')  
        return validated_inputs

if __name__ == '__main__':
    dp = DataProcessor()
    sample_inputs = ['validInput1', '123', 'invalid-input!', 'short', 'a'*21]
    print(dp.process_data(sample_inputs))
