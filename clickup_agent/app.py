import streamlit as st
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from clickup_tool import ClickUpTools
import os
from dotenv import load_dotenv, find_dotenv
from phi.agent import Agent, AgentMemory
from phi.memory.db.sqlite import SqliteMemoryDb
from phi.storage.agent.sqlite import SqlAgentStorage
_=load_dotenv(find_dotenv())

def init_session_state():
    """Initialize session state variables"""
    if 'clickup_agent' not in st.session_state:
        st.session_state.clickup_agent = None
    if 'messages' not in st.session_state:
        st.session_state.messages = []

def create_clickup_agent():
    """Initialize ClickUp agent with OpenAI model"""
    openai_model = OpenAIChat(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    return Agent(
        name="ClickUp Assistant",
        role="Help users interact with ClickUp",
        tools=[ClickUpTools()],
        model=openai_model,
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
        memory=AgentMemory(
        db=SqliteMemoryDb(
            table_name="agent_memory",
            db_file="tmp/agent_memory.db",
        ),
        # Create and store session summaries
        create_session_summary=True,
        
    ),
    # Store agent sessions in a database, that persists between runs
    storage=SqlAgentStorage(table_name="agent_sessions", db_file="tmp/agent_storage.db"),
    )

def main():
    st.set_page_config(page_title="ClickUp Agent Assistant", layout="wide")
    init_session_state()
    
    st.title("ClickUp Agent Assistant ")
    
    # Initialize ClickUp agent if not already initialized
    try:
        if not st.session_state.clickup_agent:
            st.session_state.clickup_agent = create_clickup_agent()
    except Exception as e:
        st.error(f"Failed to initialize ClickUp Agent: {str(e)}")
        return

    # Chat interface
    st.markdown("###  Chat with your ClickUp Assistant")
    st.markdown("""Ask me anything about your ClickUp workspace! For example:
    - Show me all available spaces
    - List tasks from [space name]
    - Show me all lists in [space name]
    - Create a task in [space name] with title [task name] and description [description]""")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What would you like to know about your ClickUp workspace?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get agent response
        with st.chat_message("assistant"):
            with st.spinner("Processing your request..."):
                try:
                    response = st.session_state.clickup_agent.run(prompt)
                    response_content = response.content if response.content else next(
                        (msg.content for msg in response.messages if msg.role == 'assistant' and msg.content),
                        "I couldn't process that request. Could you try rephrasing it?"
                    )
                    st.markdown(response_content)
                    
                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": response_content})
                    
                except Exception as e:
                    error_message = f"I encountered an error: {str(e)}. Could you try again?"
                    st.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})

if __name__ == "__main__":
    main()