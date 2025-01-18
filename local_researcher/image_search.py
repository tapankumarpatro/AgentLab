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

searxng = Searxng(host="http://localhost:8080", engines=['google'], fixed_max_results=5, images=True)

openai_model = OpenAIChat(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
choosen_model = openai_model

image_search_agent = Agent(
    name="Image search Agent",
    role="Search the web for the image",
    model=choosen_model,
    tools=[searxng], 
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)

image_search_agent.print_response("Lidl's Plant-Based Push: Affordable Sustainability or Greenwashing?", stream=True)

# app = Playground(agents=[team_leader]).get_app()

# if __name__ == "__main__":
#     serve_playground_app("local_web_agent:app", reload=True)


