import json
import logging
from uuid import UUID

from aiokafka import AIOKafkaProducer
from fastapi import APIRouter, Depends
from starlette.requests import Request

from ...dependency import get_kafka_producer
from ...schemas.producer import MovieProgressMessage, ProducerResponse, \
    LikeMessage

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/topics/{topic_name}/movies/{movie_id}/view")
async def track_movie_progress(
    msg: MovieProgressMessage,
    topic_name: str,
    movie_id: UUID,
    request: Request,
    aioproducer: AIOKafkaProducer = Depends(get_kafka_producer),
):
    kafka_key = f"{request.state.user_uuid}+{movie_id}"
    await aioproducer.send(
        topic=topic_name,
        key=kafka_key.encode(),
        value=str(msg.unix_timestamp_utc).encode(),
    )
    response = ProducerResponse(
        key=kafka_key, value=str(msg.unix_timestamp_utc), topic=topic_name
    )
    logger.info(response)

    return response


@router.post("/topics/{topic_name}/movies/{movie_id}/like")
async def process_like_message(
    msg: LikeMessage,
    topic_name: str,
    movie_id: UUID,
    request: Request,
    aioproducer: AIOKafkaProducer = Depends(get_kafka_producer),
):
    kafka_key = f"{request.state.user_uuid}+{movie_id}"
    await aioproducer.send(
        topic=topic_name,
        key=kafka_key.encode(),
        value=msg.json().encode(),
    )
    response = ProducerResponse(
        key=kafka_key, value=msg.dict(), topic=topic_name
    )
    logger.info(response)

    return response
