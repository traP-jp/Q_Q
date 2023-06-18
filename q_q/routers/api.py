from fastapi import APIRouter
from .ping import router as ping_router
from .question import router as question_router
from .recommend import router as recommend_router
from .user import router as user_router
from .stamp import router as stamp_router
from .answer import router as answer_router
from .config import router as config_router
from .traq import router as traq_router

api_router = APIRouter()
api_router.include_router(ping_router, prefix="/ping", tags=["ping"])
api_router.include_router(
    question_router, prefix="/questions", tags=["question"]
)
api_router.include_router(
    recommend_router, prefix="/recommend", tags=["recommend"]
)
api_router.include_router(user_router, prefix="/users", tags=["user"])
api_router.include_router(stamp_router, prefix="/stamps", tags=["stamp"])
api_router.include_router(answer_router, prefix="/answers", tags=["answer"])
api_router.include_router(config_router, prefix="/config", tags=["config"])
api_router.include_router(traq_router, prefix="/v3", tags=["traq"])
