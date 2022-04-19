from functools import lru_cache

from aiokafka import AIOKafkaProducer
from fastapi import Depends

from ..db.kafka import get_kafka_producer
from ..engines.message_broker.kafka import KafkaProducerEngine
from . import BookmarkService, LanguageService, RatingService, ViewService, WatchService


@lru_cache()
def get_bookmark_service(
    producer: AIOKafkaProducer = Depends(get_kafka_producer),
) -> BookmarkService:
    kafka_producer = KafkaProducerEngine(producer)
    return BookmarkService(kafka_producer)


@lru_cache()
def get_language_service(
    producer: AIOKafkaProducer = Depends(get_kafka_producer),
) -> LanguageService:
    kafka_producer = KafkaProducerEngine(producer)
    return LanguageService(kafka_producer)


@lru_cache()
def get_rating_service(
    producer: AIOKafkaProducer = Depends(get_kafka_producer),
) -> RatingService:
    kafka_producer = KafkaProducerEngine(producer)
    return RatingService(kafka_producer)


@lru_cache()
def get_view_service(
    producer: AIOKafkaProducer = Depends(get_kafka_producer),
) -> ViewService:
    kafka_producer = KafkaProducerEngine(producer)
    return ViewService(kafka_producer)


@lru_cache()
def get_watch_service(
    producer: AIOKafkaProducer = Depends(get_kafka_producer),
) -> WatchService:
    kafka_producer = KafkaProducerEngine(producer)
    return WatchService(kafka_producer)
