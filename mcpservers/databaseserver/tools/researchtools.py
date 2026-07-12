from mcpservers.databaseserver.database import SessionLocal
from mcpservers.databaseserver.models import ResearchSource


def save_research_source(
    topic_id: int,
    title: str,
    url: str,
    content: str
):
    db = SessionLocal()

    try:
        source = ResearchSource(
            topic_id=topic_id,
            title=title,
            url=url,
            content=content
        )

        db.add(source)
        db.commit()
        db.refresh(source)

        return {
            "source_id": source.id
        }

    finally:
        db.close()