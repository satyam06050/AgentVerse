from typing import Optional

from cortex_crawler.llm.openai_client import LLMClient
from cortex_crawler.llm.prompts import Prompts
from cortex_crawler.utils.logger import logger


class Summarizer:
    """Generate summaries from content using LLM"""
    
    def __init__(self):
        """Initialize summarizer with LLM client"""
        self.llm_client = LLMClient()
        logger.info("Summarizer initialized")
    
    def summarize(
        self,
        content: str,
        summary_type: str = "brief",
        temperature: float = 0.7
    ) -> Optional[str]:
        """
        Generate a summary of content
        
        Args:
            content: Text to summarize
            summary_type: Type of summary ('brief' or 'detailed')
            temperature: LLM sampling temperature
            
        Returns:
            Summary text or None if failed
        """
        if not content or len(content.strip()) == 0:
            logger.warning("Empty content provided to summarizer")
            return None
        
        try:
            if summary_type == "detailed":
                system_prompt, user_prompt = Prompts.get_detailed_summary_prompt(content)
            else:
                system_prompt, user_prompt = Prompts.get_summarization_prompt(content)
            
            logger.info(f"Generating {summary_type} summary for {len(content)} characters")
            
            summary = self.llm_client.send_system_prompt(
                system=system_prompt,
                user=user_prompt,
                temperature=temperature,
                max_tokens=1000
            )
            
            if summary:
                logger.info(f"Summary generated successfully: {len(summary)} characters")
            else:
                logger.error("Failed to generate summary")
            
            return summary
            
        except Exception as e:
            logger.error(f"Error during summarization: {e}")
            return None
    
    def extract_key_points(
        self,
        content: str,
        temperature: float = 0.7
    ) -> Optional[str]:
        """
        Extract key points and important information
        
        Args:
            content: Text to extract from
            temperature: LLM sampling temperature
            
        Returns:
            Extracted information or None if failed
        """
        if not content or len(content.strip()) == 0:
            logger.warning("Empty content provided for extraction")
            return None
        
        try:
            system_prompt, user_prompt = Prompts.get_extraction_prompt(content)
            
            logger.info(f"Extracting key points from {len(content)} characters")
            
            extraction = self.llm_client.send_system_prompt(
                system=system_prompt,
                user=user_prompt,
                temperature=temperature,
                max_tokens=1500
            )
            
            if extraction:
                logger.info(f"Extraction successful: {len(extraction)} characters")
            else:
                logger.error("Failed to extract key points")
            
            return extraction
            
        except Exception as e:
            logger.error(f"Error during extraction: {e}")
            return None
    
    def answer_question(
        self,
        content: str,
        question: str,
        temperature: float = 0.7
    ) -> Optional[str]:
        """
        Answer a question based on content
        
        Args:
            content: Reference content
            question: Question to answer
            temperature: LLM sampling temperature
            
        Returns:
            Answer or None if failed
        """
        if not content or len(content.strip()) == 0:
            logger.warning("Empty content provided for Q&A")
            return None
        
        if not question or len(question.strip()) == 0:
            logger.warning("Empty question provided")
            return None
        
        try:
            system_prompt, user_prompt = Prompts.get_qa_prompt(content, question)
            
            logger.info(f"Answering question about {len(content)} characters of content")
            
            answer = self.llm_client.send_system_prompt(
                system=system_prompt,
                user=user_prompt,
                temperature=temperature,
                max_tokens=1000
            )
            
            if answer:
                logger.info(f"Answer generated: {len(answer)} characters")
            else:
                logger.error("Failed to generate answer")
            
            return answer
            
        except Exception as e:
            logger.error(f"Error during Q&A: {e}")
            return None
