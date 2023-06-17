from fastapi import APIRouter
from q_q import schemas
from q_q.core.config import Settings
from q_q.database.base import SQLBase
from q_q.database.session import engine


router = APIRouter()


@router.post("/initialize")
async def initialize(
    data: schemas.AppConfig,
):
    if data.password != Settings.root_password:
        return {"message": "invalid password"}
    # create db
    SQLBase.metadata.create_all(bind=engine)
    return {"message": "ok"}
