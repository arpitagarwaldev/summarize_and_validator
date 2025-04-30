from .agent_base import AgentBase

class ArticleTool(AgentBase):
    def __init__(self, name, max_retries =2, verbose = True):
        super().__init__(name="ArticleTool", max_retries=max_retries, verbose=verbose)

    def execute(self, topic, outline=None):

        system_messgae = "You are an expert academic writer"
        user_content = f"Please write an academic article based on the following topic: {topic}"
        if outline:
            user_content += f"\n\nOutline: {outline}"
        user_content += "Article:\n"

        messages = [
            {"role": "system", "content": system_messgae},
            {"role": "user", "content": user_content}
        ]

        article =  self.call_llm(messages, max_tokens= 1000)

        return article




