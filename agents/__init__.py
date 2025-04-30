from .summarize_tool import SummarizeTool
from .sanitize_data import SanitizeData
from .article_tool import ArticleTool

from .write_article_validator_agent import WriteArticleValidatorAgent
from .sanitize_data_validator_agent import SanitizeDataValidatorAgent
from .summary_validator_agent import SummaryValidatorAgent

from .refiner_agent import RefinerAgent


class AgentManager:
    def __init__(self, max_retries=2, verbose=True):
        self.agents = {
            "summarize": SummarizeTool("summarize", max_retries=max_retries, verbose=verbose),
            "write_article": ArticleTool("write_article", max_retries=max_retries, verbose=verbose),
            "sanitize_data": SanitizeData("sanitize_data", max_retries=max_retries, verbose=verbose),
            "summary_validator": SummaryValidatorAgent("summary_validator", max_retries=max_retries, verbose=verbose),
            "write_article_validator": WriteArticleValidatorAgent("write_article_validator", max_retries=max_retries, verbose=verbose),
            "sanitize_data_validator": SanitizeDataValidatorAgent("sanitize_data_validator", max_retries=max_retries, verbose=verbose),
            "refiner": RefinerAgent("refiner", max_retries=max_retries, verbose=verbose)
        }

    def get_agent(self, agent_name):
        agent = self.agents.get(agent_name)
        if not agent:
            raise ValueError(f"Agent: {agent_name} not found")
        return agent
        