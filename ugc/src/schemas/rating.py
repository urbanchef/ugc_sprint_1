from ..schemas.base import OrjsonBaseModel


class RatingMessage(OrjsonBaseModel):
    rating: int
