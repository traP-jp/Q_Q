import datetime
from typing import List
from pydantic import UUID4, BaseModel


class Stamp(BaseModel):
    id: UUID4
    messageId: UUID4
    count: int


class Question(BaseModel):
    id: UUID4
    userId: UUID4
    content: str
    responseNum: int
    favs: int
    done: bool
    tags: List[str]
    stamps: List[Stamp]
    createdAt: datetime.datetime
    updatedAt: datetime.datetime


class Answer(BaseModel):
    id: UUID4
    userId: UUID4
    content: str
    favs: int
    stamps: List[Stamp]
    createdAt: datetime.datetime
    updatedAt: datetime.datetime


class QuestionDetail(BaseModel):
    question: Question
    answers: List[Answer]
