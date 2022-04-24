from ..schemas.base import OrjsonBaseModel


class MovieProgressMessage(OrjsonBaseModel):
    seconds_watched: int
