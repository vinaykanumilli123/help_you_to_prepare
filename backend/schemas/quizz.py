from pydantic import BaseModel


class QuizRequest(BaseModel):
    user_id: int
    topic_id: int


class QuizResponse(BaseModel):
    quiz_id: int
    questions: list