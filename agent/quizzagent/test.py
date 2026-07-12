import asyncio

from .graph import quizz_graph


async def main():

    result = await quizz_graph.ainvoke(
        {
            "user_id": 1,
            "topic_id": 4
        }
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())