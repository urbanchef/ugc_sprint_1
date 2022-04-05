from pydantic import BaseSettings, Field


class TestSettings(BaseSettings):
    service_url: str = Field("http://127.0.0.1:8000", env="SERVICE_URL")
