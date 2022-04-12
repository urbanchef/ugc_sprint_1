import logging
from datetime import datetime
from uuid import UUID

from aiokafka import AIOKafkaProducer
from fastapi import APIRouter, Depends
from starlette.requests import Request

from ...dependency import get_kafka_producer
from ...schemas import LikeMessage, MovieProgressMessage

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/movies/{movie_id}/view")
async def track_movie_progress(
    msg: MovieProgressMessage,
    movie_id: UUID,
    request: Request,
    aioproducer: AIOKafkaProducer = Depends(get_kafka_producer),
):
    """Track movie progress."""
    value = {
        "user_uuid": request.state.user_uuid,
        "movie_uuid": movie_id,
        "datetime": datetime.now(),
        "progress": msg.seconds_watched,
    }
    await aioproducer.send("views", value)
    return {"success": True}


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
