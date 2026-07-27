class CustomError(Exception):
    """Base class for exceptions in this module."""
    pass

class ValidationError(CustomError):
    """Raised when validation fails."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class ProcessingError(CustomError):
    """Raised when an error occurs during processing."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class ConfigurationError(CustomError):
    """Raised when there is a configuration issue."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class NotFoundError(CustomError):
    """Raised when an expected item is not found."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class TimeoutError(CustomError):
    """Raised when an operation times out."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message