import streamlit as st
from phi.agent import Agent
from phi.playground import Playground, serve_playground_app
from utils.model_config import ModelLoader, openai_config, gemini_config, ModelConfig
from news.business_news import business_news_agent
from news.financial_news import financial_news_agent
from news.market_strategy import market_strategy_agent
from news.reputation_social import reputation_social_agent
from news.legal_compliance import legal_compliance_agent

from phi.model.ollama import Ollama
from phi.model.google import Gemini
from phi.model.openai import OpenAIChat
import os


model_loader = ModelLoader(openai_config)


chief_research_agent = Agent(
    name="Chief Research Coordinator",
    model=model_loader.load_model(),
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
           - Key findings across all areas
           - Critical insights and recommendations
           - Overall company assessment
        
        2. Business Overview
           - Company description and mission
           - Core products/services
           - Market position
        
        3. Financial Analysis
           - Financial performance metrics
           - Market valuation
           - Investment analysis
        
        4. Market Strategy
           - Competitive position
           - Growth strategy
           - Innovation initiatives
        
        5. Reputation & Social Impact
           - Brand reputation
           - CSR activities
           - Stakeholder relationships
        
        6. Legal & Compliance
           - Regulatory compliance
           - Legal issues
           - Risk assessment
        
        7. Strategic Recommendations
           - Key opportunities
           - Risk mitigation strategies
           - Growth areas
        
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
    # reasoning=True,
    # show_full_reasoning=True,
    show_tool_calls=True,
    stream=True
)

def main():
    # Set page config
    st.set_page_config(
        page_title="Company Research Assistant",
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Sidebar for settings and history
    with st.sidebar:
        st.title("History")
        if 'search_history' not in st.session_state:
            st.session_state.search_history = []
        
        if st.session_state.search_history:
            for prev_company in st.session_state.search_history:
                if st.button(f"📋 {prev_company}"):
                    st.session_state.company_name = prev_company

    # Main content
    st.title("Company Research Assistant 🔍")
    st.markdown("Get comprehensive research about any company using our multi-agent research system")

    # Input section
    company_name = st.text_input(
        "Enter company name:",
        placeholder="e.g., Microsoft",
        value=st.session_state.get('company_name', ''),
        key="company_input"
    )
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        research_button = st.button("🔍 Research Company", type="primary", use_container_width=True)
    with col2:
        if 'research_response' in st.session_state:
            st.download_button(
                "📥 Download Report",
                st.session_state.research_response,
                file_name=f"{company_name}_research.md",
                mime="text/markdown",
                use_container_width=True
            )
    with col3:
        if 'research_response' in st.session_state:
            if st.button("🗑️ Clear Results", use_container_width=True):
                del st.session_state.research_response

    if research_button and company_name:
        if company_name not in st.session_state.search_history:
            st.session_state.search_history.append(company_name)
        st.session_state.company_name = company_name
        
        # Create a progress container
        progress_container = st.empty()
        with progress_container.container():
            st.markdown("### Research Progress")
            status_text = st.empty()
            
            # Initialize or reset the progress log
            if 'progress_log' not in st.session_state:
                st.session_state.progress_log = []
            else:
                st.session_state.progress_log = []
            
            # Get research from the chief research agent
            response = chief_research_agent.run(f"Research {company_name}")

            response_str = response.content
            
            sections = response_str.split('\n\n')
            st.session_state.sections = sections

            # Clear the progress container once complete
            progress_container.empty()

    # Display results in tabs if available
    if 'sections' in st.session_state:
        tabs = st.tabs([
            "Executive Summary",
            "Business Overview",
            "Financial Analysis",
            "Market Strategy",
            "Reputation & Social",
            "Legal & Compliance",
            "Recommendations"
        ])
        
        # Display each section in its respective tab
        for tab, section in zip(tabs, st.session_state.sections):
            with tab:
                st.markdown(section)
                
        # Add metrics or key findings in expandable sections
        with st.expander("🎯 Key Metrics"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Market Position", value="Coming soon")
            with col2:
                st.metric(label="Financial Health", value="Coming soon")
            with col3:
                st.metric(label="Risk Score", value="Coming soon")

    else:
        st.info("Enter a company name and click 'Research Company' to get started")

if __name__ == "__main__":
    main()
