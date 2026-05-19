from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    REDIS_URL: str = "redis://localhost:6379"
    CELEBRITY_THRESHOLD: int = 10000
    USE_ML_RANKING: bool = False

    model_config = {"env_file": ".env"}


settings = Settings()
