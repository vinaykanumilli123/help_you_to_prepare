from typing import TypedDict

class EvaluationState(TypedDict):
    user_id: int
    topic_id: int
    quiz_id: int

    answers: list[str]
    quiz: list

    score: int
    passed: bool

    wrong_answers: list

    weak_concepts: list[str]

    attempt_id: int