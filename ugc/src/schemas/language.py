from datetime import datetime as dt

from ..schemas.base import OrjsonBaseModel


class LanguageMovie(OrjsonBaseModel):
    language_movie: str
    datetime: dt = dt.now()
