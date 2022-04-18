from .general import GeneralService


class LanguageService(GeneralService):
    """Класс движка для отправки сообщений в соответствующий топик Kafka."""

    topic_name = "language"
