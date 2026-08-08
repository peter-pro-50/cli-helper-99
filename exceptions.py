class CustomError(Exception):
    """Base class for other exceptions."""
    pass

class ValueTooSmallError(CustomError):
    """Raised when the input value is too small."""
    def __init__(self, value):
        self.value = value
        super().__init__(f'Value {value} is too small')

class ValueTooLargeError(CustomError):
    """Raised when the input value is too large."""
    def __init__(self, value):
        self.value = value
        super().__init__(f'Value {value} is too large')

class InvalidInputError(CustomError):
    """Raised when the input is invalid."""
    def __init__(self, message):
        self.message = message
        super().__init__(message)

def process_value(value):
    if not isinstance(value, (int, float)):
        raise InvalidInputError('Input must be a number')
    if value < 10:
        raise ValueTooSmallError(value)
    if value > 100:
        raise ValueTooLargeError(value)
    return value * 2

if __name__ == '__main__':
    inputs = [5, 15, 200, 'abc']
    for inp in inputs:
        try:
            result = process_value(inp)
            print(f'Result: {result}')
        except CustomError as e:
            print(f'Error: {e}'