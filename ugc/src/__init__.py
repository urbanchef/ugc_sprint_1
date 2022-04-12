from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse
from jose import JWTError, jwt

from . import api
from .core.config import ProjectConfig
from .dependency import get_jwt_settings, get_kafka_producer

project_cfg = ProjectConfig()
app = FastAPI(
    title=project_cfg.name,
    description=project_cfg.description,
    docs_url=project_cfg.docs_url,
    openapi_url=project_cfg.openapi_url,
    default_response_class=ORJSONResponse,
)


@app.middleware("http")
async def jwt_handler(request: Request, call_next):
    """Middleware для соотнесения каждого запроса с конкретным пользователем.
    Парсит JWT токен из Authorization заголовка вынимая UUID пользователя.
    Пример payload:
        {
          "fresh": false,
          "iat": 1647788608,
          "jti": "b601df71-6452-4374-b580-64dab8574870",
          "type": "access",
          "user_uuid": "f75e4328-de43-46ca-bb44-52db4b487262",
          "nbf": 1647788608,
          "exp": 1647789508,
          "refresh_uuid": "c2a3accf-51fd-44ff-aeb4-272ca03fa2ac",
          "username": "admin",
          "email": "admin@email.com",
          "is_superuser": true,
          "created_at": "2022-03-20T15:03:18.380452",
          "roles": []
        }
    """

    jwt_cfg = get_jwt_settings()
    user_uuid: dict = {}
    token_status = "None"

    auth_header = request.headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        token_status = "OK"
        jwt_token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(
                jwt_token, jwt_cfg.secret_key, algorithms=[jwt_cfg.algorithms]
            )
            user_uuid = payload.get("user_uuid", {})
        except JWTError as e:
            token_status = f"Error: {e}"

    request.state.user_uuid = user_uuid
    response = await call_next(request)
    response.headers["X-Token-Status"] = token_status
    return response


@app.on_event("startup")
async def startup_event():
    producer = get_kafka_producer()
    await producer.start()


@app.on_event("shutdown")
async def shutdown_event():
    producer = get_kafka_producer()
    await producer.stop()


app.include_router(api.router)
