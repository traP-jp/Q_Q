import datetime
from pydantic import UUID4, BaseModel


class TraQStamp(BaseModel):
    id: UUID4
    name: str
    fileId: UUID4
    isUnicode: bool


class StampCreate(BaseModel):
    id: UUID4
    messageId: UUID4
    count: int
    fetchedAt: datetime.datetime
