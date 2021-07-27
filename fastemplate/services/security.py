from fastapi import Header, Depends
from fastapi.security import OAuth2PasswordRequestForm

from fastemplate import logger
from fastemplate.objects.user import User
from fastemplate.module import MOCK_FRIDGE_USERS
from fastemplate.services.v1.fridge import oauth2_scheme
from fastemplate.exceptions.cart import InvalidTokenException
from fastemplate.exceptions.user import InvalidUsernameOrPassword, NiceTryMeowNowGoBack

def verify_token(x_token: str = Header(...)):
    """
    # TODO: docstring
    """
    real_token = "you-will-never-guess"
    if x_token != real_token:
        raise InvalidTokenException(message="X-Token header invalid")


def verify_key(x_key: str = Header(...)):
    """
    # TODO: docstring
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
    # TODO: docstring
    """
    return ''.join([LAZY_HASH_DICT[c] if c in LAZY_HASH_DICT else c for c in password])


def lazy_generate_token(username: str):
    """
    # TODO: docstring
    """
    return {"access_token": '___token___' + username, "token_type": "bearer"}


def lazy_decode_token(token:str):
    return token.replace('___token___', '')


def validate_user(form_data: OAuth2PasswordRequestForm):
    """
    # TODO: docstring
    """
    u_name = form_data.username
    u_pass = form_data.password
    if u_name not in MOCK_FRIDGE_USERS:
        logger.info(f'Invalid login attempt: {u_name}')
        raise InvalidUsernameOrPassword(message='Invalid username or passowrd.')
    if not lazy_password_hash(u_pass) == MOCK_FRIDGE_USERS[u_name]['hashed_password']:
        logger.info(f'Invalid login attempt: {u_name}')
        raise InvalidUsernameOrPassword(message='Invalid username or passowrd.')
    logger.info(f'Generating token to user: {MOCK_FRIDGE_USERS[u_name]["full_name"]}')
    return lazy_generate_token(username=u_name)


# from fastapi import HTTPException

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = lazy_decode_token(token)
    # if user not in MOCK_FRIDGE_USERS:
    #     raise HTTPException(
    #         status_code=401,
    #         detail="Invalid authentication credentials",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )
    return MOCK_FRIDGE_USERS[user]


def is_owner(user: User = Depends(get_current_user)):
    if not user['owner']:
        raise NiceTryMeowNowGoBack(message='You will not get any tuna today!')
    return user
