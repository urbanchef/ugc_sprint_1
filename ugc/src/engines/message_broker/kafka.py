from aiokafka import AIOKafkaProducer

from .general import MessageProducerEngine


class KafkaProducerEngine(MessageProducerEngine):
    """Класс брокера сообщений Apache Kafka."""

    def __init__(self, producer: AIOKafkaProducer):
        self.producer = producer

    async def send(self, topic_name: str, message: dict):
        await self.producer.send(topic_name, message)
