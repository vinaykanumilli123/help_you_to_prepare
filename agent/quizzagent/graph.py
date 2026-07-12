from langgraph.graph import StateGraph, START, END

from .state import QuizState
from .nodes import (
    load_notes,
    read_notes,
    generate_quiz,
    save_quiz,
)


graph_builder = StateGraph(QuizState)

graph_builder.add_node("load_notes", load_notes)
graph_builder.add_node("read_notes", read_notes)
graph_builder.add_node("generate_quiz", generate_quiz)
graph_builder.add_node("save_quiz", save_quiz)

graph_builder.add_edge(START, "load_notes")
graph_builder.add_edge("load_notes", "read_notes")
graph_builder.add_edge("read_notes", "generate_quiz")
graph_builder.add_edge("generate_quiz", "save_quiz")
graph_builder.add_edge("save_quiz", END)

quizz_graph = graph_builder.compile()