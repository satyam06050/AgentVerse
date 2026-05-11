import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
ENV_PATH = Path(__file__).parent.parent / ".env"
load_dotenv(ENV_PATH)


class Config:
    """Configuration manager for CortexCrawler"""
    
    # API Configuration
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")
    DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    
    # Scraper settings
    USER_AGENT = os.getenv("USER_AGENT", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    REQUEST_TIMEOUT = 10
    MAX_CONTENT_LENGTH = 1_000_000  # 1MB limit
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # Paths
    PROJECT_ROOT = Path(__file__).parent.parent
    STORAGE_PATH = PROJECT_ROOT / "cortex_crawler" / "storage"
    LOGS_PATH = STORAGE_PATH / "logs"
    CACHE_PATH = STORAGE_PATH / "cache"
    VECTORS_PATH = STORAGE_PATH / "vectors"
    
    @staticmethod
    def validate():
        """Validate required configuration"""
        if not Config.DEEPSEEK_API_KEY:
            raise ValueError("DEEPSEEK_API_KEY not found in environment variables. Please set it in .env file.")
