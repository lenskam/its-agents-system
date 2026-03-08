from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "development"
    app_log_level: str = "INFO"
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    database_url: str = "postgresql+asyncpg://its_admin:its_dev_password@localhost:5432/its_agents"

    redis_url: str = "redis://localhost:6379/0"

    gemini_api_key: str = ""
    ollama_url: str = "http://localhost:11434"
    ollama_model: str = "phi3:mini"

    telegram_bot_token: str = ""
    telegram_chat_id: str = ""

    clients_config_dir: str = "./clients"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

    @property
    def clients_path(self) -> Path:
        return Path(self.clients_config_dir)

    @property
    def is_development(self) -> bool:
        return self.app_env == "development"

    @property
    def has_gemini(self) -> bool:
        return bool(self.gemini_api_key) and self.gemini_api_key != "your_gemini_api_key_here"

    @property
    def has_telegram(self) -> bool:
        return (
            bool(self.telegram_bot_token)
            and self.telegram_bot_token != "your_telegram_bot_token_here"
        )


settings = Settings()
