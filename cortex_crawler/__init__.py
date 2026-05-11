"""CortexCrawler - AI Web Scraping and Summarization Pipeline"""

__version__ = "0.1.0"
__author__ = "CortexCrawler Team"

from cortex_crawler.config import Config
from cortex_crawler.tools.scraper import Scraper
from cortex_crawler.tools.cleaner import Cleaner
from cortex_crawler.tools.summarizer import Summarizer
from cortex_crawler.llm.openai_client import LLMClient
from cortex_crawler.llm.prompts import Prompts

__all__ = [
    "Config",
    "Scraper",
    "Cleaner",
    "Summarizer",
    "LLMClient",
    "Prompts"
]
