from .agent_base import AgentBase

class SummarizeTool(AgentBase):
    def __init__(self, name, max_retries =2, verbose = True):
        super().__init__(name="SummarizeTool", max_retries=max_retries, verbose=verbose)

    def execute(self, text):
        messages = [
            {"role": "system", "content": "You are a helpful assistant that summarizes texts."},
            {
                "role": "user", "content": f"please provide the concise summary of the following text:\n\n{text}"
            }
        ]
        summary =  self.call_llm(messages, max_tokens=300)

        return summary




