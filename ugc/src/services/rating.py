from .general import GeneralService


class RatingService(GeneralService):
    """Класс движка для отправки сообщений в соответствующий топик Kafka."""

    topic_name = "ratings"
