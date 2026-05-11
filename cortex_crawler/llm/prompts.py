"""Reusable prompts for LLM interactions"""


class Prompts:
    """Collection of prompts for various tasks"""
    
    SUMMARIZATION_SYSTEM = """You are an expert content summarizer. Your task is to:
1. Read the provided content carefully
2. Identify the key points and main ideas
3. Create a concise, clear summary
4. Preserve important details and context
5. Use clear, professional language

Focus on the most important information and omit redundant details."""
    
    SUMMARIZATION_USER = """Please summarize the following content in 3-5 sentences, highlighting the most important points:

{content}"""
    
    DETAILED_SUMMARY_SYSTEM = """You are an expert content analyzer. Your task is to:
1. Read the provided content thoroughly
2. Extract key information, themes, and concepts
3. Organize findings into clear sections
4. Highlight important insights and takeaways
5. Provide structured, detailed summary

Format your response with clear headings and bullet points where appropriate."""
    
    DETAILED_SUMMARY_USER = """Please provide a detailed summary of the following content, organized by key topics:

{content}"""
    
    EXTRACTION_SYSTEM = """You are an expert at extracting structured information from content. Your task is to:
1. Identify key facts, concepts, and entities
2. Extract actionable information
3. Organize extracted data clearly
4. Note any important relationships between concepts"""
    
    EXTRACTION_USER = """Please extract the key facts and important information from this content:

{content}"""
    
    QA_SYSTEM = """You are a helpful assistant that answers questions based on provided content. 
Answer only based on the information given. If the answer is not in the content, say so clearly."""
    
    QA_USER = """Based on this content:

{content}

Please answer: {question}"""
    
    @staticmethod
    def get_summarization_prompt(content: str) -> tuple:
        """
        Get system and user prompts for summarization
        
        Args:
            content: Text to summarize
            
        Returns:
            Tuple of (system_prompt, user_prompt)
        """
        user_prompt = Prompts.SUMMARIZATION_USER.format(content=content)
        return Prompts.SUMMARIZATION_SYSTEM, user_prompt
    
    @staticmethod
    def get_detailed_summary_prompt(content: str) -> tuple:
        """
        Get system and user prompts for detailed summarization
        
        Args:
            content: Text to summarize
            
        Returns:
            Tuple of (system_prompt, user_prompt)
        """
        user_prompt = Prompts.DETAILED_SUMMARY_USER.format(content=content)
        return Prompts.DETAILED_SUMMARY_SYSTEM, user_prompt
    
    @staticmethod
    def get_extraction_prompt(content: str) -> tuple:
        """
        Get system and user prompts for information extraction
        
        Args:
            content: Text to extract from
            
        Returns:
            Tuple of (system_prompt, user_prompt)
        """
        user_prompt = Prompts.EXTRACTION_USER.format(content=content)
        return Prompts.EXTRACTION_SYSTEM, user_prompt
    
    @staticmethod
    def get_qa_prompt(content: str, question: str) -> tuple:
        """
        Get system and user prompts for Q&A
        
        Args:
            content: Reference content
            question: Question to answer
            
        Returns:
            Tuple of (system_prompt, user_prompt)
        """
        user_prompt = Prompts.QA_USER.format(content=content, question=question)
        return Prompts.QA_SYSTEM, user_prompt
