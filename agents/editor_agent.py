"""
Editor Agent for story writing.
This agent is responsible for final editing, polishing, and ensuring story coherence.
"""

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from llm import get_llm

class EditorAgent:
    def __init__(self):
        """Initialize the Editor Agent."""
        self.llm = get_llm()
        
        self.prompt = PromptTemplate(
            input_variables=["story_content", "context"],
            template="""
You are an Editor Assistant, an expert in refining and polishing stories to create a cohesive, engaging narrative.

Your task is to take the given story content and perform comprehensive editing. Focus on:

1. **Story Coherence**: Ensure all elements work together seamlessly
2. **Pacing**: Adjust the rhythm and flow of the narrative
3. **Character Consistency**: Maintain consistent character voices and behaviors
4. **Plot Logic**: Verify that events follow logically from one another
5. **Language Polish**: Improve clarity, style, and readability
6. **Emotional Impact**: Enhance the story's emotional resonance

Story Content: {story_content}
Previous Context: {context}

Please provide a polished version that addresses:
- Overall story structure and flow
- Character consistency and development
- Plot logic and pacing
- Language clarity and style
- Emotional impact and reader engagement
- Consistency in tone and voice
- Proper transitions between scenes and ideas
- Elimination of redundancy and unnecessary elements
- Strengthening of key moments and themes
- Ensuring the story has a satisfying beginning, middle, and end

Create a final version that is polished, engaging, and ready for readers. Maintain the story's unique voice while ensuring it meets professional storytelling standards.
"""
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
    
    def edit_story(self, story_content, context=""):
        """
        Edit and polish the story content.
        
        Args:
            story_content (str): The story content to edit
            context (str): Previous context or editing notes
            
        Returns:
            str: The edited and polished story
        """
        return self.chain.run(story_content=story_content, context=context)
