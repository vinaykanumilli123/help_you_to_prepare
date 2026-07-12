from fastapi import APIRouter

from backend.schemas.research import (
    ResearchRequest,
    ResearchResponse
)

from agent.researchagent.graph import research_graph

router = APIRouter(
    prefix="/api/research",
    tags=["Research"]
)


@router.post(
    "",
    response_model=ResearchResponse
)
async def research(request: ResearchRequest):

    result = await research_graph.ainvoke(
        {
            "user_id": request.user_id,
            "topic": request.topic,
            "weak_concepts":request.weak_concepts
        }
    )

    return {
        "topic_id": result["topic_id"],
        "markdown_path": result["markdown_path"],
        "pdf_path": result["pdf_path"],
    }