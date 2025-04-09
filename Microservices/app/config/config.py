from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env.develop")

RABBITMQ_URI = os.getenv("RABBITMQ_URI")
RABBITMQ_QUEUE_USERS = os.getenv("RABBITMQ_USERS_QUEUE")
