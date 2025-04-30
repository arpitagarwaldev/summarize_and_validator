import ollama
from abc import ABC, abstractmethod
from loguru import logger
import os
from dotenv import load_dotenv

load_dotenv()


class BaseAIProcessor(ABC):
    """
    Base class for all AI processing agents
    
    Attributes:
        name (str): Unique identifier for the agent
        max_attempts (int): Maximum number of retry attempts
        debug_mode (bool): Enable/disable debug logging
    """
    
    def __init__(self, name, max_attempts=2, debug_mode=True):
        self.name = name
        self.max_attempts = max_attempts
        self.debug_mode = debug_mode

    @abstractmethod
    def process(self, *args, **kwargs):
        """Abstract method to be implemented by child classes"""
        pass

    def invoke_model(self, messages, max_output_tokens=150):
        """
        Execute model with retry mechanism
        
        Args:
            messages (list): List of message dictionaries
            max_output_tokens (int): Maximum tokens in response
            
        Returns:
            str: Model response content
            
        Raises:
            Exception: If all attempts fail
        """
        attempt = 0
        while attempt < self.max_attempts:
            try:
                if self.debug_mode:
                    logger.info(f"[{self.name}] - Initiating model request:")
                    for msg in messages:
                        logger.info(f"[{self.name}] - Role: {msg['role']}, Content: {msg['content']}")

                model_response = ollama.chat(
                    model="llama3:latest",
                    messages=messages,
                    temperature=0.7,
                    max_tokens=max_output_tokens,
                    stream=True
                )

                response_content = ""
                for chunk in model_response:
                    if "message" in chunk and "content" in chunk["message"]:
                        response_content += chunk["message"]["content"]

                if self.debug_mode:
                    logger.info(f"[{self.name}] - Model response: {response_content}")
                return response_content

            except Exception as error:
                attempt += 1
                logger.error(f"[{self.name}] - Model execution failed: {error}. Attempt {attempt} of {self.max_attempts}")
                if attempt == self.max_attempts:
                    raise Exception(f"[{self.name}] - Model execution failed after {self.max_attempts} attempts")
