from datetime import datetime

from fastapi import APIRouter, Request

from fastemplate import logger
from fastemplate.utils import log_request_entries


router = APIRouter()


@router.get('/metrics')
def metrics():
    """
    Endpoint. Basic metrics endpoint.

    :return: dict with alive, @timestamp and no. of requests
    :rtype: dict
    """
    logger.info('Request@/metrics')
    return {
        'alive': True,
        '@timestamp': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
        'no. of requests': log_request_entries()
    }


@router.get('/explore_request')
def explore_request(request: Request):
    """
    Endpoint. Explore the request.

    :return: dict with alive, @timestamp and no. of requests
    :rtype: dict
    """
    logger.info('Request@/explore_request')
    return {
        'client': request.client,
        'cookies': request.cookies,
        'base_url': request.base_url,
        'headers': request.headers,
        'method': request.method,
        'query_params': request.query_params,
        'path_params': request.path_params
    }
