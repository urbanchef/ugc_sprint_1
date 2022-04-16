from abc import ABC, abstractmethod


class MessageBrokerEngine(ABC):
    """Класс абстрактного брокера сообщений."""

    @abstractmethod
    async def send(self, topik_name: str, message: dict) -> None:
        """Отправляет событие в виде словаря в указанный топик."""
        pass
