from abc import ABC, abstractmethod


class GeneralProducerEngine(ABC):
    """Класс абстрактного продюсера Kafka."""

    @abstractmethod
    def send(self, topic_name: str, message: dict):
        """Абстрактный метод отправки события в указанный топик."""
        pass
