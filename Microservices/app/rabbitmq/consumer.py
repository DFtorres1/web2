import aio_pika
import asyncio
from config.config import RABBITMQ_URI, RABBITMQ_QUEUE_USERS

async def consume():
    connection = await aio_pika.connect_robust(RABBITMQ_URI)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(RABBITMQ_QUEUE_USERS, durable=True)

        async def on_message(message: aio_pika.IncomingMessage):
            async with message.process():
                print(f"Message received: {message.body.decode()}")

        await queue.consume(on_message)
        print(" [*] Waiting for messages in: ", RABBITMQ_QUEUE_USERS)
        await asyncio.Future()
