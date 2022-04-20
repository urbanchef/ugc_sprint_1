import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from starlette.requests import Request

from ...schemas.bookmark import BookmarkMessage
from ...services import BookmarkService
from ...services.getters import get_bookmark_service

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/movies/{movie_id}/bookmark")
async def bookmark_movie(
    msg: BookmarkMessage,
    movie_id: UUID,
    request: Request,
    bookmark_service: BookmarkService = Depends(get_bookmark_service),
):
    """Receive event with the movie bookmark data."""
    value = {
        "user_uuid": request.state.user_uuid,
        "movie_uuid": movie_id,
        "datetime": msg.datetime,
        "bookmarked": msg.bookmarked,
    }
    await bookmark_service.send(value)
    return {
        "success": {
            "User UUID": request.state.user_uuid,
            "Movie UUID": movie_id,
            "Bookmarked": msg.bookmarked,
        }
    }
