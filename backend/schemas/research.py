from pydantic import BaseModel


class ResearchRequest(BaseModel):
    user_id: int
    topic: str
    weak_concepts: list[str]


class ResearchResponse(BaseModel):
    topic_id: int
    markdown_path: str
    pdf_path: str