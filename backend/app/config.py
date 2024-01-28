from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    echo_sql: bool = True
    test: bool = False
    project_name: str = "My FastAPI Project"
    oauth_token_secret: str = "my_dev_secret"
    debug_logs: bool = True


settings = Settings()

    