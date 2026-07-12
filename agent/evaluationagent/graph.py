from langgraph.graph import StateGraph, START, END

from .state import EvaluationState
from .nodes import (
    load_quiz,
    evaluate_answers,
    extract_weak_concepts,
    save_attempt,
)

builder = StateGraph(EvaluationState)

builder.add_node("load_quiz", load_quiz)
builder.add_node("evaluate_answers", evaluate_answers)
builder.add_node("extract_weak_concepts", extract_weak_concepts)
builder.add_node("save_attempt", save_attempt)

builder.add_edge(START, "load_quiz")
builder.add_edge("load_quiz", "evaluate_answers")
builder.add_edge("evaluate_answers", "extract_weak_concepts")
builder.add_edge("extract_weak_concepts", "save_attempt")
builder.add_edge("save_attempt", END)

evaluation_graph = builder.compile()