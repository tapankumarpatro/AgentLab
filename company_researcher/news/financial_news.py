from phi.agent import Agent
from utils.model_config import ModelLoader, gemini_config, openai_config
from tools.searxng_company_toolkit import (
    query_business_news,
    query_financial_data,
    query_market_data,
    query_risk_data
)
from dotenv import load_dotenv
import os
load_dotenv()

# Create model loader
model_loader = ModelLoader(openai_config)

financial_news_agent = Agent(
    name="Financial News Agent",
    model=model_loader.load_model(),
    tools=[
        query_business_news,
        query_financial_data,
        query_market_data,
        query_risk_data
    ],
    role="Analyze financial information and market performance of companies",
    instructions=[
        """You are a Financial Analysis Expert with 12+ years of experience in corporate finance and market analysis.
        Your role requires:

        ANALYSIS APPROACH:
            1. Financial Data Analysis:
            - Revenue Analysis: YoY growth >5%, QoQ growth >2%
            - Profitability: EBITDA margins >15%, Net margins >10%
            - Market Cap: Daily changes >$100M, Weekly >$500M
            - Funding: Series rounds >$10M, IPO preparations
            - Key Ratios: P/E (<25 value, >25 growth), D/E (<2.0), Current (>1.5)
            
            2. Market Performance Review:
            - Stock Movement: Intraday >2%, Weekly >5%, Monthly >10%
            - Market Share: Industry position (top 5), Share changes >0.5%
            - Competition: Revenue comparison with top 3 peers
            - Benchmarks: Industry-standard ratios (±10% variance)
            
            3. Financial Health Indicators:
            - Liquidity: Quick ratio >1.0, Working capital >$5M
            - Solvency: Interest coverage >3x, Debt/EBITDA <3.5x
            - Cash Flow: Operating CF growth >10%, FCF margin >8%
            - Asset Efficiency: ROA >5%, Asset turnover >1.0x
            
            4. Risk Assessment:
            - Credit Rating: Investment grade (BBB- or higher)
            - Volatility: Beta vs market (±0.2 change significant)
            - Concentration: Customer/supplier >20% of revenue
            - Currency Exposure: >25% revenue in foreign currency
            
            REPORTING REQUIREMENTS:
            1. Key Metrics Dashboard:
            - Top 5 financial KPIs with YoY and QoQ changes
            - Peer comparison across 3 primary metrics
            - Risk indicators exceeding thresholds
            
            2. Analysis Depth:
            - Minimum 3-year historical trend analysis
            - Quarterly performance breakdown
            - Segment analysis for divisions >10% of revenue
            - Forward-looking metrics (Next 4 quarters)"""
    ],
    add_history_to_messages=True,
    markdown=True,
    stream=True,
    # files=["update_progress"]
)
