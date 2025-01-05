# Local Web Agent - Multi-Agent Research System

## Overview

The Local Web Agent is a sophisticated multi-agent system designed for web-based research and content generation. It primarily uses local Ollama models for efficient, privacy-focused operation, combined with specialized web search capabilities to perform comprehensive research and generate high-quality content.

## Agent Structure

### Main Agents

1. **Web Agent**: Primary search agent that performs web research with the following capabilities:
   - Web search using Searxng (local instance)
   - Source tracking and citation
   - Structured information gathering

2. **Writer Agent**: Content generation specialist with features:
   - Well-structured content creation
   - Fact-based writing
   - Source attribution
   - Balanced opinion generation

## Technology Stack

### Primary Model

- Ollama (Local Models)
  - qwen2.5 (default)
  - llama3.1
  - llama3-groq-tool-use

### Optional Alternative Models

- Google Gemini (requires API key)
- OpenAI GPT Models (requires API key)

### Search Tools Integration

- Searxng (local instance)
- Crawl4ai Tools

## Features

### Search Capabilities

- Web content search and analysis
- Source verification
- Structured data extraction
- Configurable search parameters

### Content Generation

- Well-structured content creation
- Fact-based content
- Source attribution
- Balanced perspective

## Setup and Installation

### 1. Environment Setup

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install requirements
pip install phi-agent python-dotenv

# Create .env file
touch .env  # On Windows: type nul > .env
```

### 2. Environment Configuration

Add the following to your `.env` file if using optional cloud models:

```env
# Optional - only needed if using cloud models
GOOGLE_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key
```

### 3. Searxng Setup

Ensure you have Searxng running locally:

```bash
# Using Docker
docker run -d -p 8080:8080 searxng/searxng
```

### 4. Running the Agent

```python
# Run the agent with Phidata UI
python local_web_agent.py
```

This will start the Phidata playground UI:

```
Starting playground on http://localhost:7777
┏━━━━━━━━━━━━━━━━━━━━━━━ Agent Playground ━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                 ┃
┃  URL: https://phidata.app/playground?endpoint=localhost%3A7777  ┃
┃                                                                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

Access the UI through your browser and interact with the agents.

## Usage

The system can be used for:
1. Web research tasks
2. Content generation
3. Information synthesis
4. Article writing

## Best Practices

1. **Research Quality**
   - Always verify sources
   - Include proper citations
   - Maintain information accuracy

2. **Content Generation**
   - Ensure factual accuracy
   - Provide balanced perspectives
   - Include proper attributions

## Core Dependencies

- phi-agent
- python-dotenv
