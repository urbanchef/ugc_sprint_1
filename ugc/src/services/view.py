from .general import GeneralService


class ViewService(GeneralService):
    """Класс движка для отправки сообщений в соответствующий топик Kafka."""

    topic_name = "views"
