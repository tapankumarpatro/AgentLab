import os 
from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.model.openai import OpenAIChat
from phi.model.google import Gemini

from dotenv import load_dotenv, find_dotenv
_=load_dotenv(find_dotenv())

# NEW TOOL
from clickup_tool import ClickUpTools

openai_model = OpenAIChat(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

choosen_model = openai_model

clickup_agent = Agent(
    name="ClickUp Agent",
    role="Manage ClickUp tasks and spaces",
    model=choosen_model,
    tools=[ClickUpTools(list_spaces=True, list_lists=True, list_tasks=True)],
    instructions=[
        "List tasks from a specific ClickUp list",
        ],
    show_tool_calls=True,
    markdown=True
    )

clickup_agent.print_response(
    "List tasks from a sustain",
    markdown=True,
)
