from abc import ABCMeta, abstractmethod

from ..engines.message_broker.general import MessageProducerEngine


class GeneralService(metaclass=ABCMeta):
    def __init__(self, producer: MessageProducerEngine):
        self.producer = producer

    @property
    @abstractmethod
    def topic_name(self):
        """Индекс или таблица в поисковом движке."""
        pass

    async def send(self, message: dict):
        await self.producer.send(
            topik_name=self.topic_name,
            message=message,
        )
