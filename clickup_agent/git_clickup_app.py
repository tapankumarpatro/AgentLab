import streamlit as st
import os
from phi.agent import Agent, AgentMemory
from phi.model.openai import OpenAIChat
from clickup_tool import ClickUpTools
from phi.tools.github import GithubTools
from dotenv import load_dotenv, find_dotenv
from phi.memory.db.sqlite import SqliteMemoryDb
from phi.storage.agent.sqlite import SqlAgentStorage

_ = load_dotenv(find_dotenv())

def init_session_state():
    """Initialize session state variables"""
    if 'team_leader' not in st.session_state:
        st.session_state.team_leader = None
    if 'messages' not in st.session_state:
        st.session_state.messages = []

def create_github_agent():
    """Initialize GitHub agent with OpenAI model"""
    return Agent(
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
        markdown=True,
        memory=AgentMemory(
            db=SqliteMemoryDb(
                table_name="github_agent_memory",
                db_file="tmp/agent_memory.db",
            ),
            create_session_summary=True,
        ),
        storage=SqlAgentStorage(table_name="github_agent_sessions", db_file="tmp/agent_storage.db"),
    )

def create_clickup_agent():
    """Initialize ClickUp agent with OpenAI model"""
    return Agent(
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
        markdown=True,
        memory=AgentMemory(
            db=SqliteMemoryDb(
                table_name="clickup_agent_memory",
                db_file="tmp/agent_memory.db",
            ),
            create_session_summary=True,
        ),
        storage=SqlAgentStorage(table_name="clickup_agent_sessions", db_file="tmp/agent_storage.db"),
    )

def create_team_leader():
    """Initialize Team Leader agent that manages both GitHub and ClickUp agents"""
    github_agent = create_github_agent()
    clickup_agent = create_clickup_agent()
    
    return Agent(
        name="Team Leader",
        team=[clickup_agent, github_agent],
        model=OpenAIChat(model="gpt-4o-mini"),
        instructions=[
            "Manage both ClickUp and GitHub operations",
            "Always include sources for information",
            "Use tables to display data when appropriate",
            "You can:",
            "1. Sync tasks between ClickUp and GitHub",
            "2. Create GitHub issues from ClickUp tasks",
            "3. List and manage both ClickUp tasks and GitHub issues",
        ],
        show_tool_calls=True,
        markdown=True,
        memory=AgentMemory(
            db=SqliteMemoryDb(
                table_name="team_leader_memory",
                db_file="tmp/agent_memory.db",
            ),
            create_session_summary=True,
        ),
        storage=SqlAgentStorage(table_name="team_leader_sessions", db_file="tmp/agent_storage.db"),
    )


# Create 2 issues in https://github.com/tapankumarpatro/AgentLab.git repository, take issue title and body from AgentLab space from clickup

def main():
    st.set_page_config(page_title="📒 ClickUp-GitHub Integration Assistant", layout="wide")
    init_session_state()
    
    st.title("📒 ClickUp-GitHub Integration Assistant")
    
    # Initialize Team Leader agent if not already initialized
    try:
        if not st.session_state.team_leader:
            st.session_state.team_leader = create_team_leader()
    except Exception as e:
        st.error(f"Failed to initialize Team Leader Agent: {str(e)}")
        return

    # Chat interface
    st.markdown("### Chat with your Integration Assistant")
    st.markdown("""Ask me anything about your ClickUp workspace and GitHub repositories! For example:
    - Show me all available ClickUp spaces
    - List me my GitHub repositories
    - Create 2 issues in https://github.com/tapankumarpatro/AgentLab.git repository, take issue title and body from AgentLab space from clickup
    - List all tasks from AgentLab space
    - Show me all issues in [repository name]""")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What would you like to do with ClickUp and GitHub?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get agent response
        with st.chat_message("assistant"):
            with st.spinner("Processing your request..."):
                try:
                    response = st.session_state.team_leader.run(prompt)
                    response_content = response.content if response.content else next(
                        (msg.content for msg in response.messages if msg.role == 'assistant' and msg.content),
                        "I couldn't process your request. Please try again."
                    )
                    st.markdown(response_content)
                    st.session_state.messages.append({"role": "assistant", "content": response_content})
                except Exception as e:
                    error_message = f"Error processing your request: {str(e)}"
                    st.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})

if __name__ == "__main__":
    main()
