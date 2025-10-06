"""
Plot Developer Agent for story writing.
This agent is responsible for developing the main plot and storyline.
"""

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from llm import get_llm

class PlotAgent:
    def __init__(self):
        """Initialize the Plot Developer Agent."""
        self.llm = get_llm()
        
        self.prompt = PromptTemplate(
            input_variables=["topic", "context"],
            template="""
You are a Plot Developer Assistant, an expert storyteller specializing in crafting compelling narratives and storylines.

Your task is to develop a detailed plot based on the given topic or story idea. Focus on:

1. **Story Structure**: Create a clear beginning, middle, and end
2. **Character Arcs**: Develop character growth and transformation
3. **Conflict and Resolution**: Introduce meaningful challenges and their resolutions
4. **Pacing**: Ensure the story flows naturally with appropriate tension
5. **Themes**: Weave in underlying messages or themes
6. **World-building Elements**: Establish the setting and rules of the world

Topic/Story Idea: {topic}
Previous Context: {context}

Please develop a comprehensive plot that includes:
- A compelling opening that hooks the reader
- Key plot points and turning points
- Character motivations and conflicts
- A satisfying resolution
- Any important world-building details

Write in a clear, engaging style that maintains narrative tension while providing enough detail for other agents to build upon.
"""
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
    
    def develop_plot(self, topic, context=""):
        """
        Develop a plot based on the given topic.
        
        Args:
            topic (str): The story topic or idea
            context (str): Previous context or story elements
            
        Returns:
            str: The developed plot
        """
        return self.chain.run(topic=topic, context=context)
