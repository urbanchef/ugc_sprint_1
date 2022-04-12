import asyncio
from datetime import datetime
from random import choice
from uuid import uuid4

from ugc.src import get_kafka_producer


async def main():
    producer = get_kafka_producer()
    await producer.start()

    for _ in range(5):
        value = {
            "user_uuid": uuid4(),
            "movie_uuid": uuid4(),
            "datetime": datetime.now(),
            "liked": choice([1, 0]),
        }
        await producer.send("likes", value)
        print("Sent value:", value)
        await asyncio.sleep(1)

    await producer.stop()


if __name__ == "__main__":
    asyncio.run(main())
