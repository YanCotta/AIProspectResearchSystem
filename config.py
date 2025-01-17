"""Configuration handler for the ProspectWorkflow system"""

import os
from pathlib import Path
from typing import Dict, Any, Optional
import json
import logging

class Config:
    """Handles all configuration settings for the system"""
    
    DEFAULT_CONFIG = {
        "api_keys": {
            "openai": "",
            "linkedin": "",
            "crunchbase": ""
        },
        "paths": {
            "templates": "templates",
            "reports": "reports",
            "logs": "logs"
        },
        "settings": {
            "retry_attempts": 3,
            "timeout": 30,
            "cache_enabled": True
        }
    }

    def __init__(self, config_path: str = "config.json"):
        self.config_path = Path(config_path)
        self.config = self._load_config()
        self._validate_config()
        self._setup_directories()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default"""
        if self.config_path.exists():
            with open(self.config_path, 'r') as f:
                return {**self.DEFAULT_CONFIG, **json.load(f)}
        return self.DEFAULT_CONFIG

    def _validate_config(self) -> None:
        """Validate required configuration settings"""
        required_keys = ['openai']
        missing = [key for key in required_keys 
                if not self.config['api_keys'].get(key)]
        if missing:
            raise ValueError(f"Missing required API keys: {', '.join(missing)}")

    def _setup_directories(self) -> None:
        """Create necessary directories if they don't exist"""
        for path in self.config['paths'].values():
            Path(path).mkdir(parents=True, exist_ok=True)

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """
        Safely get a configuration value with optional default.
        """
        return self.config.get(key, default)

    def save(self) -> None:
        """Save current configuration to file"""
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)
