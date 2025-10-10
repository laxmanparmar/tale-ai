"""
DSPy-enhanced Setting Agent with reasoning capabilities.
"""

import dspy
from dspy_modules.reasoning import SettingReasoning

class EnhancedSettingAgent:
    """Setting agent with DSPy reasoning capabilities."""
    
    def __init__(self):
        self.setting_reasoner = dspy.ChainOfThought(SettingReasoning)
    
    def create_setting(self, story_content: str, context: str = "") -> str:
        """
        Create setting with structured reasoning.
        
        Args:
            story_content: The story content
            context: Previous context
            
        Returns:
            Setting creation with reasoning
        """
        # Extract relevant information
        plot_structure = self._extract_plot_structure(story_content)
        characters = self._extract_characters(story_content)
        
        # Reason about world-building
        setting_result = self.setting_reasoner(
            plot_structure=plot_structure,
            characters=characters
        )
        
        return f"WORLD-BUILDING REASONING:\n{setting_result.world_building}"
    
    def _extract_plot_structure(self, content: str) -> str:
        """Extract plot structure from content."""
        if "PLOT STRUCTURE:" in content:
            return content.split("PLOT STRUCTURE:")[1].strip()
        return content
    
    def _extract_characters(self, content: str) -> str:
        """Extract character information from content."""
        if "CHARACTER REASONING:" in content:
            return content.split("CHARACTER REASONING:")[1].strip()
        return content

