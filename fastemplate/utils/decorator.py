import time
import functools


def timer(func):
    """
    Wrapper to measure function runtime.
    """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        """
        Wrapper function for `timer`.
        """
        start_time = time.perf_counter()
        fun = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return fun
    return wrapper_timer
