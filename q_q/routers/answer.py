import uuid
from fastapi import APIRouter, Depends, HTTPException
from q_q import crud, schemas
from sqlalchemy.orm import Session

from q_q.routers import deps
from q_q.schemas import convert


router = APIRouter()


# POST /answers Create a new answer
@router.post("/", status_code=201, response_model=schemas.Answer)
async def create_answer(
    answer: schemas.AnswerCreate,
    db: Session = Depends(deps.get_db),
):
    try:
        crud.answer.create(db, obj_in=answer)
        # stamp
        for stamp in answer.stamps:
            crud.answer_stamp.create(
                db,
                obj_in=schemas.StampCreate(
                    id=str(uuid.uuid4()),
                    messageId=stamp.messageId,
                    count=stamp.count,
                    fetchedAt=answer.fetchedAt,
                ),
                no_commit=True,
            )
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")

    result = crud.answer.get_answer(db, answer_id=answer.messageId)
    if result is None:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return convert.answer_response(result)
