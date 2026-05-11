#!/usr/bin/env python3
"""
CortexCrawler - Phase 1

Main pipeline orchestrator:
URL → Scrape → Clean → Summarize → Output
"""

import sys
from pathlib import Path
from typing import Optional

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from cortex_crawler.tools.scraper import Scraper
from cortex_crawler.tools.cleaner import Cleaner
from cortex_crawler.tools.summarizer import Summarizer
from cortex_crawler.utils.logger import logger


class CortexCrawler:
    """Main orchestrator for the CortexCrawler pipeline"""
    
    def __init__(self):
        """Initialize pipeline components"""
        self.scraper = Scraper()
        self.cleaner = Cleaner()
        self.summarizer = Summarizer()
        logger.info("CortexCrawler initialized with all components")
    
    def process_url(
        self,
        url: str,
        summary_type: str = "brief",
        extract_key_points: bool = False
    ) -> Optional[dict]:
        """
        Complete pipeline: URL → Scrape → Clean → Summarize
        
        Args:
            url: Target webpage URL
            summary_type: Type of summary ('brief' or 'detailed')
            extract_key_points: Whether to extract key points in addition to summary
            
        Returns:
            Dictionary with results or None if failed
        """
        logger.info(f"Starting pipeline for URL: {url}")
        
        # Step 1: Scrape
        logger.info("Step 1: Scraping webpage...")
        raw_text = self.scraper.scrape(url)
        if not raw_text:
            logger.error("Failed to scrape URL")
            return None
        logger.info(f"✓ Scraped {len(raw_text)} characters")
        
        # Step 2: Clean
        logger.info("Step 2: Cleaning content...")
        cleaned_text = self.cleaner.clean(raw_text)
        if not cleaned_text:
            logger.error("Failed to clean content")
            return None
        logger.info(f"✓ Cleaned to {len(cleaned_text)} characters")
        
        # Step 3: Summarize
        logger.info("Step 3: Generating summary...")
        summary = self.summarizer.summarize(cleaned_text, summary_type=summary_type)
        if not summary:
            logger.error("Failed to generate summary")
            return None
        logger.info(f"✓ Summary generated")
        
        # Step 4: Optional key points extraction
        key_points = None
        if extract_key_points:
            logger.info("Step 4: Extracting key points...")
            key_points = self.summarizer.extract_key_points(cleaned_text)
            if key_points:
                logger.info(f"✓ Key points extracted")
            else:
                logger.warning("Failed to extract key points")
        
        # Prepare results
        results = {
            "url": url,
            "raw_text_length": len(raw_text),
            "cleaned_text_length": len(cleaned_text),
            "summary": summary,
            "summary_type": summary_type,
            "key_points": key_points
        }
        
        logger.info("✓ Pipeline completed successfully")
        return results
    
    def print_results(self, results: dict) -> None:
        """
        Pretty print pipeline results
        
        Args:
            results: Results dictionary from process_url
        """
        if not results:
            print("No results to display")
            return
        
        print("\n" + "="*80)
        print("CORTEX CRAWLER - RESULTS")
        print("="*80)
        
        print(f"\n📌 URL: {results['url']}")
        print(f"📊 Statistics:")
        print(f"   - Original text: {results['raw_text_length']} characters")
        print(f"   - Cleaned text: {results['cleaned_text_length']} characters")
        
        print(f"\n📝 Summary ({results['summary_type']}):")
        print("-" * 80)
        print(results['summary'])
        print("-" * 80)
        
        if results.get('key_points'):
            print(f"\n🔑 Key Points:")
            print("-" * 80)
            print(results['key_points'])
            print("-" * 80)
        
        print("\n" + "="*80 + "\n")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python main.py <URL> [--detailed] [--extract-key-points]")
        print("\nExample:")
        print("  python main.py https://example.com")
        print("  python main.py https://example.com --detailed --extract-key-points")
        sys.exit(1)
    
    url = sys.argv[1]
    summary_type = "detailed" if "--detailed" in sys.argv else "brief"
    extract_key_points = "--extract-key-points" in sys.argv
    
    try:
        crawler = CortexCrawler()
        results = crawler.process_url(url, summary_type=summary_type, extract_key_points=extract_key_points)
        
        if results:
            crawler.print_results(results)
        else:
            print("❌ Pipeline failed. Check logs for details.")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
