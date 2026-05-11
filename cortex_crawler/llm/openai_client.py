from openai import OpenAI, APIError
from typing import Optional

from cortex_crawler.config import Config
from cortex_crawler.utils.logger import logger


class LLMClient:
    """Client for interacting with DeepSeek LLM API"""
    
    def __init__(self):
        """Initialize DeepSeek client"""
        Config.validate()
        self.client = OpenAI(
            api_key=Config.DEEPSEEK_API_KEY,
            base_url=Config.DEEPSEEK_BASE_URL
        )
        self.model = Config.DEEPSEEK_MODEL
        logger.info(f"Initialized LLM client with model: {self.model}")
    
    def send_prompt(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ) -> Optional[str]:
        """
        Send a prompt to DeepSeek and get response
        
        Args:
            prompt: The prompt/message to send
            temperature: Sampling temperature (0-2, default 0.7)
            max_tokens: Maximum tokens in response (optional)
            
        Returns:
            Response text or None if failed
        """
        try:
            logger.debug(f"Sending prompt to {self.model}")
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            result = response.choices[0].message.content
            logger.debug(f"Received response: {len(result)} characters")
            return result
            
        except APIError as e:
            logger.error(f"API Error: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return None
    
    def send_system_prompt(
        self,
        system: str,
        user: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ) -> Optional[str]:
        """
        Send prompt with system message
        
        Args:
            system: System message/role
            user: User message/prompt
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response
            
        Returns:
            Response text or None if failed
        """
        try:
            logger.debug(f"Sending system + user prompt to {self.model}")
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": system
                    },
                    {
                        "role": "user",
                        "content": user
                    }
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            result = response.choices[0].message.content
            logger.debug(f"Received response: {len(result)} characters")
            return result
            
        except APIError as e:
            logger.error(f"API Error: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return None
