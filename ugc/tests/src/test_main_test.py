from http import HTTPStatus

from fastapi.testclient import TestClient

from ugc.src import app

client = TestClient(app)


def test_track_movie_progress():
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.\
        eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0ODkzMDUzMSwianRpIjoiNTlkYjUzMzUtY\
        2Q2Zi00Mjk4LTg3MDctZDFhZTE2YWQzYTM3IiwidHlwZSI6ImFjY2VzcyIsInVzZXJ\
        fdXVpZCI6IjY4ZWZlYzBkLTZiMzktNDU1ZC1hNDFjLTU4NDljMDI2OTU0YiIsIm5iZi\
        I6MTY0ODkzMDUzMSwiZXhwIjoxNzQzNTM4NTMxLCJyZWZyZXNoX3V1aWQiOiJiNGMwM2\
        E5My0xOTg1LTQ2N2YtYTNlMC01NTliMjJlZDNmODkiLCJ1c2VybmFtZSI6IlRlc3RfVX\
        NlciIsImVtYWlsIjoidXNlckBtYWlsLmNvbSIsImlzX3N1cGVydXNlciI6ZmFsc2UsIm\
        NyZWF0ZWRfYXQiOiIyMDIyLTA0LTAyVDIwOjAxOjM1LjQ4MjU3MCIsInJvbGVzIjpbIn\
        N1YnNjcmliZXIiXX0.qvItA7hrVd1KPyJKWR_MqTYNL2cPK3ZuPuBdCVZLae0"
    }
    movie_id = "d50728e2-4f3e-4070-a5ba-6c3de400a9a4"
    topic_name = "views"
    json = {"unix_timestamp_utc": 1649006765}
    response = client.post(
        f"/api/v1/producer/{topic_name}/{movie_id}", headers=headers, json=json
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "key": f"68efec0d-6b39-455d-a41c-5849c026954b+{movie_id}",
        "value": "1649006765",
        "topic": "views",
    }
