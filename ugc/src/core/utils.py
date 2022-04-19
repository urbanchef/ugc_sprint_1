from functools import lru_cache

import orjson

from .config import JWTConfig


@lru_cache()
def get_jwt_settings() -> JWTConfig:
    return JWTConfig()


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()
