import pprint
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from q_q.routers import deps
from q_q import schemas
from q_q.services import stamp


router = APIRouter()


@router.get("/", response_model=List[schemas.Stamp])
async def read_stamps(
    db: Session = Depends(deps.get_db),
):
    try:
        data = stamp.get_stamps()
        return [
            schemas.TraQStamp(
                id=stamp["id"],
                name=stamp["name"],
                fileId=stamp["fileId"],
                isUnicode=stamp["isUnicode"],
            )
            for stamp in data
        ]
    except Exception as e:
        pprint(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
