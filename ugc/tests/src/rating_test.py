import logging
from http import HTTPStatus
from random import randint

import pytest

from ugc.src.schemas import RatingMessage

from ..testdata import HEADERS, MOVIE_ID

pytestmark = pytest.mark.asyncio
logger = logging.getLogger(__name__)


class TestMovieRating:
    """Represents movie like event related tests."""

    url = f"/movies/{MOVIE_ID}/rating"

    async def test_success(self, make_post_request):
        """Test success case."""
        data = RatingMessage(rating=randint(0, 10))
        response = await make_post_request(
            self.url,
            headers=HEADERS,
            data=data.json(),
        )
        logger.debug("Response: %s %s", response.status, response)
        assert response.status == HTTPStatus.OK
