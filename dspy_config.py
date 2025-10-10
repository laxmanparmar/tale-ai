"""
DSPy configuration and setup for tale-ai.
"""

import os
import dspy
from llm import get_llm

def configure_dspy():
    """Configure DSPy with the centralized LLM."""
    # Get the LLM instance from our centralized module
    llm = get_llm()
    
    # Configure DSPy to use our LLM
    dspy.configure(lm=llm)
    
    print("✅ DSPy configured with centralized LLM")
    print(f"   Model: {os.getenv('OPENAI_MODEL_NAME', 'llama3.2')}")
    print(f"   Base URL: {os.getenv('OPENAI_BASE_URL', 'http://localhost:1234/v1')}")

# Auto-configure when module is imported
configure_dspy()

