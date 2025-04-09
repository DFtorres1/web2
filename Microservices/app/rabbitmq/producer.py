import aio_pika
from config.config import RABBITMQ_URI, RABBITMQ_QUEUE_USERS

async def send_message(message: str):
    connection = await aio_pika.connect_robust(RABBITMQ_URI)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(RABBITMQ_QUEUE_USERS, durable=True)
        await channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key=queue.name,
        )
