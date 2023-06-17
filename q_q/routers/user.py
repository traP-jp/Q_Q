from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from q_q.routers import deps
from q_q import schemas


router = APIRouter()


# GET /users/{user_id}
@router.get("/{user_id}", response_model=schemas.User)
async def read_user(
    user_id: str,
    db: Session = Depends(deps.get_db),
):
    # TODO: implement
    return []
