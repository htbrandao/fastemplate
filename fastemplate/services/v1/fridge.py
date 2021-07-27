from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer

from fastemplate import logger
from fastemplate.module import fridge
from fastemplate.objects.user import User
# from fastemplate.services.security import is_owner

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')

router = APIRouter()


@router.get('/list_fridge', dependencies=[Depends(oauth2_scheme)])
def list_fridge():
    """
    # TODO: docstring
    """
    logger.info(f'Request@/list_fridge')
    return fridge.list_fridge()


# @router.post('/buy_all_tuna_there_is', dependencies=Depends(is_owner))
@router.post('/buy_all_tuna_there_is')
def buy_all_tuna():
    logger.info(f'Request@/buy_all_tuna_there_is')
    return {'message': 'You\'ve successfully bought all tuna in the world!'}
