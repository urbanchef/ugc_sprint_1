import logging
from datetime import datetime
from uuid import UUID

from aiokafka import AIOKafkaProducer
from fastapi import APIRouter, Depends
from starlette.requests import Request

from ...dependency import get_kafka_producer
from ...schemas import BookmarkMessage, LanguageMovie, LikeMessage, MovieProgressMessage

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
    return {
        "success": {
            "User UUID": request.state.user_uuid,
            "Movie UUID": movie_id,
            "Progress": msg.seconds_watched,
        }
    }


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
    return {
        "success": {
            "User UUID": request.state.user_uuid,
            "Movie UUID": movie_id,
            "Liked": msg.liked,
        }
    }


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
    return {
        "success": {
            "User UUID": request.state.user_uuid,
            "Movie UUID": movie_id,
            "Bookmarked": msg.bookmarked,
        }
    }


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
        "language_client": request.state.language,
        "datetime": msg.datetime,
    }
    await aioproducer.send("language", value)
    return {
        "success": {
            "User UUID": request.state.user_uuid,
            "Movie UUID": movie_id,
            "Movie language": language,
            "Client language": request.state.language,
        }
    }


@router.post("/movies/{movie_id}/watched")
async def watched_movies(
    movie_id: UUID,
    request: Request,
    aioproducer: AIOKafkaProducer = Depends(get_kafka_producer),
):
    """Add viewed movie."""

    value = {
        "user_uuid": request.state.user_uuid,
        "watched_movie": movie_id,
    }
    await aioproducer.send("watched", value)
    return {
        "success": {
            "User UUID": request.state.user_uuid,
            "Movie UUID": movie_id,
        }
    }
