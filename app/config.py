from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    ai_model_path: str = '/model'


app_settings = AppConfig()
