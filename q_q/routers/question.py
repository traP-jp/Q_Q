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
    question = crud.question.get_question(db , question_id) 
    return schemas.QuestionDetail(
        question=schemas.Question(
            id=question.id,
            userId=question.user_id,
            content=question.content,
            responseNum=question.responseNum,
            favs=question.favs,
            done=question.done,
            tags=question.tags,
            stamps=question.stamps,
            createdAt=question.createdAt,
            updatedAt=question.updatedAt,
        ),
        answer=[]
        # answer: List[Answer(
        #     id=question.id
        #     userId=question.userId
        #     content=question.content
        #     favs=question.favs
        #     stamps=question.stamps
        #     createdAt=question.createdAt
        #     updatedAt=question.updatedAt
        # )]
    )

