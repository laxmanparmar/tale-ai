"""
Dialogue Writer Agent for story writing.
This agent is responsible for crafting natural, engaging dialogue between characters.
"""

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from llm import get_llm

class DialogueAgent:
    def __init__(self):
        """Initialize the Dialogue Writer Agent."""
        self.llm = get_llm()
        
        self.prompt = PromptTemplate(
            input_variables=["story_content", "context"],
            template="""
You are a Dialogue Writer Assistant, an expert in crafting natural, engaging dialogue that brings characters to life.

Your task is to analyze the given story content and create compelling dialogue. Focus on:

1. **Character Voice**: Give each character a distinct way of speaking
2. **Natural Flow**: Make conversations feel realistic and organic
3. **Subtext**: Include underlying meanings and emotions
4. **Conflict**: Use dialogue to create tension and drama
5. **Reveal Character**: Show personality through speech patterns
6. **Advance Plot**: Use dialogue to move the story forward

Story Content: {story_content}
Previous Context: {context}

Please create engaging dialogue that includes:
- Natural speech patterns that reflect each character's personality
- Appropriate use of contractions, slang, and regional speech
- Emotional subtext and underlying tensions
- Dialogue that reveals character traits and motivations
- Conversations that advance the plot and create conflict
- Varied sentence structures and speech rhythms
- Appropriate use of dialogue tags and action beats
- Moments of silence, hesitation, and non-verbal communication

Create dialogue that feels authentic and helps readers connect with the characters. Each line should serve a purpose - whether to reveal character, advance plot, or create emotional impact.
"""
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
    
    def write_dialogue(self, story_content, context=""):
        """
        Write engaging dialogue based on the story content.
        
        Args:
            story_content (str): The story content to analyze
            context (str): Previous context or dialogue information
            
        Returns:
            str: The crafted dialogue
        """
        return self.chain.run(story_content=story_content, context=context)
