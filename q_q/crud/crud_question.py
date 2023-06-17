from typing import List
from sqlalchemy.orm import Session
from q_q import schemas
from q_q.models import Question


class CRUDQuestion:
    def __init__(self, model):
        self.model = model

    def get_question(self, db: Session, question_id: str):
        return db.query(self.model).filter(Question.id == question_id).first()

    def search_questions(self, db: Session, question_content: str):
        return (
            db.query(self.model)
            .filter(Question.content.contains(question_content))
            .limit(20)
            .all()
        )

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Question]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(
        self, db: Session, *, obj_in: schemas.QuestionCreate, no_commit=False
    ) -> None:
        db.add(
            Question(
                id=obj_in.messageId,
                user_id=obj_in.userId,
                content=obj_in.content,
                favs=0,
                vector="",
                done=obj_in.done,
                fetched_at=obj_in.fetchedAt,
                created_at=obj_in.createdAt,
                updated_at=obj_in.updatedAt,
            )
        )
        if not no_commit:
            db.commit()
        return


question = CRUDQuestion(Question)
