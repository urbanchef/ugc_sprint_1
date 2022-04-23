import logging
from http import HTTPStatus

import pytest

from ...src.schemas import BookmarkMessage
from ..testdata import HEADERS, MOVIE_ID

pytestmark = pytest.mark.asyncio
logger = logging.getLogger(__name__)


class TestBookmarks:
    """Represents all bookmarks related tests."""

    url = f"/movies/{MOVIE_ID}/bookmark"

    async def test_success(self, make_post_request):
        """Test success response."""
        data = BookmarkMessage()
        response = await make_post_request(
            self.url,
            headers=HEADERS,
            data=data.json(),
        )
        logger.debug("Response: %s %s", response.status, response)
        assert response.status == HTTPStatus.OK
