import asyncio

from .graph import evaluation_graph


async def main():

    result = await evaluation_graph.ainvoke(
        {
            "user_id": 1,
            "quiz_id": 1,
            "answers": [
                "failed",
                "wrong",
                "C",
                "connections",
                "One-to-one",
                "To enable access to external systems",
                "Custom API connection complexity",
                "Claude Desktop",
                "Strict security controls",
                "Enabled dynamic connection with external tools",
            ]
        }
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())