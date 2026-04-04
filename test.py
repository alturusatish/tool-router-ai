import asyncio

from tool_router_ai.registry import ToolRegistry
from tool_router_ai.router import ToolRouter
from tool_router_ai.embedder import Embedder
from tool_router_ai.models import Tool
from tool_router_ai.feedback_store import FeedbackStore
from openai import OpenAI

client = OpenAI()

def extract_params(query, tool):

     
    prompt = f"""
Extract parameters for the tool.

Tool name: {tool.name}

Tool schema: {tool.input_schema}

User query: {query}

Return JSON only.
"""

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    import json

    try:
        return json.loads(res.choices[0].message.content)
    except:
        return {}

def weather(city):
    return f"Weather for {city}"


def stocks(symbol):
    return f"Stock price for {symbol}"


async def main():

    query = "what is the weather in San Francisco?"

    registry = ToolRegistry()
    feedback = FeedbackStore()

    registry.register(
        Tool(
            name="weather",
            description="Get weather for any city",
            input_schema={"city": "string"},
            func=weather
        )
    )

    registry.register(
        Tool(
            name="stocks",
            description="Get stock market price",
            input_schema={"symbol": "string"},
            func=stocks
        )
    )

    embedder = Embedder()

    router = ToolRouter(registry, embedder)

    await router.build_index()

    tools = await router.route(
        "What is weather in San Francisco?"
    )

    tool = tools[0]

    params = extract_params(query, tool)

    try:

        result = tool.func(**params)

        print("Tool:", tool.name)
        print("Params:", params)
        print("Result:", result)

        feedback.record_success(tool.name)

    except Exception as e:

        print("Error:", e)

        feedback.record_failure(tool.name)


asyncio.run(main())