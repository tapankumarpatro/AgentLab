from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.website import WebsiteTools
from phi.model.ollama import Ollama
from phi.tools.searxng import Searxng
import asyncio
from crawl4ai import *
import json
import re

ollama_qwen_model = "qwen2.5:latest"
local_model = Ollama(id=ollama_qwen_model)
choosen_model = local_model


searxng = Searxng(host="http://192.168.1.40:8080", engines=['google'], fixed_max_results=5)

web_agent = Agent(
    name="Website Finder",
    role="Find the official website for the given company",
    model=choosen_model,
    tools=[searxng, DuckDuckGo()],
    instructions=[
        f"Find the official website for asked company",
        "Use DuckDuckGo to search for the company website if you don't find it in the duckduckgo search using searxng engines and find the result",
        "Return only the website URL, nothing else"
    ],
    # show_tool_calls=True,
    markdown=True,
)

company_name = "iNeuorn.ai"

response = web_agent.run("Find the official website for {}".format(company_name))

official_website = response.content.strip()

print(f"Official website: {official_website}")


async def link_analysis():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=official_website,
        )
        # print(f"Found {len(result.links['internal'])} internal links")
        # print(f"Found {len(result.links['external'])} external links")

        social_media = {
            'official_website': official_website,
            'twitter': None,
            'instagram': None,
            'facebook': None,
            'youtube': None
        }
        
        for link in result.links['external']:
            href = link['href'].lower()
            if 'twitter.com' in href:
                match = re.search(r'(https?://(?:www\.)?twitter\.com/\w+)', href)
                if match:
                    social_media['twitter'] = match.group(1)
            elif 'instagram.com' in href:
                match = re.search(r'(https?://(?:www\.)?instagram\.com/\w+)', href)
                if match:
                    social_media['instagram'] = match.group(1)
            elif 'facebook.com' in href:
                match = re.search(r'(https?://(?:www\.)?facebook\.com/\w+)', href)
                if match:
                    social_media['facebook'] = match.group(1)
            elif 'youtube.com' in href:
                match = re.search(r'(https?://(?:www\.)?youtube\.com/(@?\w+))', href)
                if match:
                    social_media['youtube'] = match.group(1)
        
        final_json = json.dumps(social_media, indent=2)
        print(final_json)

if __name__ == "__main__":
    asyncio.run(link_analysis())
