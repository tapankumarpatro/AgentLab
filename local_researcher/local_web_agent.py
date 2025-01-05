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

searxng = Searxng(host="http://localhost:8080", engines=[], fixed_max_results=5, news=False, science=False)

ollama_groq_tool_model = 'llama3-groq-tool-use:latest'
ollama_llama31_model = 'llama3.1:latest'
ollama_qwen_model = "qwen2.5:latest"

local_model = Ollama(id=ollama_qwen_model)
gemini_model = Gemini(model="gemini-2.0-flash-exp", api_key=os.getenv("GOOGLE_API_KEY"))
openai_model = OpenAIChat(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

# choosen_model = openai_model
choosen_model = local_model

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=choosen_model,
    tools=[searxng], # DuckDuckGo()
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

writer_agent = Agent(
    name="Writer Agent",
    role="Create a well-structured and informative article from search results",
    model=choosen_model,
    tools=[Crawl4aiTools()],
    instructions=[
        "Given a topic, write a high-quality article on the topic.",
        "The article should be well-structured, informative, and engaging",
        "Ensure you provide a nuanced and balanced opinion, quoting facts where possible.",
        "Focus on clarity, coherence, and overall quality.",
        "Never make up facts or plagiarize. Always provide proper attribution.",
    ],
    show_tool_calls=True,
    markdown=True,
)

team_leader = Agent(
    team=[web_agent, writer_agent],
    model=choosen_model,
    instructions=["Always include sources", "Format the content based on required format"],
    show_tool_calls=True,
    markdown=True,
)

# team_leader.print_response("Difference between Phidata agentic Framework and Langchain agentic Framework", stream=True)

app = Playground(agents=[team_leader]).get_app()

if __name__ == "__main__":
    serve_playground_app("local_web_agent:app", reload=True)