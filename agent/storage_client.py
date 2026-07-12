from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
import json

class StorageClient:

    async def save_markdown(self, content: str, filename: str):

        async with streamable_http_client(
            "http://127.0.0.1:8001/mcp"
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

        data = json.loads(result.content[0].text)
        return data["file"]

    async def markdown_to_pdf(self, md_file: str):

        async with streamable_http_client(
            "http://127.0.0.1:8001/mcp"
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                result = await session.call_tool(
                    "markdown_to_pdf",
                    {
                        "md_file": md_file,
                    },
                )

        data = json.loads(result.content[0].text)
        return data["pdf"]