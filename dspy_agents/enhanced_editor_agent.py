"""
DSPy-enhanced Editor Agent with reasoning capabilities.
"""

import dspy
from dspy_modules.reasoning import StorySynthesis

class EnhancedEditorAgent:
    """Editor agent with DSPy reasoning capabilities."""
    
    def __init__(self):
        self.synthesizer = dspy.ChainOfThought(StorySynthesis)
    
    def edit_story(self, story_content: str, context: str = "") -> str:
        """
        Edit story with structured reasoning and synthesis.
        
        Args:
            story_content: The story content
            context: Previous context
            
        Returns:
            Final edited story with reasoning
        """
        # Extract all components
        plot_structure = self._extract_plot_structure(story_content)
        characters = self._extract_characters(story_content)
        world_building = self._extract_world_building(story_content)
        conflicts = self._extract_conflicts(story_content)
        dialogue_strategy = self._extract_dialogue_strategy(story_content)
        
        # Synthesize everything into final story
        synthesis_result = self.synthesizer(
            plot_structure=plot_structure,
            characters=characters,
            world_building=world_building,
            conflicts=conflicts,
            dialogue_strategy=dialogue_strategy
        )
        
        return synthesis_result.final_story
    
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
    
    def _extract_conflicts(self, content: str) -> str:
        """Extract conflict information from content."""
        if "CONFLICT REASONING:" in content:
            return content.split("CONFLICT REASONING:")[1].strip()
        return content
    
    def _extract_dialogue_strategy(self, content: str) -> str:
        """Extract dialogue strategy from content."""
        if "DIALOGUE REASONING:" in content:
            return content.split("DIALOGUE REASONING:")[1].strip()
        return content

