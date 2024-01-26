from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    echo_sql: bool = True
    test: bool = False
    project_name: str = "My FastAPI Project"
    outh_token_sercret: str = "my_dev_secret"


settings = Settings()

    