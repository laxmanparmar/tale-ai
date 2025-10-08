import asyncio
import json
from typing import AsyncGenerator
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import os

from agents.plot_agent import PlotAgent
from agents.character_agent import CharacterAgent
from agents.setting_agent import SettingAgent
from agents.dialogue_agent import DialogueAgent
from agents.conflict_agent import ConflictAgent
from agents.editor_agent import EditorAgent

# Initialize FastAPI app
app = FastAPI(
    title="Tale-AI API",
    description="AI-Powered Story Generation with Streaming",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agents
plot_agent = PlotAgent()
character_agent = CharacterAgent()
setting_agent = SettingAgent()
dialogue_agent = DialogueAgent()
conflict_agent = ConflictAgent()
editor_agent = EditorAgent()

# Pydantic models
class StoryRequest(BaseModel):
    topic: str
    max_length: int = 2000

class StreamMessage(BaseModel):
    type: str  # "step", "content", "complete", "error"
    step: str = None
    content: str = None
    progress: float = None
    error: str = None

async def stream_story_generation(topic: str, max_length: int = 2000) -> AsyncGenerator[str, None]:
    try:
        total_steps = 6
        current_step = 0
        
        # Step 1: Plot Development
        current_step += 1
        yield json.dumps({
            "type": "step",
            "step": "Developing plot...",
            "progress": current_step / total_steps,
            "content": None
        }) + "\n"
        
        plot_content = plot_agent.develop_plot(topic)
        yield json.dumps({
            "type": "content",
            "step": "Plot developed",
            "progress": current_step / total_steps,
            "content": plot_content
        }) + "\n"
        
        # Step 2: Character Development
        current_step += 1
        yield json.dumps({
            "type": "step",
            "step": "Developing characters...",
            "progress": current_step / total_steps,
            "content": None
        }) + "\n"
        
        character_content = character_agent.develop_characters(plot_content)
        yield json.dumps({
            "type": "content",
            "step": "Characters developed",
            "progress": current_step / total_steps,
            "content": character_content
        }) + "\n"
        
        # Step 3: Setting Creation
        current_step += 1
        yield json.dumps({
            "type": "step",
            "step": "Creating setting...",
            "progress": current_step / total_steps,
            "content": None
        }) + "\n"
        
        setting_content = setting_agent.create_setting(character_content, plot_content)
        yield json.dumps({
            "type": "content",
            "step": "Setting created",
            "progress": current_step / total_steps,
            "content": setting_content
        }) + "\n"
        
        # Step 4: Conflict Generation
        current_step += 1
        yield json.dumps({
            "type": "step",
            "step": "Generating conflicts...",
            "progress": current_step / total_steps,
            "content": None
        }) + "\n"
        
        conflict_content = conflict_agent.generate_conflicts(setting_content, character_content)
        yield json.dumps({
            "type": "content",
            "step": "Conflicts generated",
            "progress": current_step / total_steps,
            "content": conflict_content
        }) + "\n"
        
        # Step 5: Dialogue Writing
        current_step += 1
        yield json.dumps({
            "type": "step",
            "step": "Writing dialogue...",
            "progress": current_step / total_steps,
            "content": None
        }) + "\n"
        
        dialogue_content = dialogue_agent.write_dialogue(conflict_content, setting_content)
        yield json.dumps({
            "type": "content",
            "step": "Dialogue written",
            "progress": current_step / total_steps,
            "content": dialogue_content
        }) + "\n"
        
        # Step 6: Final Editing
        current_step += 1
        yield json.dumps({
            "type": "step",
            "step": "Final editing...",
            "progress": current_step / total_steps,
            "content": None
        }) + "\n"
        
        final_story = editor_agent.edit_story(dialogue_content, conflict_content)
        yield json.dumps({
            "type": "content",
            "step": "Story completed",
            "progress": 1.0,
            "content": final_story
        }) + "\n"
        
        # Complete
        yield json.dumps({
            "type": "complete",
            "step": "Story generation complete",
            "progress": 1.0,
            "content": final_story
        }) + "\n"
        
    except Exception as e:
        yield json.dumps({
            "type": "error",
            "step": "Error occurred",
            "progress": 0.0,
            "error": str(e)
        }) + "\n"

@app.get("/")
async def root():
    return {
        "message": "Tale-AI API",
        "version": "1.0.0",
        "endpoints": {
            "POST /generate-story": "Generate a story with streaming response",
            "GET /health": "Health check endpoint"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "tale-ai"}

@app.post("/generate-story")
async def generate_story(request: StoryRequest):
    """
    Generate a story with streaming response.
    
    Args:
        request: StoryRequest containing topic and max_length
        
    Returns:
        StreamingResponse with JSON chunks
    """
    if not request.topic.strip():
        raise HTTPException(status_code=400, detail="Topic cannot be empty")
    
    return StreamingResponse(
        stream_story_generation(request.topic, request.max_length),
        media_type="application/x-ndjson",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-ndjson",
        }
    )

@app.get("/config")
async def get_config():
    """Get current LLM configuration."""
    return {
        "model_name": os.getenv("OPENAI_MODEL_NAME", "llama3.2"),
        "base_url": os.getenv("OPENAI_BASE_URL", "http://localhost:1234/v1"),
        "temperature": float(os.getenv("TEMPERATURE", "0.7")),
        "max_tokens": int(os.getenv("MAX_TOKENS", "2000"))
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
