from fastapi import APIRouter

from agent.evaluationagent.graph import evaluation_graph
from backend.schemas.evaluation import (
    EvaluationRequest,
    EvaluationResponse
)

router = APIRouter(
    prefix="/api/evaluate",
    tags=["Evaluation"]
)


@router.post(
    "",
    response_model=EvaluationResponse
)
async def evaluate(request: EvaluationRequest):

    result = await evaluation_graph.ainvoke(
        {
            "user_id": request.user_id,
            "quiz_id": request.quiz_id,
            "answers": request.answers,
        }
    )

    return {
        "score": result["score"],
        "passed": result["passed"],
        "weak_concepts": result["weak_concepts"],
    }