"""Validation functions for input data"""

from typing import Optional
import re


def validate_url(url: str) -> tuple[bool, Optional[str]]:
    """
    Validate URL with detailed error message
    
    Args:
        url: URL to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not url:
        return False, "URL cannot be empty"
    
    if not isinstance(url, str):
        return False, "URL must be a string"
    
    url = url.strip()
    
    if not url.startswith(('http://', 'https://')):
        return False, "URL must start with http:// or https://"
    
    if len(url) < 10:
        return False, "URL is too short"
    
    if len(url) > 2048:
        return False, "URL is too long (max 2048 characters)"
    
    # Basic regex check
    url_pattern = r'^https?://[^\s]+\.[^\s]+$'
    if not re.match(url_pattern, url):
        return False, "URL format is invalid"
    
    return True, None


def validate_text(text: str, min_length: int = 1, max_length: int = 1_000_000) -> tuple[bool, Optional[str]]:
    """
    Validate text content
    
    Args:
        text: Text to validate
        min_length: Minimum text length
        max_length: Maximum text length
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not text:
        return False, "Text cannot be empty"
    
    if not isinstance(text, str):
        return False, "Text must be a string"
    
    text = text.strip()
    length = len(text)
    
    if length < min_length:
        return False, f"Text is too short (minimum {min_length} characters)"
    
    if length > max_length:
        return False, f"Text is too long (maximum {max_length} characters)"
    
    return True, None


def validate_api_key(api_key: str) -> tuple[bool, Optional[str]]:
    """
    Validate API key format
    
    Args:
        api_key: API key to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not api_key:
        return False, "API key cannot be empty"
    
    if not isinstance(api_key, str):
        return False, "API key must be a string"
    
    api_key = api_key.strip()
    
    if len(api_key) < 20:
        return False, "API key appears to be too short"
    
    return True, None


def validate_temperature(temperature: float) -> tuple[bool, Optional[str]]:
    """
    Validate LLM temperature parameter
    
    Args:
        temperature: Temperature value
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not isinstance(temperature, (int, float)):
        return False, "Temperature must be a number"
    
    if temperature < 0 or temperature > 2:
        return False, "Temperature must be between 0 and 2"
    
    return True, None
