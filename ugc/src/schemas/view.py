from pydantic import BaseModel


class MovieProgressMessage(BaseModel):
    seconds_watched: int
