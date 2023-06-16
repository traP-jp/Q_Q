from fastapi import FastAPI
from q_q.routers import api
from q_q.database.init_db import init_db

init_db()
app = FastAPI()

app.include_router(api.api_router, prefix="/api")
