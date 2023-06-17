from typing import List
from sqlalchemy.orm import Session
from q_q.models import Question


class CURDQuestion:
    def __init__(self, model):
        self.model = model
    def get_question(self, db: Session, question_id: str):
        return db.query(self.model).filter(Question.id == question_id).first()
    
    def search_questions(self, db: Session, question_content: str):
        return db.query(self.model).filter(Question.content.contains(question_content)).limit(20).all()

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Question]:
        return db.query(self.model).offset(skip).limit(limit).all()


question = CURDQuestion(Question)
