from mcpservers.databaseserver.database import SessionLocal
from mcpservers.databaseserver.models import User


def save_user(name: str, email: str, google_id: str | None = None):
    db = SessionLocal()

    try:
        existing = db.query(User).filter(User.email == email).first()

        if existing:
            return {
                "status": "exists",
                "user_id": existing.id
            }

        user = User(
            name=name,
            email=email,
            google_id=google_id
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return {
            "status": "success",
            "user_id": user.id
        }

    finally:
        db.close()


def get_user(email: str):
    db = SessionLocal()

    try:
        user = db.query(User).filter(User.email == email).first()

        if not user:
            return None

        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "google_id": user.google_id
        }

    finally:
        db.close()