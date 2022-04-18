from datetime import datetime as dt

from ugc.src.schemas.base import OrjsonBaseModel


class RatingMessage(OrjsonBaseModel):
    rating: int
    datetime: dt = dt.now()
