from datetime import datetime as dt

import orjson
from pydantic import BaseModel, Field

from ..core.utils import orjson_dumps


class OrjsonBaseModel(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps

    datetime: dt = Field(default_factory=dt.now)
