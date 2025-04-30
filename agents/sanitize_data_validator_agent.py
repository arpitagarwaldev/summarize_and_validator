from .agent_base import AgentBase

class SanitizeDataValidatorAgent(AgentBase):
    def __init__(self, name, max_retries =2, verbose = True):
        super().__init__(name="SanitizeDataValidatorAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, topic, outline=None):

        system_messgae = "You are an expert AI assistant who validates the sanitization of academic data."


        user_content = (
            "Given the original and sanitized data, verify that all the data is sanitized.\n\n"
            f"Topic: {topic}\n\n"
            f"Original Data: \n{original_data}\n\n"
            f"Sanitized Data: \n{sanitized_data}\n\n"
            "Validation"
        )

        messages = [
            {"role": "system", "content": system_messgae},
            {"role": "user", "content": user_content}
        ]

        validation =  self.call_llm(messages, max_tokens= 1000)

        return validation




