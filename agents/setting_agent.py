"""
Setting Creator Agent for story writing.
This agent is responsible for developing detailed world-building and setting descriptions.
"""

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from llm import get_llm

class SettingAgent:
    def __init__(self):
        """Initialize the Setting Creator Agent."""
        self.llm = get_llm()
        
        self.prompt = PromptTemplate(
            input_variables=["story_content", "context"],
            template="""
You are a Setting Creator Assistant, an expert in world-building and creating immersive story environments.

Your task is to analyze the given story content and develop detailed setting descriptions. Focus on:

1. **Physical Environment**: Describe locations, landscapes, and architecture
2. **Atmosphere**: Create mood, tone, and sensory details
3. **World Rules**: Establish the laws of physics, magic, or society
4. **Cultural Context**: Develop customs, traditions, and social structures
5. **Historical Background**: Create a rich history that informs the present
6. **Sensory Details**: Include sights, sounds, smells, and textures

Story Content: {story_content}
Previous Context: {context}

Please develop comprehensive setting descriptions that include:
- Detailed location descriptions with sensory details
- The rules and logic of the world (magic systems, technology, etc.)
- Cultural and social structures
- Historical events that shaped the world
- Economic and political systems
- Climate, geography, and natural features
- Architecture and urban planning
- Transportation and communication methods
- Food, clothing, and daily life details

Create a world that feels lived-in and believable, with enough detail to immerse readers while leaving room for imagination. Ensure the setting supports and enhances the story's themes and plot.
"""
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
    
    def create_setting(self, story_content, context=""):
        """
        Create detailed setting descriptions based on the story content.
        
        Args:
            story_content (str): The story content to analyze
            context (str): Previous context or setting information
            
        Returns:
            str: The developed setting descriptions
        """
        return self.chain.run(story_content=story_content, context=context)
