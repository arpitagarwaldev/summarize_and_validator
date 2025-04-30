import ollama
from abc import ABC, abstractmethod
from loguru import logger
import os
from dotenv import load_dotenv

load_dotenv()


class AgentBase(ABC):
    def __init__(self, name, max_retries=2, verbose=True):
        self.name = name
        self.max_retries = max_retries
        self.verbose = verbose

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def call_llm(self, messages, max_tokens=150):
        retries = 0
        while retries < self.max_retries:
            try:
                if self.verbose:
                    logger.info(f"[{self.name}] - Sending messages to LLM:")
                    for msg in messages:
                        logger.info(f"[{self.name}] - {msg['role']}: {msg['content']}")

                response = ollama.chat(
                    model="llama3:latest",
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    stream=True
                )

                reply_content = ""
                for chunk in response:
                    if "message" in chunk and "content" in chunk["message"]:
                        reply_content += chunk["message"]["content"]

                if self.verbose:
                    logger.info(f"[{self.name}] - LLM reply: {reply_content}")
                return reply_content

            except Exception as e:
                retries += 1
                logger.error(f"[{self.name}] - LLM call failed: {e}. Retry {retries} of {self.max_retries}")
                if retries == self.max_retries:
                    raise Exception(f"[{self.name}] - LLM call failed after {self.max_retries} retries")
