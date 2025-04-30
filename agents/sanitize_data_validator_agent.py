from .agent_base import BaseAIProcessor

class DataSanitizationValidator(BaseAIProcessor):
    """
    Validates the quality and effectiveness of data sanitization
    
    Args:
        BaseAIProcessor: Inherits from base AI processor
    """
    
    def __init__(self, name, max_attempts=2, debug_mode=True):
        super().__init__(name="DataSanitizationValidator", max_attempts=max_attempts, debug_mode=debug_mode)

    def process(self, original_data, sanitized_data):
        """
        Validate the quality of data sanitization
        
        Args:
            original_data (str): Original data before sanitization
            sanitized_data (str): Sanitized data
            
        Returns:
            str: Validation analysis and quality assessment
        """
        system_prompt = """
        You are an expert in data sanitization validation. Your task is to:
        1. Compare the original and sanitized data
        2. Verify all sensitive information is properly removed
        3. Ensure data integrity is maintained
        4. Provide a quality assessment
        """

        user_prompt = f"""
        Please validate the following data sanitization:

        Original Data:
        {original_data}

        Sanitized Data:
        {sanitized_data}

        Please provide:
        1. A detailed analysis of the sanitization quality
        2. Specific areas for improvement
        3. A quality rating (1-10) with clear justification
        """

        validation_messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        validation_result = self.invoke_model(validation_messages, max_output_tokens=1000)
        return validation_result




