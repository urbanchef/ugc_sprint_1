import asyncio

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from ugc.src import api

from .core.config import ProjectConfig
from .db.kafka import kafka_producer_connect, kafka_producer_disconnect
from .middleware.handlers_headers import jwt_handler, language_handler

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
