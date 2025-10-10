"""
FastAPI application with DSPy reasoning for Tale-AI story generation.
"""

import asyncio
import json
from typing import AsyncGenerator
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import os

# Import DSPy configuration
import dspy_config

# Import DSPy-enhanced agents
from dspy_agents.enhanced_plot_agent import EnhancedPlotAgent
from dspy_agents.enhanced_character_agent import EnhancedCharacterAgent
from dspy_agents.enhanced_setting_agent import EnhancedSettingAgent
from dspy_agents.enhanced_dialogue_agent import EnhancedDialogueAgent
from dspy_agents.enhanced_conflict_agent import EnhancedConflictAgent
from dspy_agents.enhanced_editor_agent import EnhancedEditorAgent

# Import DSPy reasoning pipeline
from dspy_modules.reasoning import StoryReasoningPipeline, StoryOptimizer

# Initialize FastAPI app
app = FastAPI(
    title="Tale-AI DSPy API",
    description="AI-Powered Story Generation with DSPy Reasoning",
    version="2.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DSPy-enhanced agents
plot_agent = EnhancedPlotAgent()
character_agent = EnhancedCharacterAgent()
setting_agent = EnhancedSettingAgent()
dialogue_agent = EnhancedDialogueAgent()
conflict_agent = EnhancedConflictAgent()
editor_agent = EnhancedEditorAgent()

# Initialize DSPy reasoning pipeline
reasoning_pipeline = StoryReasoningPipeline()
story_optimizer = StoryOptimizer()

# Pydantic models
class StoryRequest(BaseModel):
    topic: str
    use_reasoning: bool = True
    optimize: bool = False
    max_iterations: int = 3

class StreamMessage(BaseModel):
    type: str
    step: str = None
    content: str = None
    progress: float = None
    error: str = None
    reasoning: str = None

async def stream_dspy_story_generation(topic: str, use_reasoning: bool = True, optimize: bool = False, max_iterations: int = 3) -> AsyncGenerator[str, None]:
    """
    Stream DSPy-enhanced story generation with reasoning.
    """
    try:
        if use_reasoning and optimize:
            # Use DSPy reasoning pipeline with optimization
            yield json.dumps({
                "type": "step",
                "step": "Starting DSPy reasoning with optimization...",
                "progress": 0.0,
                "reasoning": "Using structured reasoning pipeline with optimization"
            }) + "\n"
            
            result = story_optimizer.optimize_story(topic, max_iterations)
            
            yield json.dumps({
                "type": "content",
                "step": "DSPy reasoning complete",
                "progress": 0.5,
                "content": result["analysis"],
                "reasoning": "Topic analysis completed"
            }) + "\n"
            
            yield json.dumps({
                "type": "content",
                "step": "Plot structure reasoned",
                "progress": 0.6,
                "content": result["plot_structure"],
                "reasoning": "Plot structure developed through reasoning"
            }) + "\n"
            
            yield json.dumps({
                "type": "content",
                "step": "Characters reasoned",
                "progress": 0.7,
                "content": result["characters"],
                "reasoning": "Character development through reasoning"
            }) + "\n"
            
            yield json.dumps({
                "type": "content",
                "step": "World-building reasoned",
                "progress": 0.8,
                "content": result["world_building"],
                "reasoning": "World-building through reasoning"
            }) + "\n"
            
            yield json.dumps({
                "type": "content",
                "step": "Conflicts reasoned",
                "progress": 0.9,
                "content": result["conflicts"],
                "reasoning": "Conflict generation through reasoning"
            }) + "\n"
            
            yield json.dumps({
                "type": "complete",
                "step": "Story generation complete",
                "progress": 1.0,
                "content": result["final_story"],
                "reasoning": "Final story synthesized through DSPy reasoning"
            }) + "\n"
            
        elif use_reasoning:
            # Use DSPy reasoning pipeline without optimization
            yield json.dumps({
                "type": "step",
                "step": "Starting DSPy reasoning...",
                "progress": 0.0,
                "reasoning": "Using structured reasoning pipeline"
            }) + "\n"
            
            result = reasoning_pipeline.reason_about_story(topic)
            
            yield json.dumps({
                "type": "content",
                "step": "DSPy reasoning complete",
                "progress": 1.0,
                "content": result["final_story"],
                "reasoning": "Story generated through DSPy reasoning pipeline"
            }) + "\n"
            
        else:
            # Use enhanced agents with reasoning
            total_steps = 6
            current_step = 0
            
            # Step 1: Enhanced Plot Development
            current_step += 1
            yield json.dumps({
                "type": "step",
                "step": "Developing plot with DSPy reasoning...",
                "progress": current_step / total_steps,
                "reasoning": "Using ChainOfThought for plot development"
            }) + "\n"
            
            plot_content = plot_agent.develop_plot(topic)
            yield json.dumps({
                "type": "content",
                "step": "Plot developed with reasoning",
                "progress": current_step / total_steps,
                "content": plot_content,
                "reasoning": "Plot structure analyzed and developed"
            }) + "\n"
            
            # Step 2: Enhanced Character Development
            current_step += 1
            yield json.dumps({
                "type": "step",
                "step": "Developing characters with DSPy reasoning...",
                "progress": current_step / total_steps,
                "reasoning": "Using ChainOfThought for character development"
            }) + "\n"
            
            character_content = character_agent.develop_characters(plot_content)
            yield json.dumps({
                "type": "content",
                "step": "Characters developed with reasoning",
                "progress": current_step / total_steps,
                "content": character_content,
                "reasoning": "Character profiles developed through reasoning"
            }) + "\n"
            
            # Step 3: Enhanced Setting Creation
            current_step += 1
            yield json.dumps({
                "type": "step",
                "step": "Creating setting with DSPy reasoning...",
                "progress": current_step / total_steps,
                "reasoning": "Using ChainOfThought for world-building"
            }) + "\n"
            
            setting_content = setting_agent.create_setting(character_content, plot_content)
            yield json.dumps({
                "type": "content",
                "step": "Setting created with reasoning",
                "progress": current_step / total_steps,
                "content": setting_content,
                "reasoning": "World-building developed through reasoning"
            }) + "\n"
            
            # Step 4: Enhanced Conflict Generation
            current_step += 1
            yield json.dumps({
                "type": "step",
                "step": "Generating conflicts with DSPy reasoning...",
                "progress": current_step / total_steps,
                "reasoning": "Using ChainOfThought for conflict generation"
            }) + "\n"
            
            conflict_content = conflict_agent.generate_conflicts(setting_content, character_content)
            yield json.dumps({
                "type": "content",
                "step": "Conflicts generated with reasoning",
                "progress": current_step / total_steps,
                "content": conflict_content,
                "reasoning": "Conflicts developed through reasoning"
            }) + "\n"
            
            # Step 5: Enhanced Dialogue Writing
            current_step += 1
            yield json.dumps({
                "type": "step",
                "step": "Writing dialogue with DSPy reasoning...",
                "progress": current_step / total_steps,
                "reasoning": "Using ChainOfThought for dialogue development"
            }) + "\n"
            
            dialogue_content = dialogue_agent.write_dialogue(conflict_content, setting_content)
            yield json.dumps({
                "type": "content",
                "step": "Dialogue written with reasoning",
                "progress": current_step / total_steps,
                "content": dialogue_content,
                "reasoning": "Dialogue developed through reasoning"
            }) + "\n"
            
            # Step 6: Enhanced Final Editing
            current_step += 1
            yield json.dumps({
                "type": "step",
                "step": "Final editing with DSPy reasoning...",
                "progress": current_step / total_steps,
                "reasoning": "Using ChainOfThought for story synthesis"
            }) + "\n"
            
            final_story = editor_agent.edit_story(dialogue_content, conflict_content)
            yield json.dumps({
                "type": "complete",
                "step": "Story generation complete",
                "progress": 1.0,
                "content": final_story,
                "reasoning": "Final story synthesized through DSPy reasoning"
            }) + "\n"
        
    except Exception as e:
        yield json.dumps({
            "type": "error",
            "step": "Error occurred",
            "progress": 0.0,
            "error": str(e),
            "reasoning": "Error in DSPy reasoning pipeline"
        }) + "\n"

@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Tale-AI DSPy API",
        "version": "2.0.0",
        "features": ["DSPy Reasoning", "ChainOfThought", "Story Optimization"],
        "endpoints": {
            "POST /generate-story": "Generate a story with DSPy reasoning",
            "GET /health": "Health check endpoint",
            "GET /reasoning-methods": "Available reasoning methods"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "tale-ai-dspy"}

@app.get("/reasoning-methods")
async def get_reasoning_methods():
    """Get available reasoning methods."""
    return {
        "reasoning_methods": [
            {
                "name": "ChainOfThought",
                "description": "Step-by-step reasoning for each story component",
                "use_case": "Detailed reasoning for plot, characters, setting, etc."
            },
            {
                "name": "StoryReasoningPipeline",
                "description": "Structured pipeline for comprehensive story reasoning",
                "use_case": "Complete story analysis and development"
            },
            {
                "name": "StoryOptimizer",
                "description": "Optimized story generation through multiple iterations",
                "use_case": "High-quality story generation with optimization"
            }
        ]
    }

@app.post("/generate-story")
async def generate_story_with_reasoning(request: StoryRequest):
    """
    Generate a story with DSPy reasoning capabilities.
    
    Args:
        request: StoryRequest containing topic and reasoning options
        
    Returns:
        StreamingResponse with JSON chunks including reasoning
    """
    if not request.topic.strip():
        raise HTTPException(status_code=400, detail="Topic cannot be empty")
    
    return StreamingResponse(
        stream_dspy_story_generation(
            request.topic, 
            request.use_reasoning, 
            request.optimize, 
            request.max_iterations
        ),
        media_type="application/x-ndjson",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-ndjson",
        }
    )

@app.get("/config")
async def get_config():
    """Get current DSPy and LLM configuration."""
    return {
        "dspy_configured": True,
        "model_name": os.getenv("OPENAI_MODEL_NAME", "llama3.2"),
        "base_url": os.getenv("OPENAI_BASE_URL", "http://localhost:1234/v1"),
        "temperature": float(os.getenv("TEMPERATURE", "0.7")),
        "max_tokens": int(os.getenv("MAX_TOKENS", "2000")),
        "reasoning_methods": ["ChainOfThought", "StoryReasoningPipeline", "StoryOptimizer"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
