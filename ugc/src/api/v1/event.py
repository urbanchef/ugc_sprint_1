import logging
from datetime import datetime
from uuid import UUID

from aiokafka import AIOKafkaProducer
from fastapi import APIRouter, Depends
from starlette.requests import Request

from ...dependency import get_kafka_producer
from ...schemas import BookmarkMessage, LikeMessage, MovieProgressMessage
from ...schemas import LanguageMovie, LikeMessage, MovieProgressMessage

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


@router.post("/movies/{movie_id}/bookmark")
async def bookmark_movie(
    msg: BookmarkMessage,
    movie_id: UUID,
    request: Request,
    aioproducer: AIOKafkaProducer = Depends(get_kafka_producer),
):
    """Receive event with the movie bookmark data."""
    value = {
        "user_uuid": request.state.user_uuid,
        "movie_uuid": movie_id,
        "datetime": msg.datetime,
        "bookmarked": msg.bookmarked,
    }
    await aioproducer.send("bookmarks", value)
    return {"success": True}


@router.post("/movies/{movie_id}/language")
async def language_movies(
    msg: LanguageMovie,
    movie_id: UUID,
    request: Request,
    aioproducer: AIOKafkaProducer = Depends(get_kafka_producer),
):
    """Add language movie."""
    language = msg.language_movie
    value = {
        "user_uuid": request.state.user_uuid,
        "movie_id": movie_id,
        "language_movie": language,
    }
    await aioproducer.send("views", value)
    return {"success": f"{language} language added for the movie with UUID {movie_id}."}


@router.post("/movies/{movie_id}/viewed")
async def viewed_movies(
    movie_id: UUID,
    request: Request,
    aioproducer: AIOKafkaProducer = Depends(get_kafka_producer),
):
    """Add viewed movie."""

    value = {
        "user_uuid": request.state.user_uuid,
        "viewed_movie": movie_id,
    }
    await aioproducer.send("views", value)
    return {"success": f"Movie with UUID {movie_id} has been added."}
