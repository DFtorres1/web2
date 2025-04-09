import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from rabbitmq.producer import send_message
from rabbitmq.consumer import consume
from api.Endpoints.Activities.activity import activity_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(consume())

    yield

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("RabbitMQ consumer task cancelled")


app = FastAPI()


@app.get("/")
async def root():
    await send_message({"pattern": {"cmd": "get_user_by_id"}, "data": 1})
    return {"message": "FastAPI microservice connected to RabbitMQ"}

app.include_router(activity_router)
