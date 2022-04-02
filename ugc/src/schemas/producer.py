from pydantic import BaseModel, StrictStr


class ProducerMessage(BaseModel):
    key: StrictStr
    value: StrictStr


class ProducerResponse(BaseModel):
    key: StrictStr
    value: StrictStr
    topic: StrictStr
