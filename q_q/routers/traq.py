from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Response,
)
from fastapi.responses import RedirectResponse
import requests
from sqlalchemy.orm import Session
from q_q.core.config import settings
from q_q.routers import deps

router = APIRouter()


@router.get("/files/{file_id}")
async def read_file(
    file_id: str,
    db: Session = Depends(deps.get_db),
):
    # get file
    file = requests.get(
        f"https://q.trap.jp/api/v3/files/{file_id}",
        headers={
            "Authorization": f"Bearer {settings.api_token}",
        },
    )
    if file.status_code != 200:
        raise HTTPException(status_code=404, detail="File not found")
    return Response(
        content=file.content, media_type=file.headers["Content-Type"]
    )
