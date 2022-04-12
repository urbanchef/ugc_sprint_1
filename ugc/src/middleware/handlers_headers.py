from fastapi import Request
from jose import JWTError, jwt

from ugc.src.core.utils import get_jwt_settings


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


async def language_handler(request: Request, call_next):

    lang_header = request.headers.get("Accept-Language", "")
    language = lang_header.split(";")[0].split(",")[0]
    request.state.language = language
    response = await call_next(request)
    response.headers["Language"] = language
    return response
