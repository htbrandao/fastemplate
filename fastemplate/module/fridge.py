from time import sleep
from random import choice

from fastapi.responses import StreamingResponse

from fastemplate.module import MOCK_FRIDGE, MOCK_CELSIUS_TEMPERATURES


def list_fridge():
    """
    List all items in the frigde.

    :return: dict with all items and amounts
    :rtype: dict
    """
    return MOCK_FRIDGE


def get_temperature():
    """
    Yields a mock fridge temperature.
    
    return: fridge temperature encoded in utf-8
    :rtype: bytes
    """
    for i in range(3):
        yield bytes(choice(MOCK_CELSIUS_TEMPERATURES), encoding='utf-8')
        sleep(1)


def stream_temperature():
    """
    Streams the fridge temperature.

    Encoded in `UTF-8`.

    :returns: fridge's temperature.
    :rtype: StreamingResponse
    """
    return StreamingResponse(get_temperature())
