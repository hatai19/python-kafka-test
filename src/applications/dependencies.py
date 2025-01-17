from typing import Annotated

from fastapi import Depends
from faststream.kafka import KafkaBroker, fastapi
from sqlalchemy.ext.asyncio import AsyncSession

from database import async_session_maker

kafka_router = fastapi.KafkaRouter("kafka:9092")

def broker() -> KafkaBroker:
    return kafka_router.broker

async def get_db() -> AsyncSession:
    async with async_session_maker() as session:
        yield session

KafkaDepend = Annotated[KafkaBroker, Depends(broker)]
DatabaseDepend = Annotated[AsyncSession, Depends(get_db)]