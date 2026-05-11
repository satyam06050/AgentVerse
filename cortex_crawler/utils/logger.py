import logging
import sys
from pathlib import Path

from cortex_crawler.config import Config

# Create logs directory if it doesn't exist
Config.LOGS_PATH.mkdir(parents=True, exist_ok=True)

# Configure logging
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
log_level = getattr(logging, Config.LOG_LEVEL, logging.INFO)

# Create logger
logger = logging.getLogger("cortex_crawler")
logger.setLevel(log_level)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(log_level)
console_formatter = logging.Formatter(log_format)
console_handler.setFormatter(console_formatter)

# File handler
log_file = Config.LOGS_PATH / "cortex_crawler.log"
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(log_level)
file_formatter = logging.Formatter(log_format)
file_handler.setFormatter(file_formatter)

# Add handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("Logger initialized")
