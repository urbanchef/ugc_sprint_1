from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from .api.v1 import event
from .core.config import ProjectConfig
from .dependency import get_kafka_producer
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
    producer = get_kafka_producer()
    await producer.start()


@app.on_event("shutdown")
async def shutdown_event():
    producer = get_kafka_producer()
    await producer.stop()


app.include_router(event.router, prefix="/api/v1", tags=["events"])
