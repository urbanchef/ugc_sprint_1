from datetime import datetime as dt

from pydantic import BaseModel


class BookmarkMessage(BaseModel):
    """Represents a bookmark message."""

    bookmarked: bool = True
    datetime: dt = dt.now()
