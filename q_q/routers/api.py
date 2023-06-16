from fastapi import APIRouter
from .ping import router as ping_router
from .question import router as question_router

api_router = APIRouter()
api_router.include_router(ping_router, prefix="/ping", tags=["ping"])
api_router.include_router(
    question_router, prefix="/questions", tags=["question"]
)
