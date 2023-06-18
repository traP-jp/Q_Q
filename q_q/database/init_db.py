from q_q.core.config import settings
from q_q.database import mockdata
from sqlalchemy.orm import sessionmaker
from .session import engine
from .base import SQLBase


def init_db() -> None:
    if settings.gen_mock_data:
        print("init_db")
        SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
        session = SessionClass()
        SQLBase.metadata.drop_all(bind=engine)
        SQLBase.metadata.create_all(bind=engine)
        mockdata.insert_mockdata(session)
    elif settings.gen_table:
        print("init_db (gen_table)")
        SQLBase.metadata.create_all(bind=engine)
    else:
        print("skip init_db")
