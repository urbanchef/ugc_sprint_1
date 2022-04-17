import logging
from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from starlette.requests import Request

from ...schemas import LanguageMovie
from ...services.getters import get_language_service
from ...services.language import LanguageService

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/movies/{movie_id}/language")
async def language_movies(
    msg: LanguageMovie,
    movie_id: UUID,
    request: Request,
    language_service: LanguageService = Depends(get_language_service),
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
    result = await language_service.send(message=value)
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Неудачная отправка события.",
        )
    return {
        "success": {
            "User UUID": request.state.user_uuid,
            "Movie UUID": movie_id,
            "Movie language": language,
            "Client language": request.state.language,
        }
    }
