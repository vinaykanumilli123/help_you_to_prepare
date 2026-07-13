from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
import json
import os
STORAGE_URL = os.getenv("STORAGE_SERVER_URL")
class StorageClient:

    async def save_markdown(self, content: str, filename: str):

        async with streamable_http_client(
           STORAGE_URL
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                result = await session.call_tool(
                    "save_markdown",
                    {
                        "content": content,
                        "filename": filename,
                    },
                )

        print(result.content[0].text)

        data = json.loads(result.content[0].text)

        return data["file"]

        

    async def markdown_to_pdf(self, md_url: str):

        async with streamable_http_client(
            STORAGE_URL
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                result = await session.call_tool(
                    "markdown_to_pdf",
                    {
                        "md_url": md_url,
                    },
                )

        print(result.content[0].text)

        data = json.loads(result.content[0].text)

        return data["pdf"]