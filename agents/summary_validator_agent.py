from .agent_base import BaseAIProcessor

class SummaryValidator(BaseAIProcessor):
    """
    Validates the quality and accuracy of text summaries
    
    Args:
        BaseAIProcessor: Inherits from base AI processor
    """
    
    def __init__(self, name, max_attempts=2, debug_mode=True):
        super().__init__(name="SummaryValidator", max_attempts=max_attempts, debug_mode=debug_mode)

    def process(self, original_content, summary):
        """
        Validate a summary against its original text
        
        Args:
            original_content (str): Original text
            summary (str): Generated summary
            
        Returns:
            str: Validation analysis and quality rating
        """
        system_prompt = """
        You are an expert in text summarization validation. Your task is to:
        1. Compare the summary with the original text
        2. Evaluate if key points are accurately captured
        3. Assess the clarity and conciseness of the summary
        4. Provide a quality rating (1-10) with detailed justification
        """

        user_prompt = f"""
        Please validate the following summary against the original text:

        Original Text:
        {original_content}

        Generated Summary:
        {summary}

        Please provide:
        1. A detailed analysis of the summary's accuracy and completeness
        2. Specific areas for improvement
        3. A quality rating (1-10) with clear justification
        """

        validation_messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        validation_result = self.invoke_model(validation_messages, max_output_tokens=1000)
        return validation_result




