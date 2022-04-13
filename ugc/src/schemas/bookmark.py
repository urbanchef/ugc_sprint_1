from datetime import datetime as dt

from ugc.src.schemas.base import OrjsonBaseModel


class BookmarkMessage(OrjsonBaseModel):
    """Represents a bookmark message."""

    bookmarked: bool = True
    datetime: dt = dt.now()
