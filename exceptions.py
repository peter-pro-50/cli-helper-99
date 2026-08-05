class CustomError(Exception):
    """Base class for other exceptions."""
    pass

class NotFoundError(CustomError):
    """Exception raised for not found errors."""
    def __init__(self, resource):
        self.resource = resource
        self.message = f'{resource} not found'
        super().__init__(self.message)

class ValidationError(CustomError):
    """Exception raised for validation errors."""
    def __init__(self, errors):
        self.errors = errors
        self.message = f'Validation failed: {errors}'
        super().__init__(self.message)

class ConfigurationError(CustomError):
    """Exception raised for configuration-related errors."""
    def __init__(self, config_item):
        self.config_item = config_item
        self.message = f'Invalid configuration for {config_item}'
        super().__init__(self.message)

class DatabaseError(CustomError):
    """Exception raised for database errors."""
    def __init__(self, db_action):
        self.db_action = db_action
        self.message = f'Database error during {db_action}'
        super().__init__(self.message)