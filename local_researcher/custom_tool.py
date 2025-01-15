from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.website import WebsiteTools
from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
# from phi.tools.yfinance import YFinanceTools
from phi.tools.crawl4ai_tools import Crawl4aiTools
from phi.tools.searxng import Searxng
from dotenv import load_dotenv
import os
from phi.model.openai import OpenAIChat
from phi.playground import Playground, serve_playground_app
from geometry_calculator import GeometryCalculator
from unit_converter import UnitConverter
load_dotenv()

ollama_qwen_model = "qwen2.5:latest"


local_model = Ollama(id=ollama_qwen_model)
# gemini_model = Gemini(model="gemini-2.0-flash-exp", api_key=os.getenv("GOOGLE_API_KEY"))
# openai_model = OpenAIChat(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

# choosen_model = openai_model
choosen_model = local_model

agent = Agent(
    model=choosen_model,
    # tools=[
    #     UnitConverter(),
    #     GeometryCalculator(),
    #     Calculator()
    # ],
    instructions=[
        "Use the calculator tool for basic math operations.",
        "Use the unit converter for converting between different units.",
        "Use the geometry calculator for geometry calculations."
    ],
    show_tool_calls=True,
    markdown=True,
)



print("\n=== Testing Agent ===")

agent.print_response("What is 5 + 5?")
agent.print_response("What is the perimeter of a triangle with sides 3, 4 and 5?")
agent.print_response("What is the area of a circle with radius 5?")
agent.print_response("What is the volume of a sphere with radius 4?")







# python .\custom_tool.py

# === Testing Converter Agent ===
# ▰▰▱▱▱▱▱ Thinking...INFO:httpx:HTTP Request: POST http://127.0.0.1:11434/api/chat "HTTP/1.1 200 OK"
# ▰▰▰▰▰▰▰ Thinking...INFO:httpx:HTTP Request: POST https://api.phidata.com/v1/telemetry/agent/run/create "HTTP/1.1 200 OK"
# ┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                                                                                                              ┃
# ┃ What is 5 + 5?                                                                                                                                                                                               ┃
# ┃                                                                                                                                                                                                              ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Response (136.2s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                                                                                                              ┃
# ┃                                                                                                                                                                                                              ┃
# ┃  The result of 5 + 5 is 10.                                                                                                                                                                                  ┃
# ┃                                                                                                                                                                                                              ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ You can use a calculator if you need to verify this!                                                                                                                                                         ┃
# ┃                                                                                                                                                                                                              ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ▰▰▰▰▰▰▱ Thinking...INFO:httpx:HTTP Request: POST http://127.0.0.1:11434/api/chat "HTTP/1.1 200 OK"
# ▰▰▰▰▰▱▱ Thinking...INFO:httpx:HTTP Request: POST https://api.phidata.com/v1/telemetry/agent/run/create "HTTP/1.1 200 OK"
# ┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                                                                                                              ┃
# ┃ What is the perimeter of a triangle with sides 3, 4 and 5?                                                                                                                                                   ┃
# ┃                                                                                                                                                                                                              ┃┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛┏━ Response (14.4s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓┃                                                                                                                                                                                                              ┃┃ To find the perimeter of a triangle with sides measuring 3, 4, and 5 units, you simply add up the lengths of all its sides.                                                                                  ┃┃                                                                                                                                                                                                              ┃┃ [ \text{Perimeter} = 3 + 4 + 5 = 12 \text{ units} ]                                                                                                                                                          ┃┃                                                                                                                                                                                                              ┃┃ Thus, the perimeter of the triangle is 12 units.                                                                                                                                                             ┃┃                                                                                                                                                                                                              ┃┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛▰▰▱▱▱▱▱ Thinking...INFO:httpx:HTTP Request: POST http://127.0.0.1:11434/api/chat "HTTP/1.1 200 OK"
# ▰▰▰▰▰▰▱ Thinking...INFO:httpx:HTTP Request: POST https://api.phidata.com/v1/telemetry/agent/run/create "HTTP/1.1 200 OK"
# ┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                                                                                                              ┃
# ┃ What is the area of a circle with radius 5?                                                                                                                                                                  ┃
# ┃                                                                                                                                                                                                              ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Response (15.3s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                                                                                                              ┃
# ┃ To find the area of a circle, we use the formula:                                                                                                                                                            ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ [ \text{Area} = \pi r^2 ]                                                                                                                                                                                    ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ where ( r ) is the radius of the circle.                                                                                                                                                                     ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ Given that the radius ( r = 5 ):                                                                                                                                                                             ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ [ \text{Area} = \pi (5)^2 = 25\pi ]                                                                                                                                                                          ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ Using (\pi \approx 3.14159):                                                                                                                                                                                 ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ [ \text{Area} \approx 25 \times 3.14159 = 78.53975 ]                                                                                                                                                         ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ So, the area of the circle is approximately:                                                                                                                                                                 ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ [ \boxed{78.54} ]                                                                                                                                                                                            ┃
# ┃                                                                                                                                                                                                              ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ▰▰▰▱▱▱▱ Thinking...INFO:httpx:HTTP Request: POST http://127.0.0.1:11434/api/chat "HTTP/1.1 200 OK"
# ▰▱▱▱▱▱▱ Thinking...INFO:httpx:HTTP Request: POST https://api.phidata.com/v1/telemetry/agent/run/create "HTTP/1.1 200 OK"
# ┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                                                                                                              ┃
# ┃ What is the volume of a sphere with radius 4?                                                                                                                                                                ┃
# ┃                                                                                                                                                                                                              ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Response (17.9s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                                                                                                              ┃
# ┃ To find the volume of a sphere, we use the formula:                                                                                                                                                          ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ [ V = \frac{4}{3} \pi r^3 ]                                                                                                                                                                                  ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ where ( r ) is the radius of the sphere.                                                                                                                                                                     ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ Given that the radius ( r = 4 ):                                                                                                                                                                             ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ [ V = \frac{4}{3} \pi (4)^3 ] [ V = \frac{4}{3} \pi (64) ] [ V = \frac{256}{3} \pi ]                                                                                                                         ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ Using (\pi \approx 3.14159):                                                                                                                                                                                 ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ [ V \approx \frac{256}{3} \times 3.14159 ] [ V \approx 85.3333 \times 3.14159 ] [ V \approx 268.0825731 ]                                                                                                    ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ So, the volume of the sphere is approximately:                                                                                                                                                               ┃
# ┃                                                                                                                                                                                                              ┃
# ┃ [ V \approx 268.08 \text{ cubic units} ]                                                                                                                                                                     ┃
# ┃                                           