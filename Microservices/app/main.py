import asyncio
from fastapi import FastAPI
from api.Endpoints.Activities.activity import activity_router
from consumidor.activity_consumer import consume_nats, nats_data

app = FastAPI()

# @app.on_event("startup")
# async def startup_event():
#     """Inicia el consumidor NATS cuando la API arranca."""
#     loop = asyncio.get_event_loop()
#     loop.create_task(consume_nats())

# @app.get("/nats-data", tags=["NATS"])
# def get_nats_data():
#     """Devuelve los datos recibidos desde NATS en JSON."""
#     return {"nats_messages": nats_data}


app.include_router(activity_router)