from datetime import datetime as dt

from pydantic import BaseModel


class LanguageMovie(BaseModel):
    language_movie: str
    datetime: dt = dt.now()
