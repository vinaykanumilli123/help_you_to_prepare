import os
import uvicorn
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

from mcpservers.storageserver.tools.markdown import save_markdown, markdown_to_pdf
from mcpservers.storageserver.tools.archieve import zip_files


load_dotenv()

mcp = FastMCP("storage-server")


mcp.tool()(save_markdown)
mcp.tool()(markdown_to_pdf)
mcp.tool()(zip_files)


app = mcp.streamable_http_app()


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001
    )