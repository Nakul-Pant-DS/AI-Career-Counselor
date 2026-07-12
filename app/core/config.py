from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central configuration for the AI Career Counselor Platform.
    """

    # ==========================================================
    # Application Configuration
    # ==========================================================

    APP_NAME: str
    APP_VERSION: str
    API_PREFIX: str

    HOST: str
    PORT: int

    ENVIRONMENT: str
    LOG_LEVEL: str

    # ==========================================================
    # LLM Configuration
    # ==========================================================

    GROQ_API_KEY: str

    LLM_PROVIDER: str = "groq"

    GROQ_MODEL: str = "llama-3.3-70b-versatile"

    LLM_TEMPERATURE: float = 0.2

    LLM_MAX_TOKENS: int = 2048

    # ==========================================================
    # RAG Configuration
    # ==========================================================

    CHUNK_SIZE: int = 500

    CHUNK_OVERLAP: int = 100

    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    VECTOR_DB_DIR: str = "data/vector_db"

    # ==========================================================
    # Pydantic Configuration
    # ==========================================================

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()