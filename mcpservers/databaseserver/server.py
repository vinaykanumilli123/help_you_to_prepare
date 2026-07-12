"""
Database MCP Server

Exposes database operations for the Study Assistant.
"""

import uvicorn
from mcp.server.fastmcp import FastMCP

# User Tools
from mcpservers.databaseserver.tools.user_tools import (
    save_user,
    get_user,
)

# Topic Tools
from mcpservers.databaseserver.tools.topic_tools import (
    create_topic,
    get_user_topics,
)

# Research Tools
from mcpservers.databaseserver.tools.researchtools import (
    save_research_source,
)

# Notes Tools
from mcpservers.databaseserver.tools.notetools import (
    save_notes,get_notes
)

# Quiz Tools
from mcpservers.databaseserver.tools.quizz_tools import (
    save_quiz,get_quiz,
    save_attempt,
)

# Progress Tools
from mcpservers.databaseserver.tools.progresstools import (
    load_progress,
)


# -------------------------------------------------
# MCP Server
# -------------------------------------------------

mcp = FastMCP("database-server")


# -------------------------------------------------
# Register Tools
# -------------------------------------------------

mcp.tool()(save_user)
mcp.tool()(get_user)

mcp.tool()(create_topic)
mcp.tool()(get_user_topics)

mcp.tool()(save_research_source)

mcp.tool()(save_notes)

mcp.tool()(get_notes)
mcp.tool()(save_quiz)
mcp.tool()(get_quiz)
mcp.tool()(save_attempt)

mcp.tool()(load_progress)


# -------------------------------------------------
# HTTP App
# -------------------------------------------------

app = mcp.streamable_http_app()


# -------------------------------------------------
# Run
# -------------------------------------------------

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8003,
    )