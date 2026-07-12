"""
mcp_server/server.py
A real MCP server exposing tools the study agent calls.

Run standalone to sanity-check it starts:
    python mcp_server/server.py
(it will just sit there waiting for a client over stdio — Ctrl+C to stop)

The agent launches this as a subprocess automatically — see agent/mcp_client.py.
"""

import os
import requests
from bs4 import BeautifulSoup
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()
mcp = FastMCP("study-assistant-tools")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")  # free tier: https://tavily.com
from pydantic import BaseModel

class SearchResult(BaseModel):
    title: str
    url: str
    content: str


class SearchOutput(BaseModel):
    query: str
    results: list[SearchResult]


class FetchDocOutput(BaseModel):
    url: str
    content: str
    length: int

@mcp.tool()
def web_search(query: str) -> SearchOutput:
    """Search the web for information on a topic. Returns combined text from top results."""
    if not TAVILY_API_KEY:
        return f"[web_search unavailable: TAVILY_API_KEY not set. Query was: '{query}']"
    # print("hello")
    response = requests.post(
        "https://api.tavily.com/search",
        json={"api_key": TAVILY_API_KEY, "query": query, "max_results": 5},
        timeout=15,
    )
    response.raise_for_status()
    results = response.json().get("results", [])

    if not results:
        return f"No results found for: {query}"

    return {
    "query": query,
    "results": [
        {
            "title": r.get("title"),
            "url": r.get("url"),
            "content": r.get("content")
        }
        for r in results
    ]
    }


@mcp.tool()
def fetch_doc_page(url: str) -> FetchDocOutput:
    """Fetch a documentation/web page and return its readable text content."""
    try:
        print(f"i am in url{url}")
        response = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
    except requests.RequestException as e:
        return {
        "status":"error",
        "url":url,
        "message":str(e)
        }

    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)
    return {
    "url": url,
    "content": text[:8000],
    "length": len(text)
    }


import uvicorn

app = mcp.streamable_http_app()

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
    )