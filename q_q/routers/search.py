from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from q_q.routers import deps
from q_q import schemas

router = APIRouter()


# GET /search?q=...
@router.get("/", response_model=List[schemas.Question])
async def search_questions(
    db: Session = Depends(deps.get_db),
    q: str = "",
    skip: int = 0,
    limit: int = 100,
):
    # TODO: implement
    return []
