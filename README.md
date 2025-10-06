# Tale-AI: AI-Powered Story Generation

A sophisticated story generation system using LangChain and multiple specialized AI agents to create compelling narratives.

## Features

- **Plot Developer Agent**: Creates detailed storylines and plot structures
- **Character Developer Agent**: Develops rich, multi-dimensional characters
- **Setting Creator Agent**: Builds immersive worlds and environments
- **Dialogue Writer Agent**: Crafts natural, engaging dialogue
- **Conflict Generator Agent**: Creates compelling conflicts and dramatic tension
- **Editor Agent**: Polishes and refines the final story

## Prerequisites

- Python 3.8+
- LM Studio (for local LLM hosting)
- Llama 3.2 model (or compatible model)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd tale-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
export OPENAI_API_KEY=fake-key
export OPENAI_MODEL_NAME=llama3.2
export OPENAI_BASE_URL=http://localhost:1234/v1
```

## Usage

1. Start LM Studio and load your Llama 3.2 model
2. Run the story generation:
```bash
python app.py
```

## Project Structure

```
tale-ai/
├── agents/                 # Individual agent modules
│   ├── __init__.py
│   ├── plot_agent.py      # Plot development agent
│   ├── character_agent.py # Character development agent
│   ├── setting_agent.py   # World-building agent
│   ├── dialogue_agent.py  # Dialogue writing agent
│   ├── conflict_agent.py  # Conflict generation agent
│   └── editor_agent.py    # Final editing agent
├── llm.py                 # Single LLM instance for all agents
├── app.py                 # Main application
├── example_switch_model.py # Example of model switching
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## How It Works

The system uses a multi-agent workflow:

1. **Plot Development**: Creates the main storyline and structure
2. **Character Development**: Develops detailed character profiles
3. **Setting Creation**: Builds the world and environment
4. **Conflict Generation**: Creates dramatic tension and obstacles
5. **Dialogue Writing**: Crafts character conversations
6. **Final Editing**: Polishes the complete story

Each agent uses LangChain with specialized prompts to ensure high-quality, coherent storytelling.

## Model Configuration

The system uses a simple centralized LLM module (`llm.py`) that creates a single instance used by all agents. Configure via environment variables.

### Environment Variables

- `OPENAI_MODEL_NAME` - Model name (default: "llama3.2")
- `OPENAI_API_KEY` - API key (default: "fake-key")
- `OPENAI_BASE_URL` - Base URL (default: "http://localhost:1234/v1")
- `TEMPERATURE` - Model temperature (default: "0.7")
- `MAX_TOKENS` - Maximum tokens (default: "2000")


## Customization

You can modify individual agent prompts in the `agents/` directory to customize the storytelling style, genre, or specific requirements for your use case.

