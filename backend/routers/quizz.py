from fastapi import APIRouter

from agent.quizzagent.graph import quizz_graph

from backend.schemas.quizz import (
    QuizRequest,
    QuizResponse
)

router = APIRouter(
    prefix="/api/quiz",
    tags=["Quiz"]
)


@router.post("",response_model=QuizResponse)
async def generate_quiz(request: QuizRequest):

    result = await quizz_graph.ainvoke(
        {
            "user_id": request.user_id,
            "topic_id": request.topic_id,
        }
    )

    questions = []

    for q in result["quiz"]:
        questions.append(
            {
                "question": q["question"],
                "options": q["options"]
            }
        )

    return {
        "quiz_id": result["quiz_id"],
        "questions": questions,
    }