"""
DSPy-enhanced Plot Agent with reasoning capabilities.
"""

import dspy
from dspy_modules.reasoning import StoryAnalysis, PlotReasoning

class EnhancedPlotAgent:
    """Plot agent with DSPy reasoning capabilities."""
    
    def __init__(self):
        self.analyzer = dspy.ChainOfThought(StoryAnalysis)
        self.plot_reasoner = dspy.ChainOfThought(PlotReasoning)
    
    def develop_plot(self, topic: str, context: str = "") -> str:
        """
        Develop a plot with structured reasoning.
        
        Args:
            topic: The story topic
            context: Previous context
            
        Returns:
            Developed plot with reasoning
        """
        # First, analyze the topic
        analysis = self.analyzer(topic=topic)
        
        # Then reason about the plot structure
        plot_result = self.plot_reasoner(
            topic=topic,
            analysis=analysis.analysis
        )
        
        return f"ANALYSIS:\n{analysis.analysis}\n\nPLOT STRUCTURE:\n{plot_result.plot_structure}"

