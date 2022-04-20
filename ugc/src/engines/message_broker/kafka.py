import logging

from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaError

from .general import GeneralProducerEngine

logger = logging.getLogger(__name__)


class KafkaProducerEngine(GeneralProducerEngine):
    """Класс брокера сообщений Apache Kafka."""

    def __init__(self, producer: AIOKafkaProducer):
        self.producer = producer

    async def send(self, topic_name: str, message: dict):
        try:
            await self.producer.send(topic_name, message)
        except KafkaError as e:
            logger.info(f"Неудачная отправка события: {e}")
