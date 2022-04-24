from ..schemas.base import OrjsonBaseModel


class WatchedMessage(OrjsonBaseModel):
    added: bool = True
