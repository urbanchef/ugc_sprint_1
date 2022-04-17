import logging
from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from starlette.requests import Request

from ...schemas import MovieProgressMessage
from ...services.getters import get_view_service
from ...services.view import ViewService

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/movies/{movie_id}/view")
async def track_movie_progress(
    msg: MovieProgressMessage,
    movie_id: UUID,
    request: Request,
    view_service: ViewService = Depends(get_view_service),
):
    """Track movie progress."""
    value = {
        "user_uuid": request.state.user_uuid,
        "movie_uuid": movie_id,
        "datetime": msg.datetime,
        "progress": msg.seconds_watched,
    }
    result = await view_service.send(value)
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Неудачная отправка события.",
        )
    return {
        "success": {
            "User UUID": request.state.user_uuid,
            "Movie UUID": movie_id,
            "Progress": msg.seconds_watched,
        }
    }
