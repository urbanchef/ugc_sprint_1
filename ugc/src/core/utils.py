from functools import lru_cache

from ..core.config import JWTConfig


@lru_cache()
def get_jwt_settings() -> JWTConfig:
    return JWTConfig()
