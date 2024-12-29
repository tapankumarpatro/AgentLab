from phi.tools.searxng import Searxng
import httpx
import json
import urllib.parse
from typing import Any, Dict, List, Optional
import os
from datetime import datetime, timedelta

def searxng_client():
    searxng = Searxng(
        host="http://localhost:8080",
        engines=[],
        fixed_max_results=3,
        news=True,
        science=True,
    )   
    return searxng

def query_political_news(query_str: str) -> str:
    """Get political news related to a company or industry.

    Args:
        query_str (str): Company or industry related query
    Returns:
        str: JSON string of relevant news articles
    """
    client = searxng_client()
    return client.news_search(
        query=f"{query_str} political news",
        max_results=3
    )

def query_business_news(query_str: str) -> str:
    """Get business news related to a company.

    Args:
        query_str (str): Company name or related business query
    Returns:
        str: JSON string of relevant news articles
    """
    client = searxng_client()
    return client.news_search(
        query=f"{query_str} business news financial results",
        max_results=3
    )

def query_crime_news(query_str: str) -> str:
    """Get news about legal issues, fraud, or controversies related to a company.

    Args:
        query_str (str): Company name or related query
    Returns:
        str: JSON string of relevant news articles
    """
    client = searxng_client()
    return client.news_search(
        query=f"{query_str} legal issues fraud controversy",
        max_results=3
    )

def query_company_info(company_name: str) -> str:
    """Get general information about company description, mission, and core products.

    Args:
        company_name (str): Name of the company
    Returns:
        str: JSON string of relevant search results
    """
    client = searxng_client()
    return client.search(
        query=f"{company_name} company overview description mission products services",
        max_results=3
    )

def query_financial_data(company_name: str) -> str:
    """Get financial information about a company including revenue, market cap, and investments.

    Args:
        company_name (str): Name of the company
    Returns:
        str: JSON string of relevant search results
    """
    client = searxng_client()
    return client.news_search(
        query=f"{company_name} financial results revenue market capitalization funding investments",
        max_results=3
    )

def query_market_data(company_name: str) -> str:
    """Get information about company's market position, strategy, and competitors.

    Args:
        company_name (str): Name of the company
    Returns:
        str: JSON string of relevant search results
    """
    client = searxng_client()
    return client.search(
        query=f"{company_name} market share competitors strategy growth partnerships",
        max_results=3
    )

def query_operations_data(company_name: str) -> str:
    """Get information about company's operations, infrastructure, and facilities.

    Args:
        company_name (str): Name of the company
    Returns:
        str: JSON string of relevant search results
    """
    client = searxng_client()
    return client.search(
        query=f"{company_name} operations facilities manufacturing supply chain infrastructure",
        max_results=3
    )

def query_reputation_data(company_name: str) -> str:
    """Get information about company's social presence, reviews, and reputation.

    Args:
        company_name (str): Name of the company
    Returns:
        str: JSON string of relevant search results
    """
    client = searxng_client()
    return client.search(
        query=f"{company_name} reviews reputation CSR employee satisfaction awards",
        max_results=3
    )

def query_legal_data(company_name: str) -> str:
    """Get information about company's legal issues and compliance.

    Args:
        company_name (str): Name of the company
    Returns:
        str: JSON string of relevant search results
    """
    client = searxng_client()
    return client.news_search(
        query=f"{company_name} legal compliance regulations governance privacy",
        max_results=3
    )

def query_innovation_data(company_name: str) -> str:
    """Get information about company's technology stack and innovation initiatives.

    Args:
        company_name (str): Name of the company
    Returns:
        str: JSON string of relevant search results
    """
    client = searxng_client()
    return client.search(
        query=f"{company_name} technology innovation digital transformation patents R&D",
        max_results=3
    )

def query_risk_data(company_name: str) -> str:
    """Get information about various risks associated with the company.

    Args:
        company_name (str): Name of the company
    Returns:
        str: JSON string of relevant search results
    """
    client = searxng_client()
    return client.news_search(
        query=f"{company_name} risks threats challenges market competition regulatory",
        max_results=3
    )

def query_social_media(company_name: str) -> str:
    """Get all social media URLs for a company.

    Args:
        company_name (str): Name of the company
    Returns:
        str: JSON string of relevant search results
    """
    client = searxng_client()
    return client.search(
        query=f"{company_name} site:twitter.com OR site:facebook.com OR site:linkedin.com OR site:instagram.com OR site:youtube.com",
        max_results=3
    )

def query_public_sentiment(company_name: str) -> str:
    """Get public sentiment about a company.

    Args:
        company_name (str): Name of the company
    Returns:
        str: JSON string of relevant search results
    """
    client = searxng_client()
    return client.search(
        query=f"{company_name} public sentiment opinion analysis",
        max_results=3
    )