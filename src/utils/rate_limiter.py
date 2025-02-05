"""API rate limiting implementation"""

import time
from collections import deque
from typing import Dict, Deque
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class RateLimiter:
    """
    Rate limiter using token bucket algorithm.

    Public Methods:
    ---------------
    can_request(api_name: str) -> bool:
        Determines if new requests are allowed within the time window.
    """
    
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests: Dict[str, Deque] = {}
        
    def can_request(self, api_name: str) -> bool:
        """Check if request is allowed within rate limits"""
        now = datetime.now()
        if api_name not in self.requests:
            self.requests[api_name] = deque()
            
        # Remove old requests
        while (self.requests[api_name] and 
            now - self.requests[api_name][0] > timedelta(seconds=self.time_window)):
            self.requests[api_name].popleft()
            
        return len(self.requests[api_name]) < self.max_requests
