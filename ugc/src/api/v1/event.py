import json
import logging

from aiokafka import AIOKafkaProducer
from fastapi import APIRouter, Depends

from dependency import get_kafka_producer
from schemas.producer import ProducerMessage, ProducerResponse


router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/producer/{topicname}")
async def kafka_produce(msg: ProducerMessage, topicname: str, aioproducer: AIOKafkaProducer = Depends(get_kafka_producer)):
    await aioproducer.send(topicname, json.dumps(msg.dict()).encode("ascii"))
    response = ProducerResponse(
        key=msg.key, value=msg.value, topic=topicname
    )
    logger.info(response)

    return response
