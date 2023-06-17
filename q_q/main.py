from fastapi import FastAPI
from q_q.routers import api
from q_q.database.init_db import init_db
from fastapi.middleware.cors import CORSMiddleware


init_db()
app = FastAPI()

# CORS
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["*"],
)

app.include_router(api.api_router, prefix="/api")
