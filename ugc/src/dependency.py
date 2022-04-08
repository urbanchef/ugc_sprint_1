import logging
import ssl
from functools import lru_cache
from typing import Any, Dict

from aiokafka import AIOKafkaProducer

from .core.config import JWTConfig, KafkaConfig

logger = logging.getLogger(__name__)


@lru_cache()
def get_kafka_producer() -> AIOKafkaProducer:
    cfg = KafkaConfig()
    params: Dict[str, Any] = dict(
        bootstrap_servers=cfg.bootstrap_servers,
        security_protocol=cfg.security_protocol,
        sasl_mechanism=cfg.sasl_mechanism,
    )
    if cfg.sasl_plain_username:
        params["sasl_plain_username"] = cfg.sasl_plain_username
    if cfg.sasl_plain_password:
        params["sasl_plain_password"] = cfg.sasl_plain_password.get_secret_value()
    if "SSL" in cfg.security_protocol:
        params["ssl_context"] = ssl.create_default_context(cafile=cfg.ssl_cafile)

    return AIOKafkaProducer(**params)


@lru_cache()
def get_jwt_settings() -> JWTConfig:
    return JWTConfig()
