from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
import json
import os
DATABASE_SERVER_URL = os.getenv(
    "DATABASE_SERVER_URL"
)

class DatabaseClient:

    async def create_topic(
        self,
        user_id: int,
        topic_name: str,
    ):

        async with streamable_http_client(
            DATABASE_SERVER_URL
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                result = await session.call_tool(
                    "create_topic",
                    {
                        "user_id": user_id,
                        "topic_name": topic_name,
                    },
                )

        # print(result)
        # print(result.content)
        # print(result.content[0])
        # print(result.content[0].text)
        data = json.loads(result.content[0].text)
        return data["topic_id"]

    async def save_note(
        self,
        topic_id: int,
        markdown_path: str,
        pdf_path: str,
    ):

        async with streamable_http_client(
           DATABASE_SERVER_URL
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                result = await session.call_tool(
                    "save_notes",
                    {
                        "topic_id": topic_id,
                        "markdown_path": markdown_path,
                        "pdf_path": pdf_path,
                    },
                )

        data = json.loads(result.content[0].text)
        return data["note_id"]

    async def save_research_source(
        self,
        topic_id: int,
        title: str,
        url: str,
        content: str,
    ):

        async with streamable_http_client(
            DATABASE_SERVER_URL
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                result = await session.call_tool(
                    "save_research_source",
                    {
                        "topic_id": topic_id,
                        "title": title,
                        "url": url,
                        "content": content,
                    },
                )

        data = json.loads(result.content[0].text)
        return data["source_id"]

    async def get_user_topics(self, user_id: int):

        async with streamable_http_client(
            DATABASE_SERVER_URL
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                result = await session.call_tool(
                    "get_user_topics",
                    {
                        "user_id": user_id,
                    },
                )

        return json.loads(result.content[0].text)

    async def save_user(
        self,
        name: str,
        email: str,
        google_id: str | None = None,
    ):

        async with streamable_http_client(
            DATABASE_SERVER_URL
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                result = await session.call_tool(
                    "save_user",
                    {
                        "name": name,
                        "email": email,
                        "google_id": google_id,
                    },
                )

        return json.loads(result.content[0].text)

    async def get_user(self, email: str):

        async with streamable_http_client(
            DATABASE_SERVER_URL
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                result = await session.call_tool(
                    "get_user",
                    {
                        "email": email,
                    },
                )

        return json.loads(result.content[0].text)

    async def save_research_source(
        self,
        topic_id: int,
        title: str,
        url: str,
        content: str,
    ):

        async with streamable_http_client(
            DATABASE_SERVER_URL
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                result = await session.call_tool(
                    "save_research_source",
                    {
                        "topic_id": topic_id,
                        "title": title,
                        "url": url,
                        "content": content,
                    },
                )

        return json.loads(result.content[0].text)


    async def get_notes(
        self,
        user_id: int,
        topic_id: int,
    ):

        async with streamable_http_client(
            DATABASE_SERVER_URL
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                result = await session.call_tool(
                    "get_notes",
                    {
                        "user_id": user_id,
                        "topic_id": topic_id,
                    },
                )

        print("========== MCP RESULT ==========")
        print(result)
        print("========== CONTENT ==========")
        print(result.content)
        print("========== TEXT ==========")
        print(result.content[0].text)

        return json.loads(result.content[0].text)



    async def save_quiz(
    self,
    topic_id: int,
    questions: list,
    ):

        async with streamable_http_client(
            DATABASE_SERVER_URL
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                result = await session.call_tool(
                    "save_quiz",
                    {
                        "topic_id": topic_id,
                        "questions": questions,
                    },
                )

        return json.loads(result.content[0].text)


    async def save_attempt(
    self,
    user_id: int,
    quiz_id: int,
    score: int,
    passed: bool,
    weak_concepts: list,
    ):

        async with streamable_http_client(
            DATABASE_SERVER_URL
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                result = await session.call_tool(
                    "save_attempt",
                    {
                        "user_id": user_id,
                        "quiz_id": quiz_id,
                        "score": score,
                        "passed": passed,
                        "weak_concepts": weak_concepts,
                    },
                )

        return json.loads(result.content[0].text)

    async def get_quiz(
    self,
    quiz_id: int
    ):

        async with streamable_http_client(
            DATABASE_SERVER_URL
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                result = await session.call_tool(
                    "get_quiz",
                    {
                        "quiz_id": quiz_id,
                    },
                )

        return json.loads(result.content[0].text)