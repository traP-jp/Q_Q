import uuid
from sqlalchemy.orm import Session
from q_q import schemas
from q_q.models import QuestionTags, Tag


class CRUDTag:
    def __init__(self, model):
        self.model = model

    def get_tag(self, db: Session, tag_id: str) -> Tag | None:
        return db.query(self.model).filter(Tag.id == tag_id).first()

    def get_tag_by_name(self, db: Session, tag_name: str) -> Tag | None:
        return db.query(self.model).filter(Tag.tag == tag_name).first()

    def create(
        self, db: Session, *, obj_in: schemas.TagCreate, no_commit=False
    ) -> None:
        prev = self.get_tag_by_name(db, obj_in.tag)
        if prev:
            return

        db.add(
            Tag(
                id=obj_in.id,
                tag=obj_in.tag,
            )
        )
        if not no_commit:
            db.commit()
        return


class CRUDTagQuestion:
    def __init__(self, model):
        self.model = model

    def get_tag_question(
        self, db: Session, tag_id: str, question_id: str
    ) -> QuestionTags | None:
        return (
            db.query(self.model)
            .filter(QuestionTags.tag_id == tag_id)
            .filter(QuestionTags.question_id == question_id)
            .first()
        )

    def create(
        self,
        db: Session,
        *,
        obj_in: schemas.TagQuestionCreate,
        no_commit=False,
    ) -> None:
        prev = self.get_tag_question(db, obj_in.tag_id, obj_in.question_id)
        if prev:
            return

        db.add(
            QuestionTags(
                tag_id=obj_in.tag_id,
                question_id=obj_in.question_id,
            )
        )
        if not no_commit:
            db.commit()
        return None


tag = CRUDTag(Tag)
tag_question = CRUDTagQuestion(QuestionTags)
