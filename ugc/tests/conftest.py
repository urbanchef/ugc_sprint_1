import asyncio
from dataclasses import dataclass
from typing import Union

import aiohttp
import pytest
from multidict import CIMultiDictProxy

from ugc.tests.settings import TestSettings

settings = TestSettings()


@dataclass
class HTTPResponse:
    body: Union[dict, str]
    headers: CIMultiDictProxy[str]
    status: int


@pytest.fixture(name="event_loop", scope="session")
def event_loop() -> asyncio.AbstractEventLoop:
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def http_client():
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@pytest.fixture
def make_get_request(http_client):
    async def inner(method: str, params: dict = None) -> HTTPResponse:
        params = params or {}
        url = f"{settings.service_url}/api/v1{method}"
        async with http_client.get(url, params=params) as response:
            try:
                body = await response.json()
            except aiohttp.ContentTypeError:
                body = await response.text()
            return HTTPResponse(
                body=body,
                headers=response.headers,
                status=response.status,
            )

    return inner


@pytest.fixture(scope="module")
def make_post_request(http_client):
    async def inner(
        method: str, data: dict = None, headers: dict = None
    ) -> HTTPResponse:
        data = data or {}
        url = f"{settings.service_url}/api/v1{method}"
        async with http_client.post(url, data=data, headers=headers) as response:
            return HTTPResponse(
                body=await response.json(),
                headers=response.headers,
                status=response.status,
            )

    return inner
