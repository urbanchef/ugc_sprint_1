from pydantic import BaseModel, StrictStr


class ProducerMessage(BaseModel):
    key: StrictStr
    value: StrictStr


class ProducerResponse(BaseModel):
    key: StrictStr
    value: StrictStr
    topic: StrictStr


class MovieProgressMessage(BaseModel):
    unix_timestamp_utc: int
