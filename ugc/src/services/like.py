from .general import GeneralService


class LikeService(GeneralService):
    """Класс движка для отправки сообщений в соответствующий топик Kafka."""

    topic_name = "likes"
