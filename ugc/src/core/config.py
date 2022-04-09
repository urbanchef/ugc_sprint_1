from logging import config as logging_config
from typing import List, Optional, Union

from pydantic import BaseSettings, FilePath, SecretStr

from .logger import LOGGING

logging_config.dictConfig(LOGGING)


class ProjectConfig(BaseSettings):
    """Represents the project configuration."""

    class Config:
        env_prefix = "PROJECT_"

    name: str = "UGC API Service"
    description: str = "User activity tracking"
    docs_url: str = "/api/openapi"
    openapi_url: str = "/api/openapi.json"


class KafkaConfig(BaseSettings):
    """Represents the configuration for the Kafka client."""

    class Config:
        env_prefix = "KAFKA_"

    bootstrap_servers: Union[List[str], str] = "127.0.0.1"
    security_protocol: str = "SASL_SSL"
    sasl_mechanism: str = "SCRAM-SHA-512"
    sasl_plain_username: Optional[str]
    sasl_plain_password: Optional[SecretStr]
    ssl_cafile: Optional[FilePath] = None


class JWTConfig(BaseSettings):
    class Config:
        env_prefix = "JWT_"

    secret_key: str = "buz"
    algorithms: str = "HS256"
