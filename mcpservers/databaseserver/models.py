from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    JSON,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import declarative_base, relationship

from sqlalchemy.sql import func


Base = declarative_base()


# -------------------------
# USERS
# -------------------------

class User(Base):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True
    )

    google_id = Column(
        String(255),
        unique=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )


    topics = relationship(
        "Topic",
        back_populates="user"
    )



# -------------------------
# TOPICS
# -------------------------

class Topic(Base):

    __tablename__ = "topics"


    id = Column(
        Integer,
        primary_key=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )


    topic_name = Column(
        String(255),
        nullable=False
    )


    created_at = Column(
        DateTime,
        server_default=func.now()
    )


    user = relationship(
        "User",
        back_populates="topics"
    )


    notes = relationship(
        "Note",
        back_populates="topic"
    )


    quizzes = relationship(
        "Quiz",
        back_populates="topic"
    )



# -------------------------
# RESEARCH SOURCES
# -------------------------

class ResearchSource(Base):

    __tablename__ = "research_sources"


    id = Column(
        Integer,
        primary_key=True
    )


    topic_id = Column(
        Integer,
        ForeignKey("topics.id")
    )


    title = Column(
        Text
    )


    url = Column(
        Text
    )


    content = Column(
        Text
    )


    created_at = Column(
        DateTime,
        server_default=func.now()
    )



# -------------------------
# NOTES
# -------------------------

class Note(Base):

    __tablename__ = "notes"


    id = Column(
        Integer,
        primary_key=True
    )


    topic_id = Column(
        Integer,
        ForeignKey("topics.id")
    )


    markdown_path = Column(
        Text
    )


    pdf_path = Column(
        Text
    )


    created_at = Column(
        DateTime,
        server_default=func.now()
    )


    topic = relationship(
        "Topic",
        back_populates="notes"
    )



# -------------------------
# QUIZZES
# -------------------------

class Quiz(Base):

    __tablename__ = "quizzes"


    id = Column(
        Integer,
        primary_key=True
    )


    topic_id = Column(
        Integer,
        ForeignKey("topics.id")
    )


    questions = Column(
        JSON
    )


    created_at = Column(
        DateTime,
        server_default=func.now()
    )


    topic = relationship(
        "Topic",
        back_populates="quizzes"
    )



# -------------------------
# QUIZ ATTEMPTS
# -------------------------

class QuizAttempt(Base):

    __tablename__ = "quiz_attempts"


    id = Column(
        Integer,
        primary_key=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )


    quiz_id = Column(
        Integer,
        ForeignKey("quizzes.id")
    )


    score = Column(
        Integer
    )


    passed = Column(
        Boolean
    )


    weak_concepts = Column(
        JSON
    )


    attempted_at = Column(
        DateTime,
        server_default=func.now()
    )



# -------------------------
# NOTIFICATIONS
# -------------------------

class Notification(Base):

    __tablename__="notifications"


    id = Column(
        Integer,
        primary_key=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )


    type = Column(
        String(50)
    )


    message = Column(
        Text
    )


    sent_at = Column(
        DateTime,
        server_default=func.now()
    )