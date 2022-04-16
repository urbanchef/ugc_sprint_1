import ssl
from datetime import datetime
from functools import lru_cache
from json import dumps
from typing import Any, Dict
from uuid import UUID

from aiokafka import AIOKafkaProducer

from ..core.config import KafkaConfig


def serializer(value: Dict[str, Any]) -> bytes:
    """Convert a Dictionary to JSON Bytes String."""
    value = value.copy()

    for k, v in value.items():
        if isinstance(v, UUID):
            value[k] = str(v)

        if isinstance(v, datetime):
            value[k] = v.strftime("%Y-%m-%d %H:%M:%S")

        if isinstance(v, bool):
            value[k] = int(v)

    return dumps(value).encode()


@lru_cache()
def get_kafka_producer() -> AIOKafkaProducer:
    cfg = KafkaConfig()
    params: Dict[str, Any] = dict(
        bootstrap_servers=cfg.bootstrap_servers,
        security_protocol=cfg.security_protocol,
        sasl_mechanism=cfg.sasl_mechanism,
        value_serializer=serializer,
    )
    if cfg.sasl_plain_username:
        params["sasl_plain_username"] = cfg.sasl_plain_username
    if cfg.sasl_plain_password:
        params["sasl_plain_password"] = cfg.sasl_plain_password.get_secret_value()
    if "SSL" in cfg.security_protocol:
        params["ssl_context"] = ssl.create_default_context(cafile=cfg.ssl_cafile)

    return AIOKafkaProducer(**params)
