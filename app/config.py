from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    ai_model_path: str


app_settings = AppConfig()
