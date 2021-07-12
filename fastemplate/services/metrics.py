from datetime import datetime

from fastapi import APIRouter

from fastemplate import logger
from fastemplate.utils import log_request_entries


router = APIRouter()


@router.get('/metrics')
def metrics():
    """
    Basic metrics endpoint.

    :return: dict
    """
    logger.info('Request @ /metrics')
    return {
        'alive': True,
        '@timestamp': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
        'no. of requests': log_request_entries()
    }
