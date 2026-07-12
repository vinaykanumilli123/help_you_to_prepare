from langchain_mcp_adapters.client import MultiServerMCPClient

research_client = MultiServerMCPClient(
    {
        "research": {
            "transport": "streamable_http",
            "url": "http://127.0.0.1:8000/mcp",
        }
    }
)

storage_client = MultiServerMCPClient(
    {
        "storage": {
            "transport": "streamable_http",
            "url": "http://127.0.0.1:8001/mcp",
        }
    }
)

from langchain_mcp_adapters.client import MultiServerMCPClient

database_client = MultiServerMCPClient(
    {
        "database": {
            "transport": "streamable_http",
            "url": "http://127.0.0.1:8003/mcp",
        }
    }
)