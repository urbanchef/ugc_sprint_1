import logging
import ssl
from typing import Any, Dict, Optional

from aiokafka import AIOKafkaProducer

from ..core.config import KafkaConfig
from .utils import serializer

logger = logging.getLogger(__name__)
async_kafka_producer: Optional[AIOKafkaProducer] = None


async def get_kafka_producer() -> AIOKafkaProducer:
    """Возвращает объект для продюсера асинхронного общения с сервисами Kafka.
    Функция понадобится при внедрении зависимостей."""
    return async_kafka_producer


async def kafka_producer_connect():
    """Устанавливает соединение продюсера с сервисом Kafka."""
    # TODO: избавится от глобальных переменных инициализировав async_kafka_producer
    #  в on_startup и складывай в app.state. Из любого места можно будет
    #  достать и использовать
    global async_kafka_producer

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
    async_kafka_producer = AIOKafkaProducer(**params)
    await async_kafka_producer.start()
    logger.info("Producer установил соединение с Kafka.")


async def kafka_producer_disconnect():
    """Закрывает соединение продюсера с сервисом Kafka."""
    # TODO: см. замечание выше.
    global async_kafka_producer
    await async_kafka_producer.stop()
    logger.info("Producer разорвал соединение с Kafka.")
