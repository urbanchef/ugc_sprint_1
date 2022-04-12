from datetime import datetime as dt

from pydantic import BaseModel


class LikeMessage(BaseModel):
    liked: bool
    datetime: dt = dt.now()
