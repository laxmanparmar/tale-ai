"""
DSPy-enhanced Conflict Agent with reasoning capabilities.
"""

import dspy
from dspy_modules.reasoning import ConflictReasoning

class EnhancedConflictAgent:
    """Conflict agent with DSPy reasoning capabilities."""
    
    def __init__(self):
        self.conflict_reasoner = dspy.ChainOfThought(ConflictReasoning)
    
    def generate_conflicts(self, story_content: str, context: str = "") -> str:
        """
        Generate conflicts with structured reasoning.
        
        Args:
            story_content: The story content
            context: Previous context
            
        Returns:
            Conflict generation with reasoning
        """
        # Extract relevant information
        plot_structure = self._extract_plot_structure(story_content)
        characters = self._extract_characters(story_content)
        world_building = self._extract_world_building(story_content)
        
        # Reason about conflicts
        conflict_result = self.conflict_reasoner(
            plot_structure=plot_structure,
            characters=characters,
            world_building=world_building
        )
        
        return f"CONFLICT REASONING:\n{conflict_result.conflict_analysis}"
    
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
    
    def _extract_world_building(self, content: str) -> str:
        """Extract world-building information from content."""
        if "WORLD-BUILDING REASONING:" in content:
            return content.split("WORLD-BUILDING REASONING:")[1].strip()
        return content

