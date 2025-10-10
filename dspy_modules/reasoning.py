"""
DSPy reasoning modules for enhanced story generation.
"""

import dspy
from typing import List, Dict, Any
import json

class StoryAnalysis(dspy.Signature):
    """Analyze a story topic and break it down into key components."""
    topic = dspy.InputField(desc="The story topic or idea")
    analysis = dspy.OutputField(desc="Structured analysis with genre, themes, key elements, and target audience")

class PlotReasoning(dspy.Signature):
    """Reason about plot structure and develop a compelling narrative arc."""
    topic = dspy.InputField(desc="The story topic")
    analysis = dspy.InputField(desc="Story analysis from previous step")
    plot_structure = dspy.OutputField(desc="Detailed plot structure with acts, key events, and character arcs")

class CharacterReasoning(dspy.Signature):
    """Reason about character development and relationships."""
    plot_structure = dspy.InputField(desc="The plot structure")
    character_analysis = dspy.OutputField(desc="Character profiles with motivations, relationships, and development arcs")

class SettingReasoning(dspy.Signature):
    """Reason about world-building and setting details."""
    plot_structure = dspy.InputField(desc="The plot structure")
    characters = dspy.InputField(desc="Character information")
    world_building = dspy.OutputField(desc="Comprehensive world-building with rules, culture, and environment")

class ConflictReasoning(dspy.Signature):
    """Reason about conflicts and dramatic tension."""
    plot_structure = dspy.InputField(desc="The plot structure")
    characters = dspy.InputField(desc="Character information")
    world_building = dspy.InputField(desc="World-building information")
    conflict_analysis = dspy.OutputField(desc="Multi-layered conflicts with internal, interpersonal, and external tensions")

class DialogueReasoning(dspy.Signature):
    """Reason about dialogue and character voice."""
    characters = dspy.InputField(desc="Character information")
    conflicts = dspy.InputField(desc="Conflict information")
    dialogue_strategy = dspy.OutputField(desc="Dialogue strategy with character voices and key conversations")

class StorySynthesis(dspy.Signature):
    """Synthesize all elements into a cohesive story."""
    plot_structure = dspy.InputField(desc="Plot structure")
    characters = dspy.InputField(desc="Character information")
    world_building = dspy.InputField(desc="World-building")
    conflicts = dspy.InputField(desc="Conflict information")
    dialogue_strategy = dspy.InputField(desc="Dialogue strategy")
    final_story = dspy.OutputField(desc="Complete, polished story")

class StoryReasoningPipeline:
    """DSPy pipeline for structured story reasoning."""
    
    def __init__(self):
        self.analyzer = dspy.ChainOfThought(StoryAnalysis)
        self.plot_reasoner = dspy.ChainOfThought(PlotReasoning)
        self.character_reasoner = dspy.ChainOfThought(CharacterReasoning)
        self.setting_reasoner = dspy.ChainOfThought(SettingReasoning)
        self.conflict_reasoner = dspy.ChainOfThought(ConflictReasoning)
        self.dialogue_reasoner = dspy.ChainOfThought(DialogueReasoning)
        self.synthesizer = dspy.ChainOfThought(StorySynthesis)
    
    def reason_about_story(self, topic: str) -> Dict[str, Any]:
        """
        Perform structured reasoning about a story topic.
        
        Args:
            topic: The story topic or idea
            
        Returns:
            Dictionary containing all reasoning steps and final story
        """
        # Step 1: Analyze the topic
        analysis = self.analyzer(topic=topic)
        
        # Step 2: Reason about plot structure
        plot_structure = self.plot_reasoner(topic=topic, analysis=analysis.analysis)
        
        # Step 3: Reason about characters
        characters = self.character_reasoner(plot_structure=plot_structure.plot_structure)
        
        # Step 4: Reason about world-building
        world_building = self.setting_reasoner(
            plot_structure=plot_structure.plot_structure,
            characters=characters.character_analysis
        )
        
        # Step 5: Reason about conflicts
        conflicts = self.conflict_reasoner(
            plot_structure=plot_structure.plot_structure,
            characters=characters.character_analysis,
            world_building=world_building.world_building
        )
        
        # Step 6: Reason about dialogue
        dialogue = self.dialogue_reasoner(
            characters=characters.character_analysis,
            conflicts=conflicts.conflict_analysis
        )
        
        # Step 7: Synthesize everything into final story
        final_story = self.synthesizer(
            plot_structure=plot_structure.plot_structure,
            characters=characters.character_analysis,
            world_building=world_building.world_building,
            conflicts=conflicts.conflict_analysis,
            dialogue_strategy=dialogue.dialogue_strategy
        )
        
        return {
            "topic": topic,
            "analysis": analysis.analysis,
            "plot_structure": plot_structure.plot_structure,
            "characters": characters.character_analysis,
            "world_building": world_building.world_building,
            "conflicts": conflicts.conflict_analysis,
            "dialogue_strategy": dialogue.dialogue_strategy,
            "final_story": final_story.final_story
        }

class StoryOptimizer:
    """DSPy optimizer for improving story quality."""
    
    def __init__(self):
        self.pipeline = StoryReasoningPipeline()
    
    def optimize_story(self, topic: str, iterations: int = 3) -> Dict[str, Any]:
        """
        Optimize story generation through multiple iterations.
        
        Args:
            topic: The story topic
            iterations: Number of optimization iterations
            
        Returns:
            Optimized story with reasoning
        """
        best_story = None
        best_score = 0
        
        for i in range(iterations):
            result = self.pipeline.reason_about_story(topic)
            
            # Simple scoring based on length and structure
            score = len(result["final_story"]) + len(result["plot_structure"])
            
            if score > best_score:
                best_score = score
                best_story = result
        
        return best_story
