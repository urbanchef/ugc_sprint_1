from pydantic import BaseModel


class LikeMessage(BaseModel):
    liked: bool
