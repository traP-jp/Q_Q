from q_q import models, schemas


def answer_response(answer: models.Answer) -> schemas.Answer:
    return schemas.Answer(
        id=answer.id,
        userId=answer.user_id,
        content=answer.content,
        favs=answer.favs,
        stamps=[
            schemas.Stamp(
                id=stamp.id, messageId=stamp.answer_id, count=stamp.count
            )
            for stamp in answer.stamps
        ],
        createdAt=answer.created_at,
        updatedAt=answer.updated_at,
    )
