from typing import Any
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from q_q.routers import deps
from q_q import crud

router = APIRouter()


@router.get("/")
async def read_questions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    questions = crud.question.get_multi(db, skip=skip, limit=limit)
    return questions
