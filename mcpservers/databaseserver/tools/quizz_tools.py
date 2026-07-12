from mcpservers.databaseserver.database import SessionLocal
from mcpservers.databaseserver.models import Quiz, QuizAttempt


def save_quiz(topic_id: int, questions: list):
    db = SessionLocal()

    try:
        quiz = Quiz(
            topic_id=topic_id,
            questions=questions
        )

        db.add(quiz)
        db.commit()
        db.refresh(quiz)

        return {
            "quiz_id": quiz.id
        }

    finally:
        db.close()


def save_attempt(
    user_id: int,
    quiz_id: int,
    score: int,
    passed: bool,
    weak_concepts: list
):
    db = SessionLocal()

    try:
        attempt = QuizAttempt(
            user_id=user_id,
            quiz_id=quiz_id,
            score=score,
            passed=passed,
            weak_concepts=weak_concepts
        )

        db.add(attempt)
        db.commit()
        db.refresh(attempt)

        return {
            "attempt_id": attempt.id
        }

    finally:
        db.close()



def get_quiz(quiz_id: int):

    db = SessionLocal()

    try:

        quiz = (
            db.query(Quiz)
            .filter(Quiz.id == quiz_id)
            .first()
        )

        if quiz is None:

            return {
                "status": "error",
                "message": "Quiz not found"
            }

        return {
            "status": "success",
            "quiz_id": quiz.id,
            "topic_id": quiz.topic_id,
            "questions": quiz.questions
        }

    finally:

        db.close()