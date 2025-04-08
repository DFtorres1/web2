import asyncio
from fastapi import FastAPI
from api.Endpoints.Activities.activity import activity_router
from api.Endpoints.Review.review import reviews
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


router_list = [
    activity_router,
    reviews
]

for router in router_list:
    app.include_router(router)

app.include_router(activity_router)