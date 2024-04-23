from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    user: str
    password: str
    db_name: str
    domain: str
    port: str

    @staticmethod
    def get_uri():
        return f"postgresql+asyncpg://{settings.user}:{settings.password}@{settings.domain}:{settings.port}/{settings.db_name}"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
