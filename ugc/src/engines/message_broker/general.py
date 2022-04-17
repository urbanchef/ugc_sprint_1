from abc import ABC, abstractmethod

from aiokafka import AIOKafkaProducer


class MessageProducerEngine(ABC):
    """Класс абстрактного продюсера Kafka."""

    def __init__(self, message_producer: AIOKafkaProducer):
        self.message_broker = message_producer

    @abstractmethod
    async def send(self, topik_name: str, message: dict) -> None:
        """Отправляет событие в виде словаря в указанный топик."""

        pass
