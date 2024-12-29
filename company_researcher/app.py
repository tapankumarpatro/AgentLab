from phi.agent import Agent
from phi.playground import Playground, serve_playground_app
from utils.model_config import ModelLoader, openai_config
from news.business_news import business_news_agent
from news.financial_news import financial_news_agent
from news.market_strategy import market_strategy_agent
from news.reputation_social import reputation_social_agent
from news.legal_compliance import legal_compliance_agent
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv
import os

load_dotenv()
model_loader = ModelLoader(openai_config)

chief_research_agent = Agent(
    name="Chief Research Coordinator",
    model=OpenAIChat(id="gpt-4o-mini"),
    team=[
        business_news_agent,
        financial_news_agent,
        market_strategy_agent,
        reputation_social_agent,
        legal_compliance_agent
    ],
    role="Coordinate and synthesize comprehensive company research from specialized agents",
    instructions=[
        """You are the Chief Research Coordinator responsible for orchestrating comprehensive company analysis.
        Your role involves:

        COORDINATION APPROACH:
        1. Research Planning:
           - Determine which specialized agents to engage based on the research needs
           - Prioritize research areas based on query context
           - Ensure comprehensive coverage across all aspects
        
        2. Data Collection:
           - Delegate specific research tasks to appropriate agents
           - Monitor the quality and relevance of gathered information
           - Identify gaps in collected data
        
        3. Analysis Integration:
           - Synthesize findings from different agents
           - Identify patterns and connections across different areas
           - Resolve any contradictions in gathered information
        
        4. Report Generation:
           - Create comprehensive research reports
           - Highlight key findings and insights
           - Provide strategic recommendations
        
        REPORT STRUCTURE:
        1. Executive Summary
        2. Business Overview
        3. Financial Analysis
        4. Market Strategy
        5. Reputation & Social Impact
        6. Legal & Compliance
        7. Strategic Recommendations
        
        CRITICAL GUIDELINES:
        - Always cite sources for all information
        - Maintain consistency across different sections
        - Highlight conflicting information when found
        - Provide confidence levels for key findings
        - Include relevant dates for all data
        - Flag areas needing additional research
        
        When responding:
        1. First understand the specific research needs
        2. Delegate tasks to appropriate specialized agents
        3. Synthesize the findings into a coherent narrative
        4. Present a comprehensive analysis with clear recommendations"""
    ],
    add_history_to_messages=True,
    markdown=True,
    reasoning=True,
    show_full_reasoning=True,
    show_tool_calls=True,
   #  stream=True,
    debug_mode=True
)

# app = Playground(agents=[chief_research_agent]).get_app()

# if __name__ == "__main__":
#     serve_playground_app("app:app", reload=True)

chief_research_agent.print_response("""
Gather info on Tide fintech company.
""")
