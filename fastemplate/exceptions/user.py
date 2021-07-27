from fastemplate.exceptions import FastemplateBaseException

class InvalidUsernameOrPassword(FastemplateBaseException):
    """
    Thrown whenever user credentials are wrong.
    """
    def __init__(self, message: str):
        name = 'InvalidUsernameOrPassword'
        super().__init__(400, message, name)


class NiceTryMeowNowGoBack(FastemplateBaseException):
    """
    Thrown whenever my cat tries to login as owner.
    """
    def __init__(self, message: str):
        name = 'NiceTryMeowNowGoBack'
        super().__init__(401, message, name)
