from typing import List
from sqlalchemy.orm import Session
from q_q.models import Question


class CURDQuestion:
    def __init__(self, model):
        self.model = model

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Question]:
        return db.query(self.model).offset(skip).limit(limit).all()


question = CURDQuestion(Question)
