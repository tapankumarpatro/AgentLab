import os 
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from clickup_tool import ClickUpTools
from phi.tools.github import GithubTools
from dotenv import load_dotenv, find_dotenv
_=load_dotenv(find_dotenv())

github_agent = Agent(
    name="GitHub Agent",
    role="Manage GitHub repositories and issues",
    model=OpenAIChat(model="gpt-4o-mini"),
    tools=[GithubTools()],
    instructions=[
        "You are a GitHub assistant that helps users manage their repositories and issues.",
        "You can:",
        "1. List repositories",
        "2. Create new issues",
        "3. List issues for a repository",
        "4. Comment on issues",
        
        "When creating issues:",
        "- Always get repository name, issue title, and description",
        "- Labels can be added if specified",
        
        "Be helpful and guide users if they need more information about GitHub operations.",
    ],
    show_tool_calls=True,
    markdown=True
)

clickup_agent = Agent(
    name="ClickUp Agent",
    role="Manage ClickUp tasks and spaces",
    model=OpenAIChat(model="gpt-4o-mini"),
    tools=[ClickUpTools(list_spaces=True, list_lists=True, list_tasks=True)],
    instructions=[
        "You are a ClickUp assistant that helps users manage their tasks and spaces.",
        "You can:",
        "1. List all available spaces",
        "2. List tasks from a specific space",
        "3. List all lists in a space",
        "4. Create new tasks with title, description, and status",
        
        "When creating tasks:",
        "- Always get space name, task name, and description",
        "- Status can be: todo, in progress, or done",
        "- If status is not specified, use 'todo' as default",
        
        "Be helpful and guide users if they need more information.",
    ],
    show_tool_calls=True,
    markdown=True
)

team_leader = Agent(
    name="Team Leader",
    team=[clickup_agent, github_agent],
    model=OpenAIChat(model="gpt-4o-mini"),
    instructions=[
        "Manage both ClickUp and GitHub operations",
        "Always include sources for information",
        "Use tables to display data when appropriate",
    ],
    show_tool_calls=True,
    markdown=True,
)

team_leader.print_response(
    "Create 2 issues in https://github.com/tapankumarpatro/AgentLab.git repository, take issue title and body from AgentLab space from clickup",
    markdown=True
)




















# ┏━ Response (299.3s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                                                                                                                                                                     ┃
# ┃ Running:                                                                                                                                                                                                                                                            ┃
# ┃                                                                                                                                                                                                                                                                     ┃
# ┃  • transfer_task_to_clickup_agent(task_description=Retrieve issue titles and bodies from the AgentLab space for creating GitHub issues., expected_output=A list of at least two issue titles and their corresponding bodies from the AgentLab space.,               ┃
# ┃    additional_information=...)                                                                                                                                                                                                                                      ┃
# ┃  • transfer_task_to_github_agent(task_description=List the repositories to confirm the existence of AgentLab repository., expected_output=A confirmation of the existence of the AgentLab repository or its details., additional_information=Check if the AgentLab  ┃
# ┃    repository exists to prepare for issue creation.)                                                                                                                                                                                                                ┃
# ┃                                                                                                                                                                                                                                                                     ┃
# ┃ Running:                                                                                                                                                                                                                                                            ┃
# ┃                                                                                                                                                                                                                                                                     ┃
# ┃  • transfer_task_to_github_agent(task_description=..., expected_output=..., additional_information=Ensure the issue is created in the tapankumarpatro/AgentLab repository.)                                                                                         ┃
# ┃  • transfer_task_to_github_agent(task_description=..., expected_output=..., additional_information=Ensure the issue is created in the tapankumarpatro/AgentLab repository.)                                                                                         ┃
# ┃                                                                                                                                                                                                                                                                     ┃
# ┃ Two issues have been successfully created in the tapankumarpatro/AgentLab repository using the titles and bodies retrieved from the AgentLab space in ClickUp. You can view the issues using the following links:                                                   ┃
# ┃                                                                                                                                                                                                                                                                     ┃
# ┃  1 Issue Title: Use Browser Use tool to automate blog creation                                                                                                                                                                                                      ┃
# ┃     • Body: Explore the capabilities of the Browser Use tool to automate the process of creating blogs. Identify key features and any limitations while ensuring the workflow is streamlined. Document the steps taken and any improvements suggested for the       ┃
# ┃       blogging tool integration.                                                                                                                                                                                                                                    ┃
# ┃     • View Issue                                                                                                                                                                                                                                                    ┃
# ┃  2 Issue Title: Create ClickUp tool in Phidata Agent                                                                                                                                                                                                                ┃
# ┃     • Body: Develop a ClickUp tool within the Phidata Agent to enhance task automation and workflow management. Focus on the integration of ClickUp functionalities into Phidata Agent, and ensure that all features operate smoothly. Provide a detailed report of ┃
# ┃       the integration process, including any challenges faced and resolved.                                                                                                                                                                                         ┃
# ┃     • View Issue                                                                                                                                                                                                                                                    ┃
# ┃                      