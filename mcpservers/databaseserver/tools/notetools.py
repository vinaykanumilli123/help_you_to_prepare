from mcpservers.databaseserver.database import SessionLocal
from mcpservers.databaseserver.models import Note,Topic


def save_notes(
    topic_id: int,
    markdown_path: str,
    pdf_path: str
):
    db = SessionLocal()

    try:
        note = Note(
            topic_id=topic_id,
            markdown_path=markdown_path,
            pdf_path=pdf_path
        )

        db.add(note)
        db.commit()
        db.refresh(note)

        return {
            "note_id": note.id
        }

    finally:
        db.close()



def get_notes(user_id: int, topic_id: int):
    """
    Fetch the notes for a topic belonging to a specific user.
    """

    db = SessionLocal()

    try:
        note = (
            db.query(Note)
            .join(Topic, Note.topic_id == Topic.id)
            .filter(
                Topic.user_id == user_id,
                Topic.id == topic_id
            )
            .first()
        )

        if not note:
            return {
                "status": "error",
                "message": "Notes not found."
            }

        return {
            "status": "success",
            "note_id": note.id,
            "topic_id": note.topic_id,
            "markdown_path": note.markdown_path,
            "pdf_path": note.pdf_path
        }

    finally:
        db.close()