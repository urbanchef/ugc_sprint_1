from logging import config as logging_config
from typing import List, Optional, Union

from pydantic import BaseSettings, SecretStr

from .logger import LOGGING

logging_config.dictConfig(LOGGING)


class ProjectConfig(BaseSettings):
    """Represents the project configuration."""

    class Config:
        env_prefix = "PROJECT_"

    name: str = "UGC API Service"
    description: str = "User activity tracking"


class KafkaConfig(BaseSettings):
    """Represents the configuration for the Kafka client."""

    class Config:
        env_prefix = "KAFKA_"

    bootstrap_servers: Union[List[str], str] = "127.0.0.1"
    security_protocol: str = "SASL_SSL"
    sasl_mechanism: str = "SCRAM-SHA-512"
    sasl_plain_username: Optional[str]
    sasl_plain_password: Optional[SecretStr]
    ssl_cafile: Optional[str] = None


class JWTConfig(BaseSettings):
    class Config:
        env_prefix = "JWT_"

    secret_key: str = "buz"
    algorithms: str = "HS256"


class SentryConfig(BaseSettings):
    """Represents Sentry config."""

    class Config:
        env_prefix = "SENTRY_"

    dsn: Optional[SecretStr]
    sample_rate: float = 1.0
    traces_sample_rate: float = 0.0
