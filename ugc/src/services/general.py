from abc import ABCMeta, abstractmethod

from ..engines.message_broker.kafka import KafkaProducerEngine


class GeneralService(metaclass=ABCMeta):
    """Базовый сервис."""

    def __init__(self, producer: KafkaProducerEngine):
        self.producer = producer

    @property
    @abstractmethod
    def topic_name(self):
        """Индекс или таблица в поисковом движке."""
        pass

    async def send(self, message: dict):
        await self.producer.send(self.topic_name, message)
