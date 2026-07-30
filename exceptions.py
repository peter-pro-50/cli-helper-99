class CustomError(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors

class NotFoundError(CustomError):
    pass

class ValidationError(CustomError):
    def __init__(self, message, field):
        super().__init__(message)
        self.field = field

class DatabaseError(CustomError):
    pass


def raise_if_none(value, message):
    if value is None:
        raise CustomError(message)


def handle_exception(exc):
    if isinstance(exc, CustomError):
        print(f'Custom error occurred: {exc}')
    else:
        print('An unexpected error occurred:', exc)


def validate_age(age):
    if age < 0:
        raise ValidationError('Age cannot be negative', 'age')
    return True


def find_item(item_list, item):
    if item not in item_list:
        raise NotFoundError('Item not found in the list')
    return item_list[item_list.index(item)]
