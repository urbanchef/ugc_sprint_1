from http import HTTPStatus

import pytest

from ugc.src.schemas.producer import LikeMessage, MovieProgressMessage

pytestmark = pytest.mark.asyncio

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9." +
                     "eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0ODkzMDUzMSwian" +
                     "RpIjoiNTlkYjUzMzUtY2Q2Zi00Mjk4LTg3MDctZDFhZTE2Y" +
                     "WQzYTM3IiwidHlwZSI6ImFjY2VzcyIsInVzZXJfdXVpZCI6I" +
                     "jY4ZWZlYzBkLTZiMzktNDU1ZC1hNDFjLTU4NDljMDI2OTU0Yi" +
                     "IsIm5iZiI6MTY0ODkzMDUzMSwiZXhwIjoxNzQzNTM4NTMxLCJ" +
                     "yZWZyZXNoX3V1aWQiOiJiNGMwM2E5My0xOTg1LTQ2N2YtYTNl" +
                     "MC01NTliMjJlZDNmODkiLCJ1c2VybmFtZSI6IlRlc3RfVXNlc" +
                     "iIsImVtYWlsIjoidXNlckBtYWlsLmNvbSIsImlzX3N1cGVydXN" +
                     "lciI6ZmFsc2UsImNyZWF0ZWRfYXQiOiIyMDIyLTA0LTAyVDIwO" +
                     "jAxOjM1LjQ4MjU3MCIsInJvbGVzIjpbInN1YnNjcmliZXIiXX0." +
                     "qvItA7hrVd1KPyJKWR_MqTYNL2cPK3ZuPuBdCVZLae0"
}

async def test_track_movie_progress(make_post_request):
    movie_id = "d50728e2-4f3e-4070-a5ba-6c3de400a9a4"
    topic_name = "views"
    data = MovieProgressMessage(unix_timestamp_utc=1649006765)
    response = await make_post_request(
        f"/topics/{topic_name}/movies/{movie_id}/view", headers=headers, data=data.json()
    )
    assert response.status == HTTPStatus.OK
    assert response.body == {
        "key": f"68efec0d-6b39-455d-a41c-5849c026954b+{movie_id}",
        "value": "1649006765",
        "topic": "views",
    }


async def test_process_like_message(make_post_request):
    movie_id = "d50728e2-4f3e-4070-a5ba-6c3de400a9a4"
    topic_name = "likes"
    data = LikeMessage(liked=True)
    response = await make_post_request(
        f"/topics/{topic_name}/movies/{movie_id}/like", headers=headers, data=data.json()
    )
    assert response.status == HTTPStatus.OK
