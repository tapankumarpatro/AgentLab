from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.website import WebsiteTools
from phi.model.ollama import Ollama
from phi.tools.searxng import Searxng
from crawl4ai import AsyncWebCrawler
import asyncio
import json
import re
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Model configuration
ollama_qwen_model = "qwen2.5:latest"
local_model = Ollama(id=ollama_qwen_model)
choosen_model = local_model

# Initialize Searxng
searxng = Searxng(host="http://192.168.1.40:8080", engines=['google'], fixed_max_results=5)

# Initialize Web Agent
web_agent = Agent(
    name="Website Finder",
    role="Find the official website for the given company",
    model=choosen_model,
    tools=[searxng, DuckDuckGo()],
    instructions=[
        "Find the official website for asked company",
        "Use DuckDuckGo to search for the company website if you don't find it in the duckduckgo search using searxng engines and find the result",
        "Return only the website URL, nothing else"
    ],
    markdown=True,
)

class CompanyRequest(BaseModel):
    company_name: str

async def get_social_media_links(official_website: str):
    try:
        async with AsyncWebCrawler() as crawler:
            try:
                result = await crawler.arun(url=official_website)
            except NotImplementedError:
                # Fallback to simpler link extraction if Playwright fails
                result = await crawler.arun(url=official_website, use_playwright=False)
            
            social_media = {
                'official_website': official_website,
                'twitter': None,
                'instagram': None,
                'facebook': None,
                'youtube': None
            }
            
            if not result or not result.links:
                return social_media
                
            for link in result.links.get('external', []):
                href = link.get('href', '').lower()
                if not href:
                    continue
                    
                if 'twitter.com' in href:
                    match = re.search(r'(https?://(?:www\.)?twitter\.com/\w+)', href)
                    if match and not social_media['twitter']:
                        social_media['twitter'] = match.group(1)
                elif 'instagram.com' in href:
                    match = re.search(r'(https?://(?:www\.)?instagram\.com/\w+)', href)
                    if match and not social_media['instagram']:
                        social_media['instagram'] = match.group(1)
                elif 'facebook.com' in href:
                    match = re.search(r'(https?://(?:www\.)?facebook\.com/\w+)', href)
                    if match and not social_media['facebook']:
                        social_media['facebook'] = match.group(1)
                elif 'youtube.com' in href:
                    match = re.search(r'(https?://(?:www\.)?youtube\.com/(@?\w+))', href)
                    if match and not social_media['youtube']:
                        social_media['youtube'] = match.group(1)
            
            return social_media
    except Exception as e:
        print(f"Error in get_social_media_links: {str(e)}")
        return {
            'official_website': official_website,
            'twitter': None,
            'instagram': None,
            'facebook': None,
            'youtube': None,
            'error': str(e)
        }

@app.post("/find_social_media")
async def find_social_media(request: CompanyRequest):
    try:
        # Get official website
        response = web_agent.run(f"Find the official website for {request.company_name}")
        official_website = response.content.strip()
        
        if not official_website:
            raise HTTPException(status_code=404, detail="Could not find official website for the company")
        
        # Get social media links
        social_media_links = await get_social_media_links(official_website)
        return social_media_links
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="192.168.1.40", port=8001)
