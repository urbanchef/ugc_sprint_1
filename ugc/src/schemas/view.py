from pydantic import BaseModel


class MovieProgressMessage(BaseModel):
    seconds_watched: int


class LanguageMovie(BaseModel):
    language_movie: str
