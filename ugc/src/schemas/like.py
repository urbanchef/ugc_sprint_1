from ..schemas.base import OrjsonBaseModel


class LikeMessage(OrjsonBaseModel):
    liked: bool
