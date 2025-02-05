"""Input validation utilities"""

from typing import Any, Dict, List, Union
from dataclasses import dataclass
import re
import logging
from functools import wraps

logger = logging.getLogger(__name__)

def validate_url(url: str) -> bool:
    """Validate URL format"""
    url_pattern = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(url_pattern.match(url))

def input_validation(func):
    """
    Decorator for input validation.
    Raises ValueError if inputs are invalid.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"Validating inputs for {func.__name__}")
        # Add validation logic here
        return func(*args, **kwargs)
    return wrapper
