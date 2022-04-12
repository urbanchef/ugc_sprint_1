from datetime import datetime as dt

from pydantic import BaseModel


class MovieProgressMessage(BaseModel):
    seconds_watched: int
    datetime: dt = dt.now()
