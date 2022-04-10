import asyncio
import ssl

from aiokafka import AIOKafkaConsumer

from ugc.src.core.config import KafkaConfig


async def consume():
    cfg = KafkaConfig()
    consumer = AIOKafkaConsumer(
        "likes",
        bootstrap_servers=cfg.bootstrap_servers,
        security_protocol=cfg.security_protocol,
        sasl_mechanism=cfg.sasl_mechanism,
        auto_offset_reset="earliest",
        sasl_plain_username=cfg.sasl_plain_username,
        sasl_plain_password=cfg.sasl_plain_password.get_secret_value(),
        ssl_context=ssl.create_default_context(cafile=cfg.ssl_cafile),
        group_id="1",
    )
    await consumer.start()
    try:
        while msg := await consumer.getone():
            print(msg.value)
            await consumer.commit()
    except KeyboardInterrupt:
        await consumer.stop()


asyncio.run(consume())
