from fastapi import APIRouter, Depends, HTTPException
from q_q import crud, schemas
from sqlalchemy.orm import Session

from q_q.routers import deps


router = APIRouter()


# POST /answers Create a new answer
@router.post("/", status_code=201, response_model=schemas.Answer)
async def create_answer(
    answer: schemas.AnswerCreate,
    db: Session = Depends(deps.get_db),
):
    answer = crud.answer.create(db, obj_in=answer)
    if answer is None:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return answer
