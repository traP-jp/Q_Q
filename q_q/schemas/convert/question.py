from q_q import models, schemas


def question_response(question: models.Question) -> schemas.Question:
    return schemas.Question(
        id=question.id,
        userId=question.user_id,
        content=question.content,
        responseNum=len(question.answers),
        favs=question.favs,
        done=question.done,
        tags=question.tags,
        stamps=[
            schemas.Stamp(
                id=stamp.id, messageId=stamp.question_id, count=stamp.count
            )
            for stamp in question.stamps
        ],
        createdAt=question.created_at,
        updatedAt=question.updated_at,
    )

def question_answer_response(
        answer: models.Answer)-> schemas.Answer:
    return schemas.Answer(
        id=answer.id,
        userId=answer.user_id,
        content=answer.content,
        favs=answer.favs,
        stamps=[
            schemas.Stamp(
                id=stamp.id,messageId=stamp.answer_id,count=stamp.count
            )
            for stamp in answer.stamps
        ],
        createdAt=answer.created_at,
        updatedAt=answer.updated_at,
    )
