import asyncio
from crawl4ai import *

# async def main():
#     async with AsyncWebCrawler() as crawler:
#         result = await crawler.arun(
#             url="https://www.tide.co",
#         )
#         print(result.markdown)


async def link_analysis():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.adobe.com/",
        )
        print(f"Found {len(result.links['internal'])} internal links")
        print(f"Found {len(result.links['external'])} external links")

        for link in result.links['internal']:
            print(f"Href: {link['href']}\nText: {link['text']}\n")  

        for link in result.links['external']:
            print(f"Href: {link['href']}\nText: {link['text']}\n")                



if __name__ == "__main__":
    # asyncio.run(main())
    asyncio.run(link_analysis())