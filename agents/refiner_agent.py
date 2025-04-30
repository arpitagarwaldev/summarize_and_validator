from .agent_base import AgentBase

class RefinerAgent(AgentBase):
    def __init__(self, name, max_retries =2, verbose = True):
        super().__init__(name="RefinerAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, draft, outline=None):

        messages = [
            {"role" : "system",
            "content" : [
                {
                    "type" : "text",
                    "text" : "You are an expert editor who refines and enhance article for clarity, coherenence and academic quality."
                }
            ]},
            {"role" : "user", "content" : f"Please refine the following article: {draft}\n\nRefinedArticle:"}
        ]

        refined_article =  self.call_llm(messages, temperature=0.2, max_tokens= 1024)

        return refined_article




