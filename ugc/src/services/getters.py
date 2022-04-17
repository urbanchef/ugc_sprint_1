from functools import lru_cache

from aiokafka import AIOKafkaProducer
from fastapi import Depends

from ..db.kafka import get_kafka_producer
from ..engines.message_broker.kafka import KafkaEngine
from .language import LanguageService


@lru_cache()
def get_language_service(
    producer: AIOKafkaProducer = Depends(get_kafka_producer),
) -> LanguageService:
    kafka_producer = KafkaEngine(producer)
    return LanguageService(kafka_producer)
