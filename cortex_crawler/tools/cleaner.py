import re
from typing import List

from cortex_crawler.utils.logger import logger


class Cleaner:
    """Clean and normalize text content"""
    
    @staticmethod
    def remove_extra_spaces(text: str) -> str:
        """
        Remove extra spaces, tabs, and normalize whitespace
        
        Args:
            text: Raw text
            
        Returns:
            Text with normalized spaces
        """
        # Replace multiple spaces with single space
        text = re.sub(r' +', ' ', text)
        # Replace multiple newlines with double newline
        text = re.sub(r'\n\n+', '\n\n', text)
        # Strip leading/trailing whitespace from each line
        lines = [line.strip() for line in text.split('\n')]
        text = '\n'.join(lines)
        
        return text.strip()
    
    @staticmethod
    def remove_urls(text: str) -> str:
        """
        Remove URLs from text
        
        Args:
            text: Text containing URLs
            
        Returns:
            Text with URLs removed
        """
        # Remove http(s) URLs
        text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
        # Remove www URLs
        text = re.sub(r'www\.[a-zA-Z0-9-]+\.[a-zA-Z]{2,}', '', text)
        
        return text
    
    @staticmethod
    def remove_special_chars(text: str, keep_punctuation: bool = True) -> str:
        """
        Remove or normalize special characters
        
        Args:
            text: Text with special characters
            keep_punctuation: Whether to keep basic punctuation
            
        Returns:
            Cleaned text
        """
        if not keep_punctuation:
            # Remove everything except alphanumeric and spaces
            text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        else:
            # Remove common noise characters but keep basic punctuation
            text = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)  # Remove control characters
        
        return text
    
    @staticmethod
    def normalize_content(text: str) -> str:
        """
        Full normalization pipeline
        
        Args:
            text: Raw text content
            
        Returns:
            Normalized text
        """
        # Remove URLs
        text = Cleaner.remove_urls(text)
        # Remove extra spaces
        text = Cleaner.remove_extra_spaces(text)
        # Remove control characters
        text = Cleaner.remove_special_chars(text, keep_punctuation=True)
        # Final space cleanup
        text = Cleaner.remove_extra_spaces(text)
        
        return text
    
    @staticmethod
    def clean(text: str) -> str:
        """
        Main cleaning method
        
        Args:
            text: Raw text to clean
            
        Returns:
            Cleaned text
        """
        if not text:
            logger.warning("Empty text provided to cleaner")
            return ""
        
        original_length = len(text)
        cleaned_text = Cleaner.normalize_content(text)
        final_length = len(cleaned_text)
        
        logger.debug(f"Cleaned text: {original_length} → {final_length} characters")
        return cleaned_text
