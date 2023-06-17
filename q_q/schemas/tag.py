from pydantic import UUID4, BaseModel


class TagCreate(BaseModel):
    id: UUID4
    tag: str
