from fastapi import Header, Depends
from fastapi.security import OAuth2PasswordRequestForm

from fastemplate import logger
from fastemplate.objects.user import User
from fastemplate.module import MOCK_FRIDGE_USERS
from fastemplate.services import oauth2_scheme
from fastemplate.exceptions.cart import InvalidTokenException
from fastemplate.exceptions.user import InvalidUsernameOrPassword, NiceTryMeowNowGoBack, InvalidAuthCredentials


def verify_token(x_token: str = Header(...)):
    """
    Validades `x_token` token from request header.

    :param str x_token: x_token
    :raises: InvalidTokenException
    """
    real_token = "you-will-never-guess"
    if x_token != real_token:
        raise InvalidTokenException(message="X-Token header invalid")


def verify_key(x_key: str = Header(...)):
    """
    Validades `x_key` token from request header.

    :param str x_key: x_key
    :raises: InvalidTokenException
    """
    real_key = "i-double-dare-you"
    if x_key != real_key:
        raise InvalidTokenException(message="X-Key header invalid")


LAZY_HASH_DICT = {
    'a': '4', 'e': '3', 'i': '1', 'o': '0', 't': '7',
    'A': '4', 'E': '3', 'I': '1', 'O': '0', 'T': '7'
}


def lazy_password_hash(password: str):
    """
    Performs a string hashing. This is **not** a good way to handle hashing.

    :param str password: string to hash
    :return: hashed str
    :rtype: str
    """
    return ''.join([LAZY_HASH_DICT[c] if c in LAZY_HASH_DICT else c for c in password])


def lazy_generate_token(username: str):
    """
    Generates a token given a username. This is **not** a good way to handle token creation.

    :param str username: string to hash
    :return: dict with access token and token type
    :rtype: dict
    """
    return {"access_token": '___token___' + username, "token_type": "bearer"}


def lazy_decode_token(token: str):
    """
    Retrieves a username from a given token. This is **not** a good way to handle token validation.

    :param str token: token string
    :return: username
    :rtype: str
    """
    return token.replace('___token___', '')


def validate_user(form_data: OAuth2PasswordRequestForm):
    """
    Validate the user's credentials to generate a token that will be used to interact with the API.

    :param form_data: form with username and password fields
    :return: dict with access token and token type
    :rtype: dict
    :raises: InvalidUsernameOrPassword
    """
    u_name = form_data.username
    u_pass = form_data.password
    if u_name not in MOCK_FRIDGE_USERS:
        logger.info(f'Invalid login attempt: {u_name}')
        raise InvalidUsernameOrPassword(message='Invalid username or password.')
    if not lazy_password_hash(u_pass) == MOCK_FRIDGE_USERS[u_name]['hashed_password']:
        logger.info(f'Invalid login attempt: {u_name}')
        raise InvalidUsernameOrPassword(message='Invalid username or password.')
    logger.info(f'Generating token to user: {MOCK_FRIDGE_USERS[u_name]["full_name"]}')
    return lazy_generate_token(username=u_name)


def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Extract the user from a token request.

    :param str token: token str
    :return: dict with user information
    :rtype: dict
    """
    user = lazy_decode_token(token)
    if user not in MOCK_FRIDGE_USERS:
        raise InvalidAuthCredentials(message='Invalid authentication credentials: {"WWW-Authenticate": "Bearer"}')
    return MOCK_FRIDGE_USERS[user]


def is_owner(user: User = Depends(get_current_user)):
    """
    Checks `owner` attribute from a given user or if my cat is trying to user auth protected endpoints.

    :param User user: user object
    :return: user object
    :rtype: User
    :raises: NiceTryMeowNowGoBack
    """
    if not user['owner']:
        raise NiceTryMeowNowGoBack(message='You will not get any tuna today!')
    return user
