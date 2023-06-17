from sqlalchemy.orm import Session
from q_q import schemas
from q_q.models import Answer


class CRUDAnswer:
    def __init__(self, model):
        self.model = model

    def get_answer(self, db: Session, answer_id: str) -> Answer | None:
        return db.query(self.model).filter(Answer.id == answer_id).first()

    def create(
        self, db: Session, *, obj_in: schemas.AnswerCreate, no_commit=False
    ) -> None:
        db.add(
            Answer(
                id=obj_in.messageId,
                question_id=obj_in.questionId,
                user_id=obj_in.userId,
                content=obj_in.content,
                favs=0,
                fetched_at=obj_in.fetchedAt,
                created_at=obj_in.createdAt,
                updated_at=obj_in.updatedAt,
            )
        )
        if not no_commit:
            db.commit()
        return None


answer = CRUDAnswer(Answer)
