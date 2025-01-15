from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.website import WebsiteTools
from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
# from phi.tools.yfinance import YFinanceTools
from phi.tools.crawl4ai_tools import Crawl4aiTools
from phi.tools.searxng import Searxng
from dotenv import load_dotenv
import os
from phi.model.openai import OpenAIChat
from phi.playground import Playground, serve_playground_app
load_dotenv()

searxng = Searxng(host="http://192.168.1.40:8080", engines=[], fixed_max_results=5, news=False, science=False)
company_name = "iNeuorn.ai"
ollama_qwen_model = "qwen2.5:latest"


local_model = Ollama(id=ollama_qwen_model)
# gemini_model = Gemini(model="gemini-2.0-flash-exp", api_key=os.getenv("GOOGLE_API_KEY"))
# openai_model = OpenAIChat(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

# choosen_model = openai_model
choosen_model = local_model

web_agent = Agent(
    name="Web Agent",
    role="Search the web for general company information",
    model=choosen_model,
    tools=[searxng,  WebsiteTools()],
    instructions=[
        f"Produce a report about {company_name}",
        "Search for their website, Huggingface, and Crunchbase",
        "Provide a detailed summary with a unique fact",
        f"Draft a message to {company_name} thanking them for their work"
    ],
    show_tool_calls=True,
    markdown=True,
)

legal_agent = Agent(
    name="Legal Agent",
    role="Analyze company's legal status and compliance",
    model=choosen_model,
    tools=[searxng, WebsiteTools(), Crawl4aiTools()],
    instructions=[
        f"Produce a legal report about {company_name}",
        "Search for their website, legal pages, and EDGAR",
        "Provide a detailed summary with a unique fact about legal standing"
    ],
    show_tool_calls=True,
    markdown=True,
)

sentiment_agent = Agent(
    name="Sentiment Analysis Agent",
    role="Analyze public sentiment and social media presence",
    model=choosen_model,
    tools=[searxng, WebsiteTools(), Crawl4aiTools()],
    instructions=[
        f"Analyze sentiment for {company_name}",
        "Search their website, social media, and review sites",
        "Provide a detailed summary with a unique fact about sentiment"
    ],
    show_tool_calls=True,
    markdown=True,
)

product_agent = Agent(
    name="Product and Services Agent",
    role="Analyze company's products and services",
    model=choosen_model,
    tools=[searxng, WebsiteTools(), Crawl4aiTools()],
    instructions=[
        f"Report on products and services of {company_name}",
        "Search their website and product/service pages",
        "Provide a detailed summary with a unique fact about offerings"
    ],
    show_tool_calls=True,
    markdown=True,
)

financial_agent = Agent(
    name="Financial Agent",
    role="Analyze company's financial status and performance",
    model=choosen_model,
    tools=[searxng, WebsiteTools(), Crawl4aiTools()],
    instructions=[
        f"Produce a financial report about {company_name}",
        "Search their website, Crunchbase, and EDGAR",
        "Provide a detailed summary with a unique financial fact"
    ],
    show_tool_calls=True,
    markdown=True,
)
# financial_agent.print_response(
#     f"Produce a financial report about {company_name}",
#     markdown=True,
# )


writer_agent = Agent(
    name="Report Coordinator",
    role="Lead the team to produce a comprehensive final report on the company",
    model=choosen_model,
    team=[
        web_agent,
        legal_agent,
        sentiment_agent,
        product_agent,
        financial_agent
    ],
    instructions=[
        "Coordinate with the team to gather all relevant information about the company.",
        "Synthesize the data from each team member into a cohesive, well-structured report.",
        "Ensure the report covers all aspects: general info, legal standing, sentiment analysis, products/services, and financials.",
        "Maintain a balanced and objective tone throughout the report.",
        "Highlight key insights and unique facts from each area of analysis.",
        "Properly attribute information to the respective team members and their sources.",
        "Conclude with an executive summary that provides a holistic view of the company.",
    ],
    show_tool_calls=True,
    markdown=True,
)


writer_agent.print_response(
    f"Produce a report about {company_name}",
    markdown=True,
)