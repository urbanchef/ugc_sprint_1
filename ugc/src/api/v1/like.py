import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from starlette.requests import Request

from ...schemas import LikeMessage
from ...services.getters import get_like_service
from ...services.like import LikeService

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/movies/{movie_id}/like")
async def process_like_message(
    msg: LikeMessage,
    movie_id: UUID,
    request: Request,
    like_service: LikeService = Depends(get_like_service),
):
    """Like a movie."""
    value = {
        "user_uuid": request.state.user_uuid,
        "movie_uuid": movie_id,
        "datetime": msg.datetime,
        "liked": msg.liked,
    }
    await like_service.send(value)
    return {
        "success": {
            "User UUID": request.state.user_uuid,
            "Movie UUID": movie_id,
            "Liked": msg.liked,
        }
    }
