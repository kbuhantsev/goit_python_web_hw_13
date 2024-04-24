from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # DB
    user: str
    password: str
    db_name: str
    domain: str
    port: str

    # MAIL
    mail_username: str
    mail_password: str
    mail_from: str
    mail_port: int
    mail_server: str
    mail_from_name: str

    # JWT
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    @staticmethod
    def get_uri():
        return f"postgresql+asyncpg://{settings.user}:{settings.password}@{settings.domain}:{settings.port}/{settings.db_name}"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
