import asyncio
import logging

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from . import api

from .core.config import ProjectConfig
from .db.kafka import get_event_broker
from .engines.message_broker.kafka import KafkaProducerEngine
from .middleware.handlers_headers import jwt_handler, language_handler
from .services import sentry

logger = logging.getLogger(__name__)


project_cfg = ProjectConfig()
app = FastAPI(
    title=project_cfg.name,
    description=project_cfg.description,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)

app.middleware("http")(jwt_handler)
app.middleware("http")(language_handler)


@app.on_event("startup")
async def startup():
    sentry.init(app)
    await asyncio.gather(
        get_event_broker(),
    )


@app.on_event("shutdown")
async def shutdown():
    event_broker: KafkaProducerEngine = get_event_broker()  # type: ignore
    await asyncio.gather(event_broker.producer.stop())


app.include_router(api.router)
