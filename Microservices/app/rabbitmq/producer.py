import json
import aio_pika
from config.DB.conection import settings


async def send_message(message: dict):
    connection = await aio_pika.connect_robust(settings.RABBITMQ_URI)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(settings.RABBITMQ_USERS_QUEUE, durable=True)
        await channel.default_exchange.publish(
            aio_pika.Message(
                body=json.dumps(message).encode()
            ),
            routing_key=queue.name,
        )
        print(f"Mensaje enviado a la cola {queue.name}, {message}")
