from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from browser_use import Agent
import asyncio
import os
from dotenv import load_dotenv, find_dotenv
_=load_dotenv(find_dotenv())

log_type = os.getenv('BROWSER_USE_LOGGING_LEVEL', 'info').lower()

# # os.env set to openai api key
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

async def main():
    agent = Agent(
        task="Go to url r/LocalLLaMA subreddit and search for browser use in the search bar and click on the first post and find the funniest comment",
        llm=ChatOpenAI(model="gpt-4o-mini", openai_api_key=os.getenv("OPENAI_API_KEY")),
    )

    # agent = Agent(
    #     task="Go to Google, search for 'Titans: Learning to Memorize at Test Time', open the first link, click on View PDF butoon and save the pdf.",
    #     llm=ChatOllama(
    #         model="qwen2.5:14b-instruct-q5_K_S", # qwen2.5:14b-instruct-q5_K_S qwen2.5:32b-instruct-q4_K_M
    #         num_ctx=32000,
    #     )
    # )
    result = await agent.run()
    print(result)

asyncio.run(main())


# pip install browser-use==0.1.22

# import os

# Optional: Disable telemetry
# os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Optional: Set the OLLAMA host to a remote server
# os.environ["OLLAMA_HOST"] = "http://x.x.x.x:11434"

# import asyncio
# from browser_use import Agent
# from langchain_ollama import ChatOllama


# async def run_search() -> str:
#     agent = Agent(
#         task="Search for a 'browser use' post on the r/LocalLLaMA subreddit and open it.",
#         llm=ChatOllama(
#             model="qwen2.5:14b-instruct-q5_K_S", # qwen2.5:14b-instruct-q5_K_S qwen2.5:32b-instruct-q4_K_M
#             num_ctx=32000,
#         ),
#     )

#     result = await agent.run()
#     return result


# async def main():
#     result = await run_search()
#     print("\n\n", result)


# if __name__ == "__main__":
#     asyncio.run(main())