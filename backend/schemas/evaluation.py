from pydantic import BaseModel


class EvaluationRequest(BaseModel):
    user_id: int
    quiz_id: int
    answers: list[str]


class EvaluationResponse(BaseModel):
    score: int
    passed: bool
    weak_concepts: list[str]