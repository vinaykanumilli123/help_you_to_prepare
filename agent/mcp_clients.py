from langchain_mcp_adapters.client import MultiServerMCPClient
import os
research_url = os.getenv("research_server_url")
research_client = MultiServerMCPClient(
    {
        "research": {
            "transport": "streamable_http",
            "url": research_url,
        }
    }
)

