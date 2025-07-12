# OpenAI Agents Testing Application

A modular application for testing and developing OpenAI agents with a shared tool registry and Chainlit UI.

## Features

- **Modular Agent System**: Easy to add new agents and integrate them into complex workflows
- **Shared Tool Registry**: Centralized tool management that agents can access
- **Chainlit UI**: Interactive web interface for testing agents during development
- **Extensible Architecture**: Clean separation of concerns for easy maintenance

## Project Structure

```
├── agents/                 # Agent implementations
│   ├── __init__.py
│   ├── base_agent.py      # Base agent class
│   ├── research_agent.py  # Example research agent
│   └── math_agent.py      # Example math agent
├── tools/                  # Tool implementations
│   ├── __init__.py
│   ├── tool_registry.py   # Central tool registry
│   ├── calculator.py      # Calculator tool
│   └── file_operations.py # File operation tools
├── workflows/             # Complex agent workflows
│   ├── __init__.py
│   └── research_workflow.py
├── config/               # Configuration files
│   ├── __init__.py
│   └── settings.py
├── chainlit_app.py       # Main Chainlit application
├── requirements.txt      # Python dependencies
└── .env.example         # Environment variables template
```

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Copy environment template:

```bash
cp .env.example .env
```

3. Add your OpenAI API key to `.env`:

```
OPENAI_API_KEY=your_api_key_here
```

4. Run the application:

```bash
chainlit run chainlit_app.py
```

## Adding New Agents

1. Create a new file in `agents/` directory
2. Inherit from `BaseAgent` class
3. Implement required methods
4. Register the agent in the main application

## Adding New Tools

1. Create a new file in `tools/` directory
2. Implement the tool function
3. Register it in `tool_registry.py`
4. Agents can now access the tool automatically

## Usage

- Start the application and open the Chainlit UI
- Select an agent from the dropdown
- Interact with the agent through the chat interface
- Use workflows to combine multiple agents

## Example Workflows

- **Research Workflow**: Combines web search and analysis agents
- **Math Workflow**: Uses calculator and validation agents
- **Custom Workflows**: Easy to create new combinations
