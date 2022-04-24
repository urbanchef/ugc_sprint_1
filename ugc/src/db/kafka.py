import asyncio
import logging
import ssl
from typing import Any, Dict, Optional

from aiokafka import AIOKafkaProducer

from ..core.config import KafkaConfig
from ..engines.message_broker.general import GeneralProducerEngine
from ..engines.message_broker.kafka import KafkaProducerEngine
from .utils import serializer

logger = logging.getLogger(__name__)
event_broker: Optional[GeneralProducerEngine] = None


async def get_event_broker() -> GeneralProducerEngine:
    global event_broker
    if not event_broker:
        cfg = KafkaConfig()
        params: Dict[str, Any] = dict(
            loop=asyncio.get_event_loop(),
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
        kafka_producer = AIOKafkaProducer(**params)
        await kafka_producer.start()
        event_broker = KafkaProducerEngine(producer=kafka_producer)
    return event_broker
