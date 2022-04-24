from functools import lru_cache

from fastapi import Depends

from ..db.kafka import get_event_broker
from ..engines.message_broker.kafka import KafkaProducerEngine
from . import BookmarkService, LanguageService, RatingService, ViewService, WatchService


@lru_cache()
def get_bookmark_service(
    producer: KafkaProducerEngine = Depends(get_event_broker),
) -> BookmarkService:
    return BookmarkService(producer)


@lru_cache()
def get_language_service(
    producer: KafkaProducerEngine = Depends(get_event_broker),
) -> LanguageService:
    return LanguageService(producer)


@lru_cache()
def get_rating_service(
    producer: KafkaProducerEngine = Depends(get_event_broker),
) -> RatingService:
    return RatingService(producer)


@lru_cache()
def get_view_service(
    producer: KafkaProducerEngine = Depends(get_event_broker),
) -> ViewService:
    return ViewService(producer)


@lru_cache()
def get_watch_service(
    producer: KafkaProducerEngine = Depends(get_event_broker),
) -> WatchService:
    return WatchService(producer)
