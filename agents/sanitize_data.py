from .agent_base import BaseAIProcessor

class DataSanitizer(BaseAIProcessor):
    """
    AI-powered data sanitization processor
    
    Args:
        BaseAIProcessor: Inherits from base AI processor
    """
    
    def __init__(self, name, max_attempts=2, debug_mode=True):
        super().__init__(name="DataSanitizer", max_attempts=max_attempts, debug_mode=debug_mode)

    def process(self, input_data):
        """
        Sanitize and clean the input data
        
        Args:
            input_data (str): Data to be sanitized
            
        Returns:
            str: Cleaned and sanitized data
        """
        prompt_messages = [
            {
                "role": "system",
                "content": "You are an expert data sanitization assistant. Your task is to clean and sanitize the input data by:\n"
                "1. Removing any special characters and formatting issues\n"
                "2. Standardizing the data format\n"
                "3. Ensuring data integrity and consistency\n"
                "4. Removing any sensitive or unnecessary information"
            },
            {
                "role": "user",
                "content": f"Please clean and sanitize the following data:\n\n{input_data}\n\n"
                "Focus on maintaining the core meaning while ensuring the data is clean and properly formatted."
            }
        ]
        
        sanitized_result = self.invoke_model(prompt_messages, max_output_tokens=300)
        return sanitized_result




