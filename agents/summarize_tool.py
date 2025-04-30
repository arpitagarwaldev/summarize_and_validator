from .agent_base import BaseAIProcessor

class TextSummarizer(BaseAIProcessor):
    """
    AI-powered text summarization processor
    
    Args:
        BaseAIProcessor: Inherits from base AI processor
    """
    
    def __init__(self, name, max_attempts=2, debug_mode=True):
        super().__init__(name="TextSummarizer", max_attempts=max_attempts, debug_mode=debug_mode)

    def process(self, content):
        """
        Generate a concise summary of the provided text
        
        Args:
            content (str): Input text to be summarized
            
        Returns:
            str: Generated summary
        """
        prompt_messages = [
            {
                "role": "system",
                "content": "You are an expert text summarization assistant. Your task is to create concise, accurate summaries that capture the key points of the input text."
            },
            {
                "role": "user",
                "content": f"Please create a concise summary of the following text:\n\n{content}\n\nFocus on capturing the main ideas while maintaining clarity and brevity."
            }
        ]
        
        summary = self.invoke_model(prompt_messages, max_output_tokens=300)
        return summary




