from fastemplate.exceptions import FastemplateBaseException

class CartIdAlreadyExistsException(FastemplateBaseException):
    """
    Thrown whenever cart id already exists.
    """
    def __init__(self, message: str):
        name = 'CartIdAlreadyExistsException'
        super().__init__(503, message, name)

class CartIdNotFoundException(FastemplateBaseException):
    """
    Thrown whenever cart id does not exist.
    """
    def __init__(self, message: str):
        name = 'CartIdNotFoundException'
        super().__init__(404, message, name)

class ItemAlreadyAddedException(FastemplateBaseException):
    """
    Thrown whenever a cart's item already exists.
    """
    def __init__(self, message: str):
        name = 'ItemAlreadyAddedException'
        super().__init__(422, message, name)

class ItemNotFoundException(FastemplateBaseException):
    """
    Thrown whenever a cart's item is not found.
    """
    def __init__(self, message: str):
        name = 'ItemNotFoundException'
        super().__init__(404, message, name)

class MismatchedLenghtException(FastemplateBaseException):
    """
    Thrown whenever a list has more/less items then prices, and vice versa.
    """
    def __init__(self, message: str):
        name = 'MismatchedLenghtException'
        super().__init__(422, message, name)

class UnsupportedFileExtensionException(FastemplateBaseException):
    """
    Thrown whenever a list has more/less items then prices, and vice versa.
    """
    def __init__(self, message: str):
        name = 'UnsupportedFileExtension'
        super().__init__(415, message, name)
