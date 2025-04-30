from .agent_base import BaseAIProcessor

class ContentRefiner(BaseAIProcessor):
    """
    AI-powered content refinement processor
    
    Args:
        BaseAIProcessor: Inherits from base AI processor
    """
    
    def __init__(self, name, max_attempts=2, debug_mode=True):
        super().__init__(name="ContentRefiner", max_attempts=max_attempts, debug_mode=debug_mode)

    def process(self, content, outline=None):
        """
        Refine and enhance the quality of the content
        
        Args:
            content (str): Content to be refined
            outline (str, optional): Content outline. Defaults to None.
            
        Returns:
            str: Refined and enhanced content
        """
        system_prompt = """
        You are an expert content editor with a focus on:
        1. Enhancing clarity and coherence
        2. Improving academic quality
        3. Maintaining original meaning
        4. Ensuring proper structure and flow
        """

        user_prompt = f"""
        Please refine the following content:
        {content}

        If provided, follow this outline:
        {outline if outline else "No specific outline provided"}

        The refined content should:
        1. Be more concise and clear
        2. Have better structure and organization
        3. Maintain academic rigor
        4. Be free of grammatical errors
        """

        refinement_messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        refined_content = self.invoke_model(refinement_messages, max_output_tokens=1024)
        return refined_content




