from datetime import datetime as dt

from ugc.src.schemas.base import OrjsonBaseModel


class MovieProgressMessage(OrjsonBaseModel):
    seconds_watched: int
    datetime: dt = dt.now()
