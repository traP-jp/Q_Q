from typing import List
import uuid
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

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
    q: str = None,
):
    questions = []
    if q is not None:
        questions = crud.question.search_questions(db, q)
    else:
        questions = crud.question.get_multi(db, skip=skip, limit=limit)
    return [convert.question_response(question) for question in questions]


# GET /questions/{question_id}
@router.get("/{question_id}", response_model=schemas.QuestionDetail)
async def read_question(
    question_id: str,
    db: Session = Depends(deps.get_db),
):
    question = crud.question.get_question(db, question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return schemas.QuestionDetail(
        question=convert.question_response(question),
        answers=[
            convert.question_answer_response(answer)
            for answer in question.answers
        ],
    )


# POST /questions Create a new question
@router.post("/", status_code=201, response_model=schemas.Question)
async def create_question(
    question: schemas.QuestionCreate,
    db: Session = Depends(deps.get_db),
):
    crud.question.create(db, obj_in=question)
    # save tags
    for tag in question.tags:
        tag_id = str(uuid.uuid4())
        crud.tag.create(db, obj_in=schemas.TagCreate(tag=tag, id=tag_id))
        crud.tag_question.create(
            db,
            obj_in=schemas.TagQuestionCreate(
                tag_id=tag_id, question_id=question.messageId
            ),
        )

    for stamp in question.stamps:
        crud.question_stamp.create(
            db,
            obj_in=schemas.StampCreate(
                id=str(uuid.uuid4()),
                messageId=stamp.messageId,
                count=stamp.count,
                fetchedAt=question.fetchedAt,
            ),
            no_commit=True,
        )
    db.commit()

    result = crud.question.get_question(db, question.messageId)
    if result is None:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return result
