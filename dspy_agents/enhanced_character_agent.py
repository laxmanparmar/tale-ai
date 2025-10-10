"""
DSPy-enhanced Character Agent with reasoning capabilities.
"""

import dspy
from dspy_modules.reasoning import CharacterReasoning

class EnhancedCharacterAgent:
    """Character agent with DSPy reasoning capabilities."""
    
    def __init__(self):
        self.character_reasoner = dspy.ChainOfThought(CharacterReasoning)
    
    def develop_characters(self, story_content: str, context: str = "") -> str:
        """
        Develop characters with structured reasoning.
        
        Args:
            story_content: The story content
            context: Previous context
            
        Returns:
            Character development with reasoning
        """
        # Extract plot structure from story content
        plot_structure = self._extract_plot_structure(story_content)
        
        # Reason about characters
        character_result = self.character_reasoner(plot_structure=plot_structure)
        
        return f"CHARACTER REASONING:\n{character_result.character_analysis}"
    
    def _extract_plot_structure(self, content: str) -> str:
        """Extract plot structure from story content."""
        if "PLOT STRUCTURE:" in content:
            return content.split("PLOT STRUCTURE:")[1].strip()
        return content
