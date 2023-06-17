from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from q_q.routers import deps
from q_q import crud, schemas

router = APIRouter()


# GET /questions?skip=...&limit=...
@router.get("/", response_model=List[schemas.Question])
async def read_questions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    questions = crud.question.get_multi(db, skip=skip, limit=limit)
    return questions


# GET /questions/{question_id}
@router.get("/{question_id}", response_model=schemas.QuestionDetail)
async def read_question(
    question_id: str,
    db: Session = Depends(deps.get_db),
):
    # TODO: implement
    return {}
