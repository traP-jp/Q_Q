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
