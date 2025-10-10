"""
DSPy-enhanced Dialogue Agent with reasoning capabilities.
"""

import dspy
from dspy_modules.reasoning import DialogueReasoning

class EnhancedDialogueAgent:
    """Dialogue agent with DSPy reasoning capabilities."""
    
    def __init__(self):
        self.dialogue_reasoner = dspy.ChainOfThought(DialogueReasoning)
    
    def write_dialogue(self, story_content: str, context: str = "") -> str:
        """
        Write dialogue with structured reasoning.
        
        Args:
            story_content: The story content
            context: Previous context
            
        Returns:
            Dialogue writing with reasoning
        """
        # Extract relevant information
        characters = self._extract_characters(story_content)
        conflicts = self._extract_conflicts(story_content)
        
        # Reason about dialogue
        dialogue_result = self.dialogue_reasoner(
            characters=characters,
            conflicts=conflicts
        )
        
        return f"DIALOGUE REASONING:\n{dialogue_result.dialogue_strategy}"
    
    def _extract_characters(self, content: str) -> str:
        """Extract character information from content."""
        if "CHARACTER REASONING:" in content:
            return content.split("CHARACTER REASONING:")[1].strip()
        return content
    
    def _extract_conflicts(self, content: str) -> str:
        """Extract conflict information from content."""
        if "CONFLICT REASONING:" in content:
            return content.split("CONFLICT REASONING:")[1].strip()
        return content

