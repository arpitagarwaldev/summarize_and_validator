from .text_summarizer import TextSummarizer
from .data_sanitizer import DataSanitizer
from .article_generator import ArticleGenerator

from .article_quality_validator import ArticleQualityValidator
from .data_sanitization_validator import DataSanitizationValidator
from .summary_validator import SummaryValidator

from .content_refiner import ContentRefiner


class AgentManager:
    def __init__(self, max_attempts=2, debug_mode=True):
        self.agents = {
            "TextSummarizer": TextSummarizer("TextSummarizer", max_attempts=max_attempts, debug_mode=debug_mode),
            "ArticleGenerator": ArticleGenerator("ArticleGenerator", max_attempts=max_attempts, debug_mode=debug_mode),
            "DataSanitizer": DataSanitizer("DataSanitizer", max_attempts=max_attempts, debug_mode=debug_mode),
            "SummaryValidator": SummaryValidator("SummaryValidator", max_attempts=max_attempts, debug_mode=debug_mode),
            "ArticleQualityValidator": ArticleQualityValidator("ArticleQualityValidator", max_attempts=max_attempts, debug_mode=debug_mode),
            "DataSanitizationValidator": DataSanitizationValidator("DataSanitizationValidator", max_attempts=max_attempts, debug_mode=debug_mode),
            "ContentRefiner": ContentRefiner("ContentRefiner", max_attempts=max_attempts, debug_mode=debug_mode)
        }

    def get_agent(self, agent_name):
        agent = self.agents.get(agent_name)
        if not agent:
            raise ValueError(f"Agent: {agent_name} not found")
        return agent
        