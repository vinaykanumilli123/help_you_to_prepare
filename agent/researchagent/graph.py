from langgraph.graph import StateGraph
from langgraph.graph import START, END

from .state import ResearchState
from .nodes import (
    research_node,
    notes_node,
    storage_node,
    database_node,
)

builder = StateGraph(ResearchState)

builder.add_node("research", research_node)
builder.add_node("notes", notes_node)
builder.add_node("storage", storage_node)
builder.add_node("database", database_node)

builder.add_edge(START, "research")
builder.add_edge("research", "notes")
builder.add_edge("notes", "storage")
builder.add_edge("storage", "database")
builder.add_edge("database", END)

research_graph = builder.compile()