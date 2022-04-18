import asyncio

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from . import api
from .core.config import ProjectConfig
from .db.kafka import kafka_producer_connect, kafka_producer_disconnect
from .middleware.handlers_headers import jwt_handler, language_handler

project_cfg = ProjectConfig()
app = FastAPI(
    title=project_cfg.name,
    description=project_cfg.description,
    docs_url=project_cfg.docs_url,
    openapi_url=project_cfg.openapi_url,
    default_response_class=ORJSONResponse,
)

app.middleware("http")(jwt_handler)
app.middleware("http")(language_handler)


@app.on_event("startup")
async def startup_event():
    await asyncio.gather(
        kafka_producer_connect(),
    )


@app.on_event("shutdown")
async def shutdown_event():
    await asyncio.gather(
        kafka_producer_disconnect(),
    )


app.include_router(api.router)
