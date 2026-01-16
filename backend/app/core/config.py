from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "ALM-DevOps"
    env: str = "dev"

    secret_key: str = "CHANGE_ME"
    access_token_expire_minutes: int = 1440

    database_url: str = "postgresql+psycopg://alm:alm@localhost:5432/alm"

    gitlab_webhook_secret: str = "CHANGE_ME"


settings = Settings()
