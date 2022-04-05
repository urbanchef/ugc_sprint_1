from typing import Union, Dict

from pydantic import BaseModel, StrictStr


class ProducerResponse(BaseModel):
    key: StrictStr
    value: Union[StrictStr, Dict]
    topic: StrictStr


class MovieProgressMessage(BaseModel):
    unix_timestamp_utc: int


class LikeMessage(BaseModel):
    liked: bool
