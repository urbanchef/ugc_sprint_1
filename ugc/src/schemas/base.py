import orjson
from pydantic import BaseModel

from ..core.utils import orjson_dumps


class OrjsonBaseModel(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
