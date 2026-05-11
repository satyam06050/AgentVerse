import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from typing import Optional, Tuple

from cortex_crawler.config import Config
from cortex_crawler.utils.logger import logger


class Scraper:
    """Scrape and extract text content from webpages"""
    
    def __init__(self):
        self.headers = {"User-Agent": Config.USER_AGENT}
        self.timeout = Config.REQUEST_TIMEOUT
        self.max_length = Config.MAX_CONTENT_LENGTH
    
    def fetch(self, url: str) -> Optional[str]:
        """
        Fetch webpage content
        
        Args:
            url: Target webpage URL
            
        Returns:
            Raw HTML content or None if failed
        """
        try:
            logger.debug(f"Fetching URL: {url}")
            response = requests.get(
                url,
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            # Check content length
            if len(response.content) > self.max_length:
                logger.warning(f"Content exceeds max length. Truncating to {self.max_length} bytes")
                return response.text[:self.max_length]
            
            return response.text
            
        except requests.RequestException as e:
            logger.error(f"Failed to fetch {url}: {e}")
            return None
    
    def parse_html(self, html: str) -> BeautifulSoup:
        """
        Parse HTML with BeautifulSoup
        
        Args:
            html: Raw HTML content
            
        Returns:
            BeautifulSoup object
        """
        return BeautifulSoup(html, "lxml")
    
    def extract_text(self, soup: BeautifulSoup) -> str:
        """
        Extract visible text from parsed HTML
        
        Args:
            soup: BeautifulSoup object
            
        Returns:
            Extracted visible text
        """
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text
        text = soup.get_text()
        
        return text
    
    def scrape(self, url: str) -> Optional[str]:
        """
        Complete scrape pipeline: fetch + parse + extract
        
        Args:
            url: Target webpage URL
            
        Returns:
            Extracted text content or None if failed
        """
        html = self.fetch(url)
        if not html:
            return None
        
        soup = self.parse_html(html)
        text = self.extract_text(soup)
        
        logger.info(f"Successfully scraped {url}. Text length: {len(text)} characters")
        return text
