from pydantic import UUID4, BaseModel


class AppConfig(BaseModel):
    password: str
