from langgraph.prebuilt import create_react_agent

from agent.llm import llm
from agent.mcp_clients import (
    research_client
)
import asyncio


async def get_research_agent():

    # tools = await research_client.get_tools()
    tools = await research_client.get_tools()
    print("Research Tools:")
    for t in tools:
        print(t.name)

    return create_react_agent(
        model=llm,
        tools=tools,
    )


# async def get_storage_agent():

#     tools = await storage_client.get_tools()

#     return create_react_agent(
#         model=llm,
#         tools=tools,
#     )

async def main():
    agent = await get_research_agent()

    result = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Model Context Protocol",
                }
            ]
        }
    )

    print(result)

if __name__ == "__main__":
    asyncio.run(main())

