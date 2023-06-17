from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from q_q.routers import deps
from q_q import schemas


router = APIRouter()


# GET /recommend?q=...
@router.get("/", response_model=List[schemas.Question])
async def read_questions(
    db: Session = Depends(deps.get_db),
    q: str = "",
    skip: int = 0,
    limit: int = 100,
):
    # TODO: implement
    return []


# GET /recommend/{question_id}
@router.get("/{question_id}", response_model=List[schemas.Question])
async def read_question(
    question_id: str,
    db: Session = Depends(deps.get_db),
):
    # TODO: implement
    return []
