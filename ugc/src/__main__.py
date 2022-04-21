import logging

import uvicorn

from ugc.src import app

from .core.logger import LOGGING

uvicorn.run(
    app,  # type: ignore
    host="0.0.0.0",
    port=8000,
    log_config=LOGGING,
    log_level=logging.DEBUG,
)
