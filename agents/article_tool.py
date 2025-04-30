from .agent_base import BaseAIProcessor

class ArticleGenerator(BaseAIProcessor):
    """
    AI-powered academic article generator
    
    Args:
        BaseAIProcessor: Inherits from base AI processor
    """
    
    def __init__(self, name, max_attempts=2, debug_mode=True):
        super().__init__(name="ArticleGenerator", max_attempts=max_attempts, debug_mode=debug_mode)

    def process(self, topic, outline=None):
        """
        Generate an academic article on the given topic
        
        Args:
            topic (str): Main topic of the article
            outline (str, optional): Article outline. Defaults to None.
            
        Returns:
            str: Generated academic article
        """
        system_prompt = """
        You are an expert academic writer with extensive knowledge in various fields. Your task is to:
        1. Create well-structured, informative academic articles
        2. Follow proper academic writing conventions
        3. Include relevant citations and references
        4. Maintain clarity and academic tone
        """

        user_prompt = f"""
        Please write an academic article on the following topic:
        {topic}

        If provided, follow this outline:
        {outline if outline else "No specific outline provided"}

        The article should:
        1. Have a clear introduction
        2. Include well-organized body paragraphs
        3. Provide supporting evidence and citations
        4. Include a comprehensive conclusion
        """

        article_messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        generated_article = self.invoke_model(article_messages, max_output_tokens=1000)
        return generated_article




