"""
Conflict Generator Agent for story writing.
This agent is responsible for creating compelling conflicts and dramatic tension.
"""

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from llm import get_llm

class ConflictAgent:
    def __init__(self):
        """Initialize the Conflict Generator Agent."""
        self.llm = get_llm()
        
        self.prompt = PromptTemplate(
            input_variables=["story_content", "context"],
            template="""
You are a Conflict Generator Assistant, an expert in creating compelling conflicts and dramatic tension that drive stories forward.

Your task is to analyze the given story content and develop meaningful conflicts. Focus on:

1. **Internal Conflict**: Character vs. self - inner struggles and moral dilemmas
2. **Interpersonal Conflict**: Character vs. character - relationship tensions
3. **External Conflict**: Character vs. society, nature, or supernatural forces
4. **Escalating Tension**: Build conflict progressively throughout the story
5. **Stakes**: Make the consequences of conflict clear and meaningful
6. **Resolution**: Plan how conflicts will be resolved or transformed

Story Content: {story_content}
Previous Context: {context}

Please develop compelling conflicts that include:
- Multiple layers of conflict (internal, interpersonal, external)
- Clear stakes and consequences for each conflict
- Escalating tension that builds throughout the story
- Conflicts that test character values and force growth
- Obstacles that seem insurmountable but are overcome
- Moral dilemmas that challenge character beliefs
- Antagonists with believable motivations
- Conflicts that arise naturally from character goals and world rules
- Moments of crisis and turning points
- How conflicts will be resolved or transformed

Create conflicts that feel inevitable given the characters and world, but also surprising in their development. Ensure each conflict serves the story's themes and character development.
"""
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
    
    def generate_conflicts(self, story_content, context=""):
        """
        Generate compelling conflicts based on the story content.
        
        Args:
            story_content (str): The story content to analyze
            context (str): Previous context or conflict information
            
        Returns:
            str: The generated conflicts
        """
        return self.chain.run(story_content=story_content, context=context)
