from fastapi import APIRouter
from .ping import router as ping_router
from .question import router as question_router
from .search import router as search_router
from .recommend import router as recommend_router
from .user import router as user_router

api_router = APIRouter()
api_router.include_router(ping_router, prefix="/ping", tags=["ping"])
api_router.include_router(
    question_router, prefix="/questions", tags=["question"]
)
api_router.include_router(search_router, prefix="/search", tags=["search"])
api_router.include_router(
    recommend_router, prefix="/recommend", tags=["recommend"]
)
api_router.include_router(user_router, prefix="/users", tags=["user"])
