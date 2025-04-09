import aio_pika
import asyncio
from config.DB.conection import settings


async def consume():
    connection = await aio_pika.connect_robust(settings.RABBITMQ_URI)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(settings.RABBITMQ_USERS_QUEUE, durable=True)

        async def on_message(message: aio_pika.IncomingMessage):
            async with message.process():
                print(f"Message received: {message.body.decode()}")

        await queue.consume(on_message)
        print(" [*] Waiting for messages in: ", settings.RABBITMQ_USERS_QUEUE)
        await asyncio.Future()
