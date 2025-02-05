"""Utility functions for the ProspectWorkflow system"""

import logging
from functools import wraps
import time
from typing import Any, Callable
from pathlib import Path

def setup_logging(log_path: Path) -> None:
    """Configure logging for the application"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_path / 'prospect_research.log'),
            logging.StreamHandler()
        ]
    )

def retry_on_failure(max_attempts: int = 3, delay: int = 1) -> Callable:
    """Decorator for retrying failed operations"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    if attempt < max_attempts - 1:
                        time.sleep(delay * (attempt + 1))
            raise last_error
        return wrapper
    return decorator

# Add more utility functions as needed...
