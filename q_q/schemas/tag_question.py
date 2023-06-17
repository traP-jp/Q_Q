from pydantic import UUID4, BaseModel


class TagQuestionCreate(BaseModel):
    question_id: UUID4
    tag_id: UUID4
