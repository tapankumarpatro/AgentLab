from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.website import WebsiteTools
from phi.model.ollama import Ollama
from phi.tools.searxng import Searxng
import asyncio
from crawl4ai import AsyncWebCrawler
import json
import re
import pandas as pd
import time

# Initialize the model
ollama_qwen_model = "qwen2.5:latest"
local_model = Ollama(id=ollama_qwen_model)

# Initialize search tools
searxng = Searxng(host="http://192.168.1.40:8080", engines=['google'], fixed_max_results=5)

# Create the web agent
web_agent = Agent(
    name="Website Finder",
    role="Find the official website for the given company",
    model=local_model,
    tools=[searxng, DuckDuckGo()],
    instructions=[
        "Find the official website for asked company",
        "Use DuckDuckGo to search for the company website if you don't find it in the searxng search",
        "Return only the website URL, nothing else"
    ],
    markdown=True,
)

url_finder_agent = Agent(
    name="URL Finder",
    role="Find the required url for the given company",
    model=local_model,
    tools=[searxng, DuckDuckGo()],
    instructions=[
        "Find the required url for asked company",
        "Use DuckDuckGo to search for the company website if you don't find it in the searxng search",
        "Return only the URL, nothing else"
    ],
    markdown=True,
)

async def get_social_media_links(company_name):
    try:
        # Find official website
        response = web_agent.run(f"Find the official website for {company_name}")
        official_website = response.content.strip()
        
        social_media = {
            'company_name': company_name,
            'company_url': official_website,
            'twitter': None,
            'instagram': None,
            'facebook': None,
            'youtube': None
        }
        
        # Analyze links from the website
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=official_website)
            
            for link in result.links['external']:
                href = link['href'].lower()
                for social in ['twitter', 'instagram', 'facebook', 'youtube']:
                    if f'{social}.com' in href:
                        match = re.search(rf'(https?://(?:www\.)?{social}\.com/\w+)', href)
                        if match:
                            social_media[social] = match.group(1)
            
            for social in ['twitter', 'instagram', 'facebook', 'youtube']:
                if not social_media[social]:
                    response = url_finder_agent.run(f"Find the {social} url  for {company_name}")
                    social_media[social] = response.content.strip()
        
        return social_media
    except Exception as e:
        print(f"Error processing {company_name}: {str(e)}")
        return {
            'company_name': company_name,
            'company_url': None,
            'twitter': None,
            'instagram': None,
            'facebook': None,
            'youtube': None
        }

async def process_companies(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Create a list to store results
    results = []
    
    # Process each company
    for index, row in df.iterrows():
        company_name = row['company_name']
        print(f"Processing {company_name} ({index + 1}/{len(df)})")
        
        # Get social media links
        result = await get_social_media_links(company_name)
        results.append(result)
        
        # Add a small delay to avoid overwhelming the servers
        time.sleep(1)
        
        # Save intermediate results
        pd.DataFrame(results).to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")

if __name__ == "__main__":
    input_file = "companies.csv"  # Your input CSV file
    output_file = "companies_with_social_media.csv"  # Your output CSV file
    
    # Run the async process
    asyncio.run(process_companies(input_file, output_file))