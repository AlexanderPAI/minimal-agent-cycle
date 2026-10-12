from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    openrouter_api_key: str = Field(..., description="OpenRouter API key")
    openrouter_model: str = Field(..., description="OpenRouter model name")
    agent_max_steps: int = Field(..., description="Max number of steps to run")
    llm_timeout_seconds: int = Field(..., description="Time to wait for LLM")

    model_config = SettingsConfigDict(
        env_file=".env",
    )


config = Settings()
