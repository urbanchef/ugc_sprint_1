import logging
from abc import ABCMeta, abstractmethod

from aiokafka.errors import KafkaError

from ..engines.message_broker.kafka import KafkaProducerEngine

logger = logging.getLogger(__name__)


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
        try:
            await self.producer.send(self.topic_name, message)
        except KafkaError as e:
            logger.info(f"Kafka GeneralService error: {e}")
