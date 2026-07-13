import json

from agent.llm import llm
from agent.database_client import DatabaseClient
from .prompts import QUIZ_PROMPT
import requests
db = DatabaseClient()


async def load_notes(state):
    """
    Fetch the markdown path for the given topic.
    """

    note = await db.get_notes(
        user_id=state["user_id"],
        topic_id=state["topic_id"],
    )

    if note["status"] != "success":
        raise Exception(note["message"])

    return {
        "markdown_path": note["markdown_path"]
    }


def read_notes(state):

    response = requests.get(
        state["markdown_path"],
        timeout=15
    )
    response.raise_for_status()

    return {
        "notes": response.text
    }


async def generate_quiz(state):
    """
    Generate quiz using Gemini.
    """

    prompt = QUIZ_PROMPT.format(
        notes=state["notes"]
    )

    response = await llm.ainvoke(prompt)

    quiz = json.loads(response.content)

    return {
        "quiz": quiz
    }


async def save_quiz(state):

    result = await db.save_quiz(
        topic_id=state["topic_id"],
        questions=state["quiz"],
    )

    return {
        "quiz_id": result["quiz_id"]
    }