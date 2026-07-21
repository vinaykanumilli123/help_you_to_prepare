from fastapi import FastAPI

# from backend.routers.auth import router as auth_router
from backend.routers.research import router as research_router
from backend.routers.quizz import router as quiz_router
from backend.routers.evaluation import router as evaluation_router

app = FastAPI(
    title="Study Assistant API"
)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.include_router(auth_router)
app.include_router(research_router)
app.include_router(quiz_router)
app.include_router(evaluation_router)


@app.get("/")
async def root():
    return {
        "message": "Study Assistant Backend Running"
    }

@app.get("/version")
def version():
    return {
        "message": "Deployment Successful 🚀",
        "version": "v2"
    }