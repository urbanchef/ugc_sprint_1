from datetime import datetime as dt

from ugc.src.schemas.base import OrjsonBaseModel


class RatingMessage(OrjsonBaseModel):
    rating: int
    # TODO: datetime реализовать через фабрику Field(default_factory=dt.now)
    datetime: dt = dt.now()
