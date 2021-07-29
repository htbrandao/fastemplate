from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from fastemplate import logger
from fastemplate.objects.user import User
from fastemplate.services.security import validate_user, get_current_user

router = APIRouter()


@router.post('')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint. Performs login to acquire the bearer token.

    :param OAuth2PasswordRequestForm form_data: form with username and password
    :return: dict with access token and token type
    :rtype: dict
    """
    logger.info('Request@/login')
    return validate_user(form_data=form_data)


@router.get('/whois')
def whois(user: User = Depends(get_current_user)):
    """
    Endpoint. Checks if user has certain attributes (`enabled`).

    :params User user: form with user name and password
    :return: dict with user info
    :rtype: dict
    """
    logger.info('Request@/whois')
    return user
