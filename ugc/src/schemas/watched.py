from ugc.src.schemas.base import OrjsonBaseModel


class WatchedMessage(OrjsonBaseModel):
    added: bool = True
