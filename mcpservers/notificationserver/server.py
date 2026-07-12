import uvicorn

from mcp.server.fastmcp import FastMCP

from tools.email_tools import (
    send_email,
    send_zip
)


mcp = FastMCP("notification-server")


mcp.tool()(send_email)
mcp.tool()(send_zip)


app = mcp.streamable_http_app()


if __name__ == "__main__":

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8002
    )