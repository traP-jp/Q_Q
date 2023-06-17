from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from q_q.routers import deps
from q_q import schemas
from q_q.services import user


router = APIRouter()


# GET /users/{user_id}
@router.get("/{user_id}", response_model=schemas.User)
async def read_user(
    user_id: str,
    db: Session = Depends(deps.get_db),
):
    try:
        data = user.get_user(user_id)
        return schemas.User(
            id=data.id,
            name=data.name,
            displayName=data.display_name,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
