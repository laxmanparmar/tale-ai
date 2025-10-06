"""
LLM module - Single instance for all agents to use.
Configure via environment variables.
"""

import os
from langchain.llms import OpenAI

llm = OpenAI(
    model_name=os.getenv("OPENAI_MODEL_NAME", "llama3.2"),
    openai_api_key=os.getenv("OPENAI_API_KEY", "fake-key"),
    openai_api_base=os.getenv("OPENAI_BASE_URL", "http://localhost:1234/v1"),
    temperature=float(os.getenv("TEMPERATURE", "0.7")),
    max_tokens=int(os.getenv("MAX_TOKENS", "2000"))
)

def get_llm():
    """Get the LLM instance."""
    return llm
