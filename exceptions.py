class CustomError(Exception):
    """Base class for other exceptions."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class ValidationError(CustomError):
    """Raised when a validation check fails."""
    def __init__(self, message):
        super().__init__(message)

class NotFoundError(CustomError):
    """Raised when a resource is not found."""
    def __init__(self, resource):
        message = f'{resource} not found.'
        super().__init__(message)

class PermissionDeniedError(CustomError):
    """Raised when permission is denied."""
    def __init__(self, action):
        message = f'Permission denied for action: {action}'
        super().__init__(message)

class ConfigurationError(CustomError):
    """Raised for configuration issues."""
    def __init__(self, setting):
        message = f'Configuration issue with setting: {setting}'
        super().__init__(message)
