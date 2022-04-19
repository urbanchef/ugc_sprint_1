from datetime import datetime as dt

from ..schemas.base import OrjsonBaseModel


class LikeMessage(OrjsonBaseModel):
    liked: bool
    datetime: dt = dt.now()
