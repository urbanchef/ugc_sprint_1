from pydantic import BaseSettings, Field


class TestSettings(BaseSettings):
    service_url: str = Field("http://0.0.0.0", env="SERVICE_URL")
