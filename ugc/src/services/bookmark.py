from .general import GeneralService


class BookmarkService(GeneralService):
    """Класс движка для отправки сообщений в соответствующий топик Kafka."""

    topic_name = "bookmarks"
