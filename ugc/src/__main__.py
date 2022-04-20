import asyncio
import logging
import socket
from typing import List, Optional

# from aiokafka.util import get_running_loop
from uvicorn import Config, Server

from ugc.src import app

from .core.logger import LOGGING


class ProActorServer(Server):
    def run(self, sockets: Optional[List[socket.socket]] = None) -> None:
        custom_loop = asyncio.get_event_loop()
        # custom_loop = get_running_loop()
        asyncio.set_event_loop(custom_loop)
        asyncio.run(self.serve(sockets=sockets))


config = Config(
    app=app,
    host="0.0.0.0",
    port=8000,
    log_config=LOGGING,
    log_level=logging.DEBUG,
    reload=True,
)
server = ProActorServer(config=config)
server.run()
