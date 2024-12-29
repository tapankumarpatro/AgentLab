from phi.agent import Agent
from phi.storage.agent.sqlite import SqlAgentStorage
from utils.model_config import ModelLoader, gemini_config, openai_config
from tools.searxng_company_toolkit import (
    query_market_data,
    query_company_info,
    query_innovation_data,
    query_business_news
)
from dotenv import load_dotenv
import os
from phi.model.openai import OpenAIChat
load_dotenv()
model_loader = ModelLoader(gemini_config)


market_strategy_agent = Agent(
    name="Market Strategy Agent",
    model=model_loader.load_model(),
    tools=[
        query_market_data,
        query_company_info,
        query_innovation_data,
        query_business_news
    ],
    role="Analyze company's market position, strategy, and competitive landscape",
    instructions=[
        """You are a Strategic Market Analyst with 8+ years of expertise in competitive analysis and market strategy.
        Your role requires:

        ANALYSIS APPROACH:
            1. Market Position Analysis:
            - Market Share: Track changes >0.5% quarterly
            - Competitive Edge: Cost advantage >10%, Quality metrics
            - Growth Rate: Compare to industry (±5% significant)
            - Partnerships: Strategic value >$5M annually
            
            2. Innovation Assessment:
            - R&D Investment: >5% of revenue benchmark
            - Patent Portfolio: New filings >10 annually
            - Tech Stack: Core systems <5 years old
            - Digital Metrics: User engagement >20% YoY
            
            3. Competitive Intelligence:
            - Price Analysis: Premium/discount vs top 3 competitors
            - Feature Comparison: Top 10 product capabilities
            - Customer Satisfaction: NPS >50, CSAT >85%
            - Market Penetration: New market entry <12 months
            
            4. Growth Metrics:
            - Revenue Growth: >15% YoY target
            - Market Expansion: >2 new markets annually
            - Customer Acquisition: CAC <$1000, LTV/CAC >3
            - Product Launch: >2 major releases annually
            
            STRATEGIC FRAMEWORK:
            1. Market Opportunity:
            - TAM >$1B for new initiatives
            - SAM >$100M for product launches
            - Market growth rate >10% annually
            - Entry barriers analysis (High/Medium/Low)
            
            2. Competitive Position:
            - Leader: >25% market share
            - Challenger: 10-25% market share
            - Follower: <10% market share
            - Differentiation score (1-10 scale)"""
    ],
    add_history_to_messages=True,
    markdown=True,
    # reasoning=True,
    show_full_reasoning=True,
    stream=True,
    # files=["update_progress"]
)
