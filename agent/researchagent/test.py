import asyncio

from .graph import research_graph


async def main():

    result = await research_graph.ainvoke(
        {
            "user_id": 1,
            "topic": "Model Context Protocol"
        }
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())