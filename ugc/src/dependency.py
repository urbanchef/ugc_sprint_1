import asyncio
from functools import lru_cache

from aiokafka import AIOKafkaProducer

from core import config


@lru_cache()
def get_kafka_producer() -> AIOKafkaProducer:
    loop = asyncio.get_event_loop()
    aioproducer = AIOKafkaProducer(
        loop=loop, bootstrap_servers=f'{config.KAFKA_HOST}:{config.KAFKA_PORT}'
    )

    return aioproducer
