"""Helper utility functions"""

from urllib.parse import urlparse
from typing import Optional


def is_valid_url(url: str) -> bool:
    """
    Validate if a string is a valid URL
    
    Args:
        url: URL string to validate
        
    Returns:
        True if valid URL, False otherwise
    """
    try:
        result = urlparse(url)
        return all([result.scheme in ['http', 'https'], result.netloc])
    except Exception:
        return False


def truncate_text(text: str, max_length: int = 1000) -> str:
    """
    Truncate text to maximum length
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


def count_words(text: str) -> int:
    """
    Count number of words in text
    
    Args:
        text: Input text
        
    Returns:
        Number of words
    """
    return len(text.split())


def get_text_preview(text: str, lines: int = 3) -> str:
    """
    Get a preview of text (first N lines)
    
    Args:
        text: Input text
        lines: Number of lines to include
        
    Returns:
        Text preview
    """
    text_lines = text.split('\n')
    preview_lines = text_lines[:lines]
    return '\n'.join(preview_lines)
