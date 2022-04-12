from http import HTTPStatus

import pytest

from ugc.src.schemas import BookmarkMessage

from ..testdata import HEADERS, MOVIE_ID

pytestmark = pytest.mark.asyncio


class TestBookmarks:
    """Represents all bookmarks related tests."""

    url = f"/movies/{MOVIE_ID}/view"

    async def test_success(self, make_post_request):
        """Test success response."""
        data = BookmarkMessage()
        response = await make_post_request(
            self.url,
            headers=HEADERS,
            data=data.json(),
        )
        assert response.status == HTTPStatus.OK
