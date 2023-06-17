from sqlalchemy.orm import Session
from q_q import schemas
from q_q.models import QuestionStamp, AnswerStamp


class CRUDQuestionStamp:
    def __init__(self, model):
        self.model = model

    def get_stamp_by_id(
        self, db: Session, stamp_id: str
    ) -> QuestionStamp | None:
        return (
            db.query(self.model).filter(QuestionStamp.id == stamp_id).first()
        )

    def get_stamp(
        self, db: Session, question_id: str, stamp_id: str
    ) -> QuestionStamp | None:
        return (
            db.query(self.model)
            .filter(QuestionStamp.question_id == question_id)
            .filter(QuestionStamp.id == stamp_id)
            .first()
        )

    def create(
        self, db: Session, *, obj_in: schemas.StampCreate, no_commit=False
    ) -> None:
        prev = self.get_stamp(db, obj_in.message_id, obj_in.id)
        if prev:
            return

        db.add(
            QuestionStamp(
                id=obj_in.id,
                question_id=obj_in.message_id,
                count=obj_in.count,
                fetched_at=obj_in.fetched_at,
            )
        )
        if not no_commit:
            db.commit()
        return


class CRUDAnswerStamp:
    def __init__(self, model):
        self.model = model

    def get_stamp_by_id(
        self, db: Session, stamp_id: str
    ) -> AnswerStamp | None:
        return db.query(self.model).filter(AnswerStamp.id == stamp_id).first()

    def get_stamp(
        self, db: Session, answer_id: str, stamp_id: str
    ) -> AnswerStamp | None:
        return (
            db.query(self.model)
            .filter(AnswerStamp.answer_id == answer_id)
            .filter(AnswerStamp.id == stamp_id)
            .first()
        )

    def create(
        self, db: Session, *, obj_in: schemas.StampCreate, no_commit=False
    ) -> None:
        prev = self.get_stamp(db, obj_in.message_id, obj_in.id)
        if prev:
            return

        db.add(
            AnswerStamp(
                id=obj_in.id,
                answer_id=obj_in.message_id,
                count=obj_in.count,
                fetched_at=obj_in.fetched_at,
            )
        )
        if not no_commit:
            db.commit()
        return


question_stamp = CRUDQuestionStamp(QuestionStamp)
answer_stamp = CRUDAnswerStamp(AnswerStamp)
