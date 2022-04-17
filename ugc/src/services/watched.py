from .general import GeneralService


class WatchService(GeneralService):
    """Класс движка для отправки сообщений в соответствующий топик Kafka."""

    topic_name = "watched"
