import logging
from http import HTTPStatus

import pytest

from ugc.src.schemas import LikeMessage

from ..testdata import HEADERS, MOVIE_ID

pytestmark = pytest.mark.asyncio
logger = logging.getLogger(__name__)


class TestMovieLike:
    """Represents movie like event related tests."""

    url = f"/movies/{MOVIE_ID}/like"

    async def test_success(self, make_post_request):
        """Test success case."""
        data = LikeMessage(liked=True)
        response = await make_post_request(
            self.url,
            headers=HEADERS,
            data=data.json(),
        )
        logger.debug("Response: %s %s", response.status, response)
        assert response.status == HTTPStatus.OK
