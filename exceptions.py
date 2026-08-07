class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class NotFoundError(CustomError):
    def __init__(self, resource):
        super().__init__(f'Resource not found: {resource}')
        self.resource = resource

class InvalidInputError(CustomError):
    def __init__(self, input_value, reason):
        super().__init__(f'Invalid input: {input_value}. Reason: {reason}')
        self.input_value = input_value
        self.reason = reason

class DatabaseConnectionError(CustomError):
    def __init__(self, db_url):
        super().__init__(f'Failed to connect to database at: {db_url}')
        self.db_url = db_url

class TimeoutError(CustomError):
    def __init__(self, operation):
        super().__init__(f'Timeout occurred during: {operation}')
        self.operation = operation
