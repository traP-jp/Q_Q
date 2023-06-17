from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
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
    id = Column(UUIDType(binary=False), primary_key=True)
    user_id = Column(UUIDType(binary=False), nullable=False)
    content = Column(Text, nullable=False)
    favs = Column(Integer, default=0, nullable=False)
    vector = Column(Text, nullable=False)
    done = Column(Boolean, default=False, nullable=False)
    fetched_at = Column(
        DateTime,
        default=datetime.now(),
        nullable=False,
    )
    created_at = Column(
        DateTime,
        nullable=False,
    )
    updated_at = Column(
        DateTime,
        nullable=False,
    )
    tags = relationship(
        "Tag", secondary=QuestionTags.__tablename__, back_populates="questions"
    )
    stamps = relationship(
        "QuestionStamp",
        back_populates="questions",
    )
    answers = relationship("Answer", back_populates="questions")


class Answer(Base):
    __tablename__ = "answers"
    id = Column(UUIDType(binary=False), primary_key=True)
    user_id = Column(UUIDType(binary=False), nullable=False)
    question_id = Column(
        UUIDType(binary=False), ForeignKey("questions.id"), nullable=False
    )
    content = Column(Text, nullable=False)
    favs = Column(Integer, default=0, nullable=False)
    fetched_at = Column(
        DateTime,
        default=datetime.now(),
        nullable=False,
    )
    created_at = Column(
        DateTime,
        nullable=False,
    )
    updated_at = Column(
        DateTime,
        nullable=False,
    )
    questions = relationship("Question", back_populates="answers")
    stamps = relationship(
        "AnswerStamp",
        back_populates="answers",
    )


class Tag(Base):
    __tablename__ = "tags"
    id = Column(UUIDType(binary=False), primary_key=True, index=True)
    tag = Column(String(50), nullable=False)
    questions = relationship(
        "Question", secondary=QuestionTags.__tablename__, back_populates="tags"
    )


class QuestionStamp(Base):
    __tablename__ = "question_stamps"
    id = Column(UUIDType(binary=False), primary_key=True)
    question_id = Column(
        UUIDType(binary=False), ForeignKey("questions.id"), nullable=False
    )
    count = Column(Integer, default=0, nullable=False)
    fetched_at = Column(
        DateTime,
        default=datetime.now(),
        nullable=False,
    )
    questions = relationship(
        "Question", back_populates="stamps", uselist=False
    )


class AnswerStamp(Base):
    __tablename__ = "answer_stamps"
    id = Column(UUIDType(binary=False), primary_key=True)
    answer_id = Column(
        UUIDType(binary=False), ForeignKey("answers.id"), nullable=False
    )
    count = Column(Integer, default=0, nullable=False)
    fetched_at = Column(
        DateTime,
        default=datetime.now(),
        nullable=False,
    )
    answers = relationship("Answer", back_populates="stamps", uselist=False)
