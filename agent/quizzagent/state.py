from typing import TypedDict


class QuizState(TypedDict):
    topic_id: int
    user_id:int
    markdown_path: str
    notes: str

    quiz: list

    quiz_id: int