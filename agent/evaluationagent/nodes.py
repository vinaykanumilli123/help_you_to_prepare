import json

from agent.llm import llm
from agent.database_client import DatabaseClient
from .prompts import WEAK_CONCEPT_PROMPT
from agent.utils import extract_json
db = DatabaseClient()


async def load_quiz(state):

    quiz = await db.get_quiz(
        quiz_id=state["quiz_id"]
    )

    return {
        "quiz": quiz["questions"]
    }


async def evaluate_answers(state):

    correct = 0
    wrong_answers = []

    for question, user_answer in zip(
        state["quiz"],
        state["answers"]
    ):

        if user_answer == question["answer"]:

            correct += 1

        else:

            wrong_answers.append(
                {
                    "question": question["question"],
                    "correct_answer": question["answer"],
                    "user_answer": user_answer,
                    "explanation": question["explanation"]
                }
            )

    score = int(
        (correct / len(state["quiz"])) * 100
    )

    passed = score >= 70

    return {
        "score": score,
        "passed": passed,
        "wrong_answers": wrong_answers
    }


async def extract_weak_concepts(state):

    # User passed -> nothing to improve
    if state["passed"]:

        return {
            "weak_concepts": []
        }

    prompt = WEAK_CONCEPT_PROMPT.format(
        wrong_answers=json.dumps(
            state["wrong_answers"],
            indent=2
        )
    )

    response =await llm.ainvoke(prompt)
    print(response)

    result = extract_json(response.content)

    return {
        "weak_concepts": result["weak_concepts"]
    }


async def save_attempt(state):

    result = await db.save_attempt(

        user_id=state["user_id"],

        quiz_id=state["quiz_id"],

        score=state["score"],

        passed=state["passed"],

        weak_concepts=state["weak_concepts"]

    )

    return {
        "attempt_id": result["attempt_id"]
    }