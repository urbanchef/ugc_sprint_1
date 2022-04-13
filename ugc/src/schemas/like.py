from datetime import datetime as dt

from ugc.src.schemas.base import OrjsonBaseModel


class LikeMessage(OrjsonBaseModel):
    liked: bool
    datetime: dt = dt.now()
