from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    Text,
    Boolean,
    DateTime,
)
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from datetime import datetime

from q_q.database.base import SQLBase as Base


class QuestionTags(Base):
    __tablename__ = "question_tags"
    question_id = Column(
        UUIDType(binary=False),
        ForeignKey("questions.id"),
        primary_key=True,
        nullable=False,
    )
    tag_id = Column(
        UUIDType(binary=False),
        ForeignKey("tags.id"),
        primary_key=True,
        nullable=False,
    )


class Question(Base):
    __tablename__ = "questions"
    id = Column(UUIDType(binary=False), primary_key=True, index=True)
    text = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    done = Column(Boolean, default=False, nullable=False)
    fetched_at = Column(
        DateTime,
        default=datetime.now(),
        nullable=False,
    )
    tags = relationship(
        "Tag", secondary=QuestionTags.__tablename__, back_populates="questions"
    )


class Tag(Base):
    __tablename__ = "tags"
    id = Column(UUIDType(binary=False), primary_key=True, index=True)
    tag = Column(String(50), nullable=False)
    questions = relationship(
        "Question", secondary=QuestionTags.__tablename__, back_populates="tags"
    )
