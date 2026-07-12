from mcpservers.databaseserver.database import SessionLocal
from mcpservers.databaseserver.models import QuizAttempt


def load_progress(user_id: int):
    db = SessionLocal()

    try:
        attempts = (
            db.query(QuizAttempt)
            .filter(QuizAttempt.user_id == user_id)
            .all()
        )

        if not attempts:
            return {
                "attempts": 0,
                "average_score": 0
            }

        average = sum(a.score for a in attempts) / len(attempts)

        return {
            "attempts": len(attempts),
            "average_score": round(average, 2)
        }

    finally:
        db.close()