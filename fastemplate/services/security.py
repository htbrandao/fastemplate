from fastapi import Header

from fastemplate.exceptions.cart import InvalidCredentialsException

def verify_token(x_token: str = Header(...)):
    """
    # TODO: docstring
    """
    real_token = "you-will-never-guess"
    if x_token != real_token:
        raise InvalidCredentialsException(message="X-Token header invalid")


def verify_key(x_key: str = Header(...)):
    """
    # TODO: docstring
    """
    real_key = "i-double-dare-you"
    if x_key != real_key:
        raise InvalidCredentialsException(message="X-Key header invalid")
