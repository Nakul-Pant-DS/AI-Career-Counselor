from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    API_PREFIX: str

    HOST: str
    PORT: int

    ENVIRONMENT: str
    LOG_LEVEL: str

    GROQ_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
