"""Модуль настройки окружения"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Класс конфигурации из переменных среды"""

    PG_USERNAME: str
    PG_PASSWORD: str
    PG_HOST: str
    PG_PORT: str
    PG_DATABASE: str

    SECRET_KEY: str
    ALGORITHM: str
    TOKEN_EXP_MIN: int
    @property
    def DATABASE_URL(self) -> str:
        """URL для синхронного подключения к БД"""
        return f"postgresql+asyncpg://{self.PG_USERNAME}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DATABASE}"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_")


settings = Settings()
