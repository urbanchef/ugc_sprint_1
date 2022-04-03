import json
import logging
from uuid import UUID

from aiokafka import AIOKafkaProducer
from fastapi import APIRouter, Depends
from starlette.requests import Request

from ...dependency import get_kafka_producer
from ...schemas.producer import MovieProgressMessage, ProducerMessage, ProducerResponse

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/producer/{topicname}")
async def kafka_produce_example(
    msg: ProducerMessage,
    topicname: str,
    request: Request,
    aioproducer: AIOKafkaProducer = Depends(get_kafka_producer),
):
    logger.info(request.state.user_uuid)
    await aioproducer.send(topicname, json.dumps(msg.dict()).encode("ascii"))
    response = ProducerResponse(key=msg.key, value=msg.value, topic=topicname)
    logger.info(response)

    return response


@router.post("/producer/{topic_name}/{movie_id}")
async def track_movie_progress(
    msg: MovieProgressMessage,
    topic_name: str,
    movie_id: UUID,
    request: Request,
    aioproducer: AIOKafkaProducer = Depends(get_kafka_producer),
):
    kafka_key = f"{request.state.user_uuid}+{movie_id}"
    await aioproducer.send(
        topic=topic_name,
        key=kafka_key.encode(),
        value=str(msg.unix_timestamp_utc).encode(),
    )
    response = ProducerResponse(
        key=kafka_key, value=str(msg.unix_timestamp_utc), topic=topic_name
    )
    logger.info(response)

    return response
