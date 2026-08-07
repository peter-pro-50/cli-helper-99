import re

class InputValidationError(Exception):
    pass

class InputValidator:
    def __init__(self, expected_type: type):
        self.expected_type = expected_type

    def validate(self, user_input: str) -> None:
        if not isinstance(user_input, str):
            raise InputValidationError('Input must be a string')
        if self.expected_type == int:
            self._validate_int(user_input)
        elif self.expected_type == float:
            self._validate_float(user_input)
        elif self.expected_type == str:
            self._validate_string(user_input)
        else:
            raise InputValidationError('Unsupported type for validation')

    def _validate_int(self, user_input: str) -> None:
        if not re.fullmatch(r'-?\d+', user_input):
            raise InputValidationError('Input must be a valid integer')

    def _validate_float(self, user_input: str) -> None:
        if not re.fullmatch(r'-?\d+(\.\d+)?', user_input):
            raise InputValidationError('Input must be a valid float')

    def _validate_string(self, user_input: str) -> None:
        if len(user_input) == 0:
            raise InputValidationError('Input cannot be empty')


def main_processing_loop():
    validator = InputValidator(int)
    while True:
        user_input = input('Enter a number: ')
        try:
            validator.validate(user_input)
            print(f'Validated input: {user_input}')
            break
        except InputValidationError as e:
            print(e)

if __name__ == '__main__':
    main_processing_loop()