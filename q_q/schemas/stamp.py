from pydantic import UUID4, BaseModel


class TraQStamp(BaseModel):
    id: UUID4
    name: str
    fileId: UUID4
    isUnicode: bool
