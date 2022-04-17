import logging
from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
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
    result = await like_service.send(value)
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Неудачная отправка события.",
        )
    return {
        "success": {
            "User UUID": request.state.user_uuid,
            "Movie UUID": movie_id,
            "Liked": msg.liked,
        }
    }
