from .agent_base import AgentBase

class SanitizeData(AgentBase):
    def __init__(self, name, max_retries =2, verbose = True):
        super().__init__(name="SanitizeData", max_retries=max_retries, verbose=verbose)

    def execute(self, data):
        messages = [
            {"role": "system", "content": "You are a helpful assistant that sanitizes data."},
            {
                "role": "user", "content": "please sanitize the following data:" 
                    f"{data}"
            }
        ]
        sanitized_data =  self.call_llm(messages, max_tokens=300)

        return sanitized_data




