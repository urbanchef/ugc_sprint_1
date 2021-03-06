from http import HTTPStatus

import pytest

from ...src.schemas import LanguageMovie
from ..testdata import HEADERS, MOVIE_ID

pytestmark = pytest.mark.asyncio


class TestLanguageMovie:
    """Presents a test of adding a movie language."""

    url = f"/movies/{MOVIE_ID}/watched"

    async def test_success(self, make_post_request):
        """Test success case."""
        data = LanguageMovie(language_movie="Ru-ru")
        response = await make_post_request(
            self.url,
            headers=HEADERS,
            data=data.json(),
        )
        assert response.status == HTTPStatus.OK
