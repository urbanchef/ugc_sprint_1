from http import HTTPStatus

import pytest

from ugc.src.schemas import WatchedMessage

from ..testdata import HEADERS, MOVIE_ID

pytestmark = pytest.mark.asyncio


class TestWatchedMovie:
    """Represents a test of adding a movie to the viewed ones."""

    url = f"/movies/{MOVIE_ID}/watched"

    async def test_success(self, make_post_request):
        """Test success case."""
        data = WatchedMessage()
        response = await make_post_request(
            self.url,
            headers=HEADERS,
            data=data.json(),
        )
        assert response.status == HTTPStatus.OK
