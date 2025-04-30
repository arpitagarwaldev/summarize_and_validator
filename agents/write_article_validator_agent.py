from .agent_base import AgentBase

class WriteArticleValidatorAgent(AgentBase):
    def __init__(self, name, max_retries =2, verbose = True):
        super().__init__(name="WriteArticleValidatorAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, topic, outline=None):

        system_messgae = "You are an expert AI assistant who validates the quality of academic articles."


        user_content = (
            "Given the topic and article, assess whether the article meets the academic standards, logical coherence, and clarity.\n"
            "Provice a brief analysis and suggestions for improvement. Also rate article on a scale of 1-10. where 10 indicates highest quality.\n\n"
            f"Topic: {topic}\n\n"
            f"Article: \n{article}\n\n"
            "Validation"
        )

        messages = [
            {"role": "system", "content": system_messgae},
            {"role": "user", "content": user_content}
        ]

        validation =  self.call_llm(messages, max_tokens= 1000)

        return validation




