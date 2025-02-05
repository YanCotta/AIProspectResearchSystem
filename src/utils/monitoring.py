"""Performance monitoring utilities"""

import time
from functools import wraps
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def performance_monitor(func: Callable) -> Callable:
    """
    Decorator for monitoring function performance.
    Logs function execution time at INFO level.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        execution_time = time.perf_counter() - start_time
        logger.info(f"{func.__name__} execution time: {execution_time:.2f} seconds")
        return result
    return wrapper
