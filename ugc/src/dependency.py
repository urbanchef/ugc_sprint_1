from functools import lru_cache

from aiokafka import AIOKafkaProducer

from .core.config import KafkaConfig


@lru_cache()
def get_kafka_producer() -> AIOKafkaProducer:
    cfg = KafkaConfig()
    return AIOKafkaProducer(
        bootstrap_servers=cfg.bootstrap_servers,
        security_protocol=cfg.security_protocol,
        sasl_mechanism=cfg.sasl_mechanism,
        sasl_plain_username=cfg.sasl_plain_username,
        sasl_plain_password=cfg.sasl_plain_password.get_secret_value(),
    )
