from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer

from fastemplate import logger
from fastemplate.module import fridge
# from fastemplate.services.security import is_owner

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')

router = APIRouter()


@router.get('/list_fridge', dependencies=[Depends(oauth2_scheme)])
def list_fridge():
    """
    Endpoint. List fridge items.

    :returns: dict with all frigde's items
    :rtype: dict
    """
    logger.info('Request@/list_fridge')
    return fridge.list_fridge()


# TODO: dep is_owner, ban kitty from using
# @router.post('/buy_all_tuna_there_is', dependencies=Depends(is_owner))
@router.post('/buy_all_tuna_there_is')
def buy_all_tuna():
    """
    Endpoint. Buys all wolrd's tuna!!!

    :returns: dict with message
    :rtype: dict
    """
    logger.info('Request@/buy_all_tuna_there_is')
    return {'message': 'You\'ve successfully bought all tuna in the world!'}
