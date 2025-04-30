from .agent_base import AgentBase

class SummaryValidatorAgent(AgentBase):
    def __init__(self, name, max_retries =2, verbose = True):
        super().__init__(name="SummaryValidatorAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, original_text, summary):
        system_message = "You are an expert AI assistant who validates the summary of academic summaries."

        user_content = (
            "Given the original and summary, assess whether the summary accurately captures the main ideas and key points.\n\n"
            "Provide a brief analysis and suggestions for improvement. Also rate summary on a scale of 1-10. Where 10 indicates highest quality.\n\n"
            f"Original Text: \n{original_text}\n\n"
            f"Summary: \n{summary}\n\n"
            "Validation"
        )

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]

        validation =  self.call_llm(messages, max_tokens= 1000)

        return validation




