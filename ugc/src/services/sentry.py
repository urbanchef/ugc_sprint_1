import logging
from typing import Any, Dict

import sentry_sdk
from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

logger = logging.getLogger(__name__)


def init(app: FastAPI) -> None:
    from ..core.config import SentryConfig

    sentry_cfg = SentryConfig()

    if sentry_cfg.dsn is None:
        logger.warning("Sentry is disabled")
        return

    params: Dict[str, Any] = {}

    if sentry_cfg.sample_rate is not None:
        params["sample_rate"] = sentry_cfg.sample_rate

    if sentry_cfg.traces_sample_rate is not None:
        params["traces_sample_rate"] = sentry_cfg.traces_sample_rate

    sentry_sdk.init(dsn=sentry_cfg.dsn.get_secret_value(), **params)
    app.add_middleware(SentryAsgiMiddleware)
    logger.warning("Sentry is configured")
