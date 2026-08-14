class CustomError(Exception):
    """Base class for other exceptions."""
    pass

class ValueTooHighError(CustomError):
    """Raised when the input value is too high."""
    def __init__(self, value, message="Value is too high!"): 
        self.value = value
        self.message = message
        super().__init__(self.message)

class ValueTooLowError(CustomError):
    """Raised when the input value is too low."""
    def __init__(self, value, message="Value is too low!"):
        self.value = value
        self.message = message
        super().__init__(self.message)

class InvalidInputError(CustomError):
    """Raised when the input is not valid."""
    def __init__(self, value, message="Invalid input provided!"):
        self.value = value
        self.message = message
        super().__init__(self.message)

def validate_value(value):
    if value < 10:
        raise ValueTooLowError(value)
    elif value > 100:
        raise ValueTooHighError(value)
    elif not isinstance(value, (int, float)):
        raise InvalidInputError(value)
    return True