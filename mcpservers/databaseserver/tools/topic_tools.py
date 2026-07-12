from mcpservers.databaseserver.database import SessionLocal
from mcpservers.databaseserver.models import Topic


def create_topic(user_id: int, topic_name: str):
    db = SessionLocal()

    try:
        topic = Topic(
            user_id=user_id,
            topic_name=topic_name
        )

        db.add(topic)
        db.commit()
        db.refresh(topic)

        return {
            "topic_id": topic.id
        }

    finally:
        db.close()


def get_user_topics(user_id: int):
    db = SessionLocal()

    try:
        topics = (
            db.query(Topic)
            .filter(Topic.user_id == user_id)
            .all()
        )

        return [
            {
                "id": t.id,
                "topic_name": t.topic_name
            }
            for t in topics
        ]

    finally:
        db.close()

if __name__=="__main__":
    create_topic(1,"mcpserver")