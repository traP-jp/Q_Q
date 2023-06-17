from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_database: str
    api_token: str
    gen_mock_data: bool = False

    class Config:
        env_file = ".env"
        fields = {
            "db_host": {"env": "NS_MARIADB_HOSTNAME"},
            "db_port": {"env": "NS_MARIADB_PORT"},
            "db_user": {"env": "NS_MARIADB_USER"},
            "db_password": {"env": "NS_MARIADB_PASSWORD"},
            "db_database": {"env": "NS_MARIADB_DATABASE"},
            "api_token": {"env": "TRAQ_API_TOKEN"},
            "gen_mock_data": {"env": "GEN_MOCK_DATA"},
        }


settings = Settings()
