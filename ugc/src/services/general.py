from abc import ABCMeta

from ..engines.message_broker.general import MessageBrokerEngine


class GeneralService(metaclass=ABCMeta):
    def __init__(self, message_broker: MessageBrokerEngine):
        self.message_broker = message_broker

    async def send(self, topik_name: str, message: dict):
        pass
