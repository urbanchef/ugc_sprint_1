from http import HTTPStatus

import pytest

from ugc.src.schemas import LikeMessage, MovieProgressMessage

from ..testdata import MOVIE_ID, SECONDS_WATCHED

pytestmark = pytest.mark.asyncio

headers = {
    "Content-Type": "application/json",
    "Authorization": (
        "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
        ".eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0ODkzMDUzMSwianRpIjoiNTlkYjUzMzUtY2Q2Zi00Mjk4L"
        "Tg3MDctZDFhZTE2YWQzYTM3IiwidHlwZSI6ImFjY2VzcyIsInVzZXJfdXVpZCI6IjY4ZWZlYzBkLTZ"
        "iMzktNDU1ZC1hNDFjLTU4NDljMDI2OTU0YiIsIm5iZiI6MTY0ODkzMDUzMSwiZXhwIjoxNzQzNTM4N"
        "TMxLCJyZWZyZXNoX3V1aWQiOiJiNGMwM2E5My0xOTg1LTQ2N2YtYTNlMC01NTliMjJlZDNmODkiLCJ"
        "1c2VybmFtZSI6IlRlc3RfVXNlciIsImVtYWlsIjoidXNlckBtYWlsLmNvbSIsImlzX3N1cGVydXNlc"
        "iI6ZmFsc2UsImNyZWF0ZWRfYXQiOiIyMDIyLTA0LTAyVDIwOjAxOjM1LjQ4MjU3MCIsInJvbGVzIjp"
        "bInN1YnNjcmliZXIiXX0.qvItA7hrVd1KPyJKWR_MqTYNL2cPK3ZuPuBdCVZLae0"
    ),
}


async def test_track_movie_progress(make_post_request):
    data = MovieProgressMessage(seconds_watched=SECONDS_WATCHED)
    response = await make_post_request(
        f"/movies/{MOVIE_ID}/view",
        headers=headers,
        data=data.json(),
    )
    assert response.status == HTTPStatus.OK


async def test_process_like_message(make_post_request):
    data = LikeMessage(liked=True)
    response = await make_post_request(
        f"/movies/{MOVIE_ID}/like",
        headers=headers,
        data=data.json(),
    )
    assert response.status == HTTPStatus.OK
