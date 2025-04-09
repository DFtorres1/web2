import json
import aio_pika
import asyncio
from config.DB.conection import settings


async def on_message(message: aio_pika.IncomingMessage):
    async with message.process():
        payload = json.loads(message.body.decode())
        print(f"Message received: {payload}")

async def consume():
    connection = await aio_pika.connect_robust(settings.RABBITMQ_URI)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(settings.RABBITMQ_FASTAPI_QUEUE, durable=True)

        await queue.consume(on_message)
        print(" [*] Waiting for messages in: ", settings.RABBITMQ_FASTAPI_QUEUE)
        await asyncio.Future()
