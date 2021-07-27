from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from fastemplate import logger
from fastemplate.objects.user import User
from fastemplate.services.security import validate_user, is_owner


router = APIRouter()


@router.post('')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    # TODO: docstring
    """
    logger.info(f'Request@/login')
    return validate_user(form_data=form_data)


@router.get('/whois')
def whois(user: User = Depends(is_owner)):
    logger.info(f'Request@/whois')
    return user
