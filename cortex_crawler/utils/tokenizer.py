"""Token counting utilities for LLM text"""

try:
    import tiktoken
except ImportError:
    tiktoken = None

from cortex_crawler.utils.logger import logger


class Tokenizer:
    """Handle token counting and estimation"""
    
    # Rough estimate: 1 token ≈ 4 characters for English
    CHARS_PER_TOKEN = 4
    
    def __init__(self, model: str = "cl100k_base"):
        """
        Initialize tokenizer
        
        Args:
            model: Tokenizer model to use
        """
        self.model = model
        self.encoding = None
        
        if tiktoken:
            try:
                self.encoding = tiktoken.get_encoding(model)
                logger.info(f"Initialized TikToken tokenizer with {model}")
            except Exception as e:
                logger.warning(f"Failed to initialize TikToken: {e}. Using fallback.")
        else:
            logger.warning("TikToken not available. Using character-based estimation.")
    
    def count_tokens(self, text: str) -> int:
        """
        Count tokens in text
        
        Args:
            text: Input text
            
        Returns:
            Estimated token count
        """
        if not text:
            return 0
        
        if self.encoding:
            try:
                tokens = self.encoding.encode(text)
                return len(tokens)
            except Exception as e:
                logger.warning(f"Token counting failed: {e}. Using fallback.")
        
        # Fallback: estimate based on character count
        return len(text) // self.CHARS_PER_TOKEN + 1
    
    def estimate_tokens(self, text: str) -> int:
        """
        Estimate tokens (alias for count_tokens)
        
        Args:
            text: Input text
            
        Returns:
            Estimated token count
        """
        return self.count_tokens(text)
    
    def truncate_to_tokens(self, text: str, max_tokens: int) -> str:
        """
        Truncate text to fit within token limit
        
        Args:
            text: Input text
            max_tokens: Maximum allowed tokens
            
        Returns:
            Truncated text
        """
        if not text:
            return ""
        
        if self.encoding:
            try:
                tokens = self.encoding.encode(text)
                if len(tokens) <= max_tokens:
                    return text
                
                truncated_tokens = tokens[:max_tokens]
                return self.encoding.decode(truncated_tokens)
            except Exception as e:
                logger.warning(f"Token truncation failed: {e}. Using fallback.")
        
        # Fallback: estimate based on character count
        estimated_chars = max_tokens * self.CHARS_PER_TOKEN
        return text[:estimated_chars]
    
    def get_token_info(self, text: str) -> dict:
        """
        Get detailed token information
        
        Args:
            text: Input text
            
        Returns:
            Dictionary with token info
        """
        token_count = self.count_tokens(text)
        char_count = len(text)
        word_count = len(text.split())
        
        return {
            "tokens": token_count,
            "characters": char_count,
            "words": word_count,
            "avg_chars_per_token": char_count / max(token_count, 1),
            "avg_tokens_per_word": token_count / max(word_count, 1)
        }
