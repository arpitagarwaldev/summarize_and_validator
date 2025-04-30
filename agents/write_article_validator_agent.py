from .agent_base import BaseAIProcessor

class ArticleQualityValidator(BaseAIProcessor):
    """
    Validates the quality and academic standards of articles
    
    Args:
        BaseAIProcessor: Inherits from base AI processor
    """
    
    def __init__(self, name, max_attempts=2, debug_mode=True):
        super().__init__(name="ArticleQualityValidator", max_attempts=max_attempts, debug_mode=debug_mode)

    def process(self, topic, article, outline=None):
        """
        Validate the quality and academic standards of an article
        
        Args:
            topic (str): Article topic
            article (str): Article content
            outline (str, optional): Article outline. Defaults to None.
            
        Returns:
            str: Quality assessment and improvement suggestions
        """
        system_prompt = """
        You are an expert in academic article validation. Your task is to:
        1. Evaluate the article against academic standards
        2. Assess logical coherence and clarity
        3. Provide detailed quality analysis
        4. Offer specific improvement suggestions
        """

        user_prompt = f"""
        Please validate the following article:

        Topic:
        {topic}

        Article:
        {article}

        If provided, follow this outline:
        {outline if outline else "No specific outline provided"}

        Please provide:
        1. A detailed analysis of the article's quality and academic standards
        2. Specific areas for improvement
        3. A quality rating (1-10) with clear justification
        """

        validation_messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        validation_result = self.invoke_model(validation_messages, max_output_tokens=1000)
        return validation_result




