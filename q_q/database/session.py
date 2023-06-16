from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from q_q.core.config import settings

db_user = settings.db_user
db_password = settings.db_password
db_host = settings.db_host
db_port = settings.db_port
db_database = settings.db_database

engine = create_engine(
    f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}?charset=utf8mb4"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
