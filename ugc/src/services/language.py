from general import GeneralService


class LanguageService(GeneralService):
    """Класс движка продюсера для брокера сообщений Kafka."""

    topic_name = "language"
