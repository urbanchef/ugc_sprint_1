from aiokafka import AIOKafkaProducer
from general import MessageBrokerEngine


class KafkaEngine(MessageBrokerEngine):
    """Класс брокера сообщений Apache Kafka."""

    def __init__(self, producer: AIOKafkaProducer):
        self.producer = producer

    def send(self, topik_name: str, message: dict) -> None:
        pass
