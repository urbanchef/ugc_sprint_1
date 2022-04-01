import logging

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse
from jose import JWTError, jwt

from api.v1 import event
from core import config
from core.config import jwt_secret_key, jwt_algorithms
from core.logger import LOGGING
from dependency import get_kafka_producer

app = FastAPI(
    title=config.PROJECT_NAME,
    description=config.PROJECT_DESCRIPTION,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.middleware("http")
async def jwt_handler(request: Request, call_next):
    user_uuid = {}
    token_status = "None"

    auth_header = request.headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        token_status = "OK"
        jwt_token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(jwt_token, jwt_secret_key, algorithms=jwt_algorithms)
            user_uuid = set(payload.get("user_uuid", {}))
        except JWTError as e:
            token_status = f"Error: {e}"

    request.state.user_uuid = user_uuid
    response = await call_next(request)
    response.headers["X-Token-Status"] = token_status
    return response


@app.on_event("startup")
async def startup_event():
    aioproducer = get_kafka_producer()
    await aioproducer.start()


@app.on_event("shutdown")
async def shutdown_event():
    aioproducer = get_kafka_producer()
    await aioproducer.stop()


app.include_router(event.router, prefix="/api/v1", tags=["events"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
