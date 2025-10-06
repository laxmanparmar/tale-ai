"""
Character Developer Agent for story writing.
This agent is responsible for developing detailed character profiles and personalities.
"""

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from llm import get_llm

class CharacterAgent:
    def __init__(self):
        """Initialize the Character Developer Agent."""
        self.llm = get_llm()
        
        self.prompt = PromptTemplate(
            input_variables=["story_content", "context"],
            template="""
You are a Character Developer Assistant, an expert in creating rich, multi-dimensional characters for stories.

Your task is to analyze the given story content and develop detailed character profiles. Focus on:

1. **Character Depth**: Create complex, believable personalities
2. **Motivations**: Define clear goals, desires, and fears
3. **Background**: Develop rich backstories that inform present behavior
4. **Relationships**: Establish connections between characters
5. **Character Arcs**: Plan how characters will grow and change
6. **Voice**: Give each character a distinct way of speaking and thinking

Story Content: {story_content}
Previous Context: {context}

Please develop comprehensive character profiles that include:
- Physical descriptions and mannerisms
- Personality traits and quirks
- Motivations, goals, and fears
- Background and history
- Relationships with other characters
- Character flaws and strengths
- How they speak and behave
- Their role in the story

Create characters that feel real and relatable, with both admirable qualities and human flaws. Ensure each character serves a purpose in the story and contributes to the overall narrative.
"""
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
    
    def develop_characters(self, story_content, context=""):
        """
        Develop detailed character profiles based on the story content.
        
        Args:
            story_content (str): The story content to analyze
            context (str): Previous context or character information
            
        Returns:
            str: The developed character profiles
        """
        return self.chain.run(story_content=story_content, context=context)
