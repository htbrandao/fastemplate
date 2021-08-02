from fastapi import Depends, APIRouter

from fastemplate import logger
from fastemplate.module import fridge
from fastemplate.objects.user import User
from fastemplate.services import oauth2_scheme
from fastemplate.services.security import is_owner

router = APIRouter(dependencies=[Depends(oauth2_scheme)])


@router.get('/list_fridge')
def list_fridge():
    """
    Endpoint. List fridge items.

    :returns: dict with all frigde's items
    :rtype: dict
    """
    logger.info('Request@/list_fridge')
    return fridge.list_fridge()


@router.post('/BUY_ALL_TUNA_THERE_IS')
def buy_all_tuna(user: User = Depends(is_owner)):
    """
    Endpoint. Buys all wolrd's tuna!!!

    :returns: dict with message
    :rtype: dict
    """
    logger.info('Request@/buy_all_tuna_there_is')
    return {'user': f'{user["username"]}', 'message': 'You\'ve successfully bought all tuna in the world!'}


@router.get('/stream_temperature')
def stream_temperature():
    """
    Endpoint. Streams the fridge temperature.

    Encoded in `UTF-8`.

    :returns: fridge's temperature
    :rtype: bytes
    """
    return fridge.stream_temperature()
