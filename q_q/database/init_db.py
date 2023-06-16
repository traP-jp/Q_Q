from .session import engine
from .base import SQLBase


def init_db() -> None:
    SQLBase.metadata.create_all(bind=engine)
