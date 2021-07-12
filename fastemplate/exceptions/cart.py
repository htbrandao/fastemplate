from fastemplate.exceptions import FastemplateBaseException


class CartIdAlreadyExistsException(Exception):
    """
    Thrown whenever cart id already exists.
    """
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        self.name = 'CartIdAlreadyExistsException'


class CartIdNotFoundException(Exception):
    """
    Thrown whenever cart id does not exist.
    """
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        self.name = 'CartIdNotFoundException'


class ItemAlreadyAddedException(Exception):
    """
    Thrown whenever a cart's item already exists.
    """
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        self.name = 'ItemAlreadyAddedException'


class ItemNotFoundException(Exception):
    """
    Thrown whenever a cart's item is not found.
    """
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        self.name = 'ItemNotFoundException'


class MismatchedLenghtException(Exception):
    """
    Thrown whenever a list has more/less items then prices, and vice versa.
    """
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        self.name = 'MismatchedLenghtException'
