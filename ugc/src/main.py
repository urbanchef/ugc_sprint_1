import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from .api.v1 import event
from .core.config import ProjectConfig
from .core.logger import LOGGING
from .dependency import get_kafka_producer

project_cfg = ProjectConfig()
app = FastAPI(
    title=project_cfg.name,
    description=project_cfg.description,
    docs_url=project_cfg.docs_url,
    openapi_url=project_cfg.openapi_url,
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
async def startup_event():
    aioproducer = get_kafka_producer()
    await aioproducer.start()


@app.on_event("shutdown")
async def shutdown_event():
    aioproducer = get_kafka_producer()
    await aioproducer.stop()


app.include_router(event.router, prefix='/api/v1', tags=['events'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
