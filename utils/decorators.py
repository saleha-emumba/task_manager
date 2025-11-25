from functools import wraps
from typing import Any, Callable, Dict, Tuple
import time


def memoize(func: Callable) -> Callable:
    cache: Dict[Tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            return cache[key]

        res = func(*args, **kwargs)
        cache[key] = res
        return res

    return wrapper


def timeit(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        t1 = time.perf_counter()
        print(f"{func.__name__} took {t1 - t0:.6f}s")
        return result

    return wrapper
