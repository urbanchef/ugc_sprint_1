from abc import ABC, abstractmethod


class MessageProducerEngine(ABC):
    """Класс абстрактного продюсера Kafka."""

    @abstractmethod
    async def send(self, topik_name: str, message: dict) -> None:
        """Абстрактный метод отправки события в указанный топик."""
        pass
