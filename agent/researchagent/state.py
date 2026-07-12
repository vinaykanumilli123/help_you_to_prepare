from typing import TypedDict


class ResearchState(TypedDict):
    # Input
    user_id: int
    topic: str
    weak_concepts: list[str]

    # Research
    raw_content: str
    sources: list[dict]

    # Notes
    markdown_notes: str

    # Storage
    markdown_path: str
    pdf_path: str

    # Database
    topic_id: int

    # Output
    status: str