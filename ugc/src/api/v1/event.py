import logging
from datetime import datetime
from uuid import UUID

from aiokafka import AIOKafkaProducer
from fastapi import APIRouter, Depends
from starlette.requests import Request

from ...dependency import get_kafka_producer
from ...schemas.producer import LikeMessage, MovieProgressMessage, ProducerResponse

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


@router.post("/movies/{movie_id}/like")
async def process_like_message(
    msg: LikeMessage,
    movie_id: UUID,
    request: Request,
    aioproducer: AIOKafkaProducer = Depends(get_kafka_producer),
):
    """Like a movie."""
    value = {
        "user_uuid": request.state.user_uuid,
        "movie_uuid": movie_id,
        "datetime": datetime.now(),
        "liked": msg.liked,
    }
    await aioproducer.send("likes", value)
    return {"success": True}
