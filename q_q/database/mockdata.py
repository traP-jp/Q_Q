from sqlalchemy.orm import Session
from q_q.models import Question, QuestionStamp


def insert_mockdata(db: Session):
    db.add(
        Question(
            id="3be4b850-dcd3-42a7-9751-a9f43d0e1732",
            user_id="5f324dc6-8f9f-4f4c-a513-61db8312e067",
            content="test",
            favs=0,
            vector="",
            done=False,
            created_at="2021-08-01 00:00:00",
            updated_at="2021-08-01 00:00:00",
        )
    )
    db.add(
        Question(
            id="55ad6186-ed64-475b-b094-9c997051f0ba",
            user_id="5f324dc6-8f9f-4f4c-a513-61db8312e067",
            content="test2",
            favs=1,
            vector="",
            done=False,
            created_at="2021-08-01 00:00:00",
            updated_at="2021-08-01 00:00:00",
        )
    )
    db.add(
        QuestionStamp(
            id="3be4b850-dcd3-42a7-9751-a9f43d0e1732",
            question_id="3be4b850-dcd3-42a7-9751-a9f43d0e1732",
            count=1,
        )
    )
    db.commit()
