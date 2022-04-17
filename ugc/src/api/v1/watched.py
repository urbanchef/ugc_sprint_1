import logging
from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from starlette.requests import Request

from ...services.getters import get_watch_service
from ...services.watched import WatchService

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/movies/{movie_id}/watched")
async def watched_movies(
    movie_id: UUID,
    request: Request,
    watch_service: WatchService = Depends(get_watch_service),
):
    """Add viewed movie."""

    value = {
        "user_uuid": request.state.user_uuid,
        "watched_movie": movie_id,
    }
    result = await watch_service.send(value)
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Неудачная отправка события.",
        )
    return {
        "success": {
            "User UUID": request.state.user_uuid,
            "Movie UUID": movie_id,
        }
    }
