# Company Researcher - Multi-Agent System

## Overview
The Company Researcher is a sophisticated multi-agent system designed to perform comprehensive company analysis using specialized agents. Each agent focuses on specific aspects of company research, coordinated by a central Chief Research Agent.

## Agent Structure

### Main Coordinator
- **Chief Research Coordinator**: The primary agent that orchestrates the entire research process, delegates tasks, and synthesizes information from specialized agents.

### Specialized Research Agents
1. **Business News Agent**: Focuses on general business news and company developments
2. **Financial News Agent**: Analyzes financial performance and metrics
3. **Market Strategy Agent**: Evaluates market position and strategic initiatives
4. **Reputation & Social Agent**: Assesses company reputation and social impact
5. **Legal Compliance Agent**: Monitors legal and regulatory compliance

## Search Tools and Capabilities

### News Research Tools
- Business news search capabilities
- Financial data analysis tools
- Market research instruments
- Social media and reputation monitoring
- Legal and compliance tracking

### Integration Features
- Cross-reference verification
- Data synthesis capabilities
- Source validation
- Temporal analysis
- Confidence scoring

## Main App Agent Management

The Chief Research Coordinator manages the system through:

### 1. Research Planning
- Task delegation to specialized agents
- Priority determination
- Coverage optimization

### 2. Data Collection
- Coordinated information gathering
- Quality monitoring
- Gap identification

### 3. Analysis Integration
- Cross-domain synthesis
- Pattern identification
- Conflict resolution

### 4. Report Generation
- Comprehensive research reports
- Key findings highlight
- Strategic recommendations

## Report Structure
1. Executive Summary
2. Business Overview
3. Financial Analysis
4. Market Strategy
5. Reputation & Social Impact
6. Legal & Compliance
7. Strategic Recommendations

## Critical Guidelines
- Source citation requirement
- Cross-sectional consistency
- Conflict identification
- Confidence level indication
- Temporal data tracking
- Research gap flagging

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Environment Setup

1. Clone the repository:
```bash
git clone [repository-url]
cd company_researcher
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install phi-agent
pip install python-dotenv
pip install openai
```

4. Create a `.env` file in the root directory with the following variables:
```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
PHIDATA_API=your_phidata_api_key
```

### Running the Application

The main application can be run in two modes:

1. **Direct Agent Execution**:
```python
# Using app.py
from app import chief_research_agent

# Example query
response = chief_research_agent.print_response("""
    Gather info on [company name].
""")
```

2. **Interactive Playground Mode**:
```python
# Uncomment these lines in app.py
# app = Playground(agents=[chief_research_agent]).get_app()
# if __name__ == "__main__":
#     serve_playground_app("app:app", reload=True)
```

### Example Usage

```python
# Basic company research query
chief_research_agent.print_response("""
    Gather info on Tide fintech company.
""")

# The agent will coordinate with specialized agents to:
# 1. Collect business news
# 2. Analyze financial data
# 3. Evaluate market strategy
# 4. Assess reputation
# 5. Check legal compliance

## Technical Implementation
The system is built using the PHI agent framework, utilizing OpenAI's language models for intelligent processing and analysis. Each agent is configured with specific roles and instructions to maintain focused expertise in their respective domains.
