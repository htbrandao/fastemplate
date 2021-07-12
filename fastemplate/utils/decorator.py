import time
from functools import wraps

from fastemplate import logger
from fastemplate.module.cart import _CART
from fastemplate.exceptions.cart import CartIdNotFoundException


def timer(func):
    """
    Print the runtime of the decorated function.

    :param func func: func to be decorated
    :return: wrapped function
    """
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        logger.info(f'Finished {func.__name__!r} in {run_time:.4f} secs')
        return value
    return wrapper_timer


def check_id(id: str):
    if id in _CART:
        return True
    else:
        raise CartIdNotFoundException(status_code=404, message=f'Cart #{id} does not exist.')
