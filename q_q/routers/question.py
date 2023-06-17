from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from q_q.routers import deps
from q_q import crud, schemas
import q_q.schemas.convert as convert

router = APIRouter()


# GET /questions?skip=...&limit=...
@router.get("/", response_model=List[schemas.Question])
async def read_questions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    questions = crud.question.get_multi(db, skip=skip, limit=limit)
    return [convert.question_response(question) for question in questions]


# GET /questions/{question_id}
@router.get("/{question_id}", response_model=schemas.QuestionDetail)
async def read_question(
    question_id: str,
    db: Session = Depends(deps.get_db),
):
    question = crud.question.get_question(db , question_id) 
    return schemas.QuestionDetail(
        question=convert.question_response(question),
        answers=[convert.question_answer_response(answer)for answer in question.answers]
    )

